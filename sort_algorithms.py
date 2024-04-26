import time
from utils import plotData

def start_sorting(algorithm, data, canvas, ax, pause_event, reset_event, timeTick=0.0000001):
    print("Sort button pressed! - ", algorithm)
    if algorithm == "Bubble Sort":
        bubble_sort(data, canvas, ax, pause_event, reset_event, timeTick)

    elif algorithm == "Insertion Sort":
        insertion_sort(data, canvas, ax, pause_event, reset_event, timeTick)


def bubble_sort(data, canvas, ax, pause_event, reset_event, timeTick):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if not pause_event.is_set():
                pause_event.wait()  # Wait here until the event is cleared
            if reset_event.is_set():
                reset_event.clear()
                return
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                colorArray = ['gray' for x in range(len(data))]
                colorArray[j: j + 2] = ['lightblue', 'lightblue']
                plotData(data, colorArray, canvas, ax)
                canvas.draw()
                time.sleep(timeTick)
    colorArray = ['green' for x in range(len(data))]
    plotData(data, colorArray, canvas, ax)
    canvas.draw()
    

def insertion_sort(data, canvas, ax, pause_event, reset_event, timeTick):
    for i in range(1, len(data)):
        j = i - 1
        while j >= 0 and data[j] > data[j + 1]:
            if not pause_event.is_set():
                pause_event.wait()  # Wait here until the event is cleared
            if reset_event.is_set():
                reset_event.clear()
                return
            data[j], data[j + 1] = data[j + 1], data[j]
            colorArray = ['gray' for x in range(len(data))]
            colorArray[j] = 'lightblue'
            j -= 1
            plotData(data, colorArray, canvas, ax)
            canvas.draw()
            time.sleep(timeTick)
    colorArray = ['green' for x in range(len(data))]
    plotData(data, colorArray, canvas, ax)
    canvas.draw()
