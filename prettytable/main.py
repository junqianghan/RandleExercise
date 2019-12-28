#!/usr/bin/python

from prettytable import PrettyTable

table = PrettyTable(['姓名','身高','体重'])
table.add_row(['h',165,66])
print(table)
