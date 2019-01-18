#!/usr/bin/env python3

# Some columns are longer than others
table1 = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose', 'duck']]
table2 = []

def print_table(table):
    # Find out the number of rows of the longest columns
    # and the longest width of each column
    max_row = 0
    widths = {}
    for col, index in zip(table, range(len(table))):
        max_row = max(max_row, len(col))
        col_width = 0
        for el in col:
            col_width = max(col_width, len(el))
        widths[index] = col_width
        print(f'{index} - {col_width}')

    # Print rows
    for row in range(max_row):
        for col, index in zip(table, range(len(table))):
            el = ' ';
            if row < len(col):
                el = col[row]
            print(el.rjust(widths[index]) + ' ', end = '')
        print()

print('Table 1')
print_table(table1)
print('Table 2')
print_table(table2)
