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

    # frame for the controls
    frame = ttk.Frame(root)
    frame.pack(side=tk.TOP)

    # add buttons - randomize array, sort, pause/resume, stop
    tk.Button(frame, text="Randomize Array", command=randomize).pack(side=tk.LEFT)
    tk.Button(frame, text="Sort", command=lambda: start_sorting(algorithm="Bubble Sort", data=data)).pack(side=tk.LEFT)

    root.mainloop()


if __name__ == "__main__":
    main() 