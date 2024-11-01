if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    st = set(arr)
    lst = list(st)
    maximo = max(lst)
    lst.remove(maximo)
    runner_up = max(lst)
    print(runner_up)