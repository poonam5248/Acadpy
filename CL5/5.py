#Using range(1,101), make a list containing even and odd numbers.
even=[]
odd=[]
for x in range(1,101):
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("even numbers are : "+ str(even))
print("odd numbers are : "+ str(odd))
