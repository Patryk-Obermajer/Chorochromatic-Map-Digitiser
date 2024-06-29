


# Here's the config file where we set the main params to ensure consistency across all the notebooks in the repo
original_image_path = r'.\data\01-source-map\winter_rain_potential_hi-res-CLIPPED.png'

# The below img_width, img_height, tile_size are for both the training dataset as well as the tiles of the original map to be classed. 
# I think this is a good thing and will ensure consistency but I can see how this can be limiting further down the line if we started playing around a bit more
img_width = img_height = tile_size = 6

TF_MODEL_FILE_PATH = 'CNN-WRAP-model.tflite'
class_names = ['Class-0-water', 'Class-1', 'Class-2', 'Class-3', 'Class-4', 'Class-5']
log_file_path = './Recreate-WRAP-log.txt'
reconstructed_image_path = './Reconstructed_WRAP_map.png'