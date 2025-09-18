import math

# Datos
datos = [
    {"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True},
    {"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False},
    {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False},
    {"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False},
    {"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True},
    {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False}
]

# Separar ejemplos positivos y negativos
positivos = [p for p in datos if p["en_formacion"]]
negativos = [p for p in datos if not p["en_formacion"]]

# Algoritmo FOIL simplificado: inducir condiciones
def inducir_regla(positivos, negativos):
    atributos = ["edad", "departamento", "nivel_educativo"]
    regla = {}
    for atributo in atributos:
        valores_pos = set(p[atributo] for p in positivos)
        valores_neg = set(p[atributo] for p in negativos)

        if atributo == "edad":
            valores_validos = [v for v in valores_pos if v not in valores_neg]
        else:
            valores_validos = list(valores_pos - valores_neg)

        if valores_validos:
            regla[atributo] = valores_validos
    return regla

# Ejecutar el algoritmo
regla_inducida = inducir_regla(positivos, negativos)

print("-----------------------------------------------------------------------------------")
print("Regla inducida para identificar a un alumno:")
for atributo, valores in regla_inducida.items():
    print(f"- {atributo} debe ser uno de: {valores}")

# Valores antes de aplicar la condición
P = sum(1 for d in datos if d["en_formacion"])
N = sum(1 for d in datos if not d["en_formacion"])

# Aplicar condición: nivel_educativo == terciario
filtrados = [d for d in datos if d["nivel_educativo"] == "terciario"]
p = sum(1 for d in filtrados if d["en_formacion"])
n = sum(1 for d in filtrados if not d["en_formacion"])

# Cálculo FOIL Gain
def log2_safe(x):
    return math.log2(x) if x > 0 else float('-inf')

foil_gain = p * (log2_safe(p / (p + n)) - log2_safe(P / (P + N)))

# Mostrar resultados
print(f"P = {P}, N = {N}")
print(f"p = {p}, n = {n}")
print(f"p / (p + n) = {p / (p + n):.3f}")
print(f"P / (P + N) = {P / (P + N):.3f}")
print(f"log2(p / (p + n)) = {log2_safe(p / (p + n)):.3f}")
print(f"log2(P / (P + N)) = {log2_safe(P / (P + N)):.3f}")
print(f"FOIL Gain = {foil_gain:.3f}")
print("-----------------------------------------------------------------------------------")

print("Regla inducida para identificar a un alumno:")
for atributo, valores in regla_inducida.items():
    print(f"- {atributo} debe ser uno de: {valores}")

# Valores antes de aplicar la condición
P = sum(1 for d in datos if d["en_formacion"])
N = sum(1 for d in datos if not d["en_formacion"])

filtrados = [d for d in datos if d["edad"] <= 23]
p = sum(1 for d in filtrados if d["en_formacion"])
n = sum(1 for d in filtrados if not d["en_formacion"])

# Cálculo FOIL Gain
def log2_safe(x):
    return math.log2(x) if x > 0 else float('-inf')

foil_gain = p * (log2_safe(p / (p + n)) - log2_safe(P / (P + N)))

# Mostrar resultados
print(f"P = {P}, N = {N}")
print(f"p = {p}, n = {n}")
print(f"p / (p + n) = {p / (p + n):.3f}")
print(f"P / (P + N) = {P / (P + N):.3f}")
print(f"log2(p / (p + n)) = {log2_safe(p / (p + n)):.3f}")
print(f"log2(P / (P + N)) = {log2_safe(P / (P + N)):.3f}")
print(f"FOIL Gain = {foil_gain:.3f}")
