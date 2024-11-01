import textwrap

def wrap(string, max_width):
    lst = []
    start = 0
    stop = len(string)
    step = max_width
    for i in range(start, stop , step):
        item = string[i:i + max_width] + '\n'
        lst.append(item)
    return ''.join(lst)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)