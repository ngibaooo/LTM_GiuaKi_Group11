import socket

HOST = '127.0.0.1'
PORT = 12345

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f"[+] Connected to server at {HOST}:{PORT}\n")

            # Nhập tên người chơi (chỉ để in local, server không xử lý)
            name = input("Enter your name: ").strip()

            while True:
                try:
                    # Nhận thông điệp từ server
                    data = s.recv(1024)
                    if not data:
                        print("\n[!] Server closed the connection.")
                        break

                    message = data.decode()
                    print(message, end='')

                    # Nếu server yêu cầu nhập lựa chọn
                    if "enter your choice" in message.lower():
                        while True:
                            choice = input(f"{name}, your move (rock/paper/scissors): ").strip().lower()
                            s.sendall(choice.encode())
                            break  # Gửi xong chờ server xử lý

                    # Sau khi chơi xong một ván, hỏi người dùng có chơi tiếp không
                    if "result" in message.lower():
                        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
                        if again != "yes":
                            print("Goodbye!")
                            break
                        print("\nWaiting for another player...\n")

                        # Kết nối lại để được ghép cặp ván mới
                        s.close()
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((HOST, PORT))
                        continue

                except ConnectionResetError:
                    print("\n[!] Server disconnected unexpectedly.")
                    break

    except ConnectionRefusedError:
        print("[-] Cannot connect to server. Is it running?")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

if __name__ == "__main__":
    main()
