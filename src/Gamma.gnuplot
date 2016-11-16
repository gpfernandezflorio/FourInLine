set terminal png
set logscale x
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

set output "GammaQ.png"
plot "Gamma/Q0.0.dat" w lines title " = 0.0", \
     "Gamma/Q0.2.dat" w lines title " = 0.2", \
     "Gamma/Q0.4.dat" w lines title " = 0.4", \
     "Gamma/Q0.6.dat" w lines title " = 0.6", \
     "Gamma/Q0.8.dat" w lines title " = 0.8", \
     "Gamma/Q1.0.dat" w lines title " = 1.0",

set output "GammaR.png"
plot "Gamma/R0.0.dat" w lines title " = 0.0", \
     "Gamma/R0.2.dat" w lines title " = 0.2", \
     "Gamma/R0.4.dat" w lines title " = 0.4", \
     "Gamma/R0.6.dat" w lines title " = 0.6", \
     "Gamma/R0.8.dat" w lines title " = 0.8", \
     "Gamma/R1.0.dat" w lines title " = 1.0",
