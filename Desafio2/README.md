---
title: "Desafio 2"
subtitle: "Tecnica Iterativa de Jacobi"
author: "Lenin Pocoaca"
date: "16-09-24"
---
# Tecnica Iterativa de Jacobi

Se resolvera el siguiente sistema (Problema planteado en el Desafio 1) mediante la tecnica itertiva de Jacobi .

$$0.52x_1+0.20x_2+0.25x3=4800$$

$$0.30x_1+0.50x_2+0.20x3=5810$$

$$0.18x_1+0.30x_2+0.55x3=5690$$

donde:

$x_{1}:m^3 \text{ a extraer de la Cantera 1.}$\
$x_{2}:m^3 \text{ a extraer de la Cantera 2.}$\
$x_{3}:m^3 \text{ a extraer de la Cantera 3.}$

## Solución implementada en Python
Para resolver $Ax=b$ dada una aproximación inicial $x^{(0)}$.

**ENTRADA:**
* El número de ecuaciones y valores desconocidos n.
* Las entradas $a_{ij},\text{ }1≤i, j≤n$
 de la matriz $A$.
* Las entradas $b_i,\text{ }1≤i≤n \text{ de } b$.
* Las entradas $XO_i,\text{ }1≤i≤n\text{ de }XO=x^{(0)}$.

* tolerancia $TOL$.
* Número máximo de iteraciones $N$.

```{python, collapse = TRUE, echo = FALSE}
import sys
# Entrada de datos

n: int = 3

A: list[list[float]] = [
    [0.52, 0.20, 0.25],
    [0.30, 0.50, 0.20],
    [0.18, 0.30, 0.55]
]

b: list[float] = [4800, 5810, 5690]

X0 = [0, 0, 0]

TOL: float = 0.001 # Valor por convención

N: int = 20 # Valor por convención
    
```

 * **Paso 1** Determine $k=1$.

 * **Paso 2** Mientras $(k≤N)$ haga los pasos 3–6.
    * **Paso 3**  Para $i=1,...,n$ determine 
    
    $$x_i = \frac{1}{a_{ii}} \left[−
    \sum_{\begin{matrix}i=j \\ j \neq i \end{matrix}}^{n} (a_{ij}XO_j) + b_i \right]$$
    * **Paso 4** Si $||x−XO||_{\infty}<TOL$ entonces SALIDA $(x_1,...,x_n)$ (El procedimiento fue exitoso.) PARE.

    * **Paso 5** Determine $k=k+1$.
    * **Paso 6** Para $i=1,...,n$ determine $XO_i=x_i$.
 * **Paso 7** SALIDA (‘número máximo de iteraciones excedido’); (El procedimiento no fue exitoso.) PARE.

 ```{python, collapse = TRUE, echo = FALSE}
# Pasos 1 - 6


def sumatoria(a: list[float], X0: list[float], n: int, i: int) -> float:
    res: float = 0.0
    for j in range(n):
        if j != i:
            res += a[j] * X0[j]
    
    return res

def tolerancia(X: list[float], X0:list[float], n: int) -> float:
    L = []
    for i in range(n):
        L.append(abs(X[i] - X0[i]))
 
    return max(L)

def Jacobi(n: int, A: list[list[float]], b: list[float], X0: list[float], TOL: float = 1e-10, N: int = 1000) -> tuple[list[float], int]:
    X: list[float] = X0[:]
    for _ in range(N):
        for i in range(n):
            X[i] = 1/A[i][i] * (-sumatoria(A[i], X0, n, i) + b[i])
        
        if tolerancia(X, X0, n) < TOL: return (X, _ + 1)
        X0 = X[:]
        
    
    else:
        sys.stdout.write("\nNumero de Iteraciones excedido...")
        return (X, _ + 1)

SOLUCION: list[float] = Jacobi(n, A, b, X0, TOL, N)

sys.stdout.write(f'\nSOLUCIÓN:')
sys.stdout.write(f'\nXi = {SOLUCION[0]}')
sys.stdout.write(f'\nIteraciones = {SOLUCION[1]}')
```
### Salida en pantalla
Con una tolerancia de 0.001 y 180 iteraciones se halla los siguientes resultados
```{python, collapse = TRUE, echo = FALSE}
Xi = [4011.627498239788, 7162.790246973516, 5125.580979616491]
Iteraciones = 180
```
### Comparacion de resultados

||$X$ Real|$X^{(k)}$ Jacobi|
|:-:|:-:|:-:|
|$x_1$|4011.62790698|4011.627498239788|
|$x_2$|7162.79069767|7162.790246973516|
|$x_3$|5125.58139535|5125.580979616491|

con error relativo: 

$$ \frac{\left\| X - X^{k} \right\|}{\left\| X \right\|} * 100 = 7.6\text{x}10^{-06}\% $$

## Referencias
Richard L. Burden (2016). ANÁLISIS NUMÉRICO (10ma ed.). (p. 337).
