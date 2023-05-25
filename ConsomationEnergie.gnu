set terminal wxt
set terminal png
set output 'ConsomationsEnergie.png'

set title "Consommation d'énergie en fonction de la distance du véhicule"
set xlabel "distance"
set ylabel "Consommation d'énergie (kWh)"
plot "ConsomationEnergieV1.txt" title "Simulation V1" with lines ls 1
