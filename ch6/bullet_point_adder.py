#!/usr/bin/env python3
# Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')

newLines = []
for line in lines:
    newLines.append(f'* {line}')

text = '\n'.join(newLines)

pyperclip.copy(text)
