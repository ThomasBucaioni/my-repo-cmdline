#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
using namespace std ;

// defini le type entier comme un int 
using entier=int ; 
//using entier=long ;
//using entier=size_t ;

int main(int argc,char **argv)
{
  entier N = 10 ;
  entier M = 1 ;
  clock_t debut,fin ; // pour mesurer les temps de calcul
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
  double h=0.5*M_PI/(N-1) ;
  cout << "tailles : n= " << N << " ,  m= " << M << " , h= " << h << endl;

  // Phase1 : création de deux vecteurs de taille N 
  start = clock();
  vector<double> x(N), y(N) ; 
  end = clock() ;
  temps = (double)(end-start)/CLOCKS_PER_SEC ; // calcul la durée 
  cout << "allocation des vecteurs en "  << temps << " s" << endl;

  // Phase2 : initialisation des deux vecteurs  
  start = clock();
  for(entier i=0;i<N;++i)
    x[i]=pow(cos(i*h),2);
  for(entier i=0;i<N;++i)
    y[i]=pow(sin(i*h),2);
  end = clock() ;
  temps = (double)(end-start)/CLOCKS_PER_SEC ;
  cout << "initialisation des vecteurs en "  << temps << " s" << endl;

  // Phase3 : calcule M fois le produit scalaire des deux vecteurs
  // M fois pour augmenter artificièlement le temps de calcul de cette phase  
  start = clock();
  double ps_tot = 0.0 ;
  for(entier j=0;j<M;++j)
  {
    double ps = 0.0 ;
    for(entier i=0;i<N;++i)
      ps += x[i]*y[i] ;

    ps_tot += ps ;
  }
  end = clock() ;
  temps = (double)(end-start)/CLOCKS_PER_SEC ;
  cout << "ps_tot= " << ps_tot << " calcluler en " << temps << " s"  << endl;
  
  fin = clock();
  temps = (double)(fin-debut)/CLOCKS_PER_SEC ;
  cout << "temps total de " << temps << " s"  << endl;
  
  return 0 ;
}
