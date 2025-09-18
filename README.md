# Trabajo Práctico – Algoritmo de FOIL

**Nombre:** Coral Tolazzi
**Tema:** Algoritmo de FOIL
**Profesora:** Yanina Ximena Scudero
**Cuatrimestre y Año:** 2.º Cuatrimestre del 2025
**Instituto:** Instituto Tecnológico Beltrán
**Materia:** Procesamiento de Aprendizaje Automático

---

## Descripción del trabajo

Este trabajo práctico tiene como objetivo aplicar el **algoritmo FOIL** (First Order Inductive Learner) para inducir reglas lógicas a partir de un conjunto de ejemplos positivos y negativos.
Se busca practicar la identificación de patrones en un dataset de empleados en formación y calcular la **ganancia de información** (FOIL Gain) para distintas condiciones.

El trabajo incluye:

* Separación de ejemplos positivos y negativos.
* Identificación de valores únicos en atributos de los positivos.
* Desarrollo de reglas inducidas para predecir `en_formacion`.
* Cálculo manual y automático del FOIL Gain en Python.
* Interpretación de los resultados.

---

## Dataset de ejemplo

```python
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
```

---

## Ejercicio 1 – Identificación de empleados en formación

### Objetivo

* Separar los ejemplos positivos (`en_formacion == True`) y negativos (`en_formacion == False`).
* Analizar los atributos para identificar valores que aparecen **solo en positivos**.
* Inducir reglas simples basadas en estos atributos.

### Análisis de atributos

| Atributo        | Valores positivos        | Valores negativos       | Observación                                        |
| --------------- | ------------------------ | ----------------------- | -------------------------------------------------- |
| Departamento    | IT, RRHH                 | IT, Finanzas, RRHH      | Ningún valor exclusivo en positivos                |
| Nivel educativo | terciario, universitario | universitario, maestría | Solo "terciario" es exclusivo de positivos         |
| Edad            | 21, 22, 23, 24           | 29, 35, 38, 40          | Todas las edades 21–24 son exclusivas de positivos |

### Regla inducida

```text
Si nivel_educativo == 'terciario' o edad <= 23 ⇒ en_formacion = True
```

---

## Ejercicio 2 – Cálculo de FOIL Gain

FOIL Gain se calcula como:

$$
\text{FOIL Gain} = p \times (\log_2(p / (p+n)) - \log_2(P / (P+N)))
$$

Donde:

* $P, N$ = positivos y negativos antes de aplicar la condición
* $p, n$ = positivos y negativos que cumplen la condición

---

### a) Condición `nivel_educativo == 'terciario'`

| Parámetro         | Valor                  |
| ----------------- | ---------------------- |
| P                 | 4                      |
| N                 | 4                      |
| p                 | 3                      |
| n                 | 0                      |
| p / (p + n)       | 1.000                  |
| P / (P + N)       | 0.500                  |
| log2(p / (p + n)) | 0.000                  |
| log2(P / (P + N)) | -1.000                 |
| FOIL Gain         | 3 × (0 - (-1)) = 3.000 |

**Interpretación:**
La condición identifica correctamente la mayoría de los positivos y excluye todos los negativos, generando una **alta ganancia de información**.

---

### b) Condición `edad <= 23`

| Parámetro         | Valor                  |
| ----------------- | ---------------------- |
| P                 | 4                      |
| N                 | 4                      |
| p                 | 3                      |
| n                 | 0                      |
| p / (p + n)       | 1.000                  |
| P / (P + N)       | 0.500                  |
| log2(p / (p + n)) | 0.000                  |
| log2(P / (P + N)) | -1.000                 |
| FOIL Gain         | 3 × (0 - (-1)) = 3.000 |

**Interpretación:**
Resultados idénticos a la condición anterior. Esta regla también es válida para predecir `en_formacion`, mostrando cómo FOIL puede encontrar múltiples condiciones con igual ganancia de información.

---

## Ejemplo de código Python para FOIL Gain

```python
import math

# Datos
P, N = 4, 4
p, n = 3, 0

# Fracciones
p_frac = p / (p + n)
P_frac = P / (P + N)

# Logaritmos base 2
log_p = math.log2(p_frac)
log_P = math.log2(P_frac)

# FOIL Gain
foil_gain = p * (log_p - log_P)

print(f"p/(p+n) = {p_frac:.3f}")
print(f"P/(P+N) = {P_frac:.3f}")
print(f"log2(p/(p+n)) = {log_p:.3f}")
print(f"log2(P/(P+N)) = {log_P:.3f}")
print(f"FOIL Gain = {foil_gain:.3f}")
```

---

## Conclusión

* Se identificaron reglas lógicas simples que permiten predecir si un empleado está en formación.
* El cálculo de FOIL Gain permite evaluar la **importancia de cada condición**.
* Las condiciones `nivel_educativo == 'terciario'` y `edad <= 23` generan la misma ganancia de información, mostrando que FOIL puede encontrar múltiples reglas equivalentes.
* Este trabajo fortalece la comprensión de la **inducción de reglas** y la **medición de su eficacia** en aprendizaje automático simbólico.
