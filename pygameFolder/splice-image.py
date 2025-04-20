from PIL import Image
import os

# Load the sprite sheet
sprite_sheet = Image.open("slime_sheet.png")

# Set the number of columns and rows
columns = 4
rows = 2
frame_width = 32
frame_height = 32

# Output directory
output_dir = "slime_frames"
os.makedirs(output_dir, exist_ok=True)

# Split and save each frame
for row in range(rows):
    for col in range(columns):
        left = col * frame_width
        top = row * frame_height
        right = left + frame_width
        bottom = top + frame_height

        frame = sprite_sheet.crop((left, top, right, bottom))

        action = "idle" if row == 0 else "walk"
        filename = f"slime_{action}_{col+1}.png"
        frame.save(os.path.join(output_dir, filename))

print("Done! Slime frames saved to:", output_dir)
