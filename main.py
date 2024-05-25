from PIL import Image

def overlay_images(image1_path, image2_path, output_path):
    # Load the images
    image1 = Image.open(image1_path).convert("RGBA")
    image2 = Image.open(image2_path).convert("RGBA")

    # Ensure both images are 250 x 250
    image1 = image1.resize((250, 250))
    image2 = image2.resize((250, 250))

    # Paste image1 onto image2 at the top-left corner
    image2.paste(image1, (0, 0), image1)

    # Save the merged image
    image2.save(output_path, format="PNG")


# Example usage
image1_path = '1.png'
image2_path = '2.png'
output_path = '3.png'
position = (50, 50)  # Top-left corner where the second image will be placed on the first image

overlay_images(image1_path, image2_path, output_path)