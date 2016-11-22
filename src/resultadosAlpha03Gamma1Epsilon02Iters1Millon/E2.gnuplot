set terminal png 30 size 1080,1080 enhanced
set logscale x
set key bottom maxrows 6
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

#set xrange[:1000000]
#set yrange[0.2:0.85]

set title "Experimento 2: Entrenamiento de los competidores"
set output "E2train.png"
plot "QEntrenadovsRandom/A-1(QlearnerEntrenadoConRandom)vs2-(QlearnerFresco).dat" w lines title "QLP1 (entrenado contra Random) vs QLP", \
     "QEntrenadovsQ/A-1(QlearnerEntrenadoConQ)vs2-(random).dat" w lines title "QLP2 (entrenado contra QLP) vs Random"
