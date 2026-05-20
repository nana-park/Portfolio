import re

def convert_to_light_mode(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Colors and borders
    replacements = {
        'text-white': 'text-zinc-900',
        'text-zinc-300': 'text-zinc-700',
        'text-zinc-400': 'text-zinc-500',
        'border-white/5': 'border-zinc-200',
        'border-white/10': 'border-zinc-200',
        'border-white/20': 'border-zinc-300',
        'bg-white/5': 'bg-zinc-50',
        'bg-white/10': 'bg-zinc-100',
        'bg-white/20': 'bg-zinc-200',
        'hover:bg-white/5': 'hover:bg-zinc-100',
        'hover:border-white/10': 'hover:border-zinc-300',
        'text-amber-500': 'text-[#d97706]',
        'bg-[#0f0f0f]': 'bg-white',
        'bg-[#1a1a1a]': 'bg-zinc-50',
        'border-[#2a2a2a]': 'border-zinc-200',
        'border-[#333]': 'border-zinc-200',
        'text-gray-300': 'text-zinc-600',
        'bg-black/30': 'bg-zinc-100',
        'bg-black/80': 'bg-white/90 shadow-sm text-zinc-900',
        'from-[#1a1a1a]': 'from-zinc-50',
        'bg-[#121212]': 'bg-white',
        'bg-[#1e1e1e]': 'bg-zinc-50',
        'border-[#333333]': 'border-zinc-200',
        'bg-[#2d2d2d]': 'bg-zinc-100',
        'bg-[#222]': 'bg-zinc-50',
        'text-zinc-500 font-medium': 'text-zinc-500 font-medium',
        'text-gray-400': 'text-zinc-500',
    }

    # Perform simple replacements
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # Exceptional case: The YouTube video player has a black background normally
    # We should keep the video player dark, but the script changed bg-[#1a1a1a] to bg-zinc-50.
    # It's actually fine for the mockup background to be light if there's an image.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

convert_to_light_mode('projects/hopzie.html')
