Attempt:

Overview - we will rotate the array in place by essentially swapping cells in the array.

1. Begin with outer later, repeating the following steps layer by layer
2. save value at 0,0 (top left) to variable
3. Do:
    4. move bottom left to top left
    5. move bottom right to bottom left
    6. move top right to bottom right
    7. move saved var (was top left) to top right
4. Move right one cell and repeat.
    5. top row second cell, right row second cell, bottom then left.
6. Repeat from step 1

Beat 95% run, 60% memory