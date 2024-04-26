import random
import threading

pause_event = threading.Event()
pause_event.set()

reset_event = threading.Event()
reset_event.clear()

def randomize():
    print("Randomize button pressed!")
    data = [random.randint(1, 100) for _ in range(100)]
    return data

def plotData(data, colorArray, canvas, ax, offset=0):
    # update only the height and color of the bars if they already exist
    if not hasattr(plotData, "bars"):
        ax.clear()
        plotData.bars = ax.bar(range(offset, offset + len(data)), data, color=colorArray)
        ax.set_title("Sorting Visualization")
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        canvas.draw_idle()
    else:
        for bar, height, color in zip(plotData.bars, data, colorArray):
            bar.set_height(height)
            bar.set_color(color)
    
