set terminal png
set output "c2.png"
set logscale x
plot "A-1(random)vs2-(Qlearner).dat" w lines title "Random", "A-2(Qlearner)vs1-(random).dat" w lines title "QLP"
