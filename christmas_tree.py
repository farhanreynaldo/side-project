import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from celluloid import Camera


def basic_christmas_tree():
    fig = plt.figure(figsize=(15, 15))
    ax = fig.gca(projection="3d")
    ax.set_facecolor("black")
    ax.get_tightbbox(fig.canvas.get_renderer())
    ax.axis("off")
    ax.view_init(10, 0.2)

    t = np.linspace(0, 8 * np.pi, 100)
    z = t
    x = t * np.cos(t)
    y = t * np.sin(t)

    # red and two shadows
    ax.plot(x, y, -z, color="#ff0000", linestyle="--")
    ax.plot(x * 0.95, y, -z, color="#ff0000", linestyle="--", alpha=0.4)
    ax.plot(x * 0.9, y, -z, color="#ff0000", linestyle="--", alpha=0.2)

    # cyan and two shadows
    ax.plot(-x, -y, -z, color="#00ffcc", linestyle="--")
    ax.plot(-x * 0.95, -y, -z, color="#00ffcc", linestyle="--", alpha=0.4)
    ax.plot(-x * 0.9, -y, -z, color="#00ffcc", linestyle="--", alpha=0.2)


def animated_christmas_tree():
    fig = plt.figure(figsize=(15, 15))
    fig.set_tight_layout({"pad": 0.0})
    ax = fig.gca(projection="3d")
    ax.set_facecolor("black")
    ax.axis("off")
    ax.view_init(10)

    camera = Camera(fig)
    t = np.linspace(0, 8 * np.pi, 200)
    for i in t:
        z = t
        x = t * np.cos(t + i)
        y = t * np.sin(t + i)
        ax.plot(x, y, -z, color="#ff0000", linestyle="--")
        ax.plot(-x, -y, -z, color="#00ffcc", linestyle="--")
        ax.scatter3D(0, 0, 0.5, color="gold", marker="*", s=100)

        lw = 1
        for i in range(10):
            ax.plot(
                x,
                y,
                -z,
                color="#ff0000",
                linestyle="-",
                linewidth=lw + (1.01 * i),
                alpha=0.05,
            )
            ax.plot(
                -x,
                -y,
                -z,
                color="#00ffcc",
                linestyle="-",
                linewidth=lw + (1.01 * i),
                alpha=0.05,
            )
        camera.snap()

    animation = camera.animate(interval=50, repeat_delay=3000, blit=True)
    animation.save("tree-glow.gif", writer="imagemagick")
