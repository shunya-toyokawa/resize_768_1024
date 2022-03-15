from PIL import Image
im = Image.open("input.png")


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))




im_new = crop_center(im, 768, 1024)
im_new.save('output.png', quality=95)
