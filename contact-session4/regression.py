# Linear regression on a csv file (no external libraries)
# Usage: python3 regression.py student_scores.csv
# The first column is used as x and the last column as y.
import csv
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "student_scores.csv"

x = []
y = []
with open(filename, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        try:
            x.append(float(row[0]))
            y.append(float(row[-1]))
        except (ValueError, IndexError):
            continue  # skip rows with missing / bad values

n = len(x)
mean_x = sum(x) / n
mean_y = sum(y) / n

# slope = sum((xi - mean_x)(yi - mean_y)) / sum((xi - mean_x)^2)
numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
denominator = sum((x[i] - mean_x) ** 2 for i in range(n))
slope = numerator / denominator
intercept = mean_y - slope * mean_x

# R-squared
ss_res = sum((y[i] - (slope * x[i] + intercept)) ** 2 for i in range(n))
ss_tot = sum((y[i] - mean_y) ** 2 for i in range(n))
r_squared = 1 - ss_res / ss_tot

print("Columns:", header[0], "->", header[-1])
print("Rows used:", n)
print("Equation: y = %.4f * x + %.4f" % (slope, intercept))
print("R-squared: %.4f" % r_squared)
print("Prediction for x = 9.25: %.2f" % (slope * 9.25 + intercept))
