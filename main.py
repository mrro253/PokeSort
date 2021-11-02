# Marshall Royce -- CS 315 -- Assignment 1 (Sorting Pokemon)
# Allows user to choose a sorting algorithm, including a binary search, to perform on a file of their choice
import os
import csv
import math
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
os.chdir("data")


insertion_comp_cnt = 0
merge_comp_cnt = 0
quick_comp_cnt = 0


def init(infile):
    global pokemon_names
    global pokemon_powers
    global insertion_comp_cnt
    global merge_comp_cnt
    global quick_comp_cnt
    insertion_comp_cnt = 0
    merge_comp_cnt = 0
    quick_comp_cnt = 0
    pokeStats = []
    try:
        file = open(infile)
    except FileNotFoundError:
        print("File not present, please check the spelling and ensure extension is included.")
        print("EX: pokemonRandomSmall.csv")
    else:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            pokeStats.append(row[1])
    return pokeStats


def insertion_sort(array):
    global insertion_comp_cnt
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            insertion_comp_cnt += 1
            array[j+1] = array[j]
            j -= 1
        insertion_comp_cnt += 1
        array[j+1] = key


def merge(arr, p, q, r):
    global merge_comp_cnt
    n1 = q - p + 1  # size of bottom
    n2 = r - q  # size of top
    L = []
    R = []
    for m in range(p, q):
        L.append(arr[m])
    for k in range(q+1, r):
        R.append(arr[k])
    for i in range(1, n1):
        L[i] = arr[p + i - 1]  # Copy bottom half
    for j in range(1, n2):
        R[j] = arr[q + j]  # Copy top half
    i = 1
    j = 1
    k = p
    for k in range(r):
        merge_comp_cnt += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i + 1
        else:
            arr[k] = R[j]
            j = j + 1


def merge_sort(arr):
    global merge_comp_cnt
    if len(arr) > 1:
        # Find middle of array
        mid = len(arr)//2

        # Divide elements into 2 halves
        L = arr[:mid]

        # Into 2 halves
        R = arr[mid:]

        # Sort the first half
        merge_sort(L)

        # Sort the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temporary arrays L[] and R[]
        while i < len(L) and j < len(R):
            merge_comp_cnt += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


def partition(arr, p, r):
    global quick_comp_cnt
    x = arr[r - 1]  # Select pivot --> last value of arr
    i = p - 1  # Keeps track of end of small array
    for j in range(p, r - 1):
        quick_comp_cnt += 1
        if arr[j] <= x:  # Compare to pivot
            i = i + 1  # Increase size of small array
            temp = arr[i]  # Swap values
            arr[i] = arr[j]
            arr[j] = temp
    new_temp = arr[i + 1]
    arr[i + 1] = arr[r - 1]  # Put pivot at end of small array
    arr[r - 1] = new_temp
    return i + 1


def print_sorted(arr):
    for i in range(1, len(arr)):
        print(arr[i], end="\n")


def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


# Main driver code
def main():
    while True:
        print("Marshall Royce Assignment 1 CS 315")
        usr_sort_choice = input("Type INSERTION or MERGE or QUICK or SEARCH (q to quit): ")
        if usr_sort_choice == "q":
            return 0
        file_choice = input("Select one of your csv files including the extension: ")
        pokeStats = init(file_choice)
        if usr_sort_choice == "INSERTION":
            insertion_sort(pokeStats)
            print("After insertion sort: ")
            print_sorted(pokeStats)
            print("Number of comparisons: ", insertion_comp_cnt)
        elif usr_sort_choice == "MERGE":
            merge_sort(pokeStats)
            print("After Merge Sort: ")
            print_sorted(pokeStats)
            print("Number of comparisons: ", merge_comp_cnt)
        elif usr_sort_choice == "QUICK":
            quick_sort(pokeStats, 1, len(pokeStats))
            print("After Quick Sort: ")
            print_sorted(pokeStats)
            print("Number of comparisons: ", quick_comp_cnt)
        elif usr_sort_choice == "SEARCH":
            merge_sort(pokeStats)
            search_value = input("What power value would you like to search for?: ")
            search_result = binary_search(pokeStats, search_value, 1, len(pokeStats))
            if search_result == -1:
                print("Sorry, the value you searched for isn't in the dataset.")
            else:
                print("The value is located at index: ", search_result)
        else:
            print("Invalid input, try again (Make sure all caps)")


if __name__ == "__main__":
    main()








