total_sum = 0
count_three_or_five = 0

for num in range(1, 51):
    if num % 2 == 0:
        total_sum += num
        if num % 3 == 0:
            print("Three")
            count_three_or_five += 1
        elif num % 5 == 0:
            print("Three")
            count_three_or_five += 1
        else:
            print(num)
    else:
        pass

print(f"Total sum of all even numbers from 1 to 50 is: {total_sum}")
print(f"The count of numbers replaced with 'Three' or 'Five' is: {count_three_or_five}")