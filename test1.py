import numpy as np
from mpi4py import MPI




comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0 :
    print('my rank is', rank)
    data = {'a':0 , 'b':1}
    comm.send(data, dest=1)

if rank == 1:
    print('my rank is', rank)
    data = comm.recv(source=0)
    print(data)