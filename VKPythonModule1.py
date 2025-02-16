# Необходимо написать программу, которая будет принимать на вход строку,
# разбивать строку на слова по пробелу. Далее нужно из всех слов убрать следующие пунктуационные знаки:
# !,.?;:#$%^&*(),
# а также привести слова к нижнему регистру.
# В итоге нужно вывести в алфавитном порядке И КАЖДОЕ С НОВОЙ СТРОКИ слова, которые состоят как минимум из 5 символов,
# а также имеют как минимум 4 уникальных символа, и которые встретились в исходном тексте более 2х раз.

str_list = input().split()
new_str_list = []
for string in str_list:
    for ch in '!,.?;:#$%^&*()':
        string = string.replace(ch, '')
    new_str_list.append(string.lower())

#print (new_str_list)

result_list = []
for string in new_str_list:
    if len(string) >= 5 and len(set(string)) >= 4 and new_str_list.count(string) > 2:
        result_list.append(string)

result_list = list(set(result_list))
result_list.sort()
print('\n'.join(result_list))