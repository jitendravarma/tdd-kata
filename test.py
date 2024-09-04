from add import add

# simple testcase
assert add("") == 0
assert add("1") == 1
assert add("1,2") == 3

# test case to handle new line
assert add("1,\n6") == 7
# test case to handle multiple new line
assert add("2,\n3\n\n") == 5
