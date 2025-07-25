import socket

HOST = '127.0.0.1'
PORT = 12345

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        data = client.recv(1024).decode()
        print(data, end='')

        if "Enter your move" in data:
            move = input("Your move: ")
            client.sendall(move.encode())

if __name__ == "__main__":
    main()
