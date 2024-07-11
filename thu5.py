
def shape(lis):
    
    for num in lis:
        output = ''

        while num > 0:
            output += "*"

            num = num -1
        print( output)


print(shape([2,3,4,5,6]))