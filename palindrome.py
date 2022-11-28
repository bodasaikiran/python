# using string slicing
num = int(input("enter a number:"))
reverse = int(str(num)[::-1])
if num == reverse:
    print('it is a palindrome')
else:
    print('not a palindrome')    