# Parallel computation

## Open MP

`g++ -fopenmp -O1 -o helloomp helloworldomp.cpp ; export OMP_NUM_THREADS=3 ; ./helloomp`

## Open MPI

`mpic++ -O1 -o hellompi helloworldmpi.cpp ; mpirun -np 2 ./hellompi`


