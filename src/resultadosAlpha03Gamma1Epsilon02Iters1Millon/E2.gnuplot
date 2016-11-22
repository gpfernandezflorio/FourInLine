set terminal png 30 size 1080,720 enhanced
set logscale x
set key bottom maxrows 6
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

set title "Experimento 2: Entrenamiento de los competidores"
set output "E2train.png"

#Reemplazar X1.dat por el path al .dat correspondiente al entrenamiento del caso 2, QLP (entrenado contra Random) contra QLP
#Reemplazar X2.dat por el path al .dat correspondiente al entrenamiento del caso 2, QLP (entrenado contra QLP) contra Random

plot "X1.dat" w lines title "QLP1 (entrenado contra Random) vs QLP", \
     "X2.dat" w lines title "QLP2 (entrenado contra QLP) vs Random"
