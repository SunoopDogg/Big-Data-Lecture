from YouTube_API_build import getMyYoutubeBuild


def youtubeSearch(keyword):
    youtube = getMyYoutubeBuild()

    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=keyword.max_results
    ).execute()
