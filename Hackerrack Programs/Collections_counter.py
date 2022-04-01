# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

number_of_shoes = int(input())
shoes_list = list(map(int, input().split()))
# print(shoes_list)
shoes_count = Counter(shoes_list)
# print(shoes_count.items())
number_of_customers = int(input())
earnings = 0
for x in range(int(number_of_customers)):
    size, x_i = map(int, input().split())
    if size in shoes_count and shoes_count[size] > 0:
        shoes_count[size] -= 1
        earnings += x_i
print(earnings)

""" Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

output
200
"""
