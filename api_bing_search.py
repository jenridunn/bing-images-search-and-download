import requests
import json
import urllib.parse
from tqdm import tqdm
import pandas as pd
from datetime import date
import os


class BingImagesSearchAndSave:

    def __init__(self, bing_api_key, save_path_folder, folder_name, search_term, image_count, image_min_width, image_min_height):
        self.bing_api_key = bing_api_key
        self.save_path_folder = save_path_folder
        self.search_term = search_term
        self.image_count = image_count
        self.image_min_width = image_min_width
        self.image_min_height = image_min_height
        self.folder_name = folder_name

    # Helper Method
    def request_images(self):
        res = requests.get(f"https://api.bing.microsoft.com/v7.0/images/search?count={self.image_count}&&minHeight={self.image_min_height}&&minWidth={self.image_min_width}&&q={urllib.parse.quote_plus(self.search_term)}",
                           headers={'Ocp-Apim-Subscription-Key': self.bing_api_key})
        return json.loads(res.content)

    # Helper Method
    def extract_images_urls(self):
        response = self.request_images()
        image_items = response["value"]
        images = []
        thumbnails = []
        for image_item in image_items:
            images.append(image_item["contentUrl"])
            thumbnails.append(image_item["thumbnailUrl"])

        # Saving images urls to a csv file, in case something goes wrong when saving images to your computer
        link_df = pd.DataFrame({'ORIGINALS': images, 'THUMBNAILS': thumbnails})
        link_df.to_csv(
            f'link_images_{self.folder_name}_{date.today().strftime("%b-%d-%Y")}.csv')
        print('Images links saved')

        return list(enumerate(images)), list(enumerate(thumbnails))

    # Helper Method
    def createDirectories(self):
        originals_dir = os.path.join(
            self.save_path_folder, f'{self.folder_name}\\originals')
        thumbnails_dir = os.path.join(
            self.save_path_folder, f'{self.folder_name}\\thumbnails')

        if not os.path.exists(originals_dir):
            os.makedirs(originals_dir)

        if not os.path.exists(thumbnails_dir):
            os.makedirs(thumbnails_dir)

        return (originals_dir, thumbnails_dir)

    # Helper Method
    def save_image(self, mode, images, save_dir):
        if(mode == "image"):
            for i in tqdm(range(0, len(images))):
                try:
                    response = requests.get(images[i][1])
                    file = open(
                        f"{save_dir}\\{str(images[i][0])}.jpg", "wb")
                    file.write(response.content)
                    file.close()
                except:
                    print(f'Couldn\'t get image from url {images[i][1]}')

        elif (mode == "thumbnail"):
            for i in tqdm(range(0, len(images))):
                response = requests.get(images[i][1])
                file = open(
                    f"{save_dir}\\{str(images[i][0])}.jpg", "wb")
                file.write(response.content)
                file.close()

    # Executor Method for saving images
    def save_images(self):
        images, thumbnails = self.extract_images_urls()
        originals_dir, thumbnails_dir = self.createDirectories()

        # print('Saving Images...')
        # self.save_image("image", images, originals_dir)

        print('Saving Thumbnails...')
        self.save_image("thumbnail", thumbnails, thumbnails_dir)

        print('All images saved!')

    # Executor Method for saving images from a csv File
    def save_images_from_csv(self, csvFile):
        originals_dir, thumbnails_dir = self.createDirectories()

        df = pd.read_csv(csvFile)
        thumbnails = list(enumerate(df['THUMBNAILS'].tolist()))
        images = list(enumerate(df['ORIGINALS'].tolist()))

        # print('Saving Images...')
        # self.save_image("image", images, originals_dir)

        print('Saving Thumbnails...')
        self.save_image("thumbnail", thumbnails, thumbnails_dir)
