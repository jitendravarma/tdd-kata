from add import add

# simple testcase
assert add("") == 0
assert add("1") == 1
assert add("1,2") == 3

# test case to handle new line
assert add("1,\n6") == 7
# test case to handle multiple new line
assert add("2,\n3\n\n") == 5

# to test special delimiters
assert add("//;\n1;2") == 3
assert add("//@\n1@2") == 3

# validate negative numbers
try:
    add("//;\n1;-2;3")
except ValueError as e:
    assert str(e) == "negative numbers not allowed: -2"
