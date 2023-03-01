# Sequence Generator

print('')

while True:
    response = input('Enter the starting number(e.g. 0): ')
    if response == '':
        response = '0'  # Start at 0 by default
        break
    if response.isdecimal():
        break
    print('Please Enter a number greater than "0".')
start = int(response)

while True:
    response = input('Enter how many number\'s to display(e.g 100): ')
    if response == '':
        response = '100'  # Display 100 number by default
        break
    if response.isdecimal():
        break
    print('Please Enter a number.')

amount = int(response)

for number in range(start, start+amount):  # Main loop
    # Convert to Hexdecimal/binary and remove the prefix
    hex_number = hex(number)[2:].upper()
    bin_number = bin(number)[2:]
    print('DEC:', number, 'HEX:', hex_number, 'BIN:', bin_number)
