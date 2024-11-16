import re

regex = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s']+$"

checkName = lambda name: re.match(regex, name) is not None