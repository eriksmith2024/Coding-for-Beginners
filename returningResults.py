# num = input('Enter an Integer:')

# # def square( num ):
# #     if not num.isdigit():
# #         return 'Invalid Entry'
# #     num = int(num)
# #     return num * num

# # print( num, 'Squared is:', square( num ))



def square(num):
    return num * num

while True:
    num = input('Enter an Integer: ')
    if num.isdigit():
        num = int(num)
        print(num, 'Squared is:', square(num))
        break
    else:
        print('Invalid Entry. Please enter a valid integer.')
