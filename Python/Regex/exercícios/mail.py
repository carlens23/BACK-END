import re

cpf = "mamadou89@gmail.com"
main = re.compile("[\w]+@[\w]+\.com")
x = re.fullmatch(main, cpf)
print(x)
