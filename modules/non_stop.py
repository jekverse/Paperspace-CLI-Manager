from datetime import datetime
import time, pytz, subprocess, json
import modules.utils

api_key = modules.utils.api_key
notebooks_client = modules.utils.notebooks_client

def running_nonstop(notebook_id):
    is_first_check = True
    just_start = False
    notebook_id = modules.utils.load_notebook_id("selected_notebook.json")
    machine_type = "Free-RTX4000"
    print("="*50)
    print(f"Notebook_ID saat ini: {notebook_id}")
    def wait_until_notebook_active(just_start):
        while True:
            notebook_details = notebooks_client.get(id=notebook_id)
            if notebook_details.state == "Running":
                dt_started = notebook_details.dt_started
                # dt started = Mengecek apakah waktu notebook sudah muncul(ini sebagai indikasi apakah notebook saat diperintahkan untuk dijalankan sudah benar benar siap digunakan atau belum)
                # Jika sudah dijalankan :
                if dt_started:
                    # Mengonversi waktu UTC ke zona waktu Jakarta (WIB)
                    jakarta_tz = pytz.timezone('Asia/Jakarta')
                    jakarta_time = datetime.now(jakarta_tz)
                    dt_started_jakarta = dt_started.astimezone(jakarta_tz)
                    now = jakarta_time.strftime('%I:%M:%S')

                    if just_start:
                        # Mendapatkan waktu sekarang di zona waktu Jakarta
                        print(f"Notebook dengan ID {notebook_id} berhasil dijalankan ulang pada: {dt_started_jakarta.strftime('%Y-%m-%d %H:%M:%S')} WIB")
                        open_jupyter_lab(notebook_id, notebooks_client)
        
                        # Hitung mundur selama 3600 detik
                        countdown = 60
                        while countdown > 0:
                            minutes, seconds = divmod(countdown, 60)
                            print(f"\rMenunggu selama {minutes:02}:{seconds:02} sebelum mengecek lagi...", end='')
                            time.sleep(1)  # Tidur selama 1 detik
                            countdown -= 1
                        # Menghapus output countdown setelah selesai
                        print("\r" + " " * 50 + "\r", end='')  # Membersihkan garis terakhir
                        just_start = False
                        # timer.start_timer()
                        
                    else:
                        # Menampilkan waktu eksekusi dan jumlah pengecekan
                        print(f"( {now} ) | Status Notebook {notebook_id} Aktif ...")
        
                        # Hitung mundur selama 3600 detik
                        countdown = 60
                        while countdown > 0:
                            minutes, seconds = divmod(countdown, 60)
                            print(f"\rMenunggu selama {minutes:02}:{seconds:02} sebelum mengecek lagi...", end='')
                            time.sleep(1)  
                            countdown -= 1
                        # Menghapus output countdown setelah selesai
                        print("\r" + " " * 50 + "\r", end='')  # Membersihkan garis terakhir
                    break
                else:
                    print("Notebook sedang dalam proses provisioning.")
            else:
                countdown = 15
                while countdown > 0:
                    minutes, seconds = divmod(countdown, 60)
                    print(f"\rNotebook sedang memuat dependensi : {minutes:02}:{seconds:02}", end='')
                    time.sleep(1)  
                    countdown -= 1
                print("\r" + " " * 50 + "\r", end='')  # Membersihkan garis terakhir

    def open_jupyter_lab(notebook_id,notebooks_client):
        # Mendapatkan data notebook
        notebook = notebooks_client.get(id=notebook_id)   
        # Membuat URL
        url = f"https://{notebook.id}.{notebook.cluster_id}.paperspacegradient.com/lab?token={notebook.token}"
    
        # Membuka URL di browser tanpa menunggu
        subprocess.Popen(['xdg-open', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

###################################################################################################
                    #  MAIN CODE HERE 
####################################################################################################    
    try:
        #Loop
        while True:
            notebook_details = notebooks_client.get(id=notebook_id)
            ############################################################
            ## JIKA SAAT DICEK TERNYATA NOTEBOOK DALAM KEADAAN HIDUP  ##
            ############################################################
            if notebook_details.state == 'Running':
                # jika ini adalah pengecekan pertama
                if is_first_check:
                    # 1. MATIKAN
                    modules.utils.stop_notebook(notebook_id)
                    countdown = 10
                    while countdown > 0:
                        minutes, seconds = divmod(countdown, 60)
                        print(f"\rMenonaktfkan notebook {minutes:02}:{seconds:02}",end='')
                        time.sleep(1)  
                        countdown -= 1
                    print("\r" + " " * 50 + "\r", end='')  # Membersihkan garis terakhir
                    # 2. NYALAKAN LAGI
                    new_notebook_id = modules.utils.start_notebook(notebook_id, machine_type)
                    just_start = True
                    # ini kode untuk kalo pas mau jalan ternyata gpu nya ga available
                    if new_notebook_id is False:
                        option = input("Pilih opsi:\n1. Coba sampai dapat\n2. Ganti machine_type\nMasukkan pilihan (1 atau 2): ")
                        if option == '1':
                            notebook_id = modules.utils.retry_until_success(notebook_id, current_machine_type)
                        elif option == '2':
                            new_machine_type = modules.utils.list_available_gpus(from_main_menu=True)
                            if new_machine_type:
                                current_machine_type = new_machine_type
                                notebook_id = modules.utils.retry_until_success(notebook_id, current_machine_type)
                        else:
                            print("Pilihan tidak valid. Program dihentikan.")
                            break
                        is_first_check = False # Sebagai variable check agar pengecekan kedua tidak di restart jika menemukan notebook dalam keadaan hidup    
                    else:
                        # Jika gpu yang anda niatkan ternyata tersedia
                        print(f"Default Machine : {machine_type} tersedia")
                        # membuat siklus notebook_id agar next check bisa ngecek lagi.
                        notebook_id = new_notebook_id
                        with open("selected_notebook.json", "w") as f:
                                    json.dump({"notebook_id": notebook_id}, f)
                        dt_started = notebook_details.dt_started
                        print(f"Notebook dengan ID baru : {notebook_id} sedang dijalankan ulang.")
                        is_first_check = False
                # Jika pengecekan berikutnya
                else:
                    is_first_check = False
                    just_start = False

            ############################################################    
            ## JIKA SAAT DICEK TERNYATA NOTEBOOK DALAM KEADAAN MATI ! ##    
            ############################################################    
            else:
                jakarta_tz = pytz.timezone('Asia/Jakarta')
                dt_finished = notebook_details.dt_finished
                if dt_finished:
                    dt_finished_jakarta = dt_finished.astimezone(jakarta_tz)
                    print(f"Notebook tidak aktif sejak : {dt_finished_jakarta.strftime('%Y-%m-%d %H:%M:%S')} WIB")
                else:
                    print("Notebook belum selesai berjalan.")

                print("Memulai ulang notebook...")
                
                new_notebook_id = modules.utils.start_notebook(notebook_id, machine_type)

                just_start = True
                # Jika saat di dijalankan ternyata mesin tidak tersedia maka
                if new_notebook_id is False:
                    # Jika ini adalah pengecekan pertama | Berikan user kesempatan untuk mengganti GPU yang tersedia
                    if is_first_check:
                        option = input("Pilih opsi:\n1. Coba sampai dapat\n2. Ganti machine_type\nMasukkan pilihan (1 atau 2): ")

                        if option == '1':
                            notebook_id = modules.utils.retry_until_success(notebook_id, machine_type)
                        elif option == '2':
                            new_machine_type = modules.utils.list_available_gpus(from_main_menu=True)
                            if new_machine_type:
                                current_machine_type = new_machine_type
                                notebook_id = modules.utils.retry_until_success(notebook_id, current_machine_type)
                                
                        else:
                            print("Pilihan tidak valid. Program dihentikan.")
                            break
                        is_first_check = False
                        
                    # jika ini bukan pengecekan pertama | gausah kasih kesempatan, kalo ga dapet ya harus dapet.
                    else:
                        print("Mencoba lagi sampai mesin tersedia...")
                        notebook_id = modules.utils.retry_until_success(notebook_id, machine_type)
                # Jika saat dijalankan ternyata mesin yang kamu pilih diawal tersedia 
                else:
                    # membuat siklus notebook_id agar next check bisa ngecek lagi.
                    notebook_id = new_notebook_id
                    with open("selected_notebook.json", "w") as f:
                                json.dump({"notebook_id": notebook_id}, f)
                    dt_started = notebook_details.dt_started
                    print(f"Notebook dengan ID {notebook_id} sedang dijalankan ulang.")
                    is_first_check = False
            # mengecek apakah notebook sudah siap digunakan
            wait_until_notebook_active(just_start)

    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")
