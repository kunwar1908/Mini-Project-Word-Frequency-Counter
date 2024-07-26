import tkinter as tk
from collections import Counter

def count_word_frequency():
    text = input_text.get("1.0", "end-1c")
    words = text.split()
    word_count = Counter(words)
    
    # Create a new window for displaying results
    result_window = tk.Toplevel(window)
    result_window.title("Word Frequency Results")
    result_window.configure(bg="lightgray")
    
    result_label = tk.Label(result_window, text="Word Frequency Results", font=("Arial", 16, "bold"), bg="lightgray")
    result_label.pack(pady=10)
    
    result_frame = tk.Frame(result_window, bg="lightgray")
    result_frame.pack(pady=10)
    
    result_text = tk.Text(result_frame, height=20, width=50, font=("Arial", 12), bg="white", fg="black", wrap="word")
    result_text.pack(side="left", fill="both", expand=True)
    
    scrollbar = tk.Scrollbar(result_frame, command=result_text.yview)
    scrollbar.pack(side="right", fill="y")
    
    result_text.config(yscrollcommand=scrollbar.set)
    
    for word, count in word_count.items():
        result_text.insert(tk.END, f"{word}: {count}\n")

# Create GUI
window = tk.Tk()
window.title("Word Frequency Counter")
window.configure(bg="lightblue")

input_label = tk.Label(window, text="Enter text:", font=("Arial", 14), bg="lightblue")
input_label.pack(pady=10)

input_text = tk.Text(window, height=10, width=50, font=("Arial", 12), bg="white", fg="black", wrap="word")
input_text.pack(pady=10)

count_button = tk.Button(window, text="Count", command=count_word_frequency, font=("Arial", 14), bg="darkblue", fg="white")
count_button.pack(pady=20)

window.mainloop()