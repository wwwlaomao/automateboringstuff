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
    widths = []
    for col in table:
        max_row = max(max_row, len(col))
        col_width = 0
        for el in col:
            col_width = max(col_width, len(el))
        widths.append(col_width)

    # Add padding spaces
    # Waring: a list which may be even larger then the original one is created
    # This is not scalable for large table
    justified = []
    for col, width in zip(table, widths):
        row = []
        for el in col:
            row.append(el.rjust(width))
        # Add additional spaces to the columns shorter than the longest
        for padding in range(len(col), max_row):
            row.append(' '.rjust(width))
        justified.append(row)

    # Group the words into rows
    # Waring: a list which may be even larger then the original one is created
    # This is not scalable for large table
    rows = [ [] for i in range(max_row) ]
    for col in justified:
        for row in range(len(col)):
            rows[row].append(col[row])

    # Print the rows
    for row in rows:
        print(' '.join(row))

print('Table 1')
print_table(table1)
print('Table 2')
print_table(table2)
