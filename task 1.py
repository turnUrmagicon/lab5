# a = input().lower()
# c = list(a)
# print("Created list is: ", c)

#1.2

str = input()
char_list = list(str.lower())
def freq(char_list):
    i = {}
    for STR in char_list:
        if STR in i:
            i[STR] += 1
        else:
            i[STR] = 1
    frequency_list = [(char, frequency) for char, frequency in i.items()]
    return frequency_list
result = freq(char_list)
print("Result: ", result)

#1.3
str = input()
input_list = list(str.lower())
vowels = 'aeiou'
vow = [i for i in input_list if i in vowels]
cons = [i for i in input_list if i.isalpha() and i not in vowels]
symb = [i for i in input_list if not i.isalpha()]
print("vow =", vow)
print("cons =", cons)
print("symb =", symb)

# 1.4
# try:
#     list_A = input("Write a list of numbers separated by commas: ")#     if not list_A:
#         print("Input is empty!!!")#
#     number_list = [int(x) for x in list_A.split(',')]#     number_list.sort()
##     num = len(number_list)
#     q1 = number_list[:num // 4]#     q2 = number_list[num // 4:num // 2]
#     q3 = number_list[num // 2:3 * num // 4]#     q4 = number_list[3 * num // 4:]
##     print("q1 =", q1)
#     print("q2 =", q2)#     print("q3 =", q3)
#     print("q4 =", q4)#
# except (ValueError, IndexError):#     print("Wrong value or sequence out of range!!! ")