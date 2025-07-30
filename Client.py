import socket

HOST = '127.0.0.1'
PORT = 12345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print(f"[+] Connected to server at {HOST}:{PORT}\n")

            # Gửi tên người chơi
            name = input("Enter your name: ").strip()
            s.sendall(name.encode())

            while True:
                data = s.recv(1024)
                if not data:
                    print("\n[-] Server disconnected.")
                    break

                message = data.decode()
                print(message, end='')

                # Nếu server yêu cầu nhập lựa chọn
                if "enter your choice" in message.lower():
                    choice = input(">> ").strip().lower()
                    s.sendall(choice.encode())

                # Nếu hỏi có chơi tiếp không
                if "play again" in message.lower():
                    answer = input(">> ").strip().lower()
                    s.sendall(answer.encode())

        except ConnectionRefusedError:
            print("[-] Cannot connect to the server.")
        except Exception as e:
            print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
