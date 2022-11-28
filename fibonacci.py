n_terms = int(input("how many terms the user wants to print:"))
# first two terms
n1 = 0
n2 = 1
count = 0
# now,we will check if the number is valid or not
if n_terms <=0:
    print("please enter a positive integer, the given number is not valid")
    # if there is only one term,it will return n1
elif n_terms == 1:
    print("the fibonacci sequence of the numbers up to",n_terms,":")
    print(n1)
    # then we will generate fibonacci sequence of number
else:
    print("the fibonacci sequence of the number is:")
    while count<n_terms:
        print(n1)
        nth = n1+n2
        #at last,we will update values
        n1 = n2
        n2 = nth
        count += 1        

