Following the advice in https://www.open-mpi.org/faq/?category=debugging, under point 6, this is a brief example of how to do MPI debugging for small problems with gdb and screen. The approach is the following:
- Create a main screen
- Create a window in the main screen for the mpirun command
- Create a window in the main screen for each of the spawned processes, in which a separate gdb session is attached to each of them.

Note that on some distributions you may get a "ptrace: Operation not permitted" when gdb attempts to attach to the child processes. This is a security choice, and depending on the distribution and your preference, there are different ways around it. Searching for "gdb attach ptrace not permitted" for your distribution should bring up something appropriate.

To terminate the screen, either:
- Type Ctrl+a \
- or detach with Ctrl+a d, and run "screen -S debugging -X quit".
