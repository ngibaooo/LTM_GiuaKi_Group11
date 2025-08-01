import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

HOST = '127.0.0.1'
PORT = 12345

class GameClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")
        self.sock = None
        self.name = ""
        self.is_connected = False

        self.create_widgets()
        self.connect_to_server()

    def create_widgets(self):
        self.status_label = tk.Label(self.master, text="Waiting for connection...", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.result_text = tk.Text(self.master, height=6, width=50, state='disabled')
        self.result_text.pack(pady=10)

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)

        for choice in ["rock", "paper", "scissors"]:
            button = tk.Button(self.button_frame, text=choice.capitalize(), width=10,
                               command=lambda c=choice: self.send_choice(c))
            button.pack(side=tk.LEFT, padx=5)

    def connect_to_server(self):
        self.name = simpledialog.askstring("Enter your name", "Name:")
        if not self.name:
            self.master.destroy()
            return

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))
            self.is_connected = True
            self.status_label.config(text=f"Connected as {self.name}")
            threading.Thread(target=self.receive_data, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Connection Error", f"Cannot connect to server: {e}")
            self.master.destroy()

    def send_choice(self, choice):
        try:
            self.sock.sendall(choice.encode())
        except:
            messagebox.showerror("Error", "Lost connection to server.")
            self.master.destroy()

    def receive_data(self):
        try:
            while True:
                data = self.sock.recv(1024)
                if not data:
                    break

                message = data.decode()

                self.result_text.config(state='normal')
                self.result_text.insert(tk.END, message + '\n')
                self.result_text.see(tk.END)
                self.result_text.config(state='disabled')

                if "result" in message.lower():
                    replay = messagebox.askyesno("Play Again?", "Do you want to play another round?")
                    if replay:
                        self.sock.close()
                        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.sock.connect((HOST, PORT))
                        threading.Thread(target=self.receive_data, daemon=True).start()
                    else:
                        self.sock.close()
                        self.master.quit()
                        break
        except:
            self.result_text.config(state='normal')
            self.result_text.insert(tk.END, "[Disconnected from server]\n")
            self.result_text.config(state='disabled')

# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    client = GameClient(root)
    root.mainloop()
