import re

cpf = "800.849.339-98"
main = re.compile("[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}")
x = re.fullmatch(main, cpf)
print(x)
