import time
from utils import plotData

def start_sorting(algorithm, data, canvas, ax, pause_event, reset_event, timeTick=0.0000001):
    print("Sort button pressed! - ", algorithm)
    if algorithm == "Bubble Sort":
        bubble_sort(data, canvas, ax, pause_event, reset_event, timeTick)

    elif algorithm == "Selection Sort":
        selection_sort(data, canvas, ax, pause_event, reset_event, timeTick)

    elif algorithm == "Insertion Sort":
        insertion_sort(data, canvas, ax, pause_event, reset_event, timeTick)

    elif algorithm == "Merge Sort":
        # print(data)
        for idx, data in enumerate(merge_sort(data, 0, len(data) - 1)):
            # print(data)
            if not pause_event.is_set():
                pause_event.wait()
            if reset_event.is_set():
                reset_event.clear()
                return
            colorArray = ['gray' for x in range(len(data))]
            plotData(data, colorArray, canvas, ax)
            canvas.draw()
            time.sleep(timeTick)
        colorArray = ['green' for x in range(len(data))]
        plotData(data, colorArray, canvas, ax)
        canvas.draw()
    
    elif algorithm == "Quick Sort":
        for data, pivot_index, low, high in quick_sort(data):
            if not pause_event.is_set():
                pause_event.wait()
            if reset_event.is_set():
                reset_event.clear()
                return
            colorArray = ['gray' for x in range(len(data))]
            if pivot_index is not None:
                colorArray[pivot_index] = 'green'
            if low is not None:
                colorArray[low] = 'lightblue'
            if high is not None:
                colorArray[high] = 'lightblue'
            plotData(data, colorArray, canvas, ax)
            canvas.draw()
            time.sleep(timeTick + 0.1)
        colorArray = ['green' for x in range(len(data))]
        plotData(data, colorArray, canvas, ax)
        canvas.draw()


def bubble_sort(data, canvas, ax, pause_event, reset_event, timeTick):
    """
    Sorts the given list of data using the bubble sort algorithm.

    Parameters:
    - data (list): The list of data to be sorted.
    - canvas: The canvas object for plotting the data.
    - ax: The axes object for plotting the data.
    - pause_event: The event object for pausing the sorting process.
    - reset_event: The event object for resetting the sorting process.
    - timeTick: The time delay between each step of the sorting process.

    Returns:
    - None
    """
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


def selection_sort(data, canvas, ax, pause_event, reset_event, timeTick):
    """
    Sorts the given list of data using the selection sort algorithm.

    Parameters:
    - data (list): The list of data to be sorted.
    - canvas: The canvas object for plotting the data.
    - ax: The axes object for the plot.
    - pause_event: The event object for pausing the sorting process.
    - reset_event: The event object for resetting the sorting process.
    - timeTick: The time delay between each step of the sorting process.

    Returns:
    - None
    """
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if not pause_event.is_set():
                pause_event.wait()
            if reset_event.is_set():
                reset_event.clear()
                return
            if data[j] < data[min_index]:
                min_index = j
                colorArray = ['gray' for x in range(len(data))]
                colorArray[i] = 'lightblue'
                colorArray[min_index] = 'lightblue'
                plotData(data, colorArray, canvas, ax)
                canvas.draw()
                time.sleep(timeTick)
    
        data[i], data[min_index] = data[min_index], data[i]

    colorArray = ['green' for x in range(len(data))]
    plotData(data, colorArray, canvas, ax)
    canvas.draw()


def insertion_sort(data, canvas, ax, pause_event, reset_event, timeTick):
    """
    Sorts the given list using the insertion sort algorithm.

    Parameters:
    - data (list): The list to be sorted.
    - canvas: The canvas object for visualization.
    - ax: The axes object for visualization.
    - pause_event: The event object for pausing the sorting process.
    - reset_event: The event object for resetting the sorting process.
    - timeTick (float): The time delay between each step of the sorting process.

    Returns:
    None
    """
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


def merge(data, p, q, r):
    """
    Merge two sorted subarrays of `data` into a single sorted subarray.
    Yields only when an element is placed in the merged array.

    Args:
        data (list): The list containing the subarrays to be merged.
        p (int): The starting index of the first subarray.
        q (int): The ending index of the first subarray.
        r (int): The ending index of the second subarray.

    Yields:
        list: The updated `data` list after each change is made.
    """
    left = data[p:q+1]  # Includes the midpoint
    right = data[q+1:r+1]  # Goes up to r
    i = j = 0
    k = p

    # Merge the sorted subarrays back to data
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
        yield data  # Yield after each insertion into the data array

    # Copy remaining elements from left, if any
    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1
        yield data  # Yield after each insertion into the data array

    # Copy remaining elements from right, if any
    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1
        yield data  # Yield after each insertion into the data array


def merge_sort(data, p, r):
    """
    Sorts the given list 'data' in ascending order using the merge sort algorithm.

    Parameters:
    - data (list): The list to be sorted.
    - p (int): The starting index of the sublist to be sorted.
    - r (int): The ending index of the sublist to be sorted.

    Yields:
    - data (list): The sorted list after each recursive call.

    Returns:
    - None
    """
    if p < r:
        q = (p + r) // 2
        yield from merge_sort(data, p, q)
        yield from merge_sort(data, q + 1, r)
        yield from merge(data, p, q, r)
    yield data

def quick_sort(data, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(data) - 1
    if low < high:
        pivot_index = partition(data, low, high)
        yield data, pivot_index, low, high  # Yield before recursive calls for the current state
        yield from quick_sort(data, low, pivot_index - 1)
        yield from quick_sort(data, pivot_index + 1, high)
    yield data, None, low, high  # Final yield when the function returns

def partition(data, low, high):
    pivot = data[high]  # Use the last element as the pivot
    i = low - 1  # Index of the smaller element
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1  # Return the final position of the pivot
