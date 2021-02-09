from google_images_download import google_images_download  #google scrapper package
import certifi

print(certifi.where())

class ImageDownloader(object):
    def __init__(self):
        self.response = google_images_download.googleimagesdownload()
        
    def search_images(self, search_query, limit):
        arguments = {"keywords":search_query,"limit":limit,"print_urls":True}   
        paths = self.response.download(arguments)   
        print(paths) 
        

