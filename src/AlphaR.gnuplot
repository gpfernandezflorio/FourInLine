set terminal png
set output "AlphaR.png"
set logscale x
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"
plot "Alpha/R0.0.dat" w lines title " = 0.0", \
     "Alpha/R0.2.dat" w lines title " = 0.2", \
     "Alpha/R0.4.dat" w lines title " = 0.4", \
     "Alpha/R0.6.dat" w lines title " = 0.6", \
     "Alpha/R0.8.dat" w lines title " = 0.8", \
     "Alpha/R1.0.dat" w lines title " = 1.0",
