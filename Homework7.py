# This program reads all the numbers from a file called "numbers.txt"
# The program prints total numbers, total prime numbers, and a list of the prime numbers in the file.

def main():
    numbTotal = 0 
    listOfNumbers = read_file()
    listOfPrimes = []   

    for index in listOfNumbers:
        numbTotal += count_numb(index)
        if is_prime(index) > 0:
            listOfPrimes.append(is_prime(index))

    print_summary(numbTotal, listOfPrimes)

def read_file():
    listOfNumbers = []
    numbersFile = open('numbers.txt', 'r')
    line = numbersFile.readline()

    while line != '':
        line = line.rstrip('\n')
        listOfNumbers.append(line)
        line = numbersFile.readline()

    numbersFile.close()    
    return listOfNumbers

def count_numb(number):
    return 1
    
def is_prime(number):
    number = int(number)
    numberHalved = int(number / 2) # Increases efficiency.

    for index in range(2, numberHalved):
        if(number % index) == 0:
            return 0
    else:
        return number
                    
def print_summary(numbTotal, primeList):
    primeTotal = 0
    for index in primeList:
        primeTotal += count_numb(index)
    
    print('There are', numbTotal, 'numbers in the file.')
    print('There are', primeTotal, 'prime numbers in the file.')

    #print('The prime numbers are:')
    #for primeNumb in primeList:
        #print(primeNumb)

    input('\nPress ENTER to close program:  ')

main()
