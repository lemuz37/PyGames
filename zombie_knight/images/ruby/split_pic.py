from PIL import Image

def split_image_into_tiles(image_path, tile_size=24):
    # Load the image
    image = Image.open(image_path)
    image_width, image_height = image.size

    # Calculate the number of horizontal and vertical tiles
    horizontal_tiles = image_width // tile_size
    vertical_tiles = image_height // tile_size

    # Loop over the image and save each tile
    counter = 0
    for i in range(vertical_tiles):
        for j in range(horizontal_tiles):
            counter += 1
            # Define the box to crop the image
            left = j * tile_size
            upper = i * tile_size
            right = left + tile_size
            lower = upper + tile_size
            box = (left, upper, right, lower)

            # Crop the image and save it
            tile = image.crop(box)
            tile.save(f"zombie_knight\images\\ruby\\ruby({counter}).png")

    print("Tiles are saved in the current directory.")

# Usage example
split_image_into_tiles("zombie_knight\images\\ruby\\ruby2.png")
