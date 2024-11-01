def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if sub_string == string[i:len(sub_string) + i]:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)