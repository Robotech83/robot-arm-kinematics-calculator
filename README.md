# Robot Arm Kinematics Calculator

A Python app that calculates and visualizes the end-effector position of a 2-link robotic arm using **forward kinematics**.

## Overview

This project demonstrates a basic robotics concept: calculating where the end of a robot arm will be based on link lengths and joint angles.

The app allows users to:

- Enter the length of each robot arm link
- Adjust joint angles interactively
- Calculate the final `(x, y)` end-effector position
- Visualize the arm in a 2D plot

## Features

- Interactive controls for link lengths and joint angles
- Real-time forward kinematics calculations
- 2D robot arm visualization
- Clear explanation of the math behind the app
- Built with Python, Streamlit, and Matplotlib

## Technologies Used

- Python
- Streamlit
- Matplotlib
- Math / Trigonometry
- Robotics Fundamentals

## Forward Kinematics Formula

For a 2-link planar robot arm:

```python
x = L1 * cos(theta1) + L2 * cos(theta1 + theta2)
y = L1 * sin(theta1) + L2 * sin(theta1 + theta2)
