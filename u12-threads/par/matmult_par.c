#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#define SIZE 1024

int num_threads;

int A[SIZE][SIZE];
int B[SIZE][SIZE];
int C[SIZE][SIZE];
int Aref[SIZE][SIZE];
int Bref[SIZE][SIZE];
int Cref[SIZE][SIZE];

void *mult_thread(void *threadid)
{
  int i, j, k;
  unsigned int tid;
  tid = (unsigned long long) threadid & 0xffffffff;
  int tstart = (SIZE/num_threads)*tid;
  int tfinish = (SIZE/num_threads)*(tid+1);

  printf("In thread %d\n", tid);

  for(i = tstart; i < tfinish; i++) {
    for(j = 0; j < SIZE; j++) {
      for(k = 0; k < SIZE; k++) {
	C[i][j] = C[i][j] + A[i][k]*B[k][j];
      }
    }
  }
  return 0;

}


int main(int argc, char *argv[])
{

  pthread_t *threads;
  pthread_attr_t attr;
  int t, rc, i, j, k, ii, jj, kk, count;
  struct timeval start, finish;
  unsigned usec;
  void *status;
  int bsize = 32;

  if (argc < 2){
    fprintf(stderr, "Usage ./exec_file num_threads\n");
    exit(1);
  }

  num_threads = atoi(argv[1]);

  threads = new pthread_t[num_threads];

  for(i = 0; i < SIZE; i++){
    for(j = 0; j < SIZE; j++){
      A[i][j] = Aref[i][j] = i*SIZE+j;
      B[i][j] = Bref[i][j] = j*SIZE+i;
      C[i][j] = Cref[i][j] = 0;
    }
  }

  printf("Performing reference implementation for comparison purposes\n");
  for(i = 0; i < SIZE; i+=bsize) {
    for(j = 0; j < SIZE; j+=bsize) {
      for(k = 0; k < SIZE; k+=bsize) {
	for(ii = i; ii < i+bsize; ii++) {
	  for(jj = j; jj < j+bsize; jj++) {
	    for(kk = k; kk < k+bsize; kk++) {
	      Cref[ii][jj] = Cref[ii][jj] + Aref[ii][kk] * Bref[kk][jj];
	    }
	  }
	}
      }
    }
  }

  printf("In main: Creating %d threads for row parallel.\n", num_threads);
  gettimeofday(&start, NULL);

  // Create num_threads-1 more threads in addition to main()
  for(t = 0; t < num_threads-1; t++){
    pthread_attr_init(&attr);
    rc = pthread_create(&threads[t], &attr, mult_thread, (void*)t);
    if(rc){
      printf("Error: return code from pthread_create is %d.\n", rc);
    }

  }
  // Let the main() thread do some work as well
  mult_thread((void *)(num_threads-1));

  // Wait for threads to finish
  for(t = 0; t < num_threads-1; t++) {
    rc = pthread_join(threads[t], &status);
    if(rc){
      printf("Error from pthread_join().\n");
    }
  }

  gettimeofday(&finish, NULL);
  usec = finish.tv_sec*1000*1000 + finish.tv_usec;
  usec -= (start.tv_sec*1000*1000 + start.tv_usec);
  printf("Time taken with row parallelization = %u us & %d threads.\n", usec, num_threads);

  // Checking row parallel
  count = 0;
  for(i = 0; i < SIZE; i++) {
    for(j = 0; j < SIZE; j++)	{
      if(Cref[i][j] != C[i][j]){
	count++;
      }
    }
  }
  printf("Error count = %d.\n", count);

  delete [] threads;

}
