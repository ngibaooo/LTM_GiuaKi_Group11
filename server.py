import socket
import threading
from locgic_game import * 

# Cấu hình server
HOST = '0.0.0.0'
PORT = 12345

# Danh sách client đang chờ
waiting_clients = []

def handle_client(conn, addr, player_id, opponent_conn):
    try:
        conn.sendall(b"Please enter your choice (rock, paper, or scissors): ")
        choice = conn.recv(1024).decode().strip().lower()
    except:
        return None

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"✅ Server listening on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            print(f"🔌 Client connected from {addr}")
            waiting_clients.append((conn, addr))

if __name__ == "__main__":
    main()
