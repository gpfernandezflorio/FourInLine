set terminal png
set output "GammaR.png"
set logscale x
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"
plot "Gamma/R0.0.dat" w lines title " = 0.0", \
     "Gamma/R0.2.dat" w lines title " = 0.2", \
     "Gamma/R0.4.dat" w lines title " = 0.4", \
     "Gamma/R0.6.dat" w lines title " = 0.6", \
     "Gamma/R0.8.dat" w lines title " = 0.8", \
     "Gamma/R1.0.dat" w lines title " = 1.0",
