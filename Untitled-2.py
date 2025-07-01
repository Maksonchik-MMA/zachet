def count_digits(number):
    digit_counts = {}
    for digit in str(number):
        digit_counts[digit] = digit_counts.get(digit, 0) + 1
    return digit_counts


print(count_digits(12345))      
print(count_digits(112233))     
print(count_digits(100500))   