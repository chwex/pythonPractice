def collatz(number):
    if number%2==0:
        print(str(number // 2))
        return (number // 2)
    elif number == 1:
        print(number)
        return number
    else:
        print(str(3 * number + 1))
        return (3 * number + 1)

print('Enter number:')
try:
    number = int(input())
except ValueError:
    print('You must enter an interger')
    exit()

while number != 1:
    number = collatz(number)
