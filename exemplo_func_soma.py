from utils_log import log_decorator

# Definindo funcao decorator
@log_decorator
def soma(x, y):
    return x + y

soma(2,3)
soma(5,5)
soma(4,"2")