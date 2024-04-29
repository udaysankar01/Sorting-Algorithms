import threading
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from sort_algorithms import start_sorting
from utils import randomize, plotData, pause_event, reset_event

def toggle_pause_resume():
    global toggle_pause_resume_button
    if pause_event.is_set():
        pause_event.clear()
        toggle_pause_resume_button.config(text="Resume")
        print("Pause button pressed!")
    else:
        pause_event.set()
        toggle_pause_resume_button.config(text="Pause")
        print("Resume button pressed!")

def reset(canvas, ax):
    global data, sorting_thread, original_data
    if sorting_thread.is_alive():
        print("Reset button pressed!")
        data = original_data.copy()
        reset_event.set()
    plotData(data=data, colorArray=['gray' for x in range(len(data))], canvas=canvas, ax=ax)
    canvas.draw_idle()

def randomize_array(canvas, ax):
    global data, original_data
    data = randomize()
    plotData(data=data, colorArray=['gray' for x in range(len(data))], canvas=canvas, ax=ax)
    original_data = data.copy()
    canvas.draw_idle()

def start_sorting_thread(algorithm, data, canvas, ax):
    global sorting_thread
    if not sorting_thread.is_alive():
        sorting_thread = threading.Thread(target=start_sorting, args=(algorithm, data, canvas, ax, pause_event, reset_event))
        sorting_thread.daemon = True
        sorting_thread.start()

def main():

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

    global data, original_data
    data = randomize()
    original_data = data.copy()
    plotData(data=data, colorArray=['gray' for x in range(len(data))], canvas=canvas, ax=ax)

    # Dropdown menu for selecting the sorting algorithm
    algorithm = tk.StringVar()
    algorithm.set("Quick Sort")
    dropdown = ttk.Combobox(control_frame, textvariable=algorithm, width=15)
    dropdown['values'] = ("Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort")
    dropdown.grid(row=0, column=0, padx=10, pady=10)

    # Buttons for array manipulation and sorting
    tk.Button(control_frame, text="Randomize Array", command=lambda: randomize_array(canvas, ax), width=15).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(control_frame, text="Sort", command=lambda: start_sorting_thread(algorithm.get(), data, canvas, ax), width=15).grid(row=0, column=2, padx=10, pady=10)
    global toggle_pause_resume_button
    toggle_pause_resume_button = tk.Button(control_frame, text="Pause", command=toggle_pause_resume, width=15)
    toggle_pause_resume_button.grid(row=0, column=3, padx=10, pady=10)
    tk.Button(control_frame, text="Reset", command=lambda: reset(canvas, ax), width=15).grid(row=0, column=4, padx=10, pady=10)

    global sorting_thread
    sorting_thread = threading.Thread(target=start_sorting, args=(algorithm.get(), data, canvas, ax))

    root.mainloop()


if __name__ == "__main__":
    main() 