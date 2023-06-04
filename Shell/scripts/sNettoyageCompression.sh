#!/bin/bash

SCRATCH=/scratch/cnt0024/eat2127/tbucaioni

pause ()
{
    read -n1 -p 'Press any key when ready...'
}
    
num_archive=1

while [[ 1 ]]
do

	# Test de sortie
	[[ -e ~/fin.txt ]] && break

	# Parcours des répertoires de résultats
	cd ${SCRATCH}/Angles
	#cd ~/bin/Angles

	list_dir=$(ls -d */)
	echo "liste des repertoires: "
	echo "-----"
	echo "$list_dir"
	echo "-----"

	# Parcours des repertoires
	for my_dir in $list_dir
	do
		echo "-----"
		echo "repertoire analysé: $my_dir"
		#cd $my_dir
		#pwd 
		echo "-----"
		echo "contenu: $(ls $my_dir)"

		#pause

		# Test sur les fins d'execution
		if [[ -e $my_dir/ExecutionTermineeNormalement.txt ]] && [[ $(wc -c < $my_dir/ExecutionTermineeNormalement.txt) -eq 46 ]]
		then

			echo "Le fichier 'ExecutionTermineeNormalement.txt' existe"

			# Nettoyage des jobs terminés
			if [[ $my_dir =~ p([0-3][0-9][0-9])a([-0][0-9][0-9])tx([0-3])ty([0-3])tz([0-3]) ]]
			then
				echo "indices: ${BASH_REMATCH[@]}"
				#cp "p${BASH_REMATCH[1]}a${BASH_REMATCH[2]}tx${BASH_REMATCH[3]}ty${BASH_REMATCH[4]}tz${BASH_REMATCH[5]}" $SCRATCH/AnglesArchivage/
				echo copie : ${my_dir}GENEFILMINCE0001 ${SCRATCH}/AnglesArchivage/p${BASH_REMATCH[1]}a${BASH_REMATCH[2]}tx${BASH_REMATCH[3]}ty${BASH_REMATCH[4]}tz${BASH_REMATCH[5]}
				mkdir ${SCRATCH}/AnglesArchivage/p${BASH_REMATCH[1]}a${BASH_REMATCH[2]}tx${BASH_REMATCH[3]}ty${BASH_REMATCH[4]}tz${BASH_REMATCH[5]}
				cp "${my_dir}GENEFILMINCE0001" "${SCRATCH}/AnglesArchivage/p${BASH_REMATCH[1]}a${BASH_REMATCH[2]}tx${BASH_REMATCH[3]}ty${BASH_REMATCH[4]}tz${BASH_REMATCH[5]}/gene-p${BASH_REMATCH[1]}a${BASH_REMATCH[2]}tx${BASH_REMATCH[3]}ty${BASH_REMATCH[4]}tz${BASH_REMATCH[5]}"
				cp "${my_dir}S11_TFR_GENEFILMINCE0001" "${SCRATCH}/AnglesArchivage/p${BASH_REMATCH[1]}a${BASH_REMATCH[2]}tx${BASH_REMATCH[3]}ty${BASH_REMATCH[4]}tz${BASH_REMATCH[5]}/s11-p${BASH_REMATCH[1]}a${BASH_REMATCH[2]}tx${BASH_REMATCH[3]}ty${BASH_REMATCH[4]}tz${BASH_REMATCH[5]}"
				cp "${my_dir}dipole_41m.out" "${SCRATCH}/AnglesArchivage/p${BASH_REMATCH[1]}a${BASH_REMATCH[2]}tx${BASH_REMATCH[3]}ty${BASH_REMATCH[4]}tz${BASH_REMATCH[5]}/dipole_41m-p${BASH_REMATCH[1]}a${BASH_REMATCH[2]}tx${BASH_REMATCH[3]}ty${BASH_REMATCH[4]}tz${BASH_REMATCH[5]}"
				#awk 
				rm -r $my_dir
			fi
		
		else
			echo "Le fichier 'ExecutionTermineeNormalement.txt' n'existe pas dans $my_dir"
		fi
		
		#pause

    	done

	# Test sur les repertoires ouverts
	# (autre idee de comptage : "readarray -t -d'.' lines")

	cd $SCRATCH/AnglesArchivage/

	list_dir=$(ls -l | grep ^d | awk '{print $9}') #$(ls -d */)
	nb_dir=$(ls -l | grep ^d | wc -l)
	echo "Il y a $nb_dir répertoires (seuil à $((4**3))) :"
	echo "-----"
	echo "$list_dir"
	echo "-----"

	# Compression des repertoires d'archivage et copie dans le $HOME
	if [[ nb_dir -ge $(( 4*4*4 )) ]]
	then
		tar --remove-files --create --verbose --gzip --file="angleArchive${num_archive}.tar.gz" $list_dir
		mv angleArchive${num_archive}.tar.gz ~/AngleArchivage/
		echo "-----"
		echo " Au moins $((4**3)) travaux terminés - " $(date)
		num_archive=$((num_archive+1))
	fi

	# Affichage des travaux en cours et attente 1mn 
	squeue -u tbucaioni
	echo "-----"
	echo " Sleep 30 secondes - " $(date)
	echo "-----"
	sleep 30
done
