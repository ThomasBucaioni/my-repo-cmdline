#include <iostream>
#include <mpi.h>
using namespace std ;

int main(int argc,char **argv)
{
  int n;
  int t;
  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &n);
  MPI_Comm_rank(MPI_COMM_WORLD, &t);
  cout << "Hello World du processus " << t << " parmi " << n << " processus" << endl;
  MPI_Finalize();
  return 0 ;
}
