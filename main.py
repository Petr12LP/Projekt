import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from generate import mandelbrot, julia


def update(val):
    ax.clear()
    max_iter = int(slider_iter.val)
    cx = slider_cx.val
    cy = slider_cy.val
    cmap = radio.value_selected
    if radio_fractal.value_selected == 'Mandelbrot':
        data = mandelbrot(-2, 2, -2, 2, 600, 600, max_iter)
    else:
        c = complex(cx, cy)
        data = julia(-2, 2, -2, 2, 600, 600, max_iter, c)
    ax.imshow(data, extent=(-2, 2, -2, 2), cmap=cmap)
    fig.canvas.draw_idle()


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.35)

#přednastavene hodnoty
initial_iter = 100
initial_cx = -0.7
initial_cy = 0.27015

# Vkresleni zakladniho malderbrota
image = mandelbrot(-2, 2, -2, 2, 600, 600, initial_iter)
ax.imshow(image, extent=(-2, 2, -2, 2), cmap='inferno')


# Sliders
ax_iter = plt.axes([0.25, 0.25, 0.65, 0.03])
slider_iter = Slider(ax_iter, 'Iterace', 50, 500, valinit=initial_iter, valstep=10)

ax_cx = plt.axes([0.25, 0.20, 0.65, 0.03])
slider_cx = Slider(ax_cx, 'Re(c)', -1.5, 1.5, valinit=initial_cx)

ax_cy = plt.axes([0.25, 0.15, 0.65, 0.03])
slider_cy = Slider(ax_cy, 'Im(c)', -1.5, 1.5, valinit=initial_cy)

# Radio buttons
ax_radio = plt.axes([0.025, 0.5, 0.15, 0.15])
radio = RadioButtons(ax_radio, ('inferno', 'plasma', 'viridis'))

ax_fractal = plt.axes([0.025, 0.3, 0.15, 0.15])
radio_fractal = RadioButtons(ax_fractal, ('Mandelbrot', 'Julia'))

# propojeni slideru a radio buttonu s update funkcí pro aktualizaci grafu
slider_iter.on_changed(update)
slider_cx.on_changed(update)
slider_cy.on_changed(update)
radio.on_clicked(update)
radio_fractal.on_clicked(update)

plt.show()
