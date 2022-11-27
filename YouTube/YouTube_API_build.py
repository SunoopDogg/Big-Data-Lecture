from googleapiclient.discovery import build

api_key = 'AIzaSyB6HO77rx7xC324k4twsOG8twj1spHNVFE'


def getYoutubeBuild(api_key):
    return build('youtube', 'v3', developerKey=api_key)


def getMyYoutubeBuild():
    return getYoutubeBuild(api_key)
