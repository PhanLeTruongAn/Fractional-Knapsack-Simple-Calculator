from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk, messagebox
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class KnapsackAlgorithm:

    # Thuật toán giải Fractional Knapsack
    @staticmethod
    def fractional_knapsack(weights, values, capacity):
        start_time = time.time()
        ratio = sorted([(values[i] / weights[i], i) for i in range(len(weights))], reverse=True)
        total_value, process_log = 0, "Quá trình giải bằng Greedy:\n"

        for r, i in ratio:
            if weights[i] <= capacity:
                total_value += values[i]
                capacity -= weights[i]
                process_log += f"- Chọn toàn bộ vật phẩm {i + 1} (trọng lượng {weights[i]}, giá trị {values[i]})\n"
            else:
                total_value += values[i] * (capacity / weights[i])
                process_log += f"- Chọn một phần vật phẩm {i + 1} (trọng lượng {capacity}, giá trị {values[i] * (capacity / weights[i]):.2f})\n"
                break

        exec_time = (time.time() - start_time) * 1e9  # ns
        return total_value, exec_time, process_log + f"-> Tổng giá trị: {total_value:.2f}\n"

    @staticmethod
    def backtracking_knapsack(weights, values, capacity):
        n, max_value, best_solution = len(weights), 0, []

        def backtrack(i, current_weight, current_value, current_solution):
            nonlocal max_value, best_solution
            if current_weight > capacity or i == n:
                if current_value > max_value:
                    max_value, best_solution = current_value, current_solution[:]
                return
            backtrack(i + 1, current_weight, current_value, current_solution)  # Không chọn
            if current_weight + weights[i] <= capacity:  # Chỉ chọn nếu đủ sức chứa
                backtrack(i + 1, current_weight + weights[i],
                          current_value + values[i], current_solution + [i])

        start_time = time.time()
        backtrack(0, 0, 0, [])
        exec_time = (time.time() - start_time) * 1e9  # ns
        return max_value, exec_time, f"Backtracking result: {best_solution}\n-> Tổng giá trị: {max_value:.2f}\n"

    @staticmethod
    def hill_climbing_knapsack(weights, values, capacity):
        start_time = time.time()
        n = len(weights)

        # Khởi tạo trạng thái ngẫu nhiên
        current_solution = [random.choice([0, 1]) for _ in range(n)]
        current_value = sum(values[i] for i in range(n) if current_solution[i] == 1)
        current_weight = sum(weights[i] for i in range(n) if current_solution[i] == 1)

        def get_neighbors(solution):
            neighbors = []
            for i in range(len(solution)):
                neighbor = solution[:]
                neighbor[i] = 1 - neighbor[i]  # Đảo bit
                weight = sum(weights[j] for j in range(n) if neighbor[j] == 1)
                if weight <= capacity:  # Chỉ lấy lân cận hợp lệ
                    neighbors.append(neighbor)
            return neighbors

        iteration_limit = 1000
        iteration = 0
        while iteration < iteration_limit:
            neighbors = get_neighbors(current_solution)
            next_solution = None
            next_value = current_value
            for neighbor in neighbors:
                value = sum(values[i] for i in range(n) if neighbor[i] == 1)
                if value > next_value:
                    next_solution, next_value = neighbor, value
            if next_solution is None:
                break
            current_solution, current_value = next_solution, next_value
            iteration += 1

        exec_time = (time.time() - start_time) * 1e9  # ns
        return current_value, exec_time, f"Hill Climbing solution: {current_solution}\n-> Tổng giá trị: {current_value:.2f}\n"

    # Ánh xạ thuật toán vào từ điển
    ALGORITHMS = {
        "Greedy": fractional_knapsack,
        "Backtracking": backtracking_knapsack,
        "Hill Climbing": hill_climbing_knapsack,
    }

    @staticmethod   
    def solve_knapsack(weights, values, capacity, algorithm):
        """Hàm giải thuật toán từ ánh xạ ALGORITHMS"""
        func = KnapsackAlgorithm.ALGORITHMS.get(algorithm)
        if func:
            return func(weights, values, capacity)
        return None, None, "Thuật toán chưa được hỗ trợ."

# Giao diện và chức năng chính
def get_input_data():
    """Lấy dữ liệu từ các trường nhập liệu và kiểm tra lỗi"""
    try:
        weights = list(map(float, weight_entry.get().replace(' ', '').split(',')))
        values = list(map(float, value_entry.get().replace(' ', '').split(',')))
        capacity = float(capacity_entry.get())
        if len(weights) != len(values):
            raise ValueError("Số lượng trọng lượng và giá trị không khớp.")
        if any(w <= 0 for w in weights) or any(v <= 0 for v in values):
            raise ValueError("Trọng lượng và giá trị phải lớn hơn 0.")
        if capacity <= 0:
            raise ValueError("Sức chứa phải lớn hơn 0.")
        return weights, values, capacity
    except ValueError as e:
        messagebox.showerror("Lỗi nhập liệu", f"Lỗi: {e}")
        return None, None, None


def display_solution(algorithm):
    """Hiển thị kết quả của thuật toán đã chọn"""
    weights, values, capacity = get_input_data()
    if weights is None:
        return
    total_value, runtime, log = KnapsackAlgorithm.solve_knapsack(weights, values, capacity, algorithm)
    result_text.delete(1.0, END)
    result_text.insert(END, f"Thuật toán: {algorithm}\n{log}Thời gian thực thi: {runtime:.2f} ns\n")


def compare_and_display():
    """So sánh các thuật toán và hiển thị biểu đồ"""
    weights, values, capacity = get_input_data()
    if weights is None:
        return

    runtimes, valid_algorithms = [], []
    for algo in KnapsackAlgorithm.ALGORITHMS:
        _, runtime, _ = KnapsackAlgorithm.solve_knapsack(weights, values, capacity, algo)
        runtimes.append(runtime)
        valid_algorithms.append(algo)

    # Vẽ biểu đồ
    fig, ax = plt.subplots()
    ax.barh(valid_algorithms, runtimes, color='skyblue')
    ax.set_xlabel('Thời gian thực thi (ns)')
    ax.set_title('So sánh thời gian thực thi giữa các thuật toán')
    plt.tight_layout()

    # Hiển thị biểu đồ
    plt_window = Toplevel(root)
    plt_window.title("Biểu đồ so sánh")
    canvas = FigureCanvasTkAgg(fig, master=plt_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Giao diện chính
root = Tk()
root.title("Fractional Knapsack Solver")
font = tkFont.Font(family="Helvetica", size=25, weight="bold")
header = Label(root, text="Knapsack Calculator", font=font).pack()

# Khung nhập dữ liệu
input_frame = Frame(root)
input_frame.pack(padx=10, pady=5, fill=X)

Label(input_frame, text="Trọng lượng (phân cách bởi dấu phẩy):").pack(anchor=W)
weight_entry = Entry(input_frame)
weight_entry.pack(fill=X, padx=5, pady=2)

Label(input_frame, text="Giá trị (phân cách bởi dấu phẩy):").pack(anchor=W)
value_entry = Entry(input_frame)
value_entry.pack(fill=X, padx=5, pady=2)

Label(input_frame, text="Sức chứa tối đa:").pack(anchor=W)
capacity_entry = Entry(input_frame)
capacity_entry.pack(fill=X, padx=5, pady=2)

# Khung điều khiển
control_frame = Frame(root)
control_frame.pack(padx=10, pady=5)

Label(control_frame, text="Chọn thuật toán:").pack(side=LEFT)
algo_choice = StringVar()
algo_menu = ttk.Combobox(control_frame, textvariable=algo_choice, state="readonly")
algo_menu['values'] = list(KnapsackAlgorithm.ALGORITHMS.keys())
algo_menu.pack(side=LEFT, padx=5)
algo_menu.current(0)

Button(control_frame, text="Giải thuật toán", command=lambda: display_solution(algo_choice.get())).pack(side=LEFT, padx=5)
Button(control_frame, text="So sánh thuật toán", command=compare_and_display).pack(side=LEFT, padx=5)

# Kết quả
result_text = Text(root, height=15, wrap=WORD)
result_text.pack(padx=10, pady=5, fill=X)

root.mainloop()
