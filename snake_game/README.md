# Snake Game (Tkinter)

A classic Snake game built with Python’s `tkinter`.  
Control the snake with the arrow keys, eat food to grow, and avoid hitting the walls or yourself.  
After game over, you can press **Space** to play again.

## File

- `snake.game.py` – main Tkinter app.

## Features

- Grid-based snake movement using a `Canvas`.
- Configurable constants:
  - `GAME_WIDTH`, `GAME_HEIGHT`
  - `SPEED` (movement delay)
  - `SPACE_SIZE` (grid cell size)
  - `BODY_PARTS` (starting length)
- Growing mechanic:
  - Snake grows when it eats food.
  - Food appears at random grid positions aligned to the grid.
- Collision detection:
  - Snake dies if it hits a wall.
  - Snake dies if it runs into its own body.
- Score tracking:
  - Score label at the top.
  - Score increases when food is eaten.
- Game over screen:
  - “GAME OVER” in the center.
  - “Press SPACE to play again” below it.
- Restart logic:
  - Press Space to reset snake, food, score, and restart the loop.
  - Space binding is removed after restart to avoid multiple overlapping games.
- Direction control:
  - Arrow keys (`Left`, `Right`, `Up`, `Down`) change direction.
  - Prevents reversing directly into the opposite direction (no instant self-kill).
 
## What I Learned
- How to use tkinter to build an interactive game window (Tk, Canvas, Label).
- How to represent the snake as:
  - A list of coordinates (snake.coordinates) for logic.
  - A list of canvas shape ids (snake.squares) for drawing.
- How grid-based movement works:
  - Head position changes by ±SPACE_SIZE in x or y each step.
  - New head is added at the front, tail is removed when the snake does not eat.
- How growing works:
  - Always add a new head segment.
  - Only delete the tail segment if the snake did not eat food.
  - This difference in behavior creates growth.
- How to place food correctly:
  - Use integer grid indices with GAME_WIDTH // SPACE_SIZE and GAME_HEIGHT // SPACE_SIZE.
  - Multiply by SPACE_SIZE to get pixel positions.
- How to manage global game state:
  - score, direction, snake, food as shared state across functions.
  - Update the score label dynamically with label.config(...).
- How to detect collisions:
  - Wall collision by checking if head x/y is outside [0, GAME_WIDTH) or [0, GAME_HEIGHT).
  - Self-collision by comparing the head coordinate to all other body coordinates.
- How to use window.after(SPEED, ...) to create a game loop without blocking the UI.
- How to bind and unbind keys:
  - Arrow keys to change direction.
  - Space key to restart after game over.
  - window.unbind('<space>') to avoid multiple restarts stacking up.
- How to display centered text on a canvas using canvas.winfo_width() / 2 and canvas.winfo_height() / 2.

## How to Run

From the root of this project:

```bash
python snake.game.py
