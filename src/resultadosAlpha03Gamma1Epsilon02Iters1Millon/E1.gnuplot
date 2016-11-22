set terminal png 30 size 1080,1080 enhanced
set logscale x
set key bottom maxrows 6
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

#set xrange[:1000000]
#set yrange[0.2:0.85]

set title "Experimento 1: Entrenamiento de los competidores"
set output "E1train.png"
plot "QvsRandom/A-1(Qlearner)vs2-(random).dat" w lines title "QLP1 vs Random", \
     "QvsQ/A-1(Qlearner)vs2-(Qlearner).dat" w lines title "QLP2 vs QLP"
