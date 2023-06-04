#!/bin/bash

pi=$(echo "scale=10; 4*a(1)" | bc -l)

taille_cellule=$(sed -n 5p tlmscn.dat | cut -f6)

if [[ $# -eq 2 ]]
then
	phi=$1
	alpha=$2
	printf -v suffixe_fichier "p%03da%03d" $phi $alpha
        nouveau_fichier=tlmscn-${suffixe_fichier}.dat

	echo $phi
	echo $alpha
	echo $suffixe_fichier
	echo $nouveau_fichier

        cp -b tlmscn.dat $nouveau_fichier

	delta_fil_x=$(echo "scale=5 ; 41*c($alpha*$pi/180)*c($phi*$pi/180)" | bc -l)
	delta_fil_y=$(echo "scale=5 ; 41*c($alpha*$pi/180)*s($phi*$pi/180)" | bc -l) 
	delta_fil_z=$(echo "scale=5 ; 41*s($alpha*$pi/180)" | bc -l)

	echo "delta_fil_x=$delta_fil_x"
	echo "delta_fil_y=$delta_fil_y"
	echo "delta_fil_z=$delta_fil_z"

	abs_delta_fil_x=${delta_fil_x#-}
	abs_delta_fil_y=${delta_fil_y#-}
	abs_delta_fil_z=${delta_fil_z#-}

	echo "abs_delta_fil_x=$abs_delta_fil_x"
        echo "abs_delta_fil_y=$abs_delta_fil_y"
        echo "abs_delta_fil_z=$abs_delta_fil_z"

	delta_cell_x=${delta_fil_x%.*}
	delta_cell_y=${delta_fil_y%.*}
	delta_cell_z=${delta_fil_z%.*}

	printf "delta_cell_x=$delta_cell_x\n"
	printf "delta_cell_y=$delta_cell_y\n"
	printf "delta_cell_z=$delta_cell_z\n"

	abs_delta_cell_x=${delta_cell_x#-}
	abs_delta_cell_y=${delta_cell_y#-}
	abs_delta_cell_z=${delta_cell_z#-}

	printf "abs_delta_cell_x=$abs_delta_cell_x\n"
	printf "abs_delta_cell_y=$abs_delta_cell_y\n"
	printf "abs_delta_cell_z=$abs_delta_cell_z\n"

	offset_fil_x=$([[ $delta_cell_x -lt 0 ]] && echo $abs_delta_fil_x || echo 0 )
	offset_fil_y=$([[ $delta_cell_y -lt 0 ]] && echo $abs_delta_fil_y || echo 0 )
	offset_fil_z=$([[ $delta_cell_z -lt 0 ]] && echo $abs_delta_fil_z || echo 0 )
	
	echo "offset_fil_x=$offset_fil_x"
	echo "offset_fil_y=$offset_fil_y"
	echo "offset_fil_z=$offset_fil_z"
	
	debut_fil_x=$(echo "scale=5 ; (5.125*30+4+2+5+$offset_fil_x)*$taille_cellule+0.1" | bc -l)
	debut_fil_y=$(echo "scale=5 ; (5.125*30+4+2+5+$offset_fil_y)*$taille_cellule+0.2" | bc -l)
	debut_fil_z=$(echo "scale=5 ; (5.125*30+4+2+5+$offset_fil_z)*$taille_cellule+0.3" | bc -l)
	
	echo "debut_fil_x=$debut_fil_x"
	echo "debut_fil_y=$debut_fil_y"
	echo "debut_fil_z=$debut_fil_z"
	
	echo "fin_fil_x=$(echo "scale=5 ; $debut_fil_x + 41*c($alpha*$pi/180)*c($phi*$pi/180)*$taille_cellule" | bc -l)"
	echo "fin_fil_y=$(echo "scale=5 ; $debut_fil_y + 41*c($alpha*$pi/180)*s($phi*$pi/180)*$taille_cellule" | bc -l)"
	echo "fin_fil_z=$(echo "scale=5 ; $debut_fil_z + 41*s($alpha*$pi/180)*$taille_cellule" | bc -l)"

	echo "debut de 'zone x' : " $(echo "scale=5 ; (5.125*30+4+2+5)*$taille_cellule" | bc -l)
	echo "debut de 'zone y' : " $(echo "scale=5 ; (5.125*30+4+2+5)*$taille_cellule" | bc -l)
	echo "debut de 'zone z' : " $(echo "scale=5 ; (5.125*30+4+2+5)*$taille_cellule" | bc -l)
	echo "fin de 'zone x' : " $(echo "scale=5 ; (5.125*30+4+2+5+$abs_delta_cell_x+1)*$taille_cellule" | bc -l)
	echo "fin de 'zone y' : " $(echo "scale=5 ; (5.125*30+4+2+5+$abs_delta_cell_y+1)*$taille_cellule" | bc -l)
	echo "fin de 'zone z' : " $(echo "scale=5 ; (5.125*30+4+2+5+$abs_delta_cell_z+1)*$taille_cellule" | bc -l)
	
	nb_cell_x=$(( (30+1+1+5)*2 + $abs_delta_cell_x + 1 ))
	nb_cell_y=$(( (30+1+1+5)*2 + $abs_delta_cell_y + 1 ))
	nb_cell_z=$(( (30+1+1+5)*2 + $abs_delta_cell_z + 1 ))
	
	echo "nb_cell_x=$nb_cell_x"
	echo "nb_cell_y=$nb_cell_y"
	echo "nb_cell_z=$nb_cell_z"
	
	mur_fil_x=$(( 30+1+1+5+ $abs_delta_cell_x + 1 + 5 ))
	mur_fil_y=$(( 30+1+1+5+ $abs_delta_cell_y + 1 + 5 ))
	mur_fil_z=$(( 30+1+1+5+ $abs_delta_cell_z + 1 + 5 ))
	
	echo "mur_fil_x=$mur_fil_x"
	echo "mur_fil_y=$mur_fil_y"
	echo "mur_fil_z=$mur_fil_z"
	
	list_murs_x=(1 30 31 32 $mur_fil_x $((mur_fil_x+1)) $((mur_fil_x+2)) $((mur_fil_x+32)) )
	list_murs_y=(1 30 31 32 $mur_fil_y $((mur_fil_y+1)) $((mur_fil_y+2)) $((mur_fil_y+32)) )
	list_murs_z=(1 30 31 32 $mur_fil_z $((mur_fil_z+1)) $((mur_fil_z+2)) $((mur_fil_z+32)) )
	
	echo "list_murs_x=${list_murs_x[*]}"
	echo "list_murs_y=${list_murs_y[*]}"
	echo "list_murs_z=${list_murs_z[*]}"
	
	# transformation du fichier de données
	sed -i "5s/.*/\t\t$nb_cell_x\t$nb_cell_y\t$nb_cell_z\t$taille_cellule/" $nouveau_fichier
	sed -i "87s/.*/${list_murs_x[*]}/" $nouveau_fichier
	sed -i "90s/.*/${list_murs_y[*]}/" $nouveau_fichier
	sed -i "93s/.*/${list_murs_z[*]}/" $nouveau_fichier
	sed -i "141s/.*/\t$debut_fil_x\t$debut_fil_y\t$debut_fil_z\t1\t0\t0/" $nouveau_fichier
	sed -i "144s/.*/\t$phi\t$alpha\t10\t0\t$taille_cellule\t41\t0 0 0 0 0 0/" $nouveau_fichier
	
else
	echo "Takes two arguments"
fi
