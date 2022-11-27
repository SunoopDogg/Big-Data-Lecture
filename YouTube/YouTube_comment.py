import pandas as pd
from YouTube_API_build import getMyYoutubeBuild


def getVideoComment(id):
    result = list()

    youtube = getMyYoutubeBuild()

    response = youtube.commentThreads().list(
        part='snippet', videoId=id, maxResults=100).execute()

    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            result.append([comment['textDisplay'], comment['authorDisplayName'],
                           comment['publishedAt'], comment['likeCount']])

            if item['snippet']['totalReplyCount'] > 0:
                for reply_item in item['replies']['comments']:
                    reply = reply_item['snippet']
                    result.append([reply['textDisplay'], reply['authorDisplayName'],
                                   reply['publishedAt'], reply['likeCount']])

        if 'nextPageToken' in response:
            response = youtube.commentThreads().list(part='snippet,replies', videoId=id,
                                                     pageToken=response['nextPageToken'], maxResults=100).execute()
        else:
            break

    return result


def commentToCSV(comment, id):
    df = pd.DataFrame(comment, columns=['Comment', 'Author', 'Date', 'Likes'])
    df.to_csv(f'{id}_comments.csv', mode='a', header=False, index=False)


def getCommentCSV(id):
    df = pd.read_csv(f'{id}_comments.csv')
    return df


df = getCommentCSV('03nkQSfSm2A')
