import numpy as np
from mpi4py import MPI

N = 840

def calculating_Pi(n):
    # Calculating PI
    sum = 0
    for i in range(1, n+1):
        sum += 1 / (1 + ((i - 0.5) / n)**2)
    return  (sum * (1/n))*4

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
processor = MPI.Get_processor_name()
n_process = comm.Get_size()
times = []
# Calculating time
comm.Barrier()
initialTime = MPI.Wtime()
pi = calculating_Pi(N)
comm.Barrier()
finalTime = MPI.Wtime()
time = (finalTime-initialTime)
times.append(time)
#print('-----------------------------------------------')
print('Process ', rank, 'in the machine: ', processor, '| Result = ', str(pi),' Execution time: ', time)
#print(max(times))
