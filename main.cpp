#include <mpi.h>
#include <unistd.h>
#include <string>

int main (int argc, char *argv[])
{
	// Initialize MPI
	MPI_Init(&argc, &argv);
	int worldSize;
	int worldRank;
	MPI_Comm_size(MPI_COMM_WORLD, &worldSize);
	MPI_Comm_rank(MPI_COMM_WORLD, &worldRank);

	// By default, don't wait for gdb to attach
	bool waitForGDB = false;

	// Parse arguments
	int argIndex = 0;    
	while (argIndex < argc){
		if (std::string(argv[argIndex]) == "-gdbwait"){
			waitForGDB = true;
			argIndex++;
		}
		else{
			argIndex++;
		}
	}

	// Wait for gdb to attach
	if (waitForGDB) {
		printf("PID %d (rank %d) ready for attach.\n", getpid(), worldRank);
		printf("Run 'gdb executablePath PID' to attach gdb.\n");
		printf("Then run 'frame 2' to move up to this frame.\n");
		printf("Finally, run 'set doWait=false' and 'c' (continue) to continue.\n");
		bool doWait = true;
		while (doWait) {
			sleep(5);
		}
		printf("Continuing...\n");
	}
    
    // Test behavior around a barrier
    printf("Rank %d before barrier.\n", worldRank);
    MPI_Barrier(MPI_COMM_WORLD);
    printf("Rank %d after barrier.\n", worldRank);
    
    // Finalize MPI
    MPI_Finalize();
}
