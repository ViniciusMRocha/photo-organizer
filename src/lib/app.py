# import PIL
# import PIL
import os
import pprint
import shutil
import glob

from PIL import Image


# for photo in photo_list:

def save_rename(photo_path):
    with Image.open(photo_path) as im:

        # TODO: Use Regex to find the extension
        # extension = photo_path.find()

        # Get picture metadata
        exif_data_PIL = im._getexif()
        # Get date of picture
        timestamp = exif_data_PIL[306].replace(':', '-').replace(' ', '_')
        # year = timestamp[:4]
        # month = timestamp[5:7]
        # day = timestamp[8:10]
        # hour = timestamp[11:13]
        # minutes = timestamp[14:16]
        # seconds = timestamp[17:19]

        # TODO: Check if file does not have a timestamp on it and save on a folder without timestamp

        year = timestamp[:4]
        try:
            directory_year = '../out/{}'.format(year)
            is_directory = os.path.isfile(directory_year)
            # Check for year folder
            if not is_directory:
                os.mkdir(directory_year)
        except:
            pass

        month = timestamp[5:7]
        try:
            directory_month = '../out/{}/{}'.format(year, month)
            is_directory = os.path.isfile(directory_month)
            # Check for year folder
            if not is_directory:
                os.mkdir(directory_month)
        except:
            pass

        # Move and rename the file
        shutil.move(
            photo_path, '{}/{}.jpeg'.format(directory_month, timestamp))


photo_list = glob.glob('../data/*')
# pprint.pprint(photo_list)

for photo in photo_list:
    # save_rename(photo)
    with Image.open(photo) as im:
        # Get picture metadata
        exif_data_PIL = im._getexif()
        pprint.pprint(exif_data_PIL)
