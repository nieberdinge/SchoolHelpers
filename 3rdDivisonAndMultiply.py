
def multiply():
    # print("Enter the multiplicand \nexample: '0010'")
    # multiplicand = input("Multiplicand: ")

    # print("Enter product as one string\nexample: '00000011'")
    # product = input("Product:")
    
    multiplicand = '0110'
    product = '00000010'
    multiplicand = int(multiplicand,2)
    product = int(product,2)

    stepStr = "|{:^11}|{:^26}|{:^18}|{:^11}|".format('Iteration','Step', 'Multiplicand', 'Product')
    topRow = ''
    for x in range(len(stepStr)):
        if stepStr[x] == '|':
            topRow += '+'
        else:
            topRow += '-'
    step = '1 -> Prod = Prod + Mcand'
    shiftStep = 'Shift right Product'
    noStep = '0 -> No operation'

    #Making the table
    print(topRow)
    print(stepStr)
    print(topRow)
    print("|{:^11}|{:^26}|       {:04b}       |  {:08b} |".format(0,'Initial Step', multiplicand,product))
    print(topRow)
    for x in range(8):
        #If it is the first
        if(x % 2 == 0):
            if(str(bin(product))[2:][-1] == '0'):
                print("|{0:^11}|{1:^26}|       {2:04b}       |  {3:08b} |".format(x/2+1,noStep,multiplicand,product))
            else:
                binToStr = str(bin(product))[2:]
                while len(binToStr) < 8:
                    binToStr = '0' + binToStr
                number = int(binToStr[0:4],2) + multiplicand
                number = str(bin(number))[2:]
                while len(number) < 4:
                    number = '0' + number
                lastFour = str(bin(product)[2:])[-4:]
                while len(lastFour) < 4:
                    lastFour = '0' + lastFour
                product = int(number + lastFour,2)
                print("|{0:^11}|{1:^26}|       {2:04b}       |  {3:08b} |".format(x/2+1,step,multiplicand,product))
        #Shift to the right
        else:
            product = product >> 1
            if(len(str(product)) > 8):
                product = int(str(product)[1:],2)
            print("|{0:^11}|{1:^26}|       {2:04b}       |  {3:08b} |".format('',shiftStep,multiplicand,product))
            print(topRow)




if __name__ == "__main__":
    # print("1. Multiply\n2. Divide\n3. Exit")
    # ans = input("Response:")
    # ans = int(ans)
    # while(ans < 1 or ans > 3):
    #     ans = input("Enter a correct response (1 - 3): ")
    # ans = int(ans)
    ans = 1
    if ans == 1:
        multiply()
    elif ans == 2:
        print("Too complicated")
        #divide()
    else:
        print("Thanks for using")


    