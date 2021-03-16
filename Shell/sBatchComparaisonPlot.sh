#!/bin/bash
#set -v
#set -n
#set -x
pause ()
{
    read -n1 -p 'Press any key when ready...'
    echo
    echo -----
}
cd ~/TLM-Code/TLM+TW-AlgoReineix
rm tlmscn2
sMakeCpToScratch.sh
list_angles_phi=$(eval echo {90..00..-10})
for phi in $list_angles_phi
do
    echo -----
    echo "Angle en cours : $phi"
    while [ ! -f tlmscn2 ] ;
    do
	sleep 5
    done
    cd /scratch/cnt0024/eat2127/tbucaioni
    ~/bin/Angles/sChoixAngle.sh $phi 0 > sChoixAngle.log
    mv tlmscn-p0${phi}a000.dat tlmscn.dat
    pause # controle
    if [ -f tlmscn2 ]
    then
	rm ExecutionTermineeNormalement.txt
	echo -----
	echo "Lancement du job, angle $phi"
	echo -----
	sbatch job.slurm
    fi
    until [[ -e ExecutionTermineeNormalement.txt ]] && [[ $(wc -c < ExecutionTermineeNormalement.txt) -eq 46 ]]
    do 
	echo -----
	echo "Execution du script en cours, angle $phi"
	echo -----
	squeue -u tbucaioni
	if [ -f GENEFILMINCE0001 ] 
	then
	    echo -----
	    echo 'Fichier GENEFILMINCE0001 créé'
	    gnuplot script-gnuplot-geneencours &
	    sleep 1
	    display gene.png
	else
	    echo -----
	    echo 'Fichier GENEFILMINCE0001 non créé'
	fi
	sleep 30
    done
    echo -----
    echo 'Execution du script terminée normalement'
    until [ -f S11_TFR_GENEFILMINCE0001 ]
    do
	echo -----
        echo 'Fichier S11_TFR_GENEFILMINCE0001 non créé'
	sleep 1
    done
    echo -----
    echo 'Fichier S11_TFR_GENEFILMINCE0001 créé'
    gnuplot script-gnuplot-s11encours &
    sleep 1
    display s11.png
    echo -----
    echo "Déplacement des courbes dans ~/FichiersSortieAConserver/SchemaExpliciteParallele, fichiers gene|s11-p${phi}a00-para"
    mv GENEFILMINCE0001 ~/FichiersSortieAConserver/SchemaExpliciteParallele/gene-p${phi}a00-para
    mv S11_TFR_GENEFILMINCE0001 ~/FichiersSortieAConserver/SchemaExpliciteParallele/s11-p${phi}a00-para
    pause # controle
done
gnuplot script-gnuplot-genetotaux
sleep 1
display gene.png
gnuplot script-gnuplot-s11totaux
sleep 1
display s11.png
