import math
import streamlit as st
import matplotlib.pyplot as plt


def forward_kinematics(link1: float, link2: float, theta1_deg: float, theta2_deg: float):
    theta1 = math.radians(theta1_deg)
    theta2 = math.radians(theta2_deg)

    # First joint position
    x1 = link1 * math.cos(theta1)
    y1 = link1 * math.sin(theta1)

    # End-effector position
    x2 = x1 + link2 * math.cos(theta1 + theta2)
    y2 = y1 + link2 * math.sin(theta1 + theta2)

    return x1, y1, x2, y2


def plot_robot_arm(link1: float, link2: float, x1: float, y1: float, x2: float, y2: float):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Draw links
    ax.plot([0, x1], [0, y1], marker="o", linewidth=3, label="Link 1")
    ax.plot([x1, x2], [y1, y2], marker="o", linewidth=3, label="Link 2")

    # End effector
    ax.scatter([x2], [y2], s=120, label="End Effector")

    # Set plot boundaries
    max_range = link1 + link2 + 2
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_aspect("equal", adjustable="box")

    ax.grid(True)
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.set_title("2-Link Robot Arm Visualization")
    ax.legend()

    return fig


def main():
    st.set_page_config(page_title="Robot Arm Kinematics Calculator", layout="centered")

    st.title("Robot Arm Kinematics Calculator")
    st.write(
        "An interactive Python app that calculates and visualizes the "
        "end-effector position of a 2-link robot arm using forward kinematics."
    )

    st.subheader("Input Values")

    link1 = st.number_input("Length of Link 1", min_value=0.1, value=10.0, step=0.1)
    link2 = st.number_input("Length of Link 2", min_value=0.1, value=8.0, step=0.1)

    theta1_deg = st.slider("Theta 1 (degrees)", min_value=-180, max_value=180, value=30)
    theta2_deg = st.slider("Theta 2 (degrees)", min_value=-180, max_value=180, value=45)

    x1, y1, x2, y2 = forward_kinematics(link1, link2, theta1_deg, theta2_deg)

    st.subheader("Results")
    st.write(f"**Joint 1 Position:** ({x1:.2f}, {y1:.2f})")
    st.write(f"**End Effector Position:** ({x2:.2f}, {y2:.2f})")

    fig = plot_robot_arm(link1, link2, x1, y1, x2, y2)
    st.pyplot(fig)

    st.subheader("How It Works")
    st.markdown(
        """
This app uses **forward kinematics** to find the final position of a robot arm.

For a 2-link planar arm:

- **Link 1** rotates by angle **theta1**
- **Link 2** rotates by angle **theta2** relative to Link 1
- The final **(x, y)** position is the end effector location

### Equations

- `x = L1*cos(theta1) + L2*cos(theta1 + theta2)`
- `y = L1*sin(theta1) + L2*sin(theta1 + theta2)`

This is one of the core math concepts used in robotics, motion planning, and arm positioning.
"""
    )


if __name__ == "__main__":
    main()
