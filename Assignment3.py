#Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
odd_no_count=0
even_no_count=0
for i in numbers:
    if i%2==0:
        even_no_count=even_no_count+1
    else:
        odd_no_count=odd_no_count+1
print("Count of even numbers: ",even_no_count)
print("Count of odd numbers: ",odd_no_count)
        