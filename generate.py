from PIL import Image, ImageDraw

WIDTH = 480
HEIGHT = 400

FPS = 30
FRAMES = 1200

# Small square like the DVD logo
SIZE = 52

# Starting position
x = 45
y = 25

# Movement
vx = 5
vy = 3

# DVD-style colors
COLORS = [
    (235, 35, 35),   # RED
    (35, 90, 235),   # BLUE
    (35, 220, 65),   # GREEN
]

# Change color every N frames
COLOR_DURATION = 180

frames = []

for frame in range(FRAMES):

    # Completely black screen
    img = Image.new("RGB", (WIDTH, HEIGHT), (10, 10, 10))
    draw = ImageDraw.Draw(img)

    # Current color
    color_index = (frame // COLOR_DURATION) % len(COLORS)
    color = COLORS[color_index]

    # Pixel square
    draw.rectangle(
        [x, y, x + SIZE - 1, y + SIZE - 1],
        fill=color
    )

    # Move
    x += vx
    y += vy

    # Left / right edges
    if x <= 0:
        x = 0
        vx = abs(vx)

    elif x + SIZE >= WIDTH:
        x = WIDTH - SIZE
        vx = -abs(vx)

    # Top / bottom edges
    if y <= 0:
        y = 0
        vy = abs(vy)

    elif y + SIZE >= HEIGHT:
        y = HEIGHT - SIZE
        vy = -abs(vy)

    frames.append(img)

# Save GIF
frames[0].save(
    "pixel-cube.gif",
    save_all=True,
    append_images=frames[1:],
    duration=1000 // FPS,
    loop=0,
    optimize=True
)

print("Created pixel-cube.gif")
