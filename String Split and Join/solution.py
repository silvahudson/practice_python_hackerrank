def split_and_join(line):
    lst_string = line.split()
    return('-'.join(lst_string))
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)