set terminal png
set output "GammaQ.png"
set logscale x
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"
plot "Gamma/Q0.0.dat" w lines title " = 0.0", \
     "Gamma/Q0.2.dat" w lines title " = 0.2", \
     "Gamma/Q0.4.dat" w lines title " = 0.4", \
     "Gamma/Q0.6.dat" w lines title " = 0.6", \
     "Gamma/Q0.8.dat" w lines title " = 0.8", \
     "Gamma/Q1.0.dat" w lines title " = 1.0",
