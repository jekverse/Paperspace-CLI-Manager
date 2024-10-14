from dotenv import load_dotenv
import os
import json, time
from gradient import NotebooksClient, MachineTypesClient
from datetime import datetime, timedelta

# Memuat file .env
load_dotenv()
# Mengambil variabel dari file .env
api_key = os.getenv('API_KEY')
project_id = os.getenv('PROJECT_ID')
notebooks_client = NotebooksClient(api_key)


def create_notebook(machine_type, container , name, command, shutdown_timeout):
    print(f"Membuat Notebook Baru Dengan Template : {name}")
    print(project_id)
    try:
        response = notebooks_client.create(
            machine_type=machine_type,
            container=container,
            project_id=project_id,
            name=name,
            command=command,
            shutdown_timeout=shutdown_timeout
        )
        print("Notebook berhasil dibuat:", response)
        return True  # Notebook created successfully

    except Exception as e:
        # Handle specific error for unavailable GPU
        if 'out of capacity for the selected VM type' in str(e):
            print(f"Status: {machine_type} tidak tersedia.")
        else:
            print("Terjadi kesalahan lain:", e)

        # Opsi untuk mencoba lagi atau mengganti machine_type
        option = input("Pilih opsi:\n1. Coba sampai dapat\n2. Ganti machine_type\nMasukkan pilihan (1 atau 2): ")

        if option == '1':
            retry_until_create_success(machine_type, container, name, command, shutdown_timeout)  # Coba sampai dapat
        elif option == '2':
            new_machine_type = list_available_gpus(from_main_menu=True)  # Tampilkan daftar GPU gratis dan pilih salah satu
            if new_machine_type:
                retry_until_create_success(new_machine_type, container, name, command, shutdown_timeout)  # Ganti dan coba lagi dengan machine_type baru
        else:
            print("Pilihan tidak valid. Program dihentikan.")


def retry_until_create_success(machine_type, container, name,command,shutdown_timeout):
    attempt_count = 0  # Hitungan percobaan
    while True:
        attempt_count += 1
        success = create_notebook(machine_type, container, name,command,shutdown_timeout)
        if success:
            break
        elif success is False:
            print(f"Percobaan {attempt_count}: Mesin tidak tersedia. Mencoba lagi dalam 30 detik...")
            time.sleep(30)  # Tunggu 30 detik sebelum mencoba lagi
        else:
            break  # Terjadi kesalahan lain, keluar dari loop

def start_notebook(notebook_id,machine_type):
    notebooks_client = NotebooksClient(api_key)
    try:
        response = notebooks_client.start(
            id=notebook_id,
            machine_type=machine_type,
            shutdown_timeout="6" 
        )
        print("Notebook dengan ID :", response," akan dimulai")
        
        return response.id if hasattr(response, 'id') else response
    except Exception as e:
        if 'out of capacity for the selected VM type' in str(e):
            print("Status: Mesin tidak tersedia.")
            return False
        else:
            print("Terjadi kesalahan lain:", e)
            return None
        
def retry_until_success(notebook_id,machine_type):
    attempt_count = 0
    while True:
        attempt_count += 1
        new_notebook_id = start_notebook(notebook_id,machine_type)
        if new_notebook_id:
            return new_notebook_id
        elif new_notebook_id is False:
            print(f"Percobaan {attempt_count}: Mesin tidak tersedia. Mencoba lagi dalam 30 detik...")
            time.sleep(30)
        else:
            break

def stop_notebook(notebook_id):
    try:
        notebooks_client = NotebooksClient(api_key)
        notebooks_client.stop(id=notebook_id)
        print("Notebook berhasil dihentikan")
        return True
    except Exception as e:
        print("Terjadi kesalahan saat menghentikan notebook:", e)
        return False

def list_available_gpus(from_main_menu):
    machineTypes_client = MachineTypesClient(api_key)
    machines = machineTypes_client.list()
    desired_labels = ['Free-P5000', 'Free-RTX4000', 'Free-RTX5000', 'Free-A4000']

    print("="*50)
    print("📝 Available GPU       ")
    print("="*50)
    available_machines = []

    # Loop through available machines and display desired labels
    for index, machine in enumerate(machines):
        if machine.label in desired_labels:
            available_machines.append(machine)
            print(f"{len(available_machines)}.| {machine.label} | CPU Count: {machine.cpu_count} | RAM: {machine.ram_in_bytes / (1024 ** 3):.2f} GB | GPU Memory: {machine.gpu_model.memory_in_bytes / (1024 ** 3):.2f} GB |")

    print("="*50)

    # Only execute the GPU selection block if from_main_menu is True
    if from_main_menu:
        choice = int(input("Pilih nomor GPU yang ingin Anda gunakan: ")) - 1

        if 0 <= choice < len(available_machines):
            selected_machine = available_machines[choice]
            print(f"Anda memilih GPU {selected_machine.label}")
            return selected_machine.label
        else:
            print("Pilihan tidak valid.")
            return None


def load_notebook_id(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            notebook_id = data["notebook_id"]
            # print(f"Notebook ID terpilih: {notebook_id}")
            return notebook_id  # Mengembalikan ID notebook
    except FileNotFoundError:
        print("Tidak ada notebook yang dipilih.")
        return None  # Mengembalikan None jika file tidak ditemukan
    except json.JSONDecodeError:
        print("Error decoding JSON. Pastikan file dalam format yang benar.")
        return None  # Mengembalikan None jika terjadi kesalahan saat memuat JSON
    except KeyError:
        print("Kunci 'notebook_id' tidak ditemukan dalam data.")
        return None  # Mengembalikan None jika kunci tidak ada

def show_notebook_list(notebooks):
    # Display a title and notebook list with numbering and formatting
    print("\n" + "="*40)
    print("Paperspace Gradient CLI Manager")
    print("="*40 + "\n")
    
    print("Available Notebooks:\n")
    for idx, notebook in enumerate(notebooks, start=1):
        print(f"{idx}.| Tags: {notebook.tags or 'None'} | ID: {notebook.id} | State: {notebook.state} | VM Type: {notebook.vm_type} |")


# Fungsi untuk menampilkan detail notebook
def notebook_data():
    # Fungsi internal untuk memformat waktu ke WIB
    def format_datetime(dt):
        if isinstance(dt, str):
            dt = datetime.fromisoformat(dt[:-1])  # Menghapus 'Z' dan mengonversi ke datetime
        if dt:
            wib_time = dt + timedelta(hours=7)
            return wib_time.strftime("%Y-%m-%d %H:%M:%S") + " WIB"
        return 'N/A'

    notebook_id = load_notebook_id("selected_notebook.json")
    notebook = notebooks_client.get(id=notebook_id)

    # Mencetak detail notebook dengan format yang lebih rapi
    print("="*50)
    print("📝 Notebook Details")
    print("="*50)
    print(f"🗂️   Tags: {notebook.tags if notebook.tags else 'None'}")
    print(f"🔖  ID: {notebook.id}")
    print(f"⚙️   State: {notebook.state}")
    print(f"💻  VM Type: {notebook.vm_type}")
    print(f"📦  Container: {notebook.container}")
    print(f"🌐  Is Public: {'Yes' if notebook.is_public else 'No'}")
    print(f"⏳  Shutdown Timeout: {notebook.shutdown_timeout} seconds")
    print(f"📅  Created At: {format_datetime(notebook.dt_created)}")
    print(f"🛠️   Modified At: {format_datetime(notebook.dt_modified)}")
    print(f"🚀  Provisioning Started: {format_datetime(notebook.dt_provisioning_started)}")
    print(f"✅  Provisioning Finished: {format_datetime(notebook.dt_provisioning_finished)}")
    print(f"🕒  Started At: {format_datetime(notebook.dt_started)}")
    print(f"🔗  Jupyter Lab URL: https://{notebook.id}.{notebook.cluster_id}.paperspacegradient.com/lab?token={notebook.token}")
    print("="*50)

def clear_output():
    # Cek apakah sistem operasi adalah Windows
    if os.name == 'nt':
        os.system('cls')  # Perintah 'cls' untuk Windows
    else:
        os.system('clear')  # Perintah 'clear' untuk Linux/Mac