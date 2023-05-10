set terminal wxt
set terminal png
set output 'Vitesse.png'

set title "La Vitesse en fonction de la distance du véhicule"
set xlabel "distance en mètre "
set ylabel "Vitesse km/h"
plot "VitesseV1.txt" title "Simulation V1" with lines ls 1,\
     "VitesseV2.txt" title "Simulation V2" with lines ls 2,\
     "VitesseV3.txt" title "Simulation V3" with lines ls 3
