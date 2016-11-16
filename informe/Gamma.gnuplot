set terminal png 30 size 1080,1080 enhanced
#set logscale x
set key bottom
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

set xrange[:1000000]
set yrange[0.2:0.85]

set title "vs Random variando {/Symbol g}"
set output "GammaR.png"
plot "Gamma/R0.0.dat" w lines title "{/Symbol g} = 0.0", \
     "Gamma/R0.2.dat" w lines title "{/Symbol g} = 0.2", \
     "Gamma/R0.4.dat" w lines title "{/Symbol g} = 0.4", \
     "Gamma/R0.6.dat" w lines title "{/Symbol g} = 0.6", \
     "Gamma/R0.8.dat" w lines title "{/Symbol g} = 0.8", \
     "R.dat" w lines title "{/Symbol g} = 0.9", \
     "Gamma/R1.0.dat" w lines title "{/Symbol g} = 1.0",

unset key

set title "vs otro QLP (por defecto) variando {/Symbol g}"
set output "GammaQ.png"
plot "Gamma/Q0.0.dat" w lines title "{/Symbol g} = 0.0", \
     "Gamma/Q0.2.dat" w lines title "{/Symbol g} = 0.2", \
     "Gamma/Q0.4.dat" w lines title "{/Symbol g} = 0.4", \
     "Gamma/Q0.6.dat" w lines title "{/Symbol g} = 0.6", \
     "Gamma/Q0.8.dat" w lines title "{/Symbol g} = 0.8", \
     "Q.dat" w lines title "{/Symbol g} = 0.9", \
     "Gamma/Q1.0.dat" w lines title "{/Symbol g} = 1.0",
