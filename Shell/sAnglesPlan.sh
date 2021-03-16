#!/bin/bash

pi=$(echo "scale=10; 4*a(1)" | bc -l)

# initialisation
taille_cellule=$(sed -n 5p tlmscn.dat | cut -f6)
pas_phi=10 # en degree
pas_alpha=10 # en degree
nb_angles_phi=$(( 360 / pas_phi ))
nb_angles_alpha=$(( 180 / pas_alpha ))
nb_trans=4
list_angles_phi=$(eval echo {0..$(($nb_angles_phi-1))})
list_angles_alpha=$(eval echo {0..$(($nb_angles_alpha-1))})
list_trans=$(eval echo {0..$(($nb_trans-1))})

# verifications
echo $taille_cellule
echo $pas_phi
echo $pas_alpha
echo $nb_angles_phi
echo $nb_angles_alpha
echo $list_angles_phi
echo $list_angles_alpha
echo $list_trans

pause ()
{
    read -n1 -p 'Press any key when ready...'
}

pause

echo go

for phi in $list_angles_phi
do
    for alpha in $list_angles_alpha
    do
	for trans_x in $list_trans
	do
	    t_x=$(echo "scale=3 ; $taille_cellule*$trans_x/$nb_trans" | bc -l)
	    for trans_y in $list_trans
	    do
	    	t_y=$(echo "scale=3 ; $taille_cellule*$trans_y/$nb_trans" | bc -l)
		for trans_z in $list_trans
		do
	    	    t_z=$(echo "scale=3 ; $taille_cellule*$trans_z/$nb_trans" | bc -l)
	    	    echo "phi=$((phi * pas_phi)) ; alpha=$((alpha * pas_alpha - 85)) ; t_x=$t_x : t_y=$t_y ; t_z=$t_z"
	
		    printf -v nom_repertoire "p%03da%03dtx%01dty%01dtz%01d" $((phi * pas_phi)) $((alpha * pas_alpha - 85)) $((trans_x)) $((trans_y)) $((trans_z))
		    echo "nom du repertoire: $nom_repertoire"

		    [[ -d "$nom_repertoire" ]] || mkdir "$nom_repertoire" && cd "$nom_repertoire"
		    cp ../tlmscn.dat .

		    #phi=12 # TEST
		    #alpha=3 # TEST

		    delta_fil_x=$(echo "scale=5 ; 41*c(($alpha*$pas_alpha-85)*$pi/180)*c($phi*$pas_phi*$pi/180)" | bc -l)
		    delta_fil_y=$(echo "scale=5 ; 41*c(($alpha*$pas_alpha-85)*$pi/180)*s($phi*$pas_phi*$pi/180)" | bc -l) 
		    delta_fil_z=$(echo "scale=5 ; 41*s(($alpha*$pas_alpha-85)*$pi/180)" | bc -l)

		    #echo "delta_fil_x=$delta_fil_x"
		    #echo "delta_fil_y=$delta_fil_y"
		    #echo "delta_fil_z=$delta_fil_z"

		    abs_delta_fil_x=${delta_fil_x#-}
		    abs_delta_fil_y=${delta_fil_y#-}
		    abs_delta_fil_z=${delta_fil_z#-}

		    #echo "abs_delta_fil_x=$abs_delta_fil_x"
                    #echo "abs_delta_fil_y=$abs_delta_fil_y"
                    #echo "abs_delta_fil_z=$abs_delta_fil_z"

		    delta_cell_x=${delta_fil_x%.*}
		    delta_cell_y=${delta_fil_y%.*}
		    delta_cell_z=${delta_fil_z%.*}

		    #printf "delta_cell_x=$delta_cell_x\n"
		    #printf "delta_cell_y=$delta_cell_y\n"
		    #printf "delta_cell_z=$delta_cell_z\n"

		    abs_delta_cell_x=${delta_cell_x#-}
		    abs_delta_cell_y=${delta_cell_y#-}
		    abs_delta_cell_z=${delta_cell_z#-}

		    #printf "abs_delta_cell_x=$abs_delta_cell_x\n"
		    #printf "abs_delta_cell_y=$abs_delta_cell_y\n"
		    #printf "abs_delta_cell_z=$abs_delta_cell_z\n"

		    offset_fil_x=$([[ $delta_cell_x -lt 0 ]] && echo $abs_delta_fil_x || echo 0 )
		    offset_fil_y=$([[ $delta_cell_y -lt 0 ]] && echo $abs_delta_fil_y || echo 0 )
		    offset_fil_z=$([[ $delta_cell_z -lt 0 ]] && echo $abs_delta_fil_z || echo 0 )

		    #echo "offset_fil_x=$offset_fil_x"
		    #echo "offset_fil_y=$offset_fil_y"
		    #echo "offset_fil_z=$offset_fil_z"

		    debut_fil_x=$(echo "scale=5 ; (5.125*30+4+2+5+$offset_fil_x)*$taille_cellule+$t_x+0.1" | bc -l)
		    debut_fil_y=$(echo "scale=5 ; (5.125*30+4+2+5+$offset_fil_y)*$taille_cellule+$t_y+0.2" | bc -l)
		    debut_fil_z=$(echo "scale=5 ; (5.125*30+4+2+5+$offset_fil_z)*$taille_cellule+$t_z+0.3" | bc -l)

		    #echo "debut_fil_x=$debut_fil_x"
		    #echo "debut_fil_y=$debut_fil_y"
		    #echo "debut_fil_z=$debut_fil_z"

		    nb_cell_x=$(( (30+1+1+5)*2 + $abs_delta_cell_x + 1 ))
		    nb_cell_y=$(( (30+1+1+5)*2 + $abs_delta_cell_y + 1 ))
		    nb_cell_z=$(( (30+1+1+5)*2 + $abs_delta_cell_z + 1 ))

		    #echo "nb_cell_x=$nb_cell_x"
		    #echo "nb_cell_y=$nb_cell_y"
		    #echo "nb_cell_z=$nb_cell_z"

		    mur_fil_x=$(( 30+1+1+5+ $abs_delta_cell_x + 1 + 5 ))
		    mur_fil_y=$(( 30+1+1+5+ $abs_delta_cell_y + 1 + 5 ))
		    mur_fil_z=$(( 30+1+1+5+ $abs_delta_cell_z + 1 + 5 ))

		    #echo "mur_fil_x=$mur_fil_x"
		    #echo "mur_fil_y=$mur_fil_y"
		    #echo "mur_fil_z=$mur_fil_z"

		    list_murs_x=(1 30 31 32 $mur_fil_x $((mur_fil_x+1)) $((mur_fil_x+2)) $((mur_fil_x+32)) )
		    list_murs_y=(1 30 31 32 $mur_fil_y $((mur_fil_y+1)) $((mur_fil_y+2)) $((mur_fil_y+32)) )
		    list_murs_z=(1 30 31 32 $mur_fil_z $((mur_fil_z+1)) $((mur_fil_z+2)) $((mur_fil_z+32)) )

		    #echo "list_murs_x=${list_murs_x[*]}"
		    #echo "list_murs_y=${list_murs_y[*]}"
		    #echo "list_murs_z=${list_murs_z[*]}"

		    # transformation du fichier de données
		    sed -i "5s/.*/\t\t$nb_cell_x\t$nb_cell_y\t$nb_cell_z\t$taille_cellule/" tlmscn.dat
		    sed -i "87s/.*/${list_murs_x[*]}/"  tlmscn.dat
		    sed -i "90s/.*/${list_murs_y[*]}/"  tlmscn.dat
		    sed -i "93s/.*/${list_murs_z[*]}/"  tlmscn.dat
		    sed -i "141s/.*/\t$debut_fil_x\t$debut_fil_y\t$debut_fil_z\t1\t0\t0/"  tlmscn.dat
		    sed -i "144s/.*/\t$((phi*pas_phi))\t$((alpha*pas_alpha-85))\t10\t0\t$taille_cellule\t41\t0 0 0 0 0 0/"  tlmscn.dat

		    #pause

		    cp ../tlmscn2 .
		    cp ../job.slurm .

		    while ! [[ $(sbatch job.slurm) ]] # [[ $(sacct -u tbucaioni | grep PENDING) -ge 5 ]]
		    do
		    
		    #echo "Plus de 5 processus en cours d'execution - " $date
		    echo "$nom_repertoire : trop de processus en cours d'exécution - " $date		
		    sleep 30

		    
		    done

		    cd ..

		done
	    done
	done
	#echo sleep $(( 4*4*4*2 * 60 ))
	#sleep $(( 4*4*4*2 * 60 ))
	echo "-----"
	echo " Fin de translations - $(date) "
	echo "-----"
    done
	echo "-----"
	echo " Fin de rotations sur alpha=$((alpha*pas_alpha)) - $(date) "
	echo "-----"
done

echo fin
