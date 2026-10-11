import numpy as np
marks = np.array([85, 72, 91, 68, 78])
print("Marks:", marks)
print("Mean:", np.mean(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard Deviation:", np.std(marks))
topper = np.argmax(marks)
print("Topper Position (index):", topper)
print("Topper Position (roll number):", topper + 1)
max_index = 0
for i in range(1, len(marks)):
    if marks[i] > marks[max_index]:
        max_index = i
print("Manual Topper Index:", max_index)
print("Check:", topper == max_index)
