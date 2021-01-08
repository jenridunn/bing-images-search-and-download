# Search and Download Images from Bing

## Introduction

> Use this python class to search and download images (images from the original source and thumbnails) to your computer using Bing's API. If you are a deep learning practitioner you will find this class very useful for obtaining data sets to train neuronal networks for computer vision algorithms.

## Code Samples

<strong>NOTE:</strong> By default the methods (save_images and save_images_from_csv) doesn't save the images from the original source. If you want this functionality uncomment the following line in the executors methods:
```
#self.save_image("image", images, originals_dir)
``` 
<br>
<b>Class Parameters that need to be explained:</b>
<br>
<br>
<i>image_count</i>:
The number of images to return in the response. The actual number delivered may be less than requested. The default is 35. The maximum value is 150.
<br>
<i>image_min_width</i>: Filter images that have a width that is greater than or equal to the specified width. Specify the width in pixels.
<br>
<i>image_min_height</i>: 	Filter images that have a height that is greater than or equal to the specified height. Specify the height in pixels.
<br><br>

For saving images only:
``` 
from api_bing_search import BingImagesSearchAndSave

# Class Arguments
bing_api_key = "here_goes_your_api_key"
save_path_folder = r"E:\Learning\FastAiv2\Course\CHAPTER 2\AC7 Aircraft Trainer"
search_term ="Mirage 2000-5"
folder_name ="Mirage2000"
image_count = 150 
image_min_width = "256"
image_min_height = "256"

instance = BingImagesSearchAndSave(bing_api_key, save_path_folder, folder_name, search_term, image_count, image_min_width, image_min_height)
instance.save_images()
```

Every time you run the method save_images() a csv file is generated in case something goes wrong while downloading the images to your computer. If you want to resume the saving process of your images follow this example:

```
from api_bing_search import BingImagesSearchAndSave

bing_api_key = "956ab122ab094934af4f0fe18fcc6db9"
save_path_folder = r"E:\Learning\FastAiv2\Course\CHAPTER 2\AC7 Aircraft Trainer"
search_term ="Mirage 2000-5"
folder_name ="Mirage2000"
image_count = 150
image_min_width = "256"
image_min_height = "256"

instance = BingImagesSearchAndSave(bing_api_key, save_path_folder, folder_name, search_term, image_count, image_min_width, image_min_height)

#input as an argument the name of the csv file generated during the previous execution of the save_images() method
instance.save_images_from_csv('link_images_F22A_Jan-05-2021.csv')
```

## Pre-requisites

<ul><li>Python Version >= 3.7</li><li>Modules installed: requests, tqdm and pandas</li><li>Bing Image Search API key</li></ul>

## Installation

>1. Clone or download this repository and import the class BingImagesSearchAndSave (recommendation: place the class in the same folder where your code will be executed, to avoid any further import issues). <br><br>You might need an api key for using the Bing Image Search API, for this follow the instructions described in this link: https://www.microsoft.com/en-us/bing/apis/bing-image-search-api<br><br> If you want to use the free subscription you will have access to fetch up to 1000 images per month.
