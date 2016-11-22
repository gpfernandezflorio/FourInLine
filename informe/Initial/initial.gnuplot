set terminal png 30 size 1080,720 enhanced
set logscale x
set xtics 1,100,1e8
#set key bottom
set xlabel "Cantidad de iteraciones"
set ylabel "Proporción de victorias"

#set xrange[:1000000]
#set yrange[0.2:0.85]

#set title ""
set output "QvQ.png"
plot "QQ1.dat" w lines title "QLP 1", \
     "QQ2.dat" w lines title "QLP 2"

#set title ""
set output "QvR.png"
plot "QR1.dat" w lines title "QLP", \
     "QR2.dat" w lines title "Random"
