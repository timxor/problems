# 🛰 uss-freeflyer 🛰

Welcome to space! 🛰

The solution is pretty ugly but works for all three cases.
I did not have time to make tests or validate input and simply ignore all characters except 'R' 'L' 'T' 'C'. I also limit the size input to ~65k bytes.
I had wanted to make functions within the structs but you can't do that with c!
I also would have refactored a bunch of other things.

To compile & run this project you can use cmake (Version 3.3 or later) or gcc.
Dependencies include standard C libs `<stdio.h>` & `<stdlib.h>`.`

# build using gcc
```
cd ~/uss-freeflyer
gcc -g -o fftb freeflyer-turbo-boost.c
```

## run it
Then you can execute the binary `fftb` with simple maneuver plans like so:
```
echo TLLT | ./fftb
echo LTLLTTRRT | ./fftb
echo TLLTRTRRCCCT | ./fftb
```

# build using cmake/make
```
cd ~/uss-freeflyer
cmake .
make
```

## run it
Then you can execute the binary `freeflyer-turbo-boost` with simple maneuver plans like so:
```
echo TLLT | ./freeflyer-turbo-boost
echo LTLLTTRRT | ./freeflyer-turbo-boost
echo TLLTRTRRCCCT | ./freeflyer-turbo-boost
```
