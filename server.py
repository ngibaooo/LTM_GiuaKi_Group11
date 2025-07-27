import socket
import threading

HOST = '0.0.0.0'
PORT = 12345

def connect_client():

def logic_game():


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2) #tối đa 2 client
    print(f"Server is running at {HOST}:{PORT}")

if __name__ == "__main__":
    main()



