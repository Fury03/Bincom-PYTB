import os
import re

# ---------- Part 1: read full name from file and split it ----------
with open("name.txt", "r") as f:
    full_name = f.read().strip()

parts = full_name.split()
first_name = parts[0]
middle_name = parts[1]
last_name = parts[-1]

print("First name :", first_name)
print("Middle name:", middle_name)
print("Last name  :", last_name)

# ---------- Part 2: print local file path using os ----------
print("Current file path:", os.path.abspath(__file__))
print("Current folder   :", os.getcwd())

# ---------- Part 3: extract baby names with regex ----------
with open("baby2008.html", "r") as f:
    html = f.read()

# each table row looks like: <tr align="right"><td>1</td><td>Jacob</td><td>Emma</td>
pattern = r"<td>(\d+)</td><td>([A-Za-z]+)</td><td>([A-Za-z]+)</td>"
rows = re.findall(pattern, html)

names = []
for rank, male, female in rows:
    names.append(male)
    names.append(female)

print("Number of names extracted:", len(names))


# ---------- Sort algorithm (bubble sort) ----------
def bubble_sort(items):
    items = items[:]  # work on a copy
    n = len(items)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


sorted_names = bubble_sort(names)
print("First 10 sorted names:", sorted_names[:10])


# ---------- Binary search ----------
def binary_search(items, target):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


for target in ["Jacob", "Emma", "Zzzz"]:
    position = binary_search(sorted_names, target)
    if position == -1:
        print(target, "not found")
    else:
        print(target, "found at index", position)
