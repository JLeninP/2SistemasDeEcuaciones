---
title: "Desafio 6"
subtitle: "Sistemas mal condicionados"
author: "Lenin Pocoaca"
date: "26-09-2024"
---

# SISTEMA MAL CONDICIONADO DE 3X3 CON GRÁFICO

## Plantear un ejemplo

$$x_1 + 10.01x_2 + 100x_3 = 200$$

$$2.12x_1 + 20x_2 + 200x_3 = 300$$

$$3.1x_1 + 30x_2 + 300x_3 = 400$$

## Explicación y pruebas

### Determinante
Si el determinante es cero o muy cercano a cero, el sistema está mal condicionado, lo que implica que las soluciones pueden ser inestables.

$$A = \begin{bmatrix}
1 & 10.01 & 100 \\
2.12 & 20 & 200 \\
3.1 & 30 & 300
\end{bmatrix}$$

Calculando el determinante de la matriz $A$ por el método de matriz de cofactores.

$$|A| = \sum_{j=1}^{n}(-1)^{i+j}a_{ij}M_{ij}\text{    para } i=1, 2, ..., n$$

entnoces:

$$|A| = \begin{vmatrix}
1 & 10.01 & 100 \\
2.12 & 20 & 200 \\
3.1 & 30 & 300
\end{vmatrix}$$

$$=\begin{vmatrix}
20 & 200 \\
30 & 300
\end{vmatrix} - 
10.01*\begin{vmatrix}
2.12 & 200 \\
3.1 & 300
\end{vmatrix} +
100*\begin{vmatrix}
2.12 & 20 \\
3.1 & 30
\end{vmatrix}$$

$$=\left(
20*|300|-200*|30|
\right) - 
10.01\left(
2.12*|300| - 200*|3.1|\right) +
100\left(
2.12*|30| - 20*|3.1|
\right)$$

$$=\left(
6000-6000
\right) - 
10.01\left(
636 - 620\right) +
100\left(
63.6 - 62
\right)$$

$$=
0 - 
10.01\left(
16\right) +
100\left(
1.6
\right)$$

$$=-160.16 + 160$$

$$= -0.16$$

Vemos que el determinante calculado es proximo a $0$, lo que muestra que existe una gran probabilidad de que el sistema este mal condicionado, pero dicha conclusión es un poco ambigua ya que no nos indican cuán cercano a cero debe estar el determinante calculado, por lo que se procedera a calcular el numero de condición o condicional.

### Condicional

El número de condición ( $\kappa(A)$) se define como:

$$κ(A)=∥A∥⋅∥A^{−1}∥$$

Si el número de condición es muy grande, el sistema esta mal condicionado.

Con ayuda de la función **cond()** de **Octave**
se obtiene el siguiente resultado.
```{octave}
A = [
    1, 10.01, 100;
    2.12, 20, 200;
    3.1, 30, 300
    ]

cond(A)

ans = 5.3131e+04
```

Donde se observa que el resultado $5313.1$ es muy grande, por lo tanto se puede confirmar el mal condicionamiento del sistema.

### Pequeños cambios cambian radicalmente la solución

Realizando un cambio en el elemento $a_{11} = 1$ de la matriz $A$ por $\tilde{a}_{11} = 0.9$, se obtiene la matriz modificada $\tilde{A}$.

entonces, se tiene:
$$A = \begin{bmatrix}
1 & 10.01 & 100 \\
2.12 & 20 & 200 \\
3.1 & 30 & 300
\end{bmatrix} \text{;}\hspace{1cm} \tilde{A} = \begin{bmatrix}
0.9 & 10.01 & 100 \\
2.12 & 20 & 200 \\
3.1 & 30 & 300
\end{bmatrix}$$

Con ayuda de **Octave** obtenemos los siguientes resultados:
```{octave}
A = [
    1, 10.01, 100;
    2.12, 20, 200;
    3.1, 30, 300
    ]
b = [200; 300; 400]

A1 = [
    0.9, 10.01, 100;
    2.12, 20, 200;
    3.1, 30, 300
    ]

b1 = [200; 300; 400]

x = inv(A)*b
x1 = inv(A1)*b1
```
Respuesta:
```{octave}
x =

    625.00
   8750.00
   -880.13

x1 =

   6.2500e+02
   1.5000e+04
  -1.5051e+03
```
Se puede observar que con tan solo cambiar un decimal en uno de los coeficientes del sistema, se genera un gran impacto en los resultados.

### Matriz identidad
Con ayuda de la bibilioteca **Numpy** de **Python** se obtiene el siguiente resultado:

```{python}
import numpy as np

A = np.array([
        [1, 10.01, 100],
        [2.12, 20, 200],
        [3.1, 30, 300]
        ])

A_inv = np.linalg.inv(A)
I = np.dot(A, A_inv)

print(I)
```
Resultado
```{python}
[[ 1.00000000e+00  6.39488462e-14 -7.10542736e-14]
 [ 0.00000000e+00  1.00000000e+00 -1.42108547e-13]
 [ 0.00000000e+00  7.81597009e-14  1.00000000e+00]]
```

Los valores no satisfacen las condiciones que debe cumplir una matriz identidad, que son:

* La diagonal principal de la matriz esta compuesta por unos.
* Los valores fuera de la diagonal principal de la matriz, deben ser cero.

### Gráfico

Graficando el siguiente sistema:

$$x_1 + 10.01x_2 + 100x_3 = 200$$

$$2.12x_1 + 20x_2 + 200x_3 = 300$$

$$3.1x_1 + 30x_2 + 300x_3 = 400$$

despejando $x_3$, se tiene:
$$x_3 = \frac{200}{100} - \frac{1}{100}x_1 - \frac{10.01}{100}x_2$$

$$x_3 = \frac{300}{200} - \frac{2.12}{200}x_1 - \frac{20}{200}x_2$$

$$x_3 = \frac{400}{300} - \frac{3.1}{300}x_1 - \frac{30}{300}x_2$$

con ayuda de **Python** se obtiene el siguiente gráfico en 3 dimensiones del sistema descrito:

![Grafico](img1.png)

Realizando un acercamiento al gráfico se observa que los planos podrían ser paralelos, lo que significaría que el sistema podría contar con infinitas soluciones.

![GraficoZoom](img2.png)

En un sistema mal condicionado esto quiere decir que un amplio rango de resultados pueden satisfacer las ecuaciones en forma aproximada.

## Conclusion:
Los sistemas mal condicionados presentan problemas cuando se encuentran durante la solución númerica de ecuciones lineales, lo cual se debe a que este tipo de sistemas son extremadamente sensibles a los errores de redondeo.

## Referencias

* Richard L. Burden (2016). ANÁLISIS NUMÉRICO (10ma ed.). (p. 296).

* Steven C. Chapra (2015). MÉTODOS NUMÉRICOS (7ma ed.). (p. 230).

* Sistemas mal condicionados: https://www.youtube.com/watch?v=xuXx6ITk-T8