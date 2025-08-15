# HU-1: versión inicial funcional
history = []

def add(a, b):
    res = a + b
    history.append(f"{a} + {b} = {res}")
    return res

def sub(a, b):
    res = a - b
    history.append(f"{a} - {b} = {res}")
    return res

def mul(a, b):
    res = a * b
    history.append(f"{a} * {b} = {res}")
    return res

def div(a, b):
    # Versión inicial: no valida división por cero (se mejora en HU-2)
    res = a / b
    history.append(f"{a} / {b} = {res}")
    return res

def get_history():
    return list(history)

if __name__ == "__main__":
    print("Calculadora (HU-1). Ejemplos rápidos:")
    print(add(2, 3))
    print(sub(5, 1))
    print(mul(4, 6))
    print(div(8, 2))
    print("Historial:", get_history())
