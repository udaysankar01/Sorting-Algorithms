import time
import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from sort_algorithms import start_sorting
from utils import randomize

def main():

    # initial setup
    data = randomize()

    #main window setup
    root = tk.Tk()
    root.title("Sorting Algorithm Visualizer")
    fig = Figure(figsize=((10, 5)))
    ax = plt.Axes(fig, [0, 0, 1, 1])
    fig.add_axes(ax)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.BOTTOM, fil=tk.BOTH, expand=True)

   # Frame for the controls
    control_frame = ttk.Frame(root)
    control_frame.pack(side=tk.TOP, fill=tk.Y, padx=15, pady=15)

    # Dropdown menu for selecting the sorting algorithm
    algorithm = tk.StringVar()
    algorithm.set("Bubble Sort")
    dropdown = ttk.Combobox(control_frame, textvariable=algorithm, width=15)
    dropdown['values'] = ("Bubble Sort", "Insertion Sort")
    dropdown.grid(row=0, column=0, padx=10, pady=10)

    # Buttons for array manipulation and sorting
    tk.Button(control_frame, text="Randomize Array", command=randomize, width=15).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(control_frame, text="Sort", command=lambda: start_sorting(algorithm.get(), data), width=15).grid(row=0, column=2, padx=10, pady=10)
    pause_resume_button = tk.Button(control_frame, text="Pause/Resume", command=lambda: None, width=15)
    pause_resume_button.grid(row=0, column=3, padx=10, pady=10)
    tk.Button(control_frame, text="Stop", command=lambda: None, width=15).grid(row=0, column=4, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main() 