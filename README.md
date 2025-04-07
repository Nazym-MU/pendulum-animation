# Pendulum Simulation with Forces and Acceleration – Physics Assignment

This project is a physics visualization created using the [Manim](https://www.manim.community/) (Mathematical Animation Engine) library. It simulates a **simple pendulum** and visually demonstrates the key forces and acceleration components acting on the pendulum bob at various points in time.

[Watch the created pendulum animation](https://drive.google.com/file/d/1ThceTfiL9IyrvGR738hbB4kxWBJNjYBP/view?usp=sharing)


## Features

- Visualizations of:
  - Gravitational force (`mg`, red)
  - Tension (`T`, blue)
  - Total acceleration (`a`, purple)
- Angle arc showing the current angular displacement `θ`
- Real-time updates of motion based on physics equations:
  - `α = -g / L * sin(θ)`
  - Angular velocity and angle update over time
- Clean, educational layout with labeled vectors and axes

## Physics Concepts Covered

- Newton’s Second Law in polar coordinates
- Tangential vs. centripetal acceleration
- Forces acting on a rotating mass
- Visual understanding of angular motion

## Tech Stack

- [Python 3.12](https://www.python.org/)
- [Manim](https://docs.manim.community/) (Community Edition)

## How to Run

1. Make sure you have [Manim CE](https://docs.manim.community/en/stable/installation.html) installed.
2. Save the script as `pendulum_scene.py`.
3. Run the scene using the command:

   ```bash
   manim -pql pendulum_scene.py PendulumScene
   ```

   Use `-pqh` for higher quality, or `-pqm` for medium quality.

## File Structure

```
pendulum_scene.py     # Main animation script
README.md             # Project documentation
```

## Author

This simulation was created by Nazym Zhiyengaliyeva as part of a Physics course assignment to enhance conceptual understanding of rotational motion through animation.