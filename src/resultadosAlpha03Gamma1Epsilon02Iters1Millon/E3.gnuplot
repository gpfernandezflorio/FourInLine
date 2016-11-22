set terminal png 30 size 1080,720 enhanced
set logscale x
set key bottom maxrows 6
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

set title "Experimento 3: Entrenamiento de los competidores"
set output "E3train.png"

#Reemplazar X1.dat por el path al .dat correspondiente al entrenamiento del caso 1, QLP contra Random
#Reemplazar X2.dat por el path al .dat correspondiente al entrenamiento del caso 1, QLP contra QLP
#Reemplazar X3.dat por el path al .dat correspondiente al entrenamiento del caso 3, QLP contra SQLP

plot "Caso3/QvsR/A-1(Qlearner)vs2-(random).dat" w lines title "QLP1 vs Random", \
     "Caso3/QvsQ/A-1(Qlearner)vs2-(Qlearner).dat" w lines title "QLP2 vs QLP", \
     "Caso3/QvsS/A-1(Qlearner)vs2-(SmartQlearner).dat" w lines title "QLP3 vs SQLP"
