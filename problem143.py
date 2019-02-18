#Roof
#Problem143
#Running the roof until the input is either even or odd

while True:
    num_str = input("Enter the number : ")
    if num_str.isnumeric():
        num = int(num_str)
        if num==0:
            print("It's 0")            
            continue
        elif num%2==1:
            print("odd number")
            break
        else :
            print("even number")
            break
    else:
        print("It's not a number")
        continue
