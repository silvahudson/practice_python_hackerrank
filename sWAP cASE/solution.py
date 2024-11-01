def swap_case(s):
    swap_lst = []
    for i in range(len(s)):
        letter = s[i]
        if letter.islower():
            swap_lst.append(letter.upper())
        elif letter.isupper():
            swap_lst.append(letter.lower())
        else:
            swap_lst.append(letter)
    return(''.join(swap_lst))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)