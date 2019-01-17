#!/usr/bin/env python3
# An insecure password locker program.

import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Copy account password to system clipboard')
    print('Usage: python3 password_locker.py [account]')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard.')
else:
    print(f'There is no account named {account}.')
