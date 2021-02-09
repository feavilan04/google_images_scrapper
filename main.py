import argparse

from image_downloader import ImageDownloader

def main():
    '''
    Creates the parser to verify that arguments are well formatted
    '''
    parser = argparse.ArgumentParser(description='Download requested images from google images based on a search query.')
    parser.add_argument('search', nargs='+', help='The search query to be fetched')
    parser.add_argument('limit', type=int, nargs='+', help='The maximum quantity of results to be downloaded')

    # Get the arguments passed into command
    arguments=parser.parse_args()

    # Assigns the argumets passedto variables
    search=arguments.search[0]
    limit=arguments.limit[0]

    
    downloader=ImageDownloader()
    downloader.search_images(search, limit)


# call to the main function handler
main()
