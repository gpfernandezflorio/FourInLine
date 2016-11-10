set terminal png
set output "c1.png"
set logscale x
plot "A-1(Qlearner)vs2-(Qlearner).dat" w lines title "QLP 1", "A-2(Qlearner)vs1-(Qlearner).dat" w lines title "QLP 2"
