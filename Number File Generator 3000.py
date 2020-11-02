# This program creates a file called "numbers.txt" with a list of random numbers.
# The user is able to choose the list size and quantity of prime numbers.

def main():
    GreetUser()

    # Get user inputs.
    listSize = GetListSize()
    primeQuantity = GetPrimeQuantity(listSize)

    # Write the file.
    WriteFile(listSize, primeQuantity)

    ThankUser()

def GreetUser():
    print('Welcome to Number File Generator 3000!\n\nThis program is designed to ' + 
          'help students in COMSC-122 write a file\ncalled "numbers.txt" ' + 
          'containing a random list of numbers to test their\nprogram for ' + 
          'homework7.')

# Functions that get user inputs...
def GetListSize():
    listSize = input('\nHow many numbers would you like the file to contain?:  ')
    listSize = CheckIfInt(listSize)
    return listSize

def GetPrimeQuantity(listSize):
    primeQuantity = input('\nHow many prime numbers would you like in the file?:  ')
    primeQuantity = CheckIfInt(primeQuantity)
    
    while primeQuantity > listSize:
        try:
            primeQuantity = input('\nQuanity of prime numbers cannot be greater than ' +
                                    'total numbers in list, silly.\nPlease re-enter ' +
                                    'ammount of prime numbers:  ')
            primeQuantity = int(primeQuantity)
        except ValueError:
            primeQuantity = CheckIfInt(primeQuantity)
            
    return primeQuantity

def CheckIfInt(variable):
    inputCheck = False

    while inputCheck == False:    
        try:
            variable = int(variable)
            while variable <= 0:
                variable = int(input('\nInvalid input, please enter a positive number:  '))
            inputCheck = isinstance(variable, int)
        except ValueError:
            variable = input('\nInvalid input, please type a whole number:  ')

    return variable

# Function that writes the file...
def WriteFile(listSize, primeQuantity):
    print('\nGenerating list with', listSize, 'total numbers,',
          primeQuantity, 'of which are prime numbers...')

    # Setup file, list, import, and bool.
    numbersFile = open('numbers.txt', 'w')
    numbersFile.close()    
    numbersFile = open('numbers.txt', 'a')
    listOfNumbers = []
    import random
    isPrime = False

    print('\nGenerating non-prime numbers...')

    # Append random, non-prime numbers to list.
    nonPrimeQuantity = listSize - primeQuantity
    while nonPrimeQuantity > 0:
        randNumb = random.randint(100,9999)
        randNumbHalved = int(randNumb / 2) # Increases efficiency.
        for i in range(2, randNumbHalved):
            if(randNumb % i) == 0:
                listOfNumbers.append(randNumb)               
                nonPrimeQuantity -= 1
                break
            
    print('Non-prime numbers complete!\n\nNow generating prime numbers...')

    # Append random prime numbers to list.
    while primeQuantity > 0:
        isPrime = True
        randNumb = random.randint(100,9999)
        randNumbHalved = int(randNumb / 2)
        for i in range(2, randNumbHalved):
            if(randNumb % i) == 0:
                isPrime = False
        if isPrime == True:
            listOfNumbers.append(randNumb)
            primeQuantity -= 1

    print('Prime numbers complete!\n\nNow sorting numbers in random order...')

    random.shuffle(listOfNumbers)

    print('Sorted!\n\n\nSaving file...')
    
    # Write list to file.
    for i in listOfNumbers:
        i = str(i)
        numbersFile.write(i + '\n')

    numbersFile.close()

def ThankUser():
    input('\nFile created and saved! Thank you for using Number File Generator 3000!' +
          '\nPress ENTER to close program:  ')    

# Call main().
main()
