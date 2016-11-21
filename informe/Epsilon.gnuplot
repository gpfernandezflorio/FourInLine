set terminal png 30 size 1080,1080 enhanced
#set logscale x
set key bottom maxrows 6
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

set xrange[:200000]
set yrange[0.2:0.85]

set title "vs Random variando {/Symbol e}"
set output "EpsilonR.png"
plot "Epsilon/Rp0.0.dat" w lines title "{/Symbol e} = 0.0", \
     "Epsilon/R0.1.dat" w lines title "{/Symbol e} = 0.1", \
     "R.dat" w lines title "{/Symbol e} = 0.2", \
     "Epsilon/R0.3.dat" w lines title "{/Symbol e} = 0.3", \
     "Epsilon/Rp0.4.dat" w lines title "{/Symbol e} = 0.4", \
     "Epsilon/R0.5.dat" w lines title "{/Symbol e} = 0.5", \
     "Epsilon/Rp0.6.dat" w lines title "{/Symbol e} = 0.6", \
     "Epsilon/R0.7.dat" w lines title "{/Symbol e} = 0.7", \
     "Epsilon/Rp0.8.dat" w lines title "{/Symbol e} = 0.8", \
     "Epsilon/R0.9.dat" w lines title "{/Symbol e} = 0.9", \
     "Epsilon/Rp1.0.dat" w lines title "{/Symbol e} = 1.0"

unset key

set title "vs otro QLP (por defecto) variando {/Symbol e}"
set output "EpsilonQ.png"
plot "Epsilon/Qp0.0.dat" w lines title "{/Symbol e} = 0.0", \
     "Epsilon/Q0.1.dat" w lines title "{/Symbol e} = 0.1", \
     "Q.dat" w lines title "{/Symbol e} = 0.2", \
     "Epsilon/Q0.3.dat" w lines title "{/Symbol e} = 0.3", \
     "Epsilon/Qp0.4.dat" w lines title "{/Symbol e} = 0.4", \
     "Epsilon/Q0.5.dat" w lines title "{/Symbol e} = 0.5", \
     "Epsilon/Qp0.6.dat" w lines title "{/Symbol e} = 0.6", \
     "Epsilon/Q0.7.dat" w lines title "{/Symbol e} = 0.7", \
     "Epsilon/Qp0.8.dat" w lines title "{/Symbol e} = 0.8", \
     "Epsilon/Q0.9.dat" w lines title "{/Symbol e} = 0.9", \
     "Epsilon/Qp1.0.dat" w lines title "{/Symbol e} = 1.0"
