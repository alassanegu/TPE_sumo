set terminal wxt
set terminal png
set output 'EmissionCO2.png'

set title "Emission CO2 en fonction de la distance du véhicule"
set xlabel "distance"
set ylabel "Emission CO2"
plot "EmissionCO2V1.txt" title "Simulation V1" with lines ls 1,\
     "EmissionCO2VehThermique.txt" title "Simulation VehThermique" with lines ls 2
