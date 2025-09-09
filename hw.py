# 1. Numbers between 1–500 divisible by 3 and digit sum > 10
for num in range(1, 501):
    if num % 3 == 0:
        digit_total = 0
        for d in str(num):
            digit_total += int(d)
        if digit_total > 10:
            print(num, end=" ")

print("\n")

# 2. Armstrong numbers (1–10000)
for n in range(1, 10001):
    length = len(str(n))
    s = 0
    for d in str(n):
        s += int(d) ** length
    if s == n:
        print(n, end=" ")

print("\n")

# 3. Prime numbers till N except those ending with 3
N = 100
for val in range(2, N+1):
    if val % 10 == 3:
        continue
    prime = True
    for div in range(2, int(val**0.5) + 1):
        if val % div == 0:
            prime = False
            break
    if prime:
        print(val, end=" ")

print("\n")

# 4. Reverse a number (while loop)
n = 12345
reverse = 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
print(reverse)

# 5. Fibonacci sequence
count = 10
f1, f2 = 0, 1
i = 0
while i < count:
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2
    i += 1

print("\n")

# Pattern Making

# 1. Pyramid
rows = 5
for r in range(1, rows+1):
    print(" "*(rows-r), end="")
    seq = [str(x) for x in range(r, 2*r)]
    seq += [str(x) for x in range(2*r-2, r-1, -1)]
    print("".join(seq))

# 2. Spiral Matrix (NxN)
size = 3
mat = [[0]*size for _ in range(size)]
num, top, left, right, bottom = 1, 0, 0, size-1, size-1
while left <= right and top <= bottom:
    for k in range(left, right+1):
        mat[top][k] = num; num += 1
    top += 1
    for k in range(top, bottom+1):
        mat[k][right] = num; num += 1
    right -= 1
    for k in range(right, left-1, -1):
        mat[bottom][k] = num; num += 1
    bottom -= 1
    for k in range(bottom, top-1, -1):
        mat[k][left] = num; num += 1
    left += 1
for row in mat:
    print(row)

# 3. Diamond pattern
n = 5
for r in range(1, n+1, 2):
    print(" " * ((n-r)//2) + "*"*r)
for r in range(n-2, 0, -2):
    print(" " * ((n-r)//2) + "*"*r)

# 4. Pascal’s triangle
from math import comb
rows = 5
for i in range(rows):
    print(" "*(rows-i), end="")
    for j in range(i+1):
        print(comb(i, j), end=" ")
    print()

# 5. Alphabet triangle
rows = 4
for r in range(1, rows+1):
    letters = ""
    for j in range(r):
        letters += chr(65+j)
    print(letters)


# If-Logic & Match-Case

# 1. Grade
marks = int(input("Enter marks: "))
match marks:
    case m if m >= 90: print("Grade A")
    case m if m >= 75: print("Grade B")
    case m if m >= 60: print("Grade C")
    case m if m >= 40: print("Grade D")
    case _: print("Grade F")

# 2. FizzBuzz
for i in range(1, 51):
    if i % 35 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)

# 3. Calculator
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Enter operator: ")
match op:
    case "+": print(x+y)
    case "-": print(x-y)
    case "*": print(x*y)
    case "/": print(x/y if y != 0 else "Division by zero not allowed")
    case _: print("Unknown operation")

# 4. Leap year
yr = int(input("Enter year: "))
if (yr % 400 == 0) or (yr % 100 != 0 and yr % 4 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 5. Identify character
ch = input("Enter a character: ")
if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
