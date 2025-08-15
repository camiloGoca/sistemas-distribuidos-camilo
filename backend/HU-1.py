# HU-2-qa: validaciones, persistencia de historial y CLI simple
from pathlib import Path

history = []
HISTORY_FILE = Path(".calc_history.txt")

def _to_number(x):
    try:
        return float(x)
    except Exception:
        raise ValueError(f"Valor no numérico: {x}")

def add(a, b):
    a, b = _to_number(a), _to_number(b)
    res = a + b
    history.append(f"{a} + {b} = {res}")
    return res

def sub(a, b):
    a, b = _to_number(a), _to_number(b)
    res = a - b
    history.append(f"{a} - {b} = {res}")
    return res

def mul(a, b):
    a, b = _to_number(a), _to_number(b)
    res = a * b
    history.append(f"{a} * {b} = {res}")
    return res

def div(a, b):
    a, b = _to_number(a), _to_number(b)
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    res = a / b
    history.append(f"{a} / {b} = {res}")
    return res

def get_history():
    return list(history)

def clear_history():
    history.clear()

def save_history(filepath=HISTORY_FILE):
    with open(filepath, "a", encoding="utf-8") as f:
        for line in history:
            f.write(line + "\n")
    return str(filepath)

if __name__ == "__main__":
    print("Calculadora (HU-2). Comandos:")
    print("  add a b | sub a b | mul a b | div a b | history | clear | save | exit")
    while True:
        try:
            raw = input("> ").strip()
            if not raw:
                continue
            if raw == "exit":
                break
            if raw == "history":
                print("\n".join(get_history()) or "(vacío)")
                continue
            if raw == "clear":
                clear_history()
                print("Historial limpiado.")
                continue
            if raw == "save":
                path = save_history()
                print(f"Historial guardado en {path}")
                continue

            parts = raw.split()
            cmd = parts[0]
            if cmd in {"add", "sub", "mul", "div"} and len(parts) == 3:
                a, b = parts[1], parts[2]
                fn = {"add": add, "sub": sub, "mul": mul, "div": div}[cmd]
                print(fn(a, b))
            else:
                print("Comando no reconocido.")
        except Exception as e:
            print(f"Error: {e}")
