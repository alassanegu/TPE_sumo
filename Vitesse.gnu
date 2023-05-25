set terminal wxt
set terminal png
set output 'Vitesse.png'
set yrange [0:60]

set title "La Vitesse en fonction de la distance du véhicule"
set xlabel "distance en mètre "
set ylabel "Vitesse km/h"
plot "VitesseV1.txt" title "Simulation V1" with lines ls 1
