low = int(input("Enter a lower range :"))
up = int(input("Enter an upper range :"))
print("The primes between", low ,"and", up ,"are:")
for num in range(low,up + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
                print(num)