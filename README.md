# conways-game-of-life
A version of Conway's Game of Life
originally based on the code from https://automatetheboringstuff.com/2e/chapter4/

Recreated using PyGame for better visual appeal
Added 'cell' class to keep track of individual cell live/dead state
to color according to alive/still alive/dead/still dead

Alive cells with 2 or 3 Alive neghbors stay Alive (symbol 'o')
Dead cells with 3 Alive neighbors become Alive
All other cells become Dead. (symbol '.')

Cells that are still Alive are Green 'o'
Newly Alive cells are Black 'o'
Newly Dead cells are Red '.'
Cells that are still Dead are '.' White (can't be seen against white background)

Press Spacebar to restart simulation with new pattern


Requires Pygame

```bash
pip install pygame
```

