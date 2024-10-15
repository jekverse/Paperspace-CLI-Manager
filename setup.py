import sys, termios, tty, os

def setup_env_file():
    def mask_input(prompt):
        print(prompt, end='', flush=True)
        input_buffer = []
        
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                char = sys.stdin.read(1)
                if char in ('\r', '\n'):  # Enter key detection
                    print()  # Proper newline after Enter is pressed
                    break
                elif char == '\x7f':  # Handle backspace
                    if input_buffer:
                        input_buffer.pop()
                        print('\b \b', end='', flush=True)
                else:
                    input_buffer.append(char)
                    print('*', end='', flush=True)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ''.join(input_buffer)

    # Setup tanpa cek file .env
    print("="*50)
    print("📝 Setup Paperspace Token & Project_ID")
    print("="*50)
    
    api_key = mask_input("Enter your API_KEY: ")
    print()  # Ensure the next prompt starts on a new line

    project_id = mask_input("Enter your PROJECT_ID: ")
    
    with open(".env", "w") as env_file:
        env_file.write(f"API_KEY={api_key}\n")
        env_file.write(f"PROJECT_ID={project_id}\n")

    print("\nSetup file created/updated successfully!")

if __name__ == "__main__":
    setup_env_file()
