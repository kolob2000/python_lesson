digit_sum = 0
num = 6859
while num:
    digit_sum += num % 10
    num = num // 10
print(digit_sum)