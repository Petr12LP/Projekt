import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from fractals.generate import mandelbrot, julia
from typing import Tuple

# --- Globální proměnné pro rozsah ---
x_min, x_max = -2.0, 2.0
y_min, y_max = -2.0, 2.0

def draw_fractal() -> None:
    """
    Vykreslí aktuální fraktál podle nastavených parametrů a rozsahu.
    """
    ax.clear()
    max_iter = int(slider_iter.val)
    cx = slider_cx.val
    cy = slider_cy.val
    cmap = radio.value_selected
    if radio_fractal.value_selected == 'Mandelbrot':
        data = mandelbrot(x_min, x_max, y_min, y_max, 600, 600, max_iter)
    else:
        c = complex(cx, cy)
        data = julia(x_min, x_max, y_min, y_max, 600, 600, max_iter, c)
    ax.imshow(data, extent=(x_min, x_max, y_min, y_max), cmap=cmap)
    fig.canvas.draw_idle()

def update(val) -> None:
    """
    Callback pro widgety - aktualizuje vykreslení fraktálu.
    """
    draw_fractal()

def on_scroll(event) -> None:
    """
    Callback pro zoom kolečkem myši.
    """
    global x_min, x_max, y_min, y_max
    zoom_factor = 0.8 if event.button == 'up' else 1.25
    xdata, ydata = event.xdata, event.ydata
    if xdata is None or ydata is None:
        return
    x_range = x_max - x_min
    y_range = y_max - y_min

    x_min = xdata - (xdata - x_min) * zoom_factor
    x_max = xdata + (x_max - xdata) * zoom_factor
    y_min = ydata - (ydata - y_min) * zoom_factor
    y_max = ydata + (y_max - ydata) * zoom_factor

    draw_fractal()

is_dragging = False
drag_start: Tuple[int, int] = (0, 0)
start_xlim: Tuple[float, float] = (0.0, 0.0)
start_ylim: Tuple[float, float] = (0.0, 0.0)

def on_press(event) -> None:
    global is_dragging, drag_start, start_xlim, start_ylim
    if event.inaxes != ax:
        return
    is_dragging = True
    drag_start = (event.x, event.y)
    start_xlim = (x_min, x_max)
    start_ylim = (y_min, y_max)

def on_release(event) -> None:
    global is_dragging
    is_dragging = False

def on_motion(event) -> None:
    global x_min, x_max, y_min, y_max
    if not is_dragging or event.inaxes != ax:
        return
    dx = event.x - drag_start[0]
    dy = event.y - drag_start[1]

    width = start_xlim[1] - start_xlim[0]
    height = start_ylim[1] - start_ylim[0]

    dx_data = -dx * width / ax.bbox.width
    dy_data = dy * height / ax.bbox.height

    x_min = start_xlim[0] + dx_data
    x_max = start_xlim[1] + dx_data
    y_min = start_ylim[0] + dy_data
    y_max = start_ylim[1] + dy_data

    draw_fractal()

# --- Inicializace GUI ---
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.35)

initial_iter = 100
initial_cx = -0.7
initial_cy = 0.27015

ax_iter = plt.axes([0.25, 0.25, 0.65, 0.03])
slider_iter = Slider(ax_iter, 'Iterace', 50, 500, valinit=initial_iter, valstep=10)

ax_cx = plt.axes([0.25, 0.20, 0.65, 0.03])
slider_cx = Slider(ax_cx, 'Re(c)', -1.5, 1.5, valinit=initial_cx)

ax_cy = plt.axes([0.25, 0.15, 0.65, 0.03])
slider_cy = Slider(ax_cy, 'Im(c)', -1.5, 1.5, valinit=initial_cy)

ax_radio = plt.axes([0.025, 0.5, 0.15, 0.15])
radio = RadioButtons(ax_radio, ('inferno', 'plasma', 'viridis'))

ax_fractal = plt.axes([0.025, 0.3, 0.15, 0.15])
radio_fractal = RadioButtons(ax_fractal, ('Mandelbrot', 'Julia'))

slider_iter.on_changed(update)
slider_cx.on_changed(update)
slider_cy.on_changed(update)
radio.on_clicked(update)
radio_fractal.on_clicked(update)

fig.canvas.mpl_connect('scroll_event', on_scroll)
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)

draw_fractal()

plt.show()
