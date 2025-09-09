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

# -------------------------
# If-Logic & Match-Case
# -------------------------

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
    if i % 35 == 0: print("FizzBuzz")
    elif i % 5 == 0: print("Fizz")
    elif i % 7 == 0: print("Buzz")
    else: print(i)

# 3. Calculator
x = int(input("Enter first: "))
y = int(input("Enter second: "))
op = input("Enter operator: ")
match op:
    case "+": print(x+y)
    case "-": print(x-y)
    case "*": print(x*y)
    case "/": print(x/y if y!=0 else "Div by zero not allowed")
    case _: print("Invalid operator")

# 4. Leap year
yr = int(input("Enter year: "))
if (yr % 400 == 0) or (yr % 100 != 0 and yr % 4 == 0): print("Leap Year")
else: print("Not Leap Year")

# 5. Identify char
ch = input("Enter char: ")
if ch.isalpha():
    if ch.lower() in "aeiou": print("Vowel")
    else: print("Consonant")
elif ch.isdigit(): print("Digit")
else: print("Special Character")


# -------------------------
# Functions
# -------------------------

# 1. GCD & LCM
def gcd(a,b):
    while b: a,b = b,a%b
    return a
def lcm(a,b): return (a*b)//gcd(a,b)
print("GCD:", gcd(12,18))
print("LCM:", lcm(12,18))

# 2. Second largest
nums = [10,20,4,45,99]
m1,m2 = float("-inf"),float("-inf")
for n in nums:
    if n>m1: m1,m2 = n,m1
    elif n>m2 and n!=m1: m2=n
print("Second largest:",m2)

# 3. Palindrome string
txt = "Never Odd Or Even"
s = "".join(c.lower() for c in txt if c!=" ")
print("Palindrome" if s==s[::-1] else "Not Palindrome")

# 4. Multiplication tables
for n in range(1,6):
    for k in range(1,11): print(f"{n} x {k} = {n*k}")
    print()

# 5. Recursive digit sum
def dsum(x):
    if x==0: return 0
    return (x%10)+dsum(x//10)
print(dsum(1234))


# -------------------------
# Strings
# -------------------------

# 1. All permutations
def perm(word,cur=""):
    if not word: print(cur); return
    for i in range(len(word)): perm(word[:i]+word[i+1:],cur+word[i])
perm("ABC")

# 2. Longest palindromic substring
def longpal(s):
    best=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            part=s[i:j+1]
            if part==part[::-1] and len(part)>len(best): best=part
    return best
print(longpal("babad"))

# 3. Word frequency
txt="This is a test this is only a Test"
words=txt.lower().split()
freq={}
for w in words: freq[w]=freq.get(w,0)+1
print(freq)

# 4. Anagram
a,b="listen","silent"
print("Anagram" if sorted(a)==sorted(b) else "Not Anagram")

# 5. Remove duplicates
s="programming"; out=""
for c in s:
    if c not in out: out+=c
print(out)


# -------------------------
# Lists
# -------------------------

# 1. Rotate list
lst=[1,2,3,4,5]; steps=2
for _ in range(steps): lst.insert(0,lst.pop())
print("Rotated:",lst)

# 2. Merge sorted lists
A,B=[1,3,5,7],[2,4,6,8]; i=j=0; m=[]
while i<len(A) and j<len(B):
    if A[i]<B[j]: m.append(A[i]); i+=1
    else: m.append(B[j]); j+=1
m+=A[i:]; m+=B[j:]
print("Merged:",m)

# 3. LIS length
arr=[10,22,9,33,21,50,41,60]
dp=[1]*len(arr)
for i in range(1,len(arr)):
    for j in range(i):
        if arr[i]>arr[j]: dp[i]=max(dp[i],dp[j]+1)
print("LIS:",max(dp))

# 4. Pairs with sum
arr=[1,2,3,4,5,6]; tgt=7
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==tgt: print("Pair:",(arr[i],arr[j]))

# 5. Remove None + dups
items=[1,2,None,3,2,None,4,1,5]; clean=[]
for v in items:
    if v and v not in clean: clean.append(v)
print("Cleaned:",clean)


# -------------------------
# Tuples
# -------------------------

# 1. Swap
t1,t2=(1,2,3),(4,5,6)
print("Before:",t1,t2)
t1,t2=t2,t1
print("After:",t1,t2)

# 2. Element sum
T1,T2=(1,2,3),(4,5,6)
print(tuple(T1[i]+T2[i] for i in range(len(T1))))

# 3. List of tuples to dict
pairs=[(1,"one"),(2,"two"),(3,"three")]
d={}
for k,v in pairs: d[k]=v
print(d)

# 4. Count
t=(1,2,3,2,4,1,2,5); freq={}
for x in t: freq[x]=freq.get(x,0)+1
print(freq)

# 5. Swap min/max
t=(10,20,5,30,15); l=list(t)
mi,ma=l.index(min(l)),l.index(max(l))
l[mi],l[ma]=l[ma],l[mi]
print(tuple(l))


# -------------------------
# Sets
# -------------------------

# 1. Exactly two sets
A,B,C={1,2,3,4},{3,4,5,6},{4,6,7,8}
print((A&B-C)|(A&C-B)|(B&C-A))

# 2. Disjoint
A,B={1,2,3},{4,5,6}
print("Not disjoint" if A&B else "Disjoint")

# 3. Sym diff
X,Y={1,2,3},{3,4,5}
print((X-Y)|(Y-X))

# 4. Unique vowels
txt="Python Programming is Fun"
print({c for c in txt if c.lower() in "aeiou"})

# 5. Prime factors
n=int(input("Enter num: ")); f=set(); d=2
while d<=n:
    if n%d==0: f.add(d); n//=d
    else: d+=1
print(f)


# -------------------------
# Dictionaries
# -------------------------

# 1. Char freq
s="hello world"; freq={}
for c in s: freq[c]=freq.get(c,0)+1
print(freq)

# 2. Merge dicts
d1,d2={"a":1,"b":2},{"b":3,"c":4}
m=dict(d1)
for k,v in d2.items(): m[k]=m.get(k,0)+v
print(m)

# 3. Invert dict
d={"a":1,"b":2}; inv={}
for k,v in d.items(): inv[v]=k
print(inv)

# 4. Group words
words=["apple","banana","apricot","blueberry"]
g={}
for w in words: g.setdefault(w[0],[]).append(w)
print(g)

# 5. Key with max
d={"a":10,"b":50,"c":30}
print(max(d,key=d.get))

