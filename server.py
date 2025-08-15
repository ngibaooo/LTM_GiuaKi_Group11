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
        while True:
            conn.sendall(b"Please enter your choice (rock, paper, or scissors): ")
            choice = conn.recv(1024).decode().strip().lower()

            if not choice:
                conn.sendall(b"No input received.\n")
                continue

            if is_valid_choice(choice):
                print(f"Player {player_id} ({addr}) choose: {choice}")
                return choice  # Chỉ return khi hợp lệ
            else:
                conn.sendall(b"Invalid choice. Please choose again (rock, paper, or scissors).\n")
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
            result_msg = f"\nPlayer 1 choose: {player1_choice}\nPlayer 2 choose: {player2_choice}\nResult: {result}\n"
            player1_conn.sendall(result_msg.encode())
            player2_conn.sendall(result_msg.encode())

    finally:
        player1_conn.close()
        player2_conn.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            print(f"Client connected from {addr}")
            waiting_clients.append((conn, addr))
            
            # Nếu mới chỉ có 1 người kết nối
            if len(waiting_clients) == 1:
                conn.sendall(b"Waiting for another player to join...\n")

            # Khi đủ 2 người thì bắt đầu game
            if len(waiting_clients) >= 2:
                player1 = waiting_clients.pop(0)
                player2 = waiting_clients.pop(0)
                game_thread = threading.Thread(
                    target=game_session,
                    args=(player1[0], player1[1], player2[0], player2[1])
                )
                game_thread.start()


if __name__ == "__main__":
    main()
