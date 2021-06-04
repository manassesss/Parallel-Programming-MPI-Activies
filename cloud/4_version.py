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
results = np.zeros(1)
sum_results = np.zeros(1)

if(840 % n_process != 0):
        if rank == 0 :
            print("ERROR, it must be divisor of ", N)
else:
    comm.Barrier()
    initialTime = MPI.Wtime()
    results[0] = calculating_Pi(N, n_process, rank)
    finalTime = MPI.Wtime()

    time = finalTime-initialTime
    comm.Reduce(results, sum_results, op =MPI.SUM, root=0)
    comm.Barrier()
    comm.send([time],dest = 0)
    times.append(time)
    print('Process ', rank, 'in the machine: ', processor, '| Result = ', results[0])
    if rank == 0:
        print('Result = ', sum_results[0])
print('time ', max(times))