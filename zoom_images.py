from PIL import Image, ImageDraw

def process_image(in_path, out_path, scale_factor=0.75):
    try:
        img = Image.open(in_path).convert('RGB')
        w, h = img.size
        # Sample edge colors (we'll use the top-left corner color as the background fill)
        bg_color = img.getpixel((0, 0))
        
        # New dimensions for the inner scaled image
        new_w = int(w * scale_factor)
        new_h = int(h * scale_factor)
        
        # Resize inner image
        img_resized = img.resize((new_w, new_h), Image.LANCZOS)
        
        # Create new image with original size, filled with bg_color
        new_img = Image.new('RGB', (w, h), bg_color)
        
        new_img.paste(img_resized, ((w - new_w) // 2, (h - new_h) // 2))
        
        new_img.save(out_path)
        print(f'Saved scaled image to {out_path}')
    except Exception as e:
        print(f'Error processing {in_path}: {e}')

process_image(r'C:\Users\able2\.gemini\antigravity\brain\4394418d-90a0-477c-a43a-ad9616202655\award_trophy_orange_dark_1773211521556.png', r'C:\Users\able2\.gemini\antigravity\scratch\portfolio\award_korea_zoomed.png')
process_image(r'C:\Users\able2\.gemini\antigravity\scratch\portfolio\award_japan_orb_zoomed_out.png', r'C:\Users\able2\.gemini\antigravity\scratch\portfolio\award_japan_zoomed.png')
