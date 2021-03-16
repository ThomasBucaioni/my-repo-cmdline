#!/bin/bash

# initialisation
pas_ind=0.05 # Inductance de 2.00, 2.05, 2.10, ... , 2.90, 2.95, 3.00
nb_inductances=21
list_inductances=$(eval echo {0..$(($nb_inductances-1))})

# verifications
echo pas_ind = $pas_ind
echo nb_inductances = $nb_inductances
echo list_inductances = $list_inductances

pause ()
{
    read -n1 -p 'Press any key when ready...'
}

pause

echo go

for ind in $list_inductances
do
    L=$(echo "scale=3 ; 2.0 + $pas_ind * $ind" | bc -l)
    echo L=$L; pause

    #nom_repertoire_us=$(echo "scale=0; ( 2.0 + $ind * $pas_ind ) * 100" | bc )
    #printf -v nom_repertoire "L%3.0f" ${nom_repertoire_us/./,}
    printf -v nom_repertoire "L%3.0f" $(echo "scale=0; ( 2.0 + $ind * $pas_ind ) * 100" | bc )
    echo "nom du repertoire: $nom_repertoire"; pause

    [[ -d "$nom_repertoire" ]] || mkdir "$nom_repertoire" && cd "$nom_repertoire"
    cp ../tlmscn.dat .

    # transformation du fichier de données
    sed -i "218s/.*/$L\t\t40\t\t0\t\t/" tlmscn.dat

    echo ----------
    echo affichage du fichier de données:
    echo -----
    head -218 tlmscn.dat | tail -n 1
    echo -----
    sed -n '217,219p' tlmscn.dat
    echo ----------
    
    pause
    
    cp ../tlmscn2 .
    cp ../job.slurm .

    #    while ! [[ $(sbatch job.slurm) ]] # [[ $(sacct -u tbucaioni | grep PENDING) -ge 5 ]]
    #   do
    
    #echo "Plus de 5 processus en cours d'execution - " $date
    echo "$nom_repertoire : trop de processus en cours d'exécution - $(date) "
    sleep 30
    
    
    #  done
    
    cd ..
    
    echo "-----"
    echo " Fin de simulation pour l'inductance L = $L - $(date) "
    echo "-----"
done

echo fin
