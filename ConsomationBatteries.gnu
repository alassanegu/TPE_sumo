set terminal wxt
set terminal png
set output 'ConsomationsBatteries.png'

set title "Consommation de Batterie en fonction de la distance du véhicule"
set xlabel "Distance"
set ylabel "Consommation de la batterie (kWh)"
plot "ConsomationBatterieV1.txt" title "Simulation V1" with lines ls 1
