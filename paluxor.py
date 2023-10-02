from luxor import lexer

data = "Select name ,FroM table_2 WHEre a2 = 15"
lexer.input(data)
# Imprimir los tokens encontrados
for token in lexer:
    print(f"Token: {token.type}, Valor: {token.value}")