from PIL import Image
import os

# Folder where your walk frames are saved
folder = "slime_frames"
frames = []

# Load walk frames in order
for i in range(1, 5):
    frame_path = os.path.join(folder, f"slime_walk_{i}.png")
    frame = Image.open(frame_path)
    frames.append(frame)

# Save as animated GIF
frames[0].save("slime_walk.gif",
               save_all=True,
               append_images=frames[1:],
               duration=150,  # Time per frame in milliseconds
               loop=0)        # 0 = loop forever

print("GIF saved as slime_walk.gif")