from PIL import Image, ImageDraw, ImageFilter

def process_image(in_path, out_path, scale_factor=0.75):
    try:
        img = Image.open(in_path).convert('RGBA')
        w, h = img.size
        # Sample edge colors (use the top-left corner color as the background fill)
        bg_rgb = img.getpixel((0, 0))
        bg_color = (bg_rgb[0], bg_rgb[1], bg_rgb[2], 255)
        
        # New dimensions for the inner scaled image
        new_w = int(w * scale_factor)
        new_h = int(h * scale_factor)
        
        # Resize inner image
        img_resized = img.resize((new_w, new_h), Image.LANCZOS)
        
        # Create an alpha mask to feather the edges
        mask = Image.new('L', (new_w, new_h), 0)
        draw = ImageDraw.Draw(mask)
        # The inner rectangle is white, fading out
        draw.rectangle([60, 60, new_w - 60, new_h - 60], fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(40))
        
        # Apply mask to the resized image
        img_resized.putalpha(mask)
        
        # Create new image with original size, filled with bg_color
        new_img = Image.new('RGBA', (w, h), bg_color)
        
        # Paste the resized image using itself as an alpha mask (since it has the feathered alpha now)
        paste_x = (w - new_w) // 2
        paste_y = (h - new_h) // 2
        new_img.paste(img_resized, (paste_x, paste_y), img_resized)
        
        new_img.convert('RGB').save(out_path)
        print(f'Saved blended scaled image to {out_path}')
    except Exception as e:
        print(f'Error processing {in_path}: {e}')

# Re-process Korea image with edge blending
process_image(r'C:\Users\able2\.gemini\antigravity\brain\4394418d-90a0-477c-a43a-ad9616202655\award_trophy_orange_dark_1773211521556.png', r'C:\Users\able2\.gemini\antigravity\scratch\portfolio\award_korea_zoomed.png')
