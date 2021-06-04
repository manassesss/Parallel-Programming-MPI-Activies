import numpy as np
from mpi4py import MPI

N = 840

def calculating_Pi(n, n_proc, rank):
    # Calculating PI
    sum = 0
    i = int((1 + (n/n_proc)*rank))
    j = int((n/n_proc)*(rank+1))
    for k in range(i, j+1):
        sum += 1 / (1 + ((k - 0.5) / n)**2)
    return  (sum /n)*4

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
processor = MPI.Get_processor_name()
n_process = comm.Get_size()
times = []
# Calculating time
comm.Barrier()
initialTime = MPI.Wtime()
pi = calculating_Pi(N, n_process, rank)
comm.Barrier()
finalTime = MPI.Wtime()
time = finalTime-initialTime
times.append(time)
#print('-----------------------------------------------')
print('Process ', rank, 'in the machine: ', processor, '| Result = ', str(pi))
#print(max(times))