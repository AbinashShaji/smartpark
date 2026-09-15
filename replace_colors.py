import glob
import os

files = glob.glob('templates/public/*.html') + ['templates/base_public.html', 'templates/base.html', 'templates/base_dashboard.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace background navy-tilted grays with true black or neutral
    content = content.replace('bg-gray-900', 'bg-black')
    content = content.replace('bg-gray-800', 'bg-neutral-900')
    content = content.replace('border-gray-800', 'border-neutral-900')
    content = content.replace('border-gray-900', 'border-black')
    content = content.replace('text-gray-900', 'text-black')
    
    # User requested to also add tiny royal blue accents. 
    # We will do that manually via multi_replace later for specific things like "PARK" and "01".

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Replaced gray-900/800 with black/neutral-900 across templates.")
