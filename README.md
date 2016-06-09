Note that on some distributions you may get a "ptrace: Operation not permitted" when gdb attempts to attach to the child processes. This is a security choice, and depending on the distribution and your preference, there are different ways around it. Googling "gdb attach ptrace not permitted" for your distribution should bring up something appropriate.

To terminate the screen, run "screen -S debugging -X quit".
