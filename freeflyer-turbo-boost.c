/* ========================================================================= */
//  gcc -g -o fftb freeflyer-turbo-boost.c && echo TLLT | ./fftb

#include <stdio.h>
#include <stdlib.h>

/* ========================================================================== */
/*                          Constants                                         */
/* ========================================================================== */
#define LEFT 'L'
#define RIGHT 'R'
#define THRUST 'T'
#define CRUISE 'C'
#define LIMIT 65000
/* .......................................................................... */

/* ========================================================================== */
/*                          Structs                                           */
/* ========================================================================== */
struct gps_struct {
    int p_x;
    int p_y;
    int v_x;
    int v_y;
    int o_x;
    int o_y;
};

void update(struct gps_struct* gps, char letter);



/* ========================================================================== */
/*                          Main( )                                           */
/* ========================================================================== */
int main(int argc, char* argv[]) {
  // printf(">>>> freeflyer-turbo-boost.c >>>> \n\n");
  struct gps_struct* gps = malloc(sizeof(struct gps_struct));
  gps->p_x = 0;
  gps->p_y = 0;
  gps->v_x = 0;
  gps->v_y = 0;
  gps->o_x = 1;
  gps->o_y = 0;

  char payload[LIMIT];
  int i = 0;
  while(-1 != (payload[i++] = getchar()));
  char index;

  for(int j = 0; j < i-2; j++) {
    index = payload[j];
    update(gps, index);
    printf("Command=%c: Position(%d, %d) Velocity(%d, %d) Orientation(%d, %d) \n", index, gps->p_x, gps->p_y, gps->v_x, gps->v_y, gps->o_x, gps->o_y);
  }

  return 0;
}

void update(struct gps_struct* gps, char letter) {
    switch (letter)
    {
     case LEFT:
          gps->o_x = 1;
          gps->o_y = 1;
          break;
     case RIGHT:
           gps->o_x = 1;
           gps->o_y = 1;
         break;
     case THRUST:

         break;
     case CRUISE:

         break;
     default:
         break;
  }
}
