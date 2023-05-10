set terminal wxt
set terminal png
set output 'ConsomationsEnergie.png'

set title "Consommation d'énergie en fonction de la distance du véhicule"
set xlabel "distance"
set ylabel "Consommation d'énergie (kWh)"
plot "ConsomationEnergieV1.txt" title "Simulation V1" with lines ls 1,\
     "ConsomationEnergieV2.txt" title "Simulation V2" with lines ls 2,\
     "ConsomationEnergieV3.txt" title "Simulation V3" with lines ls 3
