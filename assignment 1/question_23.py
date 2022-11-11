#Write a code that displays the sum of all the even numbers from the given list.

numbers = [12, 75, 150, 180, 145, 525, 50]
sum = 0
for n in numbers:
    if n%2==0:
        sum +=n

print("sum of all the even numbers = ",sum)