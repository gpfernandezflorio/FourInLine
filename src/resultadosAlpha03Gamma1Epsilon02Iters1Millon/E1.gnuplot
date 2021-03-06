set terminal png 30 size 1080,720 enhanced
set logscale x
set key bottom maxrows 6
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

set title "Experimento 1: Entrenamiento de los competidores"
set output "E1train.png"

#Reemplazar X1.dat por el path al .dat correspondiente al entrenamiento del caso 1, QLP contra Random
#Reemplazar X2.dat por el path al .dat correspondiente al entrenamiento del caso 1, QLP contra QLP

plot "X1.dat" w lines title "QLP1 vs Random", \
     "X2.dat" w lines title "QLP2 vs QLP"
