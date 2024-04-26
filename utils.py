import random

def randomize():
    print("Randomize button pressed!")
    data = [random.randint(1, 100) for _ in range(50)]
    print(data)
    return data

def plotData(data, colorArray, canvas, ax):
    # update only the height and color of the bars if they already exist
    if not hasattr(plotData, "bars"):
        ax.clear()
        plotData.bars = ax.bar(range(len(data)), data, color=colorArray)
        ax.set_title("Sorting Visualization")
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        canvas.draw_idle()
    else:
        for bar, height, color in zip(plotData.bars, data, colorArray):
            bar.set_height(height)
            bar.set_color(color)
    
