# a = input().lower()
# c = list(a)
# print("Created list is: ", c)

str = input()
char_list = list(str.lower())
def freq(char_list):
    i = {}
    for char in char_list:
        if char in i:
            i[char] += 1
        else:
            i[char] = 1
    frequency_list = [(char, frequency) for char, frequency in i.items()]
    return frequency_list
result = freq(char_list)
print("Result: ", result)