str = input("Enter the string :")
ch = input("Enter the character you want too :")
i = 0
count = 0
while(i < len(str)):
    if(str[i]== ch):
        count = count + 1
    i = i + 1
print("the total number of times ", ch ,"has occured is ", count ,".")