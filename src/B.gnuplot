set terminal png
set output "B.png"
set logscale x
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"
plot "B1.dat" w lines title "QLP 1", "B2.dat" w lines title "QLP 2"
