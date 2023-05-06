import random

try:
    symbols_count = int(input('Enter symbols count: '))
except:
    symbols_count = 0
    print(" you can only type numbers in range of 10")
try:
    numbers_count = int(input('Enter numbers count: '))
except:
    numbers_count = 0
    print(" you can only type numbers in range of 10")
try:
    letters_count = int(input('Enter letters count: '))
except:
    letters_count = 0
    print(" you can only type numbers in range of 10")
try:
    big_letters_count = int(input('Enter big letters count: '))
except:
    big_letters_count = 0
    print(" you can only type numbers in range of 10")
spec_symb = [chr(random.randint(33, 47)) for i in range(symbols_count)]
numbers = [chr(random.randint(48, 57)) for i in range(numbers_count)]
letters = [chr(random.randint(97, 122)) for i in range(letters_count)]
big_letters = [chr(random.randint(65, 90)) for i in range(big_letters_count)]

password = spec_symb + numbers + letters + big_letters
random.shuffle(password)
password = ''.join(password)
print(password)

