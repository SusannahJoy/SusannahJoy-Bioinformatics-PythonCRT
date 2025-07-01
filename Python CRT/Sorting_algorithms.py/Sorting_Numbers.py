'''
Problem:
You are given an array of integers representing student scores.
Your task is to sort the array in ascending order using a  basic
sorting algorithm(Bubble Sort/Selection Sort/Insertion Sort)
Input:
An integer n -Number of students
An array of n integers- the scores

Output:
Sorted array of scores in ascending order

Input:5
Scores:[55,90,70,60,80]
Output:[55,60,70,80,90]
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if elements are in wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores separated by space: ").split()))
bubble_sort(scores)
print("Sorted scores:", scores)