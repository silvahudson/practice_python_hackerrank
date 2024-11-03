def print_formatted(number):
    # your code goes here
    for i in range(1,n+1):
         print(i,'',str(int(oct(i),8)),'',str(int(hex(i),16)),'',bin(i)[2:])
         
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
