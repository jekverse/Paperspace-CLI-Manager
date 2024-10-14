import json
import modules.utils

api_key = modules.utils.api_key
notebooks_client = modules.utils.notebooks_client

def start_notebook(notebook_id,machine_type):
    new_notebook_id = modules.utils.start_notebook(notebook_id,machine_type)
    # if the default gpu isn't ready
    if new_notebook_id is False:
        option = input("Pilih opsi:\n1. Coba sampai dapat\n2. Ganti machine_type\nMasukkan pilihan (1 atau 2): ")

        if option == '1':
            notebook_id = modules.utils.retry_until_success(notebook_id,machine_type)
        elif option == '2':
            new_machine_type = modules.utils.list_available_gpus(from_main_menu=True)
            if new_machine_type:
                current_machine_type = new_machine_type
                notebook_id = modules.utils.retry_until_success(notebook_id,current_machine_type)
        else:
            print("Pilihan tidak valid. Program dihentikan.")
    else:
            notebook_id = new_notebook_id
            with open("selected_notebook.json", "w") as f:
                        json.dump({"notebook_id": notebook_id}, f)
            print(f"Notebook dengan ID {notebook_id} berhasil dimulai kembali.")

def stoping_notebook(notebook_id):
    print (f"Menghentikan sesi notebook dengan ID : {notebook_id}")
    notebooks_client.stop(id=notebook_id)  


def delete_notebook(notebook_id):
    print (f"Menghapus sesi notebook dengan ID : {notebook_id}")
    notebooks_client.delete(id=notebook_id)  

