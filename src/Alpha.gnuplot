set terminal png
#set logscale x
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

set yrange[0.3:0.7]

set output "AlphaQ.png"
plot "Alpha/Q0.0.dat" w lines title " = 0.0", \
     "Alpha/Q0.2.dat" w lines title " = 0.2", \
     "Alpha/Q0.4.dat" w lines title " = 0.4", \
     "Alpha/Q0.6.dat" w lines title " = 0.6", \
     "Alpha/Q0.8.dat" w lines title " = 0.8", \
     "Alpha/Q1.0.dat" w lines title " = 1.0",

set yrange[0.4:0.8]

set output "AlphaR.png"
plot "Alpha/R0.0.dat" w lines title " = 0.0", \
     "Alpha/R0.2.dat" w lines title " = 0.2", \
     "Alpha/R0.4.dat" w lines title " = 0.4", \
     "Alpha/R0.6.dat" w lines title " = 0.6", \
     "Alpha/R0.8.dat" w lines title " = 0.8", \
     "Alpha/R1.0.dat" w lines title " = 1.0",
