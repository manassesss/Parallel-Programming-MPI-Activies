# :globe_with_meridians: Parallel Programming MPI Activies
This repository contain the solution for [4 problems](https://github.com/manassesss/Parallel-Programming-MPI-Activies/wiki/About-the-problems) proposed by professor in discipline of Distributed Systems.

To solution the problems, it was used Python 3.7.7 and a package of MPI in Python (mpi4py).

## :computer: Pre-requirements

### Python

To install Python you can acess the [oficial site](https://www.python.org/downloads/), download it and install it.

### mpi4py package

Install the mpi4py package using this comand on your terminal, if you use windows:

```
pip install mpi4py
```

To know more about mpi4py package, you can read the [documentation](https://mpi4py.readthedocs.io/en/stable/index.html)

### Machines

The machines used in this work was pre-configured by the professor and it is available [here](https://drive.google.com/open?id=1NnBFK06xK9eQt6oCHq9XZdCYesFZMstm&authuser=weslley%40ufpi.edu.br&usp=drive_fs)

## ⚙️ Assembly of clusters

In each machine's settings, add the project folder to the shared folders as follows:

<img src="https://i.imgur.com/IlLdPfg.png"/>

At the terminal of machines 2, 3 and 4, use the following commands:

```
sudo su -
mount -t nfs maq1:/home/mpiuser/cloud /home/mpiuser/cloud
```
Afterwards, use the following command on all machines:

```
sudo mount -t vboxsf cloud /home/mpiuser/cloud
```

## 🚀 Running the scripts

Now, just run the codes by machine 1, doing:

```
su - mpiuser
cd cloud
mpiexec -np 8 --hostfile maqs.txt python3 1_mpi.py
```
OBS.: 
* the number after *np* is the number of process in each version, you can use change this number if you want.
* in this case, the code that we use here was *1_mpi.py*
