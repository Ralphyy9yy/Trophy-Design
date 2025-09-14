# Digital Trophy – Intramurals 2025

## CONCEPT AND THEME
This project presents a Digital Trophy design for Intramurals 2025 – Overall Champion.  
The trophy captures the spirit of victory, teamwork, and celebration, aligning with the intramurals theme of Digital Trophy.

A golden cup symbolizes victory, with a unifying sphere representing success.  
The CCJ Knights and BISU logos highlight school identity, while the confetti background adds to the celebration.

---

## ASSETS
Assets are stored in the `src/assets/` folder:

- `bisu.png` – BISU Logo  
- `ccj.png` – CCJ Knights Logo  
- `confetti.png` – Celebration confetti background  

---

## FUNCTIONS/LIBRARIES USED
I used **Python, Pillow**, and **path**.

- **Canvas** – Created using `Image.new()`  
- **Path** – For file/image handling  
- **Shapes** – Trophy cup, base, sphere, and panels drawn with `ellipse()`, `polygon()`, and `rectangle()`  
- **Text** – Added with `draw.text()` for titles and labels  
- **Logos & Confetti** – Imported with `Image.open()` and blended using `.paste()`  
- **Enhancement** – Final brightness polished using `ImageEnhance.Brightness()`  

---

## DESIGN CONCEPT
- Gold and orange gradients create a metallic, celebratory finish, a unifying sphere crowns the cup, CCJ Knights and BISU logo reinforce school identity, and a confetti backdrop amplifies the festive, victorious mood.
