Knapsack Algorithm Solver

//MÔ TẢ
Ứng dụng này giải bài toán Knapsack Problem (Balo) bằng các thuật toán khác nhau, bao gồm:
*Greedy Algorithm (Fractional Knapsack), Backtracking, Hill Climbing

Ngoài ra, ứng dụng cung cấp giao diện đồ họa giúp người dùng:

1. Nhập dữ liệu đầu vào.
2. Chọn thuật toán mong muốn.
3. Hiển thị kết quả giải bài toán và thời gian thực thi.
4. So sánh thời gian thực thi giữa các thuật toán bằng biểu đồ.

//YÊU CẦU HỆ THỐNG
Python 3.8 trở lên.
Các thư viện Python cần cài đặt:
  -tkinter
  -matplotlib

//HƯỚNG DẪN SỬ DỤNG
1. Chạy ứng dụng
  Lưu mã nguồn trong file knapsack_solver.py.
  Mở Terminal hoặc Command Prompt, chạy file bằng lệnh:
      "python knapsack_solver.py"

2. Giao diện chương trình
  a. Nhập dữ liệu đầu vào:
*Trọng lượng: Nhập danh sách trọng lượng của các vật phẩm, cách nhau bằng dấu phẩy.
    Ví dụ: 10,20,30
*Giá trị: Nhập danh sách giá trị tương ứng của các vật phẩm, cách nhau bằng dấu phẩy.
    Ví dụ: 60,100,120
*Sức chứa tối đa: Nhập tổng trọng lượng tối đa mà balo có thể chứa.
    Ví dụ: 50
   
  b. Chọn thuật toán:
Chọn một thuật toán từ menu thả xuống, bao gồm: Greedy, Backtracking, Hill Climbing

  c. Xem kết quả:
Nhấn nút "Giải" thuật toán để xem kết quả chi tiết, bao gồm:
    -Các vật phẩm được chọn.
    -Tổng giá trị của các vật phẩm trong balo.
    -Thời gian thực thi của thuật toán.
  d. So sánh thuật toán:
*Nhấn nút So sánh thuật toán để hiển thị biểu đồ so sánh thời gian thực thi giữa các thuật toán.


///CHÚ Ý:
**Dữ liệu nhập: Số lượng trọng lượng và giá trị phải khớp nhau. Ví dụ, nếu có 3 trọng lượng thì phải có 3 giá trị tương ứng.
**Định dạng nhập liệu: Nhập đúng định dạng số thập phân (có thể dùng cả số nguyên và số thập phân).

//CÁCH HOẠT ĐỘNG CỦA CHƯƠNG TRÌNH:
Thuật toán
Greedy (Fractional Knapsack):
    -Dựa trên tỷ lệ giá trị/trọng lượng để chọn vật phẩm.
    -Có thể chọn một phần của vật phẩm nếu còn sức chứa.

Backtracking:
    -Duyệt qua tất cả các tổ hợp vật phẩm có thể để tìm giá trị lớn nhất mà không vượt quá sức chứa.

Hill Climbing:
    -Tìm kiếm cục bộ để cải thiện giá trị bằng cách thử thay đổi trạng thái hiện tại.

Chúc bạn sử dụng chương trình thành công!
