import copy
import time
from typing import Callable

def readValues(PValues: list[int], filename: str) -> None:
    """Reads integer values from a dataset file into PValues list."""
    PValues.clear()
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                PValues.append(int(line))

def bubbleSort(PNums: list[int]) -> list[int]:
    """Bubble sort implementation."""
    arr = PNums[:]  # copy
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quickSort(PNums: list[int]) -> list[int]:
    """Quick sort implementation."""
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[len(PNums) // 2]
    left = [x for x in PNums if x < pivot]
    middle = [x for x in PNums if x == pivot]
    right = [x for x in PNums if x > pivot]
    return quickSort(left) + middle + quickSort(right)

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    """Measures elapsed time in ns for sorting algorithm."""
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    return EndTime - StartTime

def saveResults(results: list[str], filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for line in results:
            f.write(line + "\n")

def main() -> None:
    Values: list[int] = []
    Results: list[str] = []
    dataset_filename: str = ""
    print("Program starting.")
    while True:
        print("Options:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            dataset_filename = input("Insert dataset filename: ")
            try:
                readValues(Values, dataset_filename)
                print(f"Read {len(Values)} values from '{dataset_filename}'.")
            except FileNotFoundError:
                print("File not found.")
        elif choice == "2":
            if not Values:
                print("No dataset loaded.")
                continue
            print(f"Measured speeds for dataset '{dataset_filename}':")
            builtin_time = measureSortingTime(sorted, copy.deepcopy(Values))
            bubble_time = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            quick_time = measureSortingTime(quickSort, copy.deepcopy(Values))
            print(f" - Built-in sorted {builtin_time} ns")
            print(f" - Bubble sort {bubble_time} ns")
            print(f" - Quick sort {quick_time} ns")
            Results.clear()
            Results.append(f"Measured speeds for dataset '{dataset_filename}':")
            Results.append(f" - Built-in sorted {builtin_time} ns")
            Results.append(f" - Bubble sort {bubble_time} ns")
            Results.append(f" - Quick sort {quick_time} ns")
        elif choice == "3":
            if not Results:
                print("No results to save.")
                continue
            result_filename = input("Insert results filename: ")
            saveResults(Results, result_filename)
            print(f"Results saved to {result_filename}")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
    Values.clear()
    Results.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()

