import time
from utils import plotData

def start_sorting(algorithm, data, canvas, ax, pause_event, reset_event, timeTick=0.0000001):
    print("Sort button pressed! - ", algorithm)
    if algorithm == "Bubble Sort":
        bubble_sort(data, canvas, ax, pause_event, reset_event, timeTick)

    elif algorithm == "Insertion Sort":
        insertion_sort(data, canvas, ax, pause_event, reset_event, timeTick)

    elif algorithm == "Merge Sort":
        for data in merge_sort(data, 0, len(data) - 1, pause_event, reset_event, timeTick):
            colorArray = ['gray' for x in range(len(data))]
            plotData(data, colorArray, canvas, ax)
            canvas.draw()
            time.sleep(timeTick)


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


def merge(data, p, q, r, pause_event, reset_event, timeTick):
    left = data[p:q+1]  # Includes the midpoint
    right = data[q+1:r+1]  # Goes up to r
    i = j = 0
    k = p

    while i < len(left) and j < len(right):
        if not pause_event.is_set():
            pause_event.wait()
        if reset_event.is_set():
            reset_event.clear()
            return
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
        yield data

    while i < len(left):
        if not pause_event.is_set():
            pause_event.wait()
        if reset_event.is_set():
            reset_event.clear()
            return
        data[k] = left[i]
        i += 1
        k += 1
        yield data

    while j < len(right):
        if not pause_event.is_set():
            pause_event.wait()
        if reset_event.is_set():
            reset_event.clear()
            return
        data[k] = right[j]
        j += 1
        k += 1
        yield data

def merge_sort(data, p, r, pause_event, reset_event, timeTick):
    if p < r:
        q = (p + r) // 2
        yield from merge_sort(data, p, q, pause_event, reset_event, timeTick)
        yield from merge_sort(data, q + 1, r, pause_event, reset_event, timeTick)
        yield from merge(data, p, q, r, pause_event, reset_event, timeTick)
    yield data