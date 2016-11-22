set terminal png 30 size 1080,1080 enhanced
#set logscale x
set key bottom maxrows 6
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

set xrange[:1000000]
set yrange[0.2:0.85]

set title "vs Random variando {/Symbol e}"
set output "EpsilonR.png"
plot "Epsilon/R0.0.dat" w lines title "{/Symbol e} = 0.0", \
     "Epsilon/R0.2.dat" w lines title "{/Symbol e} = 0.2", \
     "Epsilon/R0.4.dat" w lines title "{/Symbol e} = 0.4", \
     "Epsilon/R0.6.dat" w lines title "{/Symbol e} = 0.6", \
     "Epsilon/R0.8.dat" w lines title "{/Symbol e} = 0.8", \
     "Epsilon/R1.0.dat" w lines title "{/Symbol e} = 1.0"

unset key

set title "vs otro QLP (por defecto) variando {/Symbol e}"
set output "EpsilonQ.png"
plot "Epsilon/Q0.0.dat" w lines title "{/Symbol e} = 0.0", \
     "Epsilon/Q0.2.dat" w lines title "{/Symbol e} = 0.2", \
     "Epsilon/Q0.4.dat" w lines title "{/Symbol e} = 0.4", \
     "Epsilon/Q0.6.dat" w lines title "{/Symbol e} = 0.6", \
     "Epsilon/Q0.8.dat" w lines title "{/Symbol e} = 0.8", \
     "Epsilon/Q1.0.dat" w lines title "{/Symbol e} = 1.0"
