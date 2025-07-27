import random

# Danh sách lựa chọn trong trò chơi
choices = ["rock", "paper", "scissors"]

# Hàm xử lý kết quả trò chơi
def determine_winner(player1_choice, player2_choice):
    """
    Xác định kết quả trò chơi giữa Player 1 và Player 2.
    Trả về kết quả: "Player 1 wins", "Player 2 wins", hoặc "Draw"
    """
    if player1_choice == player2_choice:
        return "Draw"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "paper" and player2_choice == "rock") or \
         (player1_choice == "scissors" and player2_choice == "paper"):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

# Hàm kiểm tra tính hợp lệ của lựa chọn
def is_valid_choice(choice):
    """
    Kiểm tra xem lựa chọn của người chơi có hợp lệ không (rock, paper, scissors)
    """
    return choice in choices

# Hàm yêu cầu người chơi nhập lại nếu lựa chọn không hợp lệ
def get_player_choice(player_number):
    while True:
        choice = input(f"Player {player_number}, enter your choice (rock, paper, or scissors): ").lower()
        if is_valid_choice(choice):
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

