endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# importar o módulo regular expressions (regex)
import re

# 5 dígitos + hífen (opcional) + 3 dígitos
padrao = re.compile("[0-9]{5}-?[0-9]{3}")  # retorna um objeto Pattern
busca = padrao.search(endereco)  # retorna um objeto Match

if busca:
    cep = busca.group()
    print(cep)
