# Problem
# Given: A string s
# of length at most 10000 letters.
# Return: The number of occurrences of each word in s
# , where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
# Sample Dataset
# We tried list and we tried dicts also we tried Zen
# Sample Output
# and 1
# We 1
# tried 3
# dicts 1
# list 1
# we 2
# also 1
# Zen 1
input_file = open("file.txt")
output_file = open("result.txt", "w")
my_string = input_file.read()
my_list = my_string.split()
my_dict = {}
for word in my_list:
    if word not in my_dict.keys():
        my_dict[word] = 1
    else:
        my_dict[word] += 1
my_final_string = ''
for pair in list(my_dict.items()):
    print(' '.join(list(map(str, list(pair)))))
input_file.close()
output_file.close()