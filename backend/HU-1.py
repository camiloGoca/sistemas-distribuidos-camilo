# HU-1-qa: validaciones, persistencia de historial y CLI simple (corregido)
from __future__ import annotations
from pathlib import Path
from typing import List, Optional

history: List[str] = []
HISTORY_FILE = Path(".calc_history.txt")
_EPS = 1e-15  # umbral para tratar casi-cero en división


def _to_number(x) -> float:
    """
    Convierte entrada a float.
    Acepta strings con coma decimal, p.ej. "3,5" -> 3.5
    """
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        s = x.strip()
        if not s:
            raise ValueError("Valor vacío.")
        # Soporte simple para coma decimal
        s = s.replace(",", ".")
        return float(s)
    raise ValueError(f"Valor no numérico: {x!r}")


def add(a, b) -> float:
    a, b = _to_number(a), _to_number(b)
    res = a + b
    history.append(f"{a} + {b} = {res}")
    return res


def sub(a, b) -> float:
    a, b = _to_number(a), _to_number(b)
    res = a - b
    history.append(f"{a} - {b} = {res}")
    return res


def mul(a, b) -> float:
    a, b = _to_number(a), _to_number(b)
    res = a * b
    history.append(f"{a} * {b} = {res}")
    return res


def div(a, b) -> float:
    a, b = _to_number(a), _to_number(b)
    if abs(b) < _EPS:
        raise ZeroDivisionError("División por (casi) cero no permitida")
    res = a / b
    history.append(f"{a} / {b} = {res}")
    return res


def get_history() -> List[str]:
    return list(history)


def clear_history() -> None:
    history.clear()


def save_history(filepath: Path = HISTORY_FILE) -> Optional[str]:
    """
    Guarda solo si hay historial. Devuelve la ruta si guardó, None si no.
    """
    if not history:
        return None
    with open(filepath, "a", encoding="utf-8") as f:
        for line in history:
            f.write(line + "\n")
    return str(filepath)


def _print_help() -> None:
    print(
        "Comandos:\n"
        "  add a b | sub a b | mul a b | div a b\n"
        "  history  (muestra historial)\n"
        "  clear    (limpia historial en memoria)\n"
        "  save     (guarda historial en .calc_history.txt)\n"
        "  help     (muestra esta ayuda)\n"
        "  exit|quit|salir"
    )


if __name__ == "__main__":
    print("Calculadora (HU-2 corregida). Escribe 'help' para ver comandos.")
    while True:
        try:
            raw = input("> ").strip()
            if not raw:
                continue

            parts = raw.split()
            cmd = parts[0].lower()

            # Comandos sin argumentos
            if cmd in {"exit", "quit", "salir"}:
                break
            if cmd == "help":
                _print_help()
                continue
            if cmd == "history":
                hist = get_history()
                if not hist:
                    print("(historial vacío)")
                else:
                    for i, line in enumerate(hist, 1):
                        print(f"{i:02d}. {line}")
                continue
            if cmd == "clear":
                clear_history()
                print("Historial limpiado.")
                continue
            if cmd == "save":
                path = save_history()
                if path:
                    print(f"Historial guardado en {path}")
                else:
                    print("Nada que guardar (historial vacío).")
                continue

            # Comandos con 2 argumentos
            if cmd in {"add", "sub", "mul", "div"}:
                if len(parts) != 3:
                    print("Uso: add|sub|mul|div <a> <b>  (ej: add 3 4)")
                    continue
                a, b = parts[1], parts[2]
                fn = {"add": add, "sub": sub, "mul": mul, "div": div}[cmd]
                print(fn(a, b))
                continue

            print("Comando no reconocido. Escribe 'help' para ver opciones.")
        except Exception as e:
            print(f"Error: {e}")
