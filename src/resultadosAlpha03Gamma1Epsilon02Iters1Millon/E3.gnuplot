set terminal png 30 size 1080,720 enhanced
set logscale x
set key bottom maxrows 6
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

set title "Experimento 3: Entrenamiento de los competidores"
set output "E2train.png"

#Reemplazar X1.dat por el path al .dat correspondiente al entrenamiento del caso 1, QLP contra Random
#Reemplazar X2.dat por el path al .dat correspondiente al entrenamiento del caso 1, QLP contra QLP
#Reemplazar X3.dat por el path al .dat correspondiente al entrenamiento del caso 3, QLP contra SQLP

plot "X1.dat" w lines title "QLP1 vs Random", \
     "X2.dat" w lines title "QLP2 vs QLP", \
     "X3.dat" w lines title "QLP3 vs SQLP"
