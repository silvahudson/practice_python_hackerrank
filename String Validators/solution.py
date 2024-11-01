if __name__ == '__main__':
    s = input().strip()
    
    my_dict = {}
    my_dict['alphanumeric']    = False
    my_dict['alphabetical']    = False
    my_dict['digit']           = False
    my_dict['lower']           = False
    my_dict['uppercase']       = False
    for char in s:
        if char.isalnum():
            my_dict['alphanumeric'] = True 
        if char.isalpha():
            my_dict['alphabetical'] = True 
        if char.isdigit():
            my_dict['digit'] = True 
        if char.islower():
            my_dict['lower'] = True
        if char.isupper():
            my_dict['uppercase'] = True  
            
    for i in my_dict.values():
        print(i)
        
