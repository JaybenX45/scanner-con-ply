import ply.lex as lex

# Definición de tokens
tokens = (
    'PC',   
    'ID',       
    'OPREL',    
    'SIGNO',    
    'NUMERO',  
)
# Expresiones regulares para tokens
t_PC = r'select|SELECT|from|FROM|where|WHERE|if|IF'
t_OPREL = r'[=<>]'
t_SIGNO= r','
t_NUMERO = r'\d+'
# Función para reconocer identificadores
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value.lower() == 'select':
        t.type = 'PC'
    elif t.value.lower() == 'from':
        t.type = 'PC'
    elif t.value.lower() == 'if':
        t.type = 'PC'
    elif t.value.lower() == 'where':
        t.type = 'PC'
    return t
# Ignorar espacios en blanco
t_ignore = ' \t'
# Función para capturar errores léxicos
def t_error(t):
    print(f"Error léxico: Carácter inesperado '{t.value[0]}'")
    t.lexer.skip(1)
# Crear el analizador léxico
lexer = lex.lex()
# Prueba del analizador léxico
# Select name FroM table2 WHEre a2 = 15
# SELECT col1, col2 from mi_Tabla wHERE col1 < 20
data = "SELECT col1, col2 from mi_Tabla wHERE col1 < 20"
lexer.input(data)
# Imprimir los tokens encontrados
for token in lexer:
    print(f"Token: {token.type}, Valor: {token.value}")