from picture_generation import GenImage

def main():
    print("Create new image...")
    for index in range(10):
        new_image = GenImage(30, 30)
        wallpaper = new_image.generates()
        wallpaper.show()

main()