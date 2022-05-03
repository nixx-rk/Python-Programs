#FizzBuzz
#for numbers from 1 to 100
# FizzBuzz if num is divisible by both 5 and 3 
# Fizz for num divisible by 3 only
# Buzz for num divisible by 5 only


print('{:^10}'.format('Number'))
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('{:^10}:{:^10}'.format(i,'FizzBuzz'))
    elif i%3==0:
        print('{:^10}:{:^10}'.format(i,'Fizz'))
    elif i%5==0:
        print('{:^10}:{:^10}'.format(i,'Buzz'))
    else:
        print('{:^10}:{:^10}'.format(i,'*'))
print('\n{:^21}'.format('*****'))