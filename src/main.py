from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance  # type: ignore
from pathlib import Path #for assets path handling

width, height = 1000, 1100
poster = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(poster)

# Colors
gold = "#FFD700"
dark_gold = "#B8860B"
bright_gold = "#FFE55C"
orange = "#FF8C00"
orange_dark = "#FF6347"
white = "#FFFFFF"
shadow = "#000000"
blue = "#1E90FF"

# Fonts size and style
try:
    title_font = ImageFont.truetype("arialbd.ttf", 52)
    sub_font = ImageFont.truetype("arial.ttf", 48)
    small_font = ImageFont.truetype("arialbd.ttf", 28)
except:
    title_font = sub_font = small_font = ImageFont.load_default()

trophy_center_x = width // 2

base_y = height - 180
base_w, base_h = 300, 80

draw.rectangle([trophy_center_x - base_w//2 + 5, base_y + 5,
                trophy_center_x + base_w//2 + 5, base_y + base_h + 5],
               fill=shadow)

for i in range(15):
    color = (205 + i*3, 127 + i*2, 50)
    draw.rectangle([trophy_center_x - base_w//2 + i*2, base_y + i*2,
                    trophy_center_x + base_w//2 - i*2, base_y + base_h - i*2],
                   fill=color)

draw.rectangle([trophy_center_x - base_w//2, base_y,
                trophy_center_x + base_w//2, base_y + base_h],
               outline=white, width=3)

draw.text((trophy_center_x, base_y + 40), "OVERALL CHAMPION",
          font=small_font, fill=shadow, anchor="mm")

cup_top_y = 280
cup_bottom_y = base_y - 5
cup_top_w = 140
cup_bottom_w = 200

cup_points = [
    trophy_center_x - cup_top_w//2, cup_top_y,
    trophy_center_x + cup_top_w//2, cup_top_y,
    trophy_center_x + cup_bottom_w//2, cup_bottom_y,
    trophy_center_x - cup_bottom_w//2, cup_bottom_y
]

shadow_points = [x+8 if i%2==0 else y+8 for i,(x,y) in enumerate(zip(cup_points[::2],cup_points[1::2]))]
draw.polygon(shadow_points, fill=shadow)

for i in range(12):
    ratio = i / 12
    r = 255 - int(ratio*40)
    g = 140 + int(ratio*20)
    b = 0 + int(ratio*50)
    color = (r,g,b)
    shrink = [(trophy_center_x + (x-trophy_center_x)* (1-0.05*ratio),
               y + (cup_bottom_y-y)*0.02*ratio) for x,y in zip(cup_points[::2], cup_points[1::2])]
    flat = [v for xy in shrink for v in xy]
    draw.polygon(flat, fill=color)

draw.polygon(cup_points, outline=white, width=3)

rim = [trophy_center_x-80, cup_top_y-15, trophy_center_x+80, cup_top_y-15,
       trophy_center_x+70, cup_top_y+10, trophy_center_x-70, cup_top_y+10]
draw.polygon(rim, fill=gold, outline=white, width=2)

sphere_r = 50
sphere_y = cup_top_y - 70
for i in range(15):
    ratio = i/15
    r = 184 + int((255-184)*ratio)
    g = 134 + int((229-134)*ratio)
    b = 11 + int((92-11)*ratio)
    draw.ellipse([trophy_center_x-sphere_r+i, sphere_y-sphere_r+i,
                  trophy_center_x+sphere_r-i, sphere_y+sphere_r-i], fill=(r,g,b))

draw.ellipse([trophy_center_x-sphere_r, sphere_y-sphere_r,
              trophy_center_x+sphere_r, sphere_y+sphere_r], outline=white, width=2)

# search common locations for the assets folder
ASSET_CANDIDATES = [
    Path(__file__).resolve().parent / "assets",   # src/assets
    Path(__file__).resolve().parent.parent / "assets", 
    Path.cwd() / "assets"                              
]

def get_asset_path(filename):
    for base in ASSET_CANDIDATES:
        p = base / filename
        if p.exists():
            return p
  

try:
    logo_path = get_asset_path("bisu.png")
    logo = Image.open(logo_path).convert("RGBA")
    logo = ImageOps.fit(logo, (100, 100))
    poster.paste(logo, (trophy_center_x - 50, sphere_y - 45), logo)
except:
    print("Bisu logo not found")
cup_logo_y = (cup_top_y+cup_bottom_y)//2
try:
    logo_path = get_asset_path("ccj.png")
    logo = Image.open(logo_path).convert("RGBA").resize((130,130))
    poster.paste(logo, (trophy_center_x-65, cup_logo_y-65), logo)
except: 
    print("CCJ logo not found")

left_panel = [trophy_center_x-100, cup_bottom_y, trophy_center_x-130, cup_bottom_y-20,
              trophy_center_x-90, cup_top_y-10, trophy_center_x-70, cup_top_y]
draw.polygon(left_panel, fill=gold, outline=white)

right_panel = [trophy_center_x+100, cup_bottom_y, trophy_center_x+130, cup_bottom_y-20,
               trophy_center_x+90, cup_top_y-10, trophy_center_x+70, cup_top_y]
draw.polygon(right_panel, fill=gold, outline=white)

draw.rectangle([trophy_center_x-10, sphere_y+sphere_r,
                trophy_center_x+10, sphere_y+sphere_r+25],
               fill=gold, outline=white)

title = "PAUGNAT PASUNDAYAG 2025"
draw.text((trophy_center_x, 40), title, font=title_font, fill=bright_gold, anchor="ma")
draw.text((trophy_center_x+2, 42), title, font=title_font, anchor="ma")

subtitle = "INTRAMURALS 2025"
draw.text((trophy_center_x, height-60), subtitle, font=title_font, fill=white, anchor="ma")

for (cx,cy) in [(60,60),(width-90,60),(60,height-90),(width-90,height-90)]:
    diamond = [cx+15,cy, cx+30,cy+15, cx+15,cy+30, cx,cy+15]
    draw.polygon(diamond, fill=blue, outline=gold)

for sy in [200,400,600,800]:
    draw.polygon([30,sy,40,sy-10,50,sy,40,sy+10], fill=gold)
    draw.polygon([width-30,sy,width-40,sy-10,width-50,sy,width-40,sy+10], fill=gold)

try:
    confetti_path = get_asset_path("confetti.png")
    confetti = Image.open(confetti_path).convert("RGBA")
    confetti = confetti.resize((width, height))
    poster.paste(confetti, (100, 150), confetti)  
except:
    print("Confetti image not found")


poster = ImageEnhance.Brightness(poster).enhance(1.1) #enhance  image brightness
poster.save("CSELEC3_3B_SuquibRalphGiann_Activity1.png")
print("Image saved")
poster.show()
