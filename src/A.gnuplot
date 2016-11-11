set terminal png
set output "A.png"
set logscale x
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"
plot "A1.dat" w lines title "QLP", "A2.dat" w lines title "Random"
