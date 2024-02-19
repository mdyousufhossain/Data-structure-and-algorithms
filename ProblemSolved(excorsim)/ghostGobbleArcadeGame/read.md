## Pac-Man Functions Explained

These functions define the core rules of the classic arcade game Pac-Man:

### 1. eat_ghost

This function determines if Pac-Man can eat a ghost:

* **Parameters:**
  * `power_pellet_active`: Boolean, True if Pac-Man has an active power pellet.
  * `touching_ghost`: Boolean, True if Pac-Man is touching a ghost.
* **Return value:**
  * Boolean, True if Pac-Man can eat the ghost (requires both power pellet and touch).

### 2. score

This function checks if Pac-Man has scored:

* **Parameters:**
  * `touching_power_pellet`: Boolean, True if Pac-Man is touching a power pellet.
  * `touching_dot`: Boolean, True if Pac-Man is touching a dot.
* **Return value:**
  * Boolean, True if Pac-Man scored (by touching either a power pellet or a dot).

### 3. lose

This function checks if Pac-Man has lost the game:

* **Parameters:**
  * `power_pellet_active`: Boolean, True if Pac-Man has an active power pellet.
  * `touching_ghost`: Boolean, True if Pac-Man is touching a ghost.
* **Return value:**
  * Boolean, True if Pac-Man has lost (touching a ghost without power pellet active).

**Note:** The implementation of this function contains an infinite loop which is incorrect. If Pac-Man is touching a ghost and has a power pellet, the function should return `False` immediately, not enter an infinite loop.

### 4. win

This function checks if Pac-Man has won the game:

* **Parameters:**
  * `has_eaten_all_dots`: Boolean, True if Pac-Man has eaten all the dots.
  * `power_pellet_active`: Boolean, True if Pac-Man has an active power pellet.
  * `touching_ghost`: Boolean, True if Pac-Man is touching a ghost.
* **Return value:**
  * Boolean, True if Pac-Man has won (all dots eaten and not touching a ghost).

**Note:** This function first calls the `lose` function, even though they don't have direct logical connection. It would be more efficient to directly check the game state conditions within the `win` function.
