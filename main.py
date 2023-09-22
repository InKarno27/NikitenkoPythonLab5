"""
Лабораторная 5 Вариант 9
Написать функцию, которая принимает путь к файлу и параметр x, который может являться строкой или списком, и
возвращает частоту повторений параметра x в строке. В случае, когда параметром x является список, следует
вернуть словарь, в котором в качестве ключей будут искомые строки, а их значениями частота повторений.
"""

def count_occurrences(file_path, x):
    with open(file_path, 'r') as f:
        text = f.read()
    if isinstance(x, str):
        return text.count(x)
    elif isinstance(x, list):
        result = {}
        for item in x:
            result[item] = text.count(item)
        return result
    else:
        raise TypeError('x should be a string or a list')

file_path = 'example.txt'
x = 'Python'
count = count_occurrences(file_path, x)
print(count)

x = ['Python', 'programming']
count = count_occurrences(file_path, x)
print(count)