""" 
Multiplica¸c˜ ao com *args e verifica¸c˜ ao de tipo
 Crie uma fun¸c˜ao que multiplica todos os argumentos num´ericos, ignorando qualquer
 argumento que n˜ao seja int ou float
"""

def mult(*args):
    result = 0
    mult = 1
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            op = mult * i
            mult = op
    return mult
            
print(mult(10, "Maria", 3.5, "texto", 7, [1,2], 4))
            
