# AIM: Write a Python program to print a 
# triangle pattern (give any), emphasizing
# the transition from C to Python syntax.
# Coder:ABUTAHA IDRISI
# Date:3/3/26

print("--- Pattern Printer ---")

n = int(input(Enter Rows: ))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()




