from PIL import Image
import math


def grid_image(imgList, config):
    # TODO: 1 image grid handling
    images = [Image.open(config.SB_LOGO_PATH_PREFIX + img) for img in imgList]
    num_images = len(images)
    widths, heights = zip(*(i.size for i in images))
    total_width = int(max(widths) * 2)
    max_height = max(heights) * int(math.ceil(num_images / 2))
    combined_image = Image.new('RGBA', (total_width, max_height), (0, 0, 0, 0))

    W, H = config.VIDEO_SIZE
    x_offset = 0
    y_offset = 0

    if num_images % 2 == 0:
        for index, im in enumerate(images):
            if index % 2 == 0:
                combined_image.paste(im, (x_offset, y_offset))
                x_offset += im.size[0]
            else:
                combined_image.paste(im, (x_offset, y_offset))
                x_offset = 0
                y_offset += im.size[1]
    else:
        for index in range(len(images) - 1):
            im = images[index]
            if index % 2 == 0:
                combined_image.paste(im, (x_offset, y_offset))
                x_offset += im.size[0]
            else:
                combined_image.paste(im, (x_offset, y_offset))
                x_offset = 0
                y_offset += im.size[1]
            last_image = images[len(images) - 1]
            combined_image.paste(last_image, (int(x_offset + images[0].size[0] / 2), y_offset))

    num_images_pow = pow(2, len(imgList))
    x_pos = W / config.grid[config.frame_map['gridPosition']] - config.GRID_ICON_SIZE
    y_pos = int(H / num_images_pow)
    height = config.GRID_ICON_SIZE * int(math.ceil(len(imgList) / 2))
    return combined_image, x_pos, y_pos, height
