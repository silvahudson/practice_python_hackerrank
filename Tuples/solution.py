# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    
    print(t)
    h = hash(t)
    print(h)


