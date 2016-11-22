# FourInLine
Programa que aprende a jugar 4 en Linea mediante Q-Learning.

## Estructura Informe
### Intro
### Explicacion Modelo
### Ajuste de parametros
  Con graficos que justifiquen cada parametro (alpha, gamma y epsilon)
  Con grafico vs Q standard (si es que cambiamos algun parametros, sino al pedo no?)
### Experimentacion
Explicacion de que llamamos competencia
#### Caso 1(QQ vs QR)
Grafico del entranmiento
y grafico de torta/barra con la competencia
Resultados
#### Caso 2(QQR vs QRQ)
Grafico del entranmiento
y grafico de torta/barra con la competencia
Resultados
#### Caso 3(QQ vs QR vs QS)
Explicacion de que es el S
Grafico del entranmiento
y grafico de torta/barra con la competencia
Resultados
### Conclusiones

### Ideas que no llegamos a hacer ???
Contar de la idea de implementar un minimax, pero que no lo pusimos en practica porque era infinito.

## Como correr el tp
python fourInLine.py key1 key2 [iteraciones]
donde key son los tipos de jugadores

o

python fourInLine.py p key1 key2 a1 g1 e1 a2 g2 e2 rw rt rl rr save [iters]


## Como correr la experimentacion
./experimentacion.bash iteraciones carpeta
