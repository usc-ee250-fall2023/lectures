# Name: Mark Redekopp
# email: redekopp@usc.edu

CC = g++
CFLAGS = -g
LDFLAGS = pthread


all : matmult_par par_sum par_sum_indiv par_sum_nolock

matmult_par : matmult_par.c
	$(CC) $(CFLAGS) matmult_par.c -o $@ -lpthread
par_sum : par_sum.cpp
	$(CC) $(CFLAGS) par_sum.cpp -o $@ -lpthread
par_sum_indiv : par_sum_indiv.cpp
	$(CC) $(CFLAGS) par_sum_indiv.cpp -o $@ -lpthread
par_sum_nolock : par_sum_nolock.cpp
	$(CC) $(CFLAGS) par_sum_nolock.cpp -o $@ -lpthread


clean:
	rm -f matmult_par par_sum par_sum_indiv par_sum_nolock *~
