# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()
n, m = int(n), int(m)

line = "-"
column = ".|."
welcome = "WELCOME"

for i in range(1, n):
    
    if i <= (n - 1) / 2:
        print((column * (i * 2 - 1)).center(m, line))

    if i == (n - 1) / 2:
        print(welcome.center(m, line))

    if i > (n - 1) / 2:
        print((column * ((n - i) * 2 - 1)).center(m, line))