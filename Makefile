all: main

main: main.cpp
	mpic++ -g main.cpp -o main -lmpi
