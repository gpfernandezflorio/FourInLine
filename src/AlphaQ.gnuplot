set terminal png
set output "AlphaQ.png"
set logscale x
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"
plot "Alpha/Q0.0.dat" w lines title " = 0.0", \
     "Alpha/Q0.2.dat" w lines title " = 0.2", \
     "Alpha/Q0.4.dat" w lines title " = 0.4", \
     "Alpha/Q0.6.dat" w lines title " = 0.6", \
     "Alpha/Q0.8.dat" w lines title " = 0.8", \
     "Alpha/Q1.0.dat" w lines title " = 1.0",
