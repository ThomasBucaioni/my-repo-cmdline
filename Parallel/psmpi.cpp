#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
#include <mpi.h>
using namespace std ;

// defini le type entier comme un int
using entier=int ;
//using entier=long ;
//using entier=size_t ;

int main(int argc,char **argv)
{
  entier N = 10 ;
  entier NpP ;
  int Lim ;
  entier M = 1 ;
  int nproc ;
  int tproc ;
  double debut,fin ; // pour mesurer les temps de calcul
  clock_t start,end ; // pour mesurer les temps de calcul
  double temps ;

  debut = clock();

  // prise en compte des options de la ligne de commande pour modifier N et M
  for(int i=0;i<argc;++i)
    {
      if(argv[i]==string("-n"))
        N = stol(argv[i+1]);
      if(argv[i]==string("-m"))
        M = stol(argv[i+1]);
    }
  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &nproc) ;
  MPI_Comm_rank(MPI_COMM_WORLD, &tproc) ;
  NpP = int(N / nproc) ;
  double h=0.5*M_PI/(N-1) ;
  if (tproc == 0)
    cout << "tailles : n= " << N << " ,  m= " << M << " , h= " << h << endl;

  // Phase1 : création de deux vecteurs de taille N
  start = clock();
  vector<double> x(N), y(N) ;
  end = clock() ;
  temps = (double)(end-start)/CLOCKS_PER_SEC ; // calcul la durée
  if (tproc == 0)
    cout << "allocation des vecteurs en "  << temps << " s" << endl;

  // Phase2 : initialisation des deux vecteurs
  if (tproc<(N%nproc))
    Lim = NpP + 1 ;
  else
    Lim = NpP ;
  cout << "tproc = " << tproc << " ; Lim = " << Lim << endl ;
  start = clock();
  for(entier i=0;i<Lim;++i)
    x[i]=pow(cos(i*h),2);
  for(entier i=0;i<Lim;++i)
    y[i]=pow(sin(i*h),2);
  end = clock() ;
  temps = (double)(end-start)/CLOCKS_PER_SEC ;
  if (tproc == 0)
    cout << "initialisation des vecteurs en "  << temps << " s" << endl;

  // Phase3 : calcule M fois le produit scalaire des deux vecteurs
  // M fois pour augmenter artificièlement le temps de calcul de cette phase
  double ps_tot = 0.0 ;
  start = clock();
  for(entier j=0;j<M;++j)
    {
      double ps = 0.0 ;
      double ps2 ;
      debut = MPI_Wtime();
      for(entier i=0;i<Lim;++i)
        ps += x[i]*y[i] ;
      //cout << "AVANT : tproc = " << tproc << " ; ps = " << ps << " ; ps2 = " << ps2 << endl ;
      MPI_Allreduce(&ps, &ps2, 1, MPI_DOUBLE, MPI_SUM, MPI_COMM_WORLD) ;
      //cout << "APRÈS : tproc = " << tproc << " ; ps = " << ps << " ; ps2 = " << ps2 << endl ;
      ps_tot += ps2 ;
      fin = MPI_Wtime() ;
      if (tproc == 0)
	cout << "j = " << j << " ; Temps de calcul : " << fin - debut << endl ;
    }
  end = clock() ;
  MPI_Finalize();
  temps = (double)(end-start)/CLOCKS_PER_SEC ;
  if (tproc == 0)
    cout << "ps_tot= " << ps_tot << " calculé en " << temps << " s"  << endl;

  fin = clock();
  temps = (double)(fin-debut)/CLOCKS_PER_SEC ;
  if (tproc == 0)
    cout << "temps total de " << temps << " s"  << endl;

  return 0 ;
}
