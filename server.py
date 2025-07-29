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
    
def game_session(player1_conn, player1_addr, player2_conn, player2_addr):
    try:
        player1_choice = handle_client(player1_conn, player1_addr, 1, player2_conn)
        player2_choice = handle_client(player2_conn, player2_addr, 2, player1_conn)

        if not player1_choice or not player2_choice:
            player1_conn.sendall(b"Connection error or invalid input.\n")
            player2_conn.sendall(b"Connection error or invalid input.\n")
        else:
            result = determine_winner(player1_choice, player2_choice)
            result_msg = f"\nPlayer 1 chose: {player1_choice}\nPlayer 2 chose: {player2_choice}\nResult: {result}\n"
            player1_conn.sendall(result_msg.encode())
            player2_conn.sendall(result_msg.encode())

    finally:
        player1_conn.close()
        player2_conn.close()


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
