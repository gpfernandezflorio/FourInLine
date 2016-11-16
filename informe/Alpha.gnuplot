set terminal png 30 size 1080,1080 enhanced
#set logscale x
set key bottom
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

set xrange[:1000000]
set yrange[0.2:0.85]

set title "vs Random variando {/Symbol a}"
set output "AlphaR.png"
plot "Alpha/R0.0.dat" w lines title "{/Symbol a} = 0.0", \
     "Alpha/R0.2.dat" w lines title "{/Symbol a} = 0.2", \
     "R.dat" w lines title "{/Symbol a} = 0.3", \
     "Alpha/R0.4.dat" w lines title "{/Symbol a} = 0.4", \
     "Alpha/R0.6.dat" w lines title "{/Symbol a} = 0.6", \
     "Alpha/R0.8.dat" w lines title "{/Symbol a} = 0.8", \
     "Alpha/R1.0.dat" w lines title "{/Symbol a} = 1.0",

unset key

set title "vs otro QLP (por defecto) variando {/Symbol a}"
set output "AlphaQ.png"
plot "Alpha/Q0.0.dat" w lines title "{/Symbol a} = 0.0", \
     "Alpha/Q0.2.dat" w lines title "{/Symbol a} = 0.2", \
     "Q.dat" w lines title "{/Symbol a} = 0.3", \
     "Alpha/Q0.4.dat" w lines title "{/Symbol a} = 0.4", \
     "Alpha/Q0.6.dat" w lines title "{/Symbol a} = 0.6", \
     "Alpha/Q0.8.dat" w lines title "{/Symbol a} = 0.8", \
     "Alpha/Q1.0.dat" w lines title "{/Symbol a} = 1.0",
