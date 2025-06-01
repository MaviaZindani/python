name = input("What's your name: ")
numbers = int(input("Enter Your Numbers Between 0 or 100: "))

if numbers == 100:
    print(name + ' You are passed with A+')
elif numbers >= 80:
        print(name + ' You are passed with A')
elif numbers >= 60:
        print(name + ' You are passed with B')
elif numbers >= 40:
        print(name + ' You are passed with C')
elif numbers >= 30:
        print(name + ' You are passed with D')
else :
    print(name + ' You are passed with F')