import math
import matplotlib.pyplot as plt
import streamlit as st


# ----------------------------
# Page setup
# ----------------------------
st.set_page_config(
    page_title="Robot Arm Kinematics Calculator",
    page_icon="🤖",
    layout="centered",
)


# ----------------------------
# Custom styling
# ----------------------------
st.markdown(
    """
    <style>
        .stApp {
            background-color: #0b0f17;
            color: #e6f1ff;
        }

        h1, h2, h3 {
            color: #00ffcc !important;
        }

        .stMarkdown, .stText, .stWrite, p, li, label {
            color: #e6f1ff !important;
        }

        code {
            color: #00ffcc !important;
            background-color: #111827 !important;
            padding: 0.15rem 0.35rem;
            border-radius: 0.3rem;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------------------
# Default values
# ----------------------------
DEFAULTS = {
    "link1": 10.0,
    "link2": 8.0,
    "theta1": 30,
    "theta2": 45,
}


# ----------------------------
# Initialize session state
# ----------------------------
for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ----------------------------
# Helper functions
# ----------------------------
def reset_defaults():
    """Reset all inputs back to their default values."""
    for key, value in DEFAULTS.items():
        st.session_state[key] = value


def forward_kinematics(link1: float, link2: float, theta1_deg: float, theta2_deg: float):
    """
    Calculate the joint positions and end-effector position
    for a 2-link planar robot arm.
    """
    theta1_rad = math.radians(theta1_deg)
    theta2_rad = math.radians(theta2_deg)

    # Joint 1 position
    x1 = link1 * math.cos(theta1_rad)
    y1 = link1 * math.sin(theta1_rad)

    # End effector position
    x2 = x1 + link2 * math.cos(theta1_rad + theta2_rad)
    y2 = y1 + link2 * math.sin(theta1_rad + theta2_rad)

    return x1, y1, x2, y2


def plot_robot_arm(link1: float, link2: float, x1: float, y1: float, x2: float, y2: float):
    """
    Create a 2D plot of the robot arm.
    """
    fig, ax = plt.subplots(figsize=(7, 7))

    # Plot links
    ax.plot([0, x1], [0, y1], marker="o", linewidth=3, label="Link 1")
    ax.plot([x1, x2], [y1, y2], marker="o", linewidth=3, label="Link 2")

    # Plot end effector
    ax.scatter([x2], [y2], s=120, label="End Effector")

    # Dynamic plot limits
    max_range = max(link1 + link2 + 2, 5)
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_aspect("equal", adjustable="box")

    # Labels and grid
    ax.grid(True)
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.set_title("2-Link Robot Arm Visualization")
    ax.legend()

    return fig


# ----------------------------
# Title / intro
# ----------------------------
st.title("Robot Arm Kinematics Calculator")
st.write(
    "An interactive Python app that calculates and visualizes the end-effector "
    "position of a 2-link robot arm using forward kinematics."
)

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Reset to Default"):
        reset_defaults()
        st.rerun()

with col2:
    st.caption("Built with Python, Streamlit, and Matplotlib")


# ----------------------------
# Inputs
# ----------------------------
st.subheader("Input Values")

link1 = st.number_input(
    "Length of Link 1",
    min_value=0.1,
    step=0.1,
    key="link1",
)

link2 = st.number_input(
    "Length of Link 2",
    min_value=0.1,
    step=0.1,
    key="link2",
)

theta1_deg = st.slider(
    "Theta 1 (degrees)",
    min_value=-180,
    max_value=180,
    key="theta1",
)

theta2_deg = st.slider(
    "Theta 2 (degrees)",
    min_value=-180,
    max_value=180,
    key="theta2",
)


# ----------------------------
# Calculations
# ----------------------------
x1, y1, x2, y2 = forward_kinematics(link1, link2, theta1_deg, theta2_deg)


# ----------------------------
# Results
# ----------------------------
st.subheader("Results")
st.write(f"**Joint 1 Position:** ({x1:.2f}, {y1:.2f})")
st.write(f"**End Effector Position:** ({x2:.2f}, {y2:.2f})")


# ----------------------------
# Visualization
# ----------------------------
fig = plot_robot_arm(link1, link2, x1, y1, x2, y2)
st.pyplot(fig)


# ----------------------------
# Explanation
# ----------------------------
st.subheader("How It Works")
st.write("This app uses forward kinematics to find the final position of a robot arm.")

st.markdown(
    """
- **Link 1** rotates by angle **theta1**
- **Link 2** rotates by angle **theta2** relative to Link 1
- The final **(x, y)** position is the end-effector location
"""
)

st.subheader("Equations")
st.markdown(
    """
- `x = L1*cos(theta1) + L2*cos(theta1 + theta2)`
- `y = L1*sin(theta1) + L2*sin(theta1 + theta2)`
"""
)

st.write(
    "This is one of the core math concepts used in robotics, motion planning, "
    "and arm positioning."
)


# ----------------------------
# Sonny tie-in
# ----------------------------
st.subheader("Real-World Application (Sonny Robot)")
st.write(
    "This same forward kinematics concept can be applied to my humanoid robot "
    "project, Sonny OS, to understand arm and joint positioning."
)

st.markdown(
    """
By converting angles into positions, a humanoid robot can:

- Move its arm more accurately
- Understand where a joint should be in space
- Support coordinated motion and future object interaction
"""
)
