import random

def randomize():
    return [random.randint(1, 100) for _ in range(50)]

def plotData(data, colorArray, canvas, ax):
    ax.clear()
    ax.bar(range(len(data)), data, color=colorArray)
    ax.set_title("Sorting Algorithm Visualizer")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    canvas.draw_idle()
