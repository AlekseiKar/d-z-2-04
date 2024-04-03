def transform_number(a, b):
    if a > b:
        print("Невозможно")
        return
    
    while a != b:
        if b % 2 == 0 and b > a:
            b //= 2
        elif str(b)[-1] == '1' and b > a:
            b = int(str(b)[:-1])
        else:
            print("Невозможно")
            return
    
   
