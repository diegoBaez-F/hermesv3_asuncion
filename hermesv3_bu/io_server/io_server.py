#!/usr/bin/env python3

from mpi4py import MPI


class IoServer:
    """
    :param comm: Communicator object
    :type comm: MPI.Comm
    """
    def __init__(self, comm):
        self.comm = comm
