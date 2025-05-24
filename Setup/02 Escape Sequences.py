# Escape Sequence	Meaning
# \	Backslash (\)
# \'	Single quote (')
# \"	Double quote (")
# \n	ASCII Linefeed (adds newline)
# \b	ASCII Backspace
# \r	Carriage Return
# \t	Horizontal Tab
# \v	Vertical Tab
# \f	Formfeed
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh
# \0	Null character
# \a	ASCII Bell (alert)
# \e	ASCII Escape
# \c	ASCII Control
# \N{name}	Character named name in the Unicode database
# \uxxxx	Character with 16-bit hex value xxxx

print("List of all escape sequences in Python:")
print("Backslash: \\")
print("Single quote: \'")
print("Double quote: \"")
print("ASCII Linefeed (newline): \nNext line")
print("ASCII Backspace: abc\bdef")
print("Carriage Return: abc\rdef")
print("Horizontal Tab: a\tb")
print("Vertical Tab: a\v b")
print("Formfeed: a\f b")
print("Octal value: \101")  # 'A'
print("Hex value: \x41")    # 'A'
print("Null character: \0")
print("ASCII Bell: \a")
# Note: \e and \c are not standard in Python
print("Unicode name: \N{GREEK CAPITAL LETTER DELTA}")
print("16-bit Unicode: \u0394")  # 'Δ'
print("32-bit Unicode: \U0001F600")  # 😀
'''
Multiple lines of text in comments
'''

"""
This is a multi-line string
This is the second line of the multi-line string
"""