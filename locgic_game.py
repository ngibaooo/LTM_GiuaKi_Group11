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