#To print Squares of numbers in the given list

my_list=[1,2,3,4,5,6,7,8,9,10]
#my_list=list(map(int,input().split()))             #To take input list of numbers from user

squares={}

print('{:^20}:\t{:^20}'.format("Number","Square"))

for i in my_list:
#for i in range(1,x+1):         #this is for finding squares of numbers from 1 to x
    squares[i]=i*i
    print('{:^20}:\t{:^20}'.format(i,i*i))


print('\n{Number: square of number} : ',squares)