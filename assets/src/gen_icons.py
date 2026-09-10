from PIL import Image, ImageDraw
import math, os

S = 4
SZ = 96
OUT = os.path.join(os.path.dirname(__file__), "..", "icons")
os.makedirs(OUT, exist_ok=True)

def canvas():
    img = Image.new("RGBA", (SZ*S, SZ*S), (0,0,0,0))
    return img, ImageDraw.Draw(img)

def save(img, name):
    img = img.resize((SZ, SZ), Image.LANCZOS)
    img.save(f"{OUT}/{name}.webp", "WEBP", quality=82, method=6)
    print(name, os.path.getsize(f"{OUT}/{name}.webp"))

def sc(v): return v*S

def ellipse(d, box, fill, outline=None, width=0):
    d.ellipse([sc(box[0]),sc(box[1]),sc(box[2]),sc(box[3])], fill=fill,
              outline=outline, width=int(sc(width)) if width else 1)

def poly(d, pts, fill, outline=None, width=0):
    p = [(sc(x),sc(y)) for x,y in pts]
    d.polygon(p, fill=fill)
    if outline and width:
        d.line(p+[p[0]], fill=outline, width=int(sc(width)), joint="curve")

def rrect(d, box, r, fill, outline=None, width=0):
    d.rounded_rectangle([sc(box[0]),sc(box[1]),sc(box[2]),sc(box[3])], radius=sc(r),
                        fill=fill, outline=outline, width=int(sc(width)) if width else 1)

def star(d, cx, cy, r, fill, rot=-90):
    pts=[]
    for i in range(10):
        ang=math.radians(rot+i*36)
        rr=r if i%2==0 else r*0.45
        pts.append((cx+rr*math.cos(ang), cy+rr*math.sin(ang)))
    poly(d, pts, fill)

# ---------- coin (chunky orange rim, gold face, embossed star w/ coral shadow) ----------
img = Image.new("RGBA", (SZ*S, SZ*S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
px = SZ * S

def vgrad(size, top, bottom):
    g = Image.new("RGBA", (size, size))
    gd = ImageDraw.Draw(g)
    tr, tg, tb = top; br, bg, bb = bottom
    for y in range(size):
        t = y / size
        gd.line([(0, y), (size, y)], fill=(int(tr+(br-tr)*t), int(tg+(bg-tg)*t), int(tb+(bb-tb)*t), 255))
    return g

def circle_mask(size, box):
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse(box, fill=255)
    return m

def star_pts(cx, cy, r, rot=-90):
    pts = []
    for i in range(10):
        ang = math.radians(rot + i*36)
        rr = r if i % 2 == 0 else r * 0.48
        pts.append((sc(cx + rr*math.cos(ang)), sc(cy + rr*math.sin(ang))))
    return pts

ellipse(d, (6, 10, 90, 94), "#B86800")
img.paste(vgrad(px, (255,205,95), (235,135,5)), (0,0), circle_mask(px, (sc(6), sc(6), sc(90), sc(90))))
img.paste(vgrad(px, (255,236,120), (255,178,40)), (0,0), circle_mask(px, (sc(15), sc(14), sc(81), sc(80))))
d = ImageDraw.Draw(img)
d.ellipse([sc(15), sc(14), sc(81), sc(80)], outline="#E08E00", width=int(sc(2)))
d.arc([sc(10), sc(8), sc(86), sc(84)], 150, 300, fill=(255,240,200,220), width=int(sc(3)))
d.polygon(star_pts(50, 51.5, 21), fill="#F2664B")
star_mask = Image.new("L", (px, px), 0)
ImageDraw.Draw(star_mask).polygon(star_pts(48, 48, 21), fill=255)
img.paste(vgrad(px, (255,249,219), (255,201,60)), (0,0), star_mask)
d = ImageDraw.Draw(img)
d.line(star_pts(48, 48, 21) + [star_pts(48, 48, 21)[0]], fill="#FFF3C4", width=int(sc(1.5)), joint="curve")
save(img, "coin")

# ---------- gem ----------
img, d = canvas()
poly(d, [(30,14),(66,14),(88,40),(48,88),(8,40)], "#8E3CD9")
poly(d, [(32,18),(64,18),(82,40),(48,80),(14,40)], "#C476F5")
poly(d, [(32,18),(64,18),(56,40),(40,40)], "#F0A8FF")
poly(d, [(14,40),(40,40),(48,80)], "#DB96FF")
poly(d, [(40,40),(56,40),(48,80)], "#F6D2FF")
save(img, "gem")

# ---------- bolt ----------
img, d = canvas()
poly(d, [(56,6),(22,52),(42,52),(36,90),(74,42),(52,42)], "#B25A00")
poly(d, [(54,10),(26,50),(46,50),(40,84),(70,42),(50,42)], "#FFF6D8")
poly(d, [(54,10),(26,50),(44,50),(54,30)], "#FFFFFF")
save(img, "bolt")

# ---------- chest ----------
img, d = canvas()
rrect(d, (14,26,82,56), 12, "#8A5A1E")
rrect(d, (12,50,84,86), 8, "#A66A24")
rrect(d, (12,50,84,86), 8, None, outline="#7A4A12", width=3)
rrect(d, (14,26,82,56), 12, None, outline="#7A4A12", width=3)
rrect(d, (42,44,54,66), 4, "#FFC93C", outline="#E08E00", width=2)
d.rectangle([sc(12), sc(50), sc(84), sc(56)], fill="#7A4A12")
save(img, "chest")

# ---------- stars ----------
for name, fill, off in [("star","#FFC93C","#E08E00"), ("star_off","#B9BDC9","#9AA0B0")]:
    img, d = canvas()
    star(d, 48, 52, 34, off)
    star(d, 48, 47, 34, fill)
    save(img, name)

# ---------- lock ----------
img, d = canvas()
d.arc([sc(32),sc(14),sc(64),sc(52)], 180, 360, fill="#8A8F9E", width=int(sc(9)))
rrect(d, (24,36,72,82), 10, "#9AA0B0")
ellipse(d, (42,50,54,62), "#6B7180")
poly(d, [(46,58),(50,58),(53,74),(43,74)], "#6B7180")
save(img, "lock")

# ---------- fish (side view) ----------
def fish(name, body, dark, light, stripes=None, spot=False, spike=False):
    img, d = canvas()
    poly(d, [(66,48),(90,30),(90,66)], dark)
    poly(d, [(66,48),(88,33),(88,63)], body)
    poly(d, [(38,28),(52,12),(58,30)], dark)
    ellipse(d, (10,26,72,72), dark)
    ellipse(d, (12,27,70,69), body)
    ellipse(d, (20,30,52,46), (255,255,255,70))
    if stripes:
        for sx in stripes:
            poly(d, [(sx,28),(sx+7,28),(sx+3,70),(sx-4,70)], light)
    if spot:
        for (px_,py,pr) in [(40,40,5),(56,52,4),(30,56,4)]:
            ellipse(d, (px_-pr,py-pr,px_+pr,py+pr), light)
    if spike:
        for a in range(0,360,30):
            ang=math.radians(a)
            x2,y2=42+33*math.cos(ang),48+31*math.sin(ang)
            xa,ya=42+24*math.cos(ang+0.18),48+22*math.sin(ang+0.18)
            xb,yb=42+24*math.cos(ang-0.18),48+22*math.sin(ang-0.18)
            poly(d, [(xa,ya),(x2,y2),(xb,yb)], dark)
    ellipse(d, (22,36,36,50), "white")
    ellipse(d, (26,40,34,48), "#2B2B3B")
    save(img, name)

fish("fish_yellow", "#FFDA55", "#F0A810", "#FFF6C8", stripes=[34,48])
fish("fish_blue",   "#5FC8FF", "#2589D8", "#DCF3FF", spot=True)
fish("fish_pink",   "#FFA5D4", "#E065A8", "#FFE0EE", stripes=[40])
fish("puffer",      "#FFC04D", "#D87A10", "#9A651E", spot=True, spike=True)

# ---------- octopus ----------
img, d = canvas()
for i,(x0,x1) in enumerate([(16,30),(32,44),(46,58),(60,72)]):
    rrect(d, (x0,56,x1,82-abs(i-1.5)*4), 5, "#E2637E")
ellipse(d, (18,12,74,64), "#C94F6E")
ellipse(d, (20,13,72,60), "#FF7B9C")
ellipse(d, (30,32,42,44), "white"); ellipse(d, (33,35,40,42), "#2B2B3B")
ellipse(d, (50,32,62,44), "white"); ellipse(d, (53,35,60,42), "#2B2B3B")
save(img, "octopus")

# ---------- crab ----------
img, d = canvas()
for lx in (20,30,60,70):
    d.line([sc(lx),sc(62),sc(lx-6 if lx<48 else lx+6),sc(78)], fill="#D94F2E", width=int(sc(5)))
ellipse(d, (16,34,80,70), "#D94F2E")
ellipse(d, (18,35,78,66), "#FF6B4A")
ellipse(d, (6,22,26,42), "#D94F2E"); ellipse(d, (8,24,24,40), "#FF6B4A")
ellipse(d, (70,22,90,42), "#D94F2E"); ellipse(d, (72,24,88,40), "#FF6B4A")
ellipse(d, (32,42,42,52), "white"); ellipse(d, (35,45,40,50), "#2B2B3B")
ellipse(d, (54,42,64,52), "white"); ellipse(d, (57,45,62,50), "#2B2B3B")
save(img, "crab")

# ---------- turtle ----------
img, d = canvas()
ellipse(d, (64,38,86,58), "#7CC24A")
ellipse(d, (74,44,80,50), "#2B2B3B")
for (fx,fy) in [(20,60),(58,60),(24,22),(54,22)]:
    ellipse(d, (fx,fy,fx+18,fy+14), "#7CC24A")
ellipse(d, (16,20,76,72), "#3E8E2F")
ellipse(d, (20,23,72,66), "#6BCB5A")
poly(d, [(46,30),(60,44),(46,58),(32,44)], "#4FAE3E")
save(img, "turtle")

# ---------- shark ----------
img, d = canvas()
poly(d, [(60,44),(88,24),(86,64)], "#5B7F9E")
poly(d, [(36,26),(50,8),(56,30)], "#5B7F9E")
ellipse(d, (8,26,72,66), "#5B7F9E")
ellipse(d, (10,27,70,62), "#8FB6D4")
ellipse(d, (16,48,58,62), "#EAF6FF")
ellipse(d, (20,34,32,46), "white"); ellipse(d, (23,37,30,44), "#2B2B3B")
save(img, "shark")

# ---------- seahorse ----------
img, d = canvas()
ellipse(d, (30,16,66,50), "#C9771E")
ellipse(d, (32,17,64,46), "#F2A93B")
poly(d, [(60,30),(82,36),(60,42)], "#C9771E")
poly(d, [(28,22),(14,30),(28,38)], "#C9771E")
d.arc([sc(26),sc(40),sc(70),sc(88)], 90, 330, fill="#F2A93B", width=int(sc(13)))
ellipse(d, (46,26,54,34), "#2B2B3B")
save(img, "seahorse")

# ---------- heart ----------
img, d = canvas()
ellipse(d, (14,16,50,52), "#B02020"); ellipse(d, (46,16,82,52), "#B02020")
poly(d, [(12,38),(84,38),(48,86)], "#B02020")
ellipse(d, (17,15,51,51), "#E23A3A"); ellipse(d, (45,15,79,51), "#E23A3A")
poly(d, [(15,36),(81,36),(48,82)], "#E23A3A")
ellipse(d, (22,18,46,42), "#FF7B7B")
save(img, "heart")

# ---------- grow (fish + chunky up arrow) ----------
img, d = canvas()
poly(d, [(48,6),(74,36),(59,36),(59,50),(37,50),(37,36),(22,36)], "#37901D")
poly(d, [(48,10),(70,35),(56,35),(56,47),(40,47),(40,35),(26,35)], "#8FE05C")
poly(d, [(62,72),(84,58),(84,86)], "#E08E00")
ellipse(d, (16,56,68,90), "#E08E00")
ellipse(d, (18,57,66,87), "#FFD23F")
ellipse(d, (26,62,38,74), "white")
ellipse(d, (29,65,36,72), "#2B2B3B")
save(img, "grow")

# ---------- swarm (big fish + 2 babies) ----------
img, d = canvas()
def mini_fish(d, cx, cy, r, body, dark):
    poly(d, [(cx+r*1.1, cy),(cx+r*1.9, cy-r*.7),(cx+r*1.9, cy+r*.7)], dark)
    ellipse(d, (cx-r, cy-r*.75, cx+r, cy+r*.75), dark)
    ellipse(d, (cx-r*.9, cy-r*.65, cx+r*.9, cy+r*.65), body)
    ex = cx - r*.45
    ellipse(d, (ex-r*.24, cy-r*.32, ex+r*.24, cy+r*.16), "white")
    ellipse(d, (ex-r*.11, cy-r*.22, ex+r*.11, cy), "#2B2B3B")
mini_fish(d, 36, 56, 24, "#FFD23F", "#E08E00")
mini_fish(d, 70, 26, 13, "#4FB7FF", "#1B76B0")
mini_fish(d, 74, 72, 13, "#FF8FC7", "#C93B82")
save(img, "swarm")

# ---------- armor shield (metal, rivets, gold star) ----------
img, d = canvas()
poly(d, [(20,14),(76,14),(76,44),(48,86),(20,44)], "#5B6470")
poly(d, [(24,18),(72,18),(72,43),(48,79),(24,43)], "#9AA8BC")
poly(d, [(28,21),(68,21),(68,41),(48,71),(28,41)], "#C7D2E0")
poly(d, [(28,21),(48,21),(48,71),(28,41)], "#DCE6F2")
for (rx,ry) in [(29,26),(67,26),(48,31)]:
    ellipse(d, (rx-3,ry-3,rx+3,ry+3), "#5B6470")
star(d, 48, 46, 11, "#E08E00")
star(d, 48, 44, 11, "#FFC93C")
save(img, "armor")

# ---------- build items ----------
img, d = canvas()
rrect(d, (16,30,80,66), 14, "#8A5A1E")
rrect(d, (18,32,78,62), 12, "#B07A35")
ellipse(d, (62,30,84,66), "#8A5A1E")
ellipse(d, (65,33,81,63), "#D8A860")
ellipse(d, (69,39,77,57), "#B07A35")
save(img, "log")

img, d = canvas()
rrect(d, (24,12,32,86), 4, "#8A5A1E")
poly(d, [(32,14),(80,30),(32,50)], "#E23A3A")
poly(d, [(32,16),(74,30),(32,46)], "#FF7B7B")
save(img, "flag")

img, d = canvas()
rrect(d, (22,14,74,82), 16, "#8A5A1E")
rrect(d, (25,16,71,80), 14, "#B07A35")
d.rectangle([sc(23),sc(30),sc(73),sc(38)], fill="#6B7280")
d.rectangle([sc(23),sc(58),sc(73),sc(66)], fill="#6B7280")
save(img, "barrel")

# ---------- hand (tap pointer guide) ----------
img, d = canvas()
d.ellipse([sc(34),sc(76),sc(62),sc(96)], outline=(255,255,255,160), width=int(sc(3)))
rrect(d, (30,4,66,26), 8, "#D96A1E")
rrect(d, (31,4,65,23), 8, "#FF8A3D")
rrect(d, (41,46,57,84), 7, "#B9BDC9")
rrect(d, (42,46,56,82), 7, "#FFFFFF")
rrect(d, (26,18,70,56), 12, "#B9BDC9")
rrect(d, (27,18,69,54), 12, "#FFFFFF")
ellipse(d, (16,30,36,48), "#B9BDC9")
ellipse(d, (17,30,35,46), "#FFFFFF")
save(img, "hand")

# ---------- shop fish (6 types) ----------
def shop_fish(name, body, dark, horns=False, halo=False, sparkle=False):
    img, d = canvas()
    if halo:
        d.ellipse([sc(30),sc(2),sc(66),sc(16)], outline="#F0A420", width=int(sc(5)))
        d.ellipse([sc(30),sc(0),sc(66),sc(13)], outline="#FFE28A", width=int(sc(4)))
    poly(d, [(66,52),(90,34),(90,70)], dark)
    poly(d, [(66,52),(88,37),(88,67)], body)
    poly(d, [(38,32),(52,16),(58,34)], dark)
    ellipse(d, (10,30,72,76), dark)
    ellipse(d, (12,31,70,73), body)
    ellipse(d, (20,34,52,50), (255,255,255,70))
    if horns:
        poly(d, [(22,34),(16,14),(32,26)], "#8A1020")
        poly(d, [(44,28),(44,8),(56,22)], "#8A1020")
    if sparkle:
        for (px_,py_) in [(30,42),(52,58),(40,66)]:
            d.line([sc(px_-4),sc(py_),sc(px_+4),sc(py_)], fill="white", width=int(sc(2)))
            d.line([sc(px_),sc(py_-4),sc(px_),sc(py_+4)], fill="white", width=int(sc(2)))
    ellipse(d, (22,40,36,54), "white")
    ellipse(d, (26,44,34,52), "#2B2B3B")
    save(img, name)

shop_fish("fshop_lucky",   "#FF9E45", "#D86A20")
shop_fish("fshop_bubble",  "#FFA5D4", "#E065A8")
shop_fish("fshop_toxic",   "#9FF06A", "#4CB030")
shop_fish("fshop_diamond", "#C178FF", "#9440E0", sparkle=True)
shop_fish("fshop_devil",   "#FF4A45", "#B01828", horns=True)
shop_fish("fshop_god",     "#FFD94D", "#F0A810", halo=True)

# ---------- grey fish silhouette ----------
img, d = canvas()
poly(d, [(66,48),(90,30),(90,66)], "#9AA0B0")
ellipse(d, (10,26,72,72), "#9AA0B0")
save(img, "fish_locked")

print("done")
