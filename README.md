# 🎓 Đồ án Python: Game Kéo Búa Bao 2 người chơi (Client - Server)

## 📌 Giới thiệu

Đây là một đồ án môn học lập trình mạng sử dụng **Python socket** để xây dựng trò chơi **Kéo Búa Bao** giữa **2 người chơi** qua mạng. Ứng dụng chia thành hai phần: **Server** và **Client**. Người chơi sẽ kết nối tới server, chọn Kéo / Búa / Bao và hệ thống sẽ xử lý kết quả, gửi thông báo thắng – thua – hòa cho từng client.

## 👨‍💻 Thành viên nhóm

| Họ và tên            | Vai trò                          | MSSV                 |
|-------------------|----------------------------------|----------------------|
| Ngô Gia Bảo     | Lập trình phần server            | 079205011307                        |
| Nguyễn Hữu Hoàng       | Lập trình phần client và giao diện game            | 067205000461                      |
| Đỗ Thanh Tiến          | Thiết kế logic trò chơi | 052205004180                        |
| Mai Đại Trí        | Tester và update README.md | 080205001449                        |

## 🕹️ Luật chơi

- **Kéo** thắng **Bao**
- **Bao** thắng **Búa**
- **Búa** thắng **Kéo**
- Nếu hai người chơi chọn giống nhau → **Hòa**

## 🧑 Player 1 (Client) <------> Server <-------> Player 2 (Client)

- Server chờ kết nối từ **2 client**
- Khi cả hai người chơi đều đã gửi lựa chọn (kéo/búa/bao), server sẽ xử lý và gửi kết quả về cho cả hai

## ⚙️ Công nghệ sử dụng

- Python 3.x
- Socket TCP
- Threading (đa luồng xử lý nhiều client)
- Console-based UI