import os
from PIL import Image

img_path = r"work done\NAVER CLOUD\EBS\1 (ENG).png"

print(f"Processing {img_path}")
try:
    img = Image.open(img_path)
    w, h = img.size
    print(f"Image size: {w}x{h}")
    
    # Watermark is at ~ (2636, 1413). 
    # Let's crop a patch from immediately to the left of the watermark area.
    # We want to cover from (w - 250) to w, and (h - 250) to h.
    # Let's grab a patch from (w - 500) to (w - 250), same height.
    cover_w = 250
    cover_h = 250
    
    patch_box = (w - cover_w * 2, h - cover_h, w - cover_w, h)
    patch = img.crop(patch_box)
    
    # Paste the patch over the right edge
    img.paste(patch, (w - cover_w, h - cover_h))
    
    img.save(img_path)
    print("Watermark patched and image saved.")
except Exception as e:
    print(f"Error: {e}")
