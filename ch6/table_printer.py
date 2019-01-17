#!/usr/bin/env python3

# Some columns are longer than others
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose', 'duck']]

# Find out the number of rows of the longest columns and the longest width of each column
maxRow = 0
widths = []
for col in tableData:
    maxRow = max(maxRow, len(col))
    maxWidth = 0
    for el in col:
        maxWidth = max(maxWidth, len(el))
    widths.append(maxWidth)

# Add padding spaces
justified = []
for col, width in zip(tableData, widths):
    row = []
    for el in col:
        row.append(el.rjust(width))
    # Add additional spaces to the columns shorter than the longest
    for padding in range(len(col), maxRow):
        row.append(' '.rjust(width))
    justified.append(row)

# Group the words into rows
rows = [ [] for i in range(maxRow) ]
for col in justified:
    for row in range(len(col)):
        rows[row].append(col[row])

# Print the rows
for row in rows:
    print(' '.join(row))
