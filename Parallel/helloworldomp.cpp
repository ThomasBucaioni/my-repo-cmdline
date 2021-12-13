#include <iostream>
#include <omp.h>
using namespace std ;

int main(int argc,char **argv)
{
  int nthreads, tid;
#pragma omp parallel private(nthreads, tid)
  {
    tid = omp_get_thread_num();
    nthreads = omp_get_num_threads();
    cout << "Hello World du thread " << omp_get_thread_num() << " parmi " << omp_get_num_threads() << endl;
  }
  return 0 ;
}
