from string import Template

greet = "Hello"
name = "Yashasvi Haldiya"

temp = Template("$a! This is $b")

print(temp.substitute(a=greet, b=name))