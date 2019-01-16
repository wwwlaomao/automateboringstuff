#!/usr/bin/env python3

def concat_list_with_comma(values):
    length = len(values)
    count = 0
    output = ''
    for value in values:
        count = count + 1
        if count > 1:
            if count == length:
                output = output + ' and ' + value
            else:
                output = output + ', ' + value
        else:
            output = output + value
    return output

spam = ['apple', 'banana', 'tofu', 'cats']
print(concat_list_with_comma(spam))
empty = []
print(concat_list_with_comma(empty))
single = ['hello']
print(concat_list_with_comma(single))
double = ['hello', 'world']
print(concat_list_with_comma(double))
