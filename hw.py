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

# -------------------------
# Functions
# -------------------------

# 1. GCD & LCM
def gcd_val(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm_val(x, y):
    return (x * y) // gcd_val(x, y)

print("GCD:", gcd_val(12, 18))
print("LCM:", lcm_val(12, 18))

# 2. Second largest element
numbers = [10, 20, 4, 45, 99]
max1, max2 = float("-inf"), float("-inf")
for v in numbers:
    if v > max1:
        max2, max1 = max1, v
    elif v > max2 and v != max1:
        max2 = v
print("Second largest:", max2)

# 3. Palindrome string
text = "Never Odd Or Even"
formatted = "".join(ch.lower() for ch in text if ch != " ")
if formatted == formatted[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 4. Multiplication tables
upto = 5
for n in range(1, upto+1):
    for k in range(1, 11):
        print(f"{n} x {k} = {n*k}")
    print()

# 5. Recursive digit sum
def digit_sum(x):
    if x == 0:
        return 0
    return (x % 10) + digit_sum(x // 10)

print(digit_sum(1234))


# -------------------------
# Strings
# -------------------------

# 1. All permutations
def permutations(word, built=""):
    if len(word) == 0:
        print(built)
        return
    for idx in range(len(word)):
        permutations(word[:idx] + word[idx+1:], built + word[idx])

permutations("ABC")

# 2. Longest palindromic substring
def longest_pal(s):
    best = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            part = s[i:j+1]
            if part == part[::-1] and len(part) > len(best):
                best = part
    return best

print(longest_pal("babad"))

# 3. Word frequency
sample = "This is a test this is only a Test"
word_list = sample.lower().split()
counts = {}
for w in word_list:
    counts[w] = counts.get(w, 0) + 1
print(counts)

# 4. Anagram check
a, b = "listen", "silent"
if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")

# 5. Remove duplicates
s = "programming"
output = ""
for ch in s:
    if ch not in output:
        output += ch
print(output)


# -------------------------
# Lists
# -------------------------

# 1. Rotate list
lst = [1, 2, 3, 4, 5]
steps = 2
for _ in range(steps):
    temp = lst.pop()
    lst.insert(0, temp)
print("Rotated list:", lst)

# 2. Merge sorted lists
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
merged, i, j = [], 0, 0
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        merged.append(A[i]); i += 1
    else:
        merged.append(B[j]); j += 1
merged += A[i:]
merged += B[j:]
print("Merged sorted list:", merged)

# 3. Longest increasing subsequence length
arr = [10, 22, 9, 33, 21, 50, 41, 60]
dp = [1]*len(arr)
for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print("Length of LIS:", max(dp))

# 4. Find pairs with sum = target
arr = [1, 2, 3, 4, 5, 6]
target = 7
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair:", (arr[i], arr[j]))

# 5. Remove None and duplicates
items = [1, 2, None, 3, 2, None, 4, 1, 5]
clean = []
for val in items:
    if val is not None and val not in clean:
        clean.append(val)
print("Cleaned list:", clean)


# -------------------------
# Tuples
# -------------------------

# 1. Swap tuples
t1, t2 = (1, 2, 3), (4, 5, 6)
print("Before:", t1, t2)
t1, t2 = t2, t1
print("After:", t1, t2)

# 2. Element-wise sum
T1, T2 = (1, 2, 3), (4, 5, 6)
summed = tuple(T1[i] + T2[i] for i in range(len(T1)))
print("Sum:", summed)

# 3. Convert list of tuples to dict
pairs = [(1, "one"), (2, "two"), (3, "three")]
d = {}
for k, v in pairs:
    d[k] = v
print("Dictionary:", d)

# 4. Count occurrences
t = (1, 2, 3, 2, 4, 1, 2, 5)
freqs = {}
for x in t:
    freqs[x] = freqs.get(x, 0) + 1
print("Counts:", freqs)

# 5. Swap min and max
t = (10, 20, 5, 30, 15)
lst = list(t)
min_i, max_i = lst.index(min(lst)), lst.index(max(lst))
lst[min_i], lst[max_i] = lst[max_i], lst[min_i]
print("Swapped tuple:", tuple(lst))


# -------------------------
# Sets
# -------------------------

# 1. Elements in exactly two sets
A, B, C = {1,2,3,4}, {3,4,5,6}, {4,6,7,8}
res = (A & B - C) | (A & C - B) | (B & C - A)
print("Exactly two sets:", res)

# 2. Check disjoint
A, B = {1,2,3}, {4,5,6}
if A & B:
    print("Not disjoint")
else:
    print("Disjoint")

# 3. Symmetric difference
X, Y = {1,2,3}, {3,4,5}
sym = (X-Y) | (Y-X)
print("Sym diff:", sym)

# 4. Unique vowels
txt = "Python Programming is Fun"
vowels = {c for c in txt if c.lower() in "aeiou"}
print("Vowels:", vowels)

# 5. Prime factors
n = int(input("Enter a number: "))
factors = set()
div = 2
num = n
while div <= num:
    if num % div == 0:
        factors.add(div)
        num //= div
    else:
        div += 1
print("Prime factors:", factors)


# -------------------------
# Dictionaries
# -------------------------

# 1. Character frequency
s = "hello world"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# 2. Merge dicts (sum common keys)
d1, d2 = {"a":1, "b":2}, {"b":3, "c":4}
merged = dict(d1)
for k, v in d2.items():
    merged[k] = merged.get(k, 0) + v
print(merged)

# 3. Invert dict
d = {"a":1, "b":2}
inv = {}
for k, v in d.items():
    inv[v] = k
print(inv)

# 4. Group words by first letter
words = ["apple", "banana", "apricot", "blueberry"]
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
print(groups)

# 5. Key with max value
d = {"a":10, "b":50, "c":30}
print(max(d, key=d.get))
