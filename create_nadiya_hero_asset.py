from pathlib import Path
from math import cos, sin, pi
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "nadiya-engineering-visual.png"
SCALE = 2
W, H = 1400, 1100


def font(size, bold=False):
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size * SCALE)
    return ImageFont.load_default()


def s(value):
    return int(round(value * SCALE))


def box(draw, xy, outline, fill=None, width=2, radius=14):
    draw.rounded_rectangle(tuple(s(v) for v in xy), radius=s(radius), outline=outline, fill=fill, width=s(width))


def line(draw, points, fill, width=2):
    draw.line([(s(x), s(y)) for x, y in points], fill=fill, width=s(width))


def text(draw, xy, value, fill, size=28, bold=False, anchor=None):
    draw.text((s(xy[0]), s(xy[1])), value, fill=fill, font=font(size, bold), anchor=anchor)


img = Image.new("RGB", (s(W), s(H)), "#080b10")
draw = ImageDraw.Draw(img)

for y in range(0, H, 40):
    shade = "#151b21" if y % 120 else "#202830"
    line(draw, [(0, y), (W, y)], shade, 1)
for x in range(0, W, 40):
    shade = "#151b21" if x % 120 else "#202830"
    line(draw, [(x, 0), (x, H)], shade, 1)

for i in range(18):
    x0 = 70 + i * 72
    line(draw, [(x0, 90), (x0 + 28, 90)], "#2a343d", 2)
    line(draw, [(x0, 1010), (x0 + 28, 1010)], "#2a343d", 2)
for i in range(12):
    y0 = 116 + i * 72
    line(draw, [(82, y0), (82, y0 + 24)], "#2a343d", 2)
    line(draw, [(1318, y0), (1318, y0 + 24)], "#2a343d", 2)

box(draw, (70, 76, 1330, 1024), "#38444d", width=2, radius=18)
box(draw, (110, 116, 1290, 984), "#1b242b", width=1, radius=10)

cx, cy = 700, 515
for r, color, width in [(335, "#1e8f89", 2), (265, "#7b6537", 2), (185, "#334457", 1), (118, "#75404a", 2)]:
    draw.ellipse((s(cx-r), s(cy-r), s(cx+r), s(cy+r)), outline=color, width=s(width))

for deg in range(0, 360, 15):
    r1 = 338 if deg % 45 else 328
    r2 = 352
    a = deg * pi / 180
    line(draw, [(cx + cos(a) * r1, cy + sin(a) * r1), (cx + cos(a) * r2, cy + sin(a) * r2)], "#58656d", 1)

for deg in range(0, 360, 60):
    a = deg * pi / 180
    x = cx + cos(a) * 265
    y = cy + sin(a) * 265
    draw.ellipse((s(x-7), s(y-7), s(x+7), s(y+7)), fill="#3dd6c6")
    line(draw, [(cx, cy), (x, y)], "#1b817d", 1)

text(draw, (700, 444), "NADIYA", "#f8f5ed", 84, True, "mm")
text(draw, (700, 520), "ALIYA NANDA", "#e7b75f", 54, True, "mm")
text(draw, (700, 584), "MECHANICAL ENGINEERING / AI LITERACY", "#99ded8", 24, False, "mm")

left = 170
top = 185
box(draw, (left, top, left + 290, top + 232), "#395b60", fill="#0d1419", width=2, radius=12)
text(draw, (left + 22, top + 24), "STRUCTURAL NOTES", "#3dd6c6", 22, True)
for i, label in enumerate(["AL6005-T5 tripod", "Dual-layer filtration", "COP comparison", "Outdoor stability"]):
    y = top + 70 + i * 36
    draw.rectangle((s(left + 24), s(y - 8), s(left + 36), s(y + 4)), fill="#e7b75f")
    text(draw, (left + 52, y - 18), label, "#b7b3a8", 18)

right = 942
top2 = 176
box(draw, (right, top2, right + 288, top2 + 244), "#60464b", fill="#10151a", width=2, radius=12)
text(draw, (right + 22, top2 + 25), "AI + IMPACT MAP", "#ef6f82", 22, True)
nodes = [(right+80, top2+92, "Gemini"), (right+205, top2+104, "NotebookLM"), (right+139, top2+180, "Ethics")]
for x, y, label in nodes:
    draw.ellipse((s(x-39), s(y-24), s(x+39), s(y+24)), outline="#7aa7ff", width=s(2), fill="#111a23")
    text(draw, (x, y-7), label, "#d8d2c4", 15, True, "mm")
line(draw, [(nodes[0][0]+36, nodes[0][1]), (nodes[1][0]-36, nodes[1][1])], "#5d6f88", 2)
line(draw, [(nodes[0][0]+12, nodes[0][1]+24), (nodes[2][0]-8, nodes[2][1]-23)], "#5d6f88", 2)
line(draw, [(nodes[1][0]-14, nodes[1][1]+24), (nodes[2][0]+13, nodes[2][1]-23)], "#5d6f88", 2)

rocket = [(254, 782), (318, 644), (386, 782), (330, 756), (318, 866), (306, 756)]
draw.polygon([(s(x), s(y)) for x, y in rocket], outline="#e7b75f", fill="#141b20")
line(draw, [(318, 644), (318, 866)], "#e7b75f", 2)
draw.ellipse((s(291), s(716), s(345), s(770)), outline="#3dd6c6", width=s(3), fill="#0d1419")
line(draw, [(275, 802), (215, 874), (294, 841)], "#8d7040", 2)
line(draw, [(362, 802), (421, 874), (342, 841)], "#8d7040", 2)
text(draw, (318, 918), "ROCKETRY ITB", "#d8d2c4", 20, True, "mm")

robot_x, robot_y = 1010, 690
box(draw, (robot_x, robot_y, robot_x + 220, robot_y + 174), "#476076", fill="#101820", width=2, radius=10)
draw.rectangle((s(robot_x+48), s(robot_y+44), s(robot_x+172), s(robot_y+116)), outline="#7aa7ff", width=s(2), fill="#0b1117")
draw.ellipse((s(robot_x+73), s(robot_y+68), s(robot_x+89), s(robot_y+84)), fill="#3dd6c6")
draw.ellipse((s(robot_x+131), s(robot_y+68), s(robot_x+147), s(robot_y+84)), fill="#3dd6c6")
line(draw, [(robot_x+88, robot_y+107), (robot_x+132, robot_y+107)], "#e7b75f", 3)
line(draw, [(robot_x+110, robot_y), (robot_x+110, robot_y-40)], "#7aa7ff", 2)
draw.ellipse((s(robot_x+100), s(robot_y-54), s(robot_x+120), s(robot_y-34)), fill="#ef6f82")
line(draw, [(robot_x-38, robot_y+80), (robot_x, robot_y+80)], "#7aa7ff", 4)
line(draw, [(robot_x+220, robot_y+80), (robot_x+260, robot_y+80)], "#7aa7ff", 4)
text(draw, (robot_x+110, robot_y+218), "ROBOTICS + SYSTEMS", "#d8d2c4", 20, True, "mm")

for x, y, label in [(180, 956, "PUBLIC SPEAKING"), (528, 912, "CIRCULAR ECONOMY"), (820, 918, "RESEARCH"), (1070, 956, "LEADERSHIP")]:
    box(draw, (x-110, y-22, x+110, y+22), "#39444d", fill="#0d1419", width=1, radius=8)
    text(draw, (x, y-2), label, "#b7b3a8", 16, True, "mm")

overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
for x, y, r, color in [
    (360, 248, 180, (61, 214, 198, 34)),
    (1004, 322, 160, (239, 111, 130, 26)),
    (704, 838, 230, (231, 183, 95, 20)),
]:
    od.ellipse((s(x-r), s(y-r), s(x+r), s(y+r)), fill=color)
overlay = overlay.filter(ImageFilter.GaussianBlur(s(34)))
img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
img = img.resize((W, H), Image.Resampling.LANCZOS)
img.save(OUT, quality=94)
print(OUT)
