# Program to display the Fibonacci sequence
nTerms = int(input("Number of terms in Fibonacci Sequence? "))
n1, n2 = 0, 1
i = 0
if nTerms <= 0:
    print("Please enter a positive integer")
elif nTerms == 1:
    print("Fibonacci sequence upto"
          ,nTerms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while i < nTerms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        i += 1