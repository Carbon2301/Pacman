# Pacman AI - Project Nhập Môn Trí Tuệ Nhân Tạo

## Giới thiệu
Đây là một project game Pacman được phát triển bằng Python và Pygame, sử dụng các thuật toán trí tuệ nhân tạo để điều khiển cả Pacman và các con ma. Project này được thực hiện như một bài tập lớn cho môn Nhập Môn Trí Tuệ Nhân Tạo.

## Tính năng chính
- Game Pacman cổ điển với đồ họa được xây dựng bằng Pygame
- Nhiều thuật toán AI khác nhau cho Pacman:
  - BFS (Breadth-First Search)
  - Minimax
  - Local Search
- AI cho ma quái sử dụng thuật toán A* và Random Movement
- Hệ thống tính điểm và nhiều level
- Menu tương tác người dùng

## Cấu trúc project
```
Source/
├── Algorithms/         # Chứa các thuật toán AI
│   ├── BFS.py         # Thuật toán BFS
│   ├── Minimax.py     # Thuật toán Minimax
│   ├── LocalSearch.py # Thuật toán Local Search
│   ├── Ghost_Move.py  # Logic di chuyển của ma
│   └── SearchAgent.py # Agent tìm kiếm
├── Constants/         # Các hằng số và cấu hình
├── Object/           # Các đối tượng trong game
├── Utils/            # Các hàm tiện ích
├── Images/           # Tài nguyên hình ảnh
└── main.py           # File chính của game
```

## Các thuật toán AI được sử dụng

### 1. BFS (Breadth-First Search)
- Sử dụng để tìm đường đi ngắn nhất đến thức ăn gần nhất

### 2. Minimax
- Thuật toán đối kháng cho Pacman
- Xem xét các nước đi của ma và tìm nước đi tối ưu
- Sử dụng đánh giá trạng thái để quyết định nước đi

### 3. Local Search
- Tìm kiếm cục bộ để tối ưu hóa đường đi
- Cân nhắc giữa việc ăn thức ăn và tránh ma

### 4. A* cho Ma
- Ma sử dụng A* để đuổi theo Pacman
- Có cơ chế tránh va chạm giữa các ma

## Cách chạy game
1. Đảm bảo đã cài đặt Python và Pygame
2. Chạy file main.py:
```bash
python Source/main.py
```

## Điều khiển
- Sử dụng các phím mũi tên để di chuyển Pacman
- ESC để thoát game
- Các nút trong menu để tương tác

## Yêu cầu hệ thống
- Python 3.x
- Pygame
- Các thư viện Python chuẩn
