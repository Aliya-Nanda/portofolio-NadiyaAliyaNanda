from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
html_path = root / "outputs" / "nadiya-aliya-nanda-portfolio.html"
image_path = root / "outputs" / "nadiya-engineering-visual.png"
html = html_path.read_text(encoding="utf-8")

checks = {
    "html_exists": html_path.exists(),
    "image_exists": image_path.exists(),
    "title_ok": "<title>Nadiya Aliya Nanda" in html,
    "linkedin_ok": "https://www.linkedin.com/in/nadiyaaliyananda" in html,
    "instagram_ok": "https://www.instagram.com/nadiy.aaaaaaaa/" in html,
    "youtube_ok": "https://www.youtube.com/@nadiyaaliyananda" in html,
    "image_reference_ok": 'src="nadiya-engineering-visual.png"' in html,
}

print("html_bytes", html_path.stat().st_size)
print("image_bytes", image_path.stat().st_size if image_path.exists() else 0)
for key, value in checks.items():
    print(key, value)
print("sections", ",".join(re.findall(r'<section id="([^"]+)"', html)))
print("href_count", html.count('href="'))
