// Lock on each update and see
// that performance is degraded.
#include <iostream>
#include <cstdlib>
#include <time.h>
#include <sys/time.h>
#include <pthread.h>

using namespace std;
#define MAX 100000000

int numbers[MAX];

struct ThreadInfo {
  int tid;
  int nThreads;
  int* sumPtr;
  pthread_mutex_t* lock;
};

void* tfunc(void* arg)
{
  struct ThreadInfo* info = (struct ThreadInfo*) arg;
  int start = info->tid * (MAX / info->nThreads);
  int end = (info->tid + 1) * (MAX / info->nThreads);
  
  int i, sum = 0;
  for(i= start; i < end; i++){
    pthread_mutex_lock(info->lock);
    *(info->sumPtr) += numbers[i];
    pthread_mutex_unlock(info->lock);
  }
}

int main(int argc, char *argv[])
{
  pthread_attr_t attr;
  pthread_t *threads;
  struct ThreadInfo* tinfo;
  int num_threads;
  pthread_mutex_t mylock;
  
  int seq_sum = 0, par_sum = 0, t, rc;
  
  struct timeval start, finish;
  unsigned usec;
  
  if (argc < 2){
    cerr << "Usage ./exec_file num_threads" << endl;
    return 1;
  }

  srand(time(0));
  for(int i=0; i < MAX; i++){
    numbers[i] = rand() % 100;
  }

  gettimeofday(&start, NULL);
  for(int i=0; i < MAX; i++){
    seq_sum += numbers[i];
  }
  gettimeofday(&finish, NULL);
  usec = finish.tv_sec*1000*1000 + finish.tv_usec;
  usec -= (start.tv_sec*1000*1000 + start.tv_usec);
  cout << "Sequential answer is " << seq_sum << endl;
  cout << "Time taken for 1 thread = " << usec << " us " << endl;


  num_threads = atoi(argv[1]);
  threads = new pthread_t[num_threads];
  tinfo = new struct ThreadInfo[num_threads];
  


  gettimeofday(&start, NULL);
  // Create num_threads-1 more threads in addition to main()
  pthread_attr_init(&attr);
  pthread_mutex_init(&mylock, NULL);
  for(t = 0; t < num_threads; t++){
    tinfo[t].tid = t;
    tinfo[t].nThreads = num_threads;
    tinfo[t].sumPtr = &par_sum;
    tinfo[t].lock = &mylock;
    
    rc = pthread_create(&threads[t], &attr, tfunc, (void*)&tinfo[t]);
    if(rc){
      cout << "Error: return code from pthread_create is " << rc << endl;
    }

  }
  for(t = 0; t < num_threads; t++){
    pthread_join(threads[t], NULL);
  }

  gettimeofday(&finish, NULL);
  usec = finish.tv_sec*1000*1000 + finish.tv_usec;
  usec -= (start.tv_sec*1000*1000 + start.tv_usec);

  
  cout << "Parallel answer is " << par_sum << endl;
  cout << "Time taken for " << num_threads << " = " << usec << " us " << endl;
  delete [] threads;
  delete [] tinfo;
  return 0;
}
