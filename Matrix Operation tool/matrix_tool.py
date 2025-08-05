import tkinter as tk
from tkinter import messagebox
import numpy as np

def parse_matrix(text):
    try:
        lines = text.strip().split('\n')
        matrix = [list(map(float, row.split(','))) for row in lines]
        return np.array(matrix)
    except:
        messagebox.showerror("Invalid Input", "Enter each row on a new line with comma-separated numbers.")
        return None

def get_matrices():
    A = parse_matrix(matrix_a_entry.get("1.0", tk.END))
    B = parse_matrix(matrix_b_entry.get("1.0", tk.END))
    return A, B

def show_result(result):
    result_display.delete("1.0", tk.END)
    result_display.insert(tk.END, str(result))

def add_matrices():
    A, B = get_matrices()
    if A is not None and B is not None:
        if A.shape == B.shape:
            show_result(A + B)
        else:
            messagebox.showerror("Shape Error", "Matrices must have the same shape.")

def subtract_matrices():
    A, B = get_matrices()
    if A is not None and B is not None:
        if A.shape == B.shape:
            show_result(A - B)
        else:
            messagebox.showerror("Shape Error", "Matrices must have the same shape.")

def multiply_matrices():
    A, B = get_matrices()
    if A is not None and B is not None:
        if A.shape[1] == B.shape[0]:
            show_result(A @ B)
        else:
            messagebox.showerror("Shape Error", "Matrix A columns must match Matrix B rows.")

def transpose_matrix():
    A = parse_matrix(matrix_a_entry.get("1.0", tk.END))
    if A is not None:
        show_result(A.T)

def determinant_matrix():
    A = parse_matrix(matrix_a_entry.get("1.0", tk.END))
    if A is not None:
        if A.shape[0] == A.shape[1]:
            show_result(round(np.linalg.det(A), 2))
        else:
            messagebox.showerror("Shape Error", "Determinant only works on square matrices.")


root = tk.Tk()
root.title("Matrix Operations Tool (Variable Size)")

tk.Label(root, text="Matrix A (rows as lines, comma-separated):").grid(row=0, column=0)
tk.Label(root, text="Matrix B (optional):").grid(row=0, column=1)

matrix_a_entry = tk.Text(root, height=8, width=30)
matrix_a_entry.grid(row=1, column=0, padx=5, pady=5)
matrix_b_entry = tk.Text(root, height=8, width=30)
matrix_b_entry.grid(row=1, column=1, padx=5, pady=5)


tk.Button(root, text="Add", width=15, command=add_matrices).grid(row=2, column=0)
tk.Button(root, text="Subtract", width=15, command=subtract_matrices).grid(row=2, column=1)
tk.Button(root, text="Multiply", width=15, command=multiply_matrices).grid(row=3, column=0)
tk.Button(root, text="Transpose A", width=15, command=transpose_matrix).grid(row=3, column=1)
tk.Button(root, text="Determinant of A", width=15, command=determinant_matrix).grid(row=4, column=0)


tk.Label(root, text="Result:").grid(row=5, column=0, columnspan=2)
result_display = tk.Text(root, height=6, width=65)
result_display.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
