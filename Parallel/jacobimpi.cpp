#include <iostream>
#include <array>
#include <vector>
#include <cmath>
#include <string>
#include <fstream>

#include <mpi.h>

using namespace std ;

int main(int argc,char**argv)
{
  MPI_Init(&argc,&argv);

  double a,b;
  a = MPI_Wtime();

  int rank,size ;
  MPI_Comm_rank(MPI_COMM_WORLD,&rank);
  MPI_Comm_size(MPI_COMM_WORLD,&size);

  int n = 16;
  long max_iter = 1e8 ;
  double epsilon = 1e-7 ;

  int ncsr = std::round(sqrt(size));
  bool found = false ;
  while (!found)
  {
    if(size%ncsr==0)
      found = true ;
    else
      ncsr--;
  }
  int ncl=ncsr ;
  int ncc=size/ncsr ;

  for(int i=0;i<argc;++i)
  {
    if(argv[i]==string("-n"))
     n = stoi(argv[i+1]);
    if(argv[i]==string("-e"))
     epsilon = stod(argv[i+1]);
    if(argv[i]==string("-i"))
     max_iter = stol(argv[i+1]);
    if(argv[i]==string("-ncl"))
     ncl = stoi(argv[i+1]);
    if(argv[i]==string("-ncc"))
     ncc = stoi(argv[i+1]);
    if(argv[i]==string("-h"))
  	{
  		cout << "Usage : " << argv[0] << " [-n N=16] [-e E=1e-7] [-i I=1e8] [-ncl P] [-ncc Q]" << endl; 
  		exit(0);
  	}
  
  } 

  int n2 = n + 2 ;
  int N = n2 * n2 ;
  double h = 1.0/(n+1) ;
  double h2 = h*h ;


  if(ncl*ncc!=size)
  {
    if(rank==0)
      cout << "Error : ncl * ncc must be egual to the number of cores used : " << ncl << " * " << ncc << " != " <<  size << endl; 
    exit(1) ;
  }
  if(n%ncl!=0 || n%ncc!=0)
  {
    if(rank==0)
      cout << "Error : n must be a mutiple of ncl and ncc : n= " << n << " ncl= " << ncl << " ncc= " << ncc << endl ; 
    exit(1) ;
  }

  int nll = n / ncl ;  // number of local rows
  int nlc = n / ncc ;  // number of local columns 
  int nll2 = nll + 2 ;
  int nlc2 = nlc + 2 ;
  int Nl = nll2 * nlc2 ;
  
  vector<int> BTLR_rank(4);   // Bottom, top, left , right  
  BTLR_rank[0] = rank - ncc ;
  BTLR_rank[1] = rank + ncc ;
  BTLR_rank[2] = rank - 1 ;
  BTLR_rank[3] = rank + 1 ;

  // on the border there is no neigbours (-1) 
  if(rank < ncc) 
    BTLR_rank[0] = -1 ;
  if(rank >= (ncl-1)*ncc ) 
    BTLR_rank[1] = -1 ;
  if(rank%ncc == 0 ) 
    BTLR_rank[2] = -1 ;
  if(rank%ncc == ncc-1 ) 
    BTLR_rank[3] = -1 ;

  if(rank==0)
  {
    cout << "running over " << size << " MPI processes (" << ncl << " * " << ncc  << ")" << endl ;
    cout << "N= " << n << " " << n2 << " " << N << " " << h << " "<< h2 << endl;
    cout << "Nloc= " << nll << " " << nlc << " "  << nll2 << " " << nlc2  << " " << Nl << endl;
  }

/*
  for(int i=0;i<size;i++)
  {
    if(rank==i)
      cout << "rank= " << rank << " BTLR_rank= " << BTLR_rank[0] << " " << BTLR_rank[1] << " " << BTLR_rank[2] << " " << BTLR_rank[3] << endl;
    MPI_Barrier(MPI_COMM_WORLD);
  }
*/

  vector<double> f(Nl);
  for(int i=0;i<Nl;i++)
    f[i] = 1.0 ;

  vector<double> x(Nl);
  for(int i=0;i<Nl;i++)
    x[i] = 0.0 ;

  vector<double> oldx(Nl);

  vector<double> BufferS(2*nll*nlc) ;
  vector<double> BufferR(2*nll*nlc) ;
  vector<MPI_Request> requestS(4), requestR(4) ;
  vector<MPI_Status> statusS(4), statusR(4) ;

  int iter = 0 ;
  double error = 1.0 ;

//  ofstream os("toto_"+std::to_string(rank)+".txt");

  while(error>epsilon && iter<max_iter)
  {
//    cout << "iter= " << iter << " error= " << error << endl;
    for(int i=0;i<Nl;i++)
    {
      oldx[i] = x[i] ;
    }

    for(int i=1;i<nll2-1;i++)
    {
       for(int j=1;j<nlc2-1;j++)
       {
         int p = i*nlc2+j ;
         x[p] =  0.25 * ( h2 *f[p] + (oldx[p+1] + oldx[p-1] + oldx[p+nlc2] + oldx[p-nlc2]));  
       }
    }
/*
    for(int k=0;k<nl2;k++)
    {
      for(int l=0;l<nl2;l++)
         os << x[k*nl2+l] << " ";
      os << endl;
    }
    os << endl;
*/
    array<int,4> BTLR_size = { nlc, nlc, nll, nll } ;
    array<int,5> BTLR_pos ;
    BTLR_pos[0] = 0;
    for(int i=0;i<4;i++)
      BTLR_pos[i+1] = BTLR_pos[i] + BTLR_size[i] ;

    for(int i=0;i<nlc;i++)
    {
      BufferS[0*nlc+i] = x[nlc2+1+i] ;
      BufferS[1*nlc+i] = x[(nll2-2)*nlc2+1+i] ;
    }
    for(int i=0;i<nll;i++)
    {
      BufferS[2*nlc+i] = x[(i+1)*nlc2+1] ;
      BufferS[2*nlc+nll+i] = x[(i+1)*nlc2+nlc2-2] ;
    }
/*
    for(int i=0;i<BufferS.size();i++)
      os << BufferS[i] << " " ;
    os << " BufferS " << rank << endl;
    os << endl;
*/

    for(int i=0;i<4;i++)
    {
      if(BTLR_rank[i]!=-1)
        MPI_Irecv(&(BufferR[BTLR_pos[i]]),BTLR_size[i],MPI_DOUBLE,BTLR_rank[i],123,MPI_COMM_WORLD,&(requestR[i]));
    }

    for(int i=0;i<4;i++)
    {
      if(BTLR_rank[i]!=-1)
        MPI_Isend(&(BufferS[BTLR_pos[i]]),BTLR_size[i],MPI_DOUBLE,BTLR_rank[i],123,MPI_COMM_WORLD,&(requestS[i]));
    }
   
    for(int i=0;i<4;i++)
    {
      if(BTLR_rank[i]!=-1)
       MPI_Wait(&(requestR[i]), &(statusR[i]));
    }
/*
    for(int i=0;i<BufferR.size();i++)
      os << BufferR[i] << " " ;
    os << " BufferR " << rank << endl;
    os << endl;
*/
    if(BTLR_rank[0]!=-1)
      for(int i=0;i<nlc;i++)
        x[0*nlc2 + 1 + i] = BufferR[0*nlc+i] ;
    if(BTLR_rank[1]!=-1)
      for(int i=0;i<nlc;i++)
        x[(nll2-1)*nlc2 + 1+ i] = BufferR[1*nlc+i] ;
    if(BTLR_rank[2]!=-1)
      for(int i=0;i<nll;i++)
        x[(i+1)*nlc2 + 0] = BufferR[2*nlc+i] ;
    if(BTLR_rank[3]!=-1)
      for(int i=0;i<nll;i++)
        x[(i+1)*nlc2 + nlc2-1] = BufferR[2*nlc+nll+i] ;


    double error_loc = 0.0 ;
    for(int i=1;i<nll2-1;i++)
    {
       for(int j=1;j<nlc2-1;j++)
       {
         int p = i*nlc2+j ;
         error_loc += pow(x[p] -oldx[p],2.0) ;
       }
    }
    MPI_Allreduce(&error_loc,&error,1, MPI_DOUBLE, MPI_SUM, MPI_COMM_WORLD );
    error = sqrt(error) ;

    for(int i=0;i<4;i++)
    {
      if(BTLR_rank[i]!=-1)
       MPI_Wait(&(requestS[i]), &(statusS[i]));
    }

//    cout << error << endl;
    iter++;

/*
    for(int k=0;k<nl2;k++)
    {
      for(int l=0;l<nl2;l++)
         os << x[k*nl2+l] << " ";
      os << endl;
    }
    os << endl;
*/
  }

  b = MPI_Wtime();

  array<int,2> centerX ;
  array<int,2> centerC ;
  centerC[0]=ncl/2;
  if(ncl%2==1)
    centerX[0]=nll2/2;
  else
    centerX[0]=1;

  centerC[1]=ncc/2;
  if(ncc%2==1)
    centerX[1]=nlc2/2;
  else
    centerX[1]=1 ;
   


  if(rank==centerC[0]*ncc+centerC[1])
  {
    cout << "iter= " << iter << " error= " << error << " val= " << x[centerX[0]*nlc2+centerX[1]] << " in " << b-a << " s" <<   endl;
  }  


  MPI_Finalize();
  return 0 ;
}
