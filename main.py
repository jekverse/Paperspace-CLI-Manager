# Main menu for selecting a notebook, creating a new notebook, or refreshing the display
import json
import modules.utils
import modules.notebook_setting 
import modules.non_stop
import modules.template

def main_menu():
    while True:
        notebooks_client = modules.utils.notebooks_client
        notebooks = notebooks_client.list(tags=[])
        modules.utils.show_notebook_list(notebooks)

        # Ask user to select a notebook, create a new one, or refresh the display
        print("\nOptions:")
        print("1. Notebook Setting")
        print("2. Create a new notebook")
        print("3. Available Machine")
        
        user_choice = input("\n[Q][R] Choose an option: ").strip()

        if user_choice == '1':
            # Prompt user to select a notebook by number
            selected_index = int(input("Select a notebook by number: ")) - 1
            if 0 <= selected_index < len(notebooks):
                selected_notebook_id = notebooks[selected_index].id
                # Save the selected notebook ID to a JSON file
                with open("selected_notebook.json", "w") as f:
                    json.dump({"notebook_id": selected_notebook_id}, f),
                print(f"\nAccessing Notebook with ID: '{selected_notebook_id}'\n")

                option1_menu()
                break
            else:
                print("Invalid selection, please select a valid notebook number.\n")
        elif user_choice == '2':
            option2_menu()
        elif user_choice == 'r':
            modules.utils.clear_output()
            continue  # Refresh by continuing the loop
        elif user_choice == '3':
            modules.utils.list_available_gpus(from_main_menu=False)
            print("Press ENTER to return to the main menu.")
            input()
            main_menu()
        elif user_choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose a valid option.\n")

def option1_menu():
    notebook_id = modules.utils.load_notebook_id("selected_notebook.json")
    try:
        print("="*50)
        print("📝 Notebook Setting       ")
        print("="*50)
        print("1. Jalankan ")
        print("2. Jalankan nonstop")
        print("3. Hentikan")
        print("4. Hapus")
        print("0. Notebook Detail")
        choice = input("Pilih opsi: ")

        if choice == '0':
            modules.utils.notebook_data()
            print("Press ENTER to return to the main menu")
            input()
            main_menu()
        elif choice == '1':
            modules.notebook_setting.start_notebook(notebook_id,machine_type="Free-A100-80G")
            main_menu()
        elif choice == '2':
            modules.non_stop.running_nonstop(notebook_id)
        elif choice == '3':
            modules.notebook_setting.stoping_notebook(notebook_id)
            main_menu()
        elif choice == '4':
            modules.notebook_setting.delete_notebook(notebook_id)
            main_menu()
        else:
            print("Pilihan tidak valid, coba lagi.")
            option1_menu()  #Panggil ulang menu notebook_setting jika input tidak valid
    except KeyboardInterrupt:
        print("\nKembali ke menu utama...")
        main_menu()


def option2_menu():
    try:
        print("="*50)
        print("📝 Create New Notebooks")
        print("="*50)
        print("1. Default setting")
        print("2. Template")
        print("3. Custom setting")
        
        pilihan = input("Masukkan pilihan Anda (1/2/3): ")

        if pilihan == '1':
            modules.template.default()  # Panggil fungsi default setting
            modules.utils.create_notebook(machine_type, container , name, command, shutdown_timeout)  # Panggil fungsi untuk membuat notebook
            main_menu()

        elif pilihan == '2':
            print("Anda memilih Template. Pilih sub-opsi berikut:")
            print("1. ComfyUI")
            print("2. Forge")
            print("3. Fooocus")
            
            sub_pilihan = input("Masukkan pilihan Anda (1/2/3): ")

            if sub_pilihan == '1':
                machine_type, container , name, command, shutdown_timeout = modules.template.comfyui()
                modules.utils.create_notebook(machine_type, container , name, command, shutdown_timeout)
                main_menu()
            elif sub_pilihan == '2':
                machine_type, container , name, command, shutdown_timeout = modules.template.forge()
                modules.utils.create_notebook(machine_type, container , name, command, shutdown_timeout)
                main_menu()
            elif sub_pilihan == '3':
                machine_type, container , name, command, shutdown_timeout = modules.template.fooocus()
                modules.utils.create_notebook(machine_type, container , name, command, shutdown_timeout)
                main_menu()
            else:
                print("Pilihan tidak valid, coba lagi.")
                option2_menu()

            main_menu()

        elif pilihan == '3':
            print("Pilih Custom Setting")
            # Tambahkan logika untuk custom setting di sini
        else:
            print("Pilihan tidak valid, coba lagi.")
            option2_menu()

    except KeyboardInterrupt:
        print("\nKembali ke menu utama...")
        main_menu()

if __name__ == "__main__":
    main_menu()