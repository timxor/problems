/* ========================================================================= */
//  commands below compile and run with example maneuver plans
//
//  gcc -g -o fftb freeflyer-turbo-boost.c && echo TLLT | ./fftb
//  gcc -g -o fftb freeflyer-turbo-boost.c && echo TLLTRTRRCCCT | ./fftb
//  gcc -g -o fftb freeflyer-turbo-boost.c && echo LTLLTTRRT | ./fftb

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

// this function takes the current position, velocity, orientation and command
// and updates its location.
void update(struct gps_struct* gps, char letter);

/* ========================================================================== */
/*                          Main( )                                           */
/* ========================================================================== */
int main(int argc, char* argv[]) {

  // default struct with default instance data
  struct gps_struct* gps = malloc(sizeof(struct gps_struct));
  gps->p_x = 0;
  gps->p_y = 0;
  gps->v_x = 0;
  gps->v_y = 0;
  gps->o_x = 1;
  gps->o_y = 0;

  char payload[LIMIT];
  int i = 0;
  char index;

  // grab all the input from stdin
  while(-1 != (payload[i++] = getchar()));

  // for each character from the input, update the gps location
  for(int j = 0; j < i-2; j++) {
    index = payload[j];
    update(gps, index);
    printf("Command=%c: Position(%d, %d) Velocity(%d, %d) Orientation(%d, %d) \n", index, gps->p_x, gps->p_y, gps->v_x, gps->v_y, gps->o_x, gps->o_y);
  }

  return 0;
}

// this function takes the current position, velocity, orientation and command
// and updates its location.
void update(struct gps_struct* gps, char letter) {
    switch (letter)
    {
     case LEFT:
        // update orientation
        if(gps->o_x == 1 && gps->o_y == 0) {
          gps->o_x = 0;
          gps->o_y = 1;
        }else if(gps->o_x == 0 && gps->o_y == 1) {
          gps->o_x = -1;
          gps->o_y = 0;
        }else if(gps->o_x == -1 && gps->o_y == 0) {
          gps->o_x = 0;
          gps->o_y = -1;
        }else if(gps->o_x == 0 && gps->o_y == -1) {
          gps->o_x = 1;
          gps->o_y = 0;
        }

        // // update position
        if(gps->v_x > 0) {
          gps->p_x = gps->p_x + gps->v_x;
        }else if(gps->v_y > 0) {
          gps->p_y = gps->p_y + gps->v_y;
        }else if(gps->v_x < 0) {
          gps->p_x = gps->p_x + gps->v_x;
        }else if(gps->v_y < 0) {
          gps->p_y = gps->p_y + gps->v_y;
        }
        break;
     case RIGHT:
       // update orientation
       if(gps->o_x == 1 && gps->o_y == 0) {
         gps->o_x = 0;
         gps->o_y = -1;
       }else if(gps->o_x == 0 && gps->o_y == -1) {
         gps->o_x = -1;
         gps->o_y = 0;
       }else if(gps->o_x == -1 && gps->o_y == 0) {
         gps->o_x = 0;
         gps->o_y = 1;
       }else if(gps->o_x == 0 && gps->o_y == 1) {
         gps->o_x = 1;
         gps->o_y = 0;
       }

       // // update position
       if(gps->v_x > 0) {
         gps->p_x = gps->p_x + gps->v_x;
       }else if(gps->v_y > 0) {
         gps->p_y = gps->p_y + gps->v_y;
       }else if(gps->v_x < 0) {
         gps->p_x = gps->p_x + gps->v_x;
       }else if(gps->v_y < 0) {
         gps->p_y = gps->p_y + gps->v_y;
       }
        break;
     case THRUST:
        gps->v_x = gps->v_x + gps->o_x;
        gps->v_y = gps->v_y + gps->o_y;

        // // update position
        if(gps->v_x > 0) {
          gps->p_x = gps->p_x + gps->v_x;
        }else if(gps->v_y > 0) {
          gps->p_y = gps->p_y + gps->v_y;
        }else if(gps->v_x < 0) {
          gps->p_x = gps->p_x + gps->v_x;
        }else if(gps->v_y < 0) {
          gps->p_y = gps->p_y + gps->v_y;
        }
        break;
     case CRUISE:
        // update position
       if(gps->v_x > 0) gps->p_x = gps->p_x + gps->v_x;
       if(gps->v_y > 0) gps->p_y = gps->p_y + gps->v_y;
       break;
     default:
      break;
  }
}
