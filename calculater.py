# marke a calculater
a=input('Enter first number :')
operator=input('1. Addition \n 2. Subtration \n 3. Multipication \n 4. Divided \n 5. Remander \n Choose the option :')
b=input('Enter second number :')
a=int(a)
b=int(b)
if operator=='1':
    print(a+b)
elif operator=='2':
    print(a-b)
elif operator=='3':
    print(a*b)
elif operator=='4':
    print(a%b)
elif operator=='5':
    print(a/b)
else:
    print('THIS IS NOT VALID \n Please try agen!')