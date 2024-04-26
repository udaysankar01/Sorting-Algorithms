import time
from utils import plotData

def bubble_sort(data, canvas, ax, speed):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                colorArray = ['gray' for x in range(n)]
                colorArray[j] = 'red'
                colorArray[j+1] = 'red'
                plotData(data, colorArray, canvas, ax)
                canvas.draw()
                canvas.flush_events()
                time.sleep(speed)
    
    colorArray = ['green' for x in range(n)]
    plotData(data, colorArray, canvas, ax)
    canvas.draw()
    canvas.flush_events()
    

def insertion_sort(data, canvas, ax, speed):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            colorArray = ['gray' for x in range(n)]
            colorArray[j] = 'red'
            colorArray[j+1] = 'red'
            plotData(data, colorArray, canvas, ax)
            canvas.draw()
            canvas.flush_events()
            time.sleep(speed)
            j -= 1
        data[j+1] = key
    colorArray = ['green' for x in range(n)]
    plotData(data, colorArray, canvas, ax)
    canvas.draw()
    canvas.flush_events()

def start_sorting(algorithm, data, canvas, ax, speed=0.00000001):
    print("Sort button pressed! - ", algorithm)
    print(data)
    if algorithm == "Bubble Sort":
        bubble_sort(data, canvas, ax, speed)

    elif algorithm == "Insertion Sort":
        insertion_sort(data, canvas, ax, speed)