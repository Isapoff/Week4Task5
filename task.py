# task 1

# def sum_rec(num):

#     if num == 1:
#         return num
#     return (num - 3, num - 2, num - 1, num)

# print(sum_rec(4))


# task 2

# def factorial(num):
#     if num == 0:
#         return 0
#     return num + factorial(num - 1)
# print(factorial(10))


# task 3

# def rev(n):
#     i = 0
#     while(n > 0):
#         i = i * 10 + n % 10
#         n = n // 10
#     return i
# print(rev(567))


# task 4

# def fib(num):
#     if num <= 1:
#         return num
#     return fib(num - 1) + fib(num - 2)
# print(fib(10))

# task 5

# result = dict()

# def stepPerms(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
#     if n not in result:
#         result[n] = stepPerms(n - 1) + stepPerms(n - 2) + stepPerms (n - 3) 
#     return result[n]
















