# import requests
# from bs4 import BeautifulSoup

# # The URL of the page containing the TEDx talks in Indonesian
# url = 'https://www.ted.com/tedx/events?language=id'

# # Send a GET request to the page
# response = requests.get(url)

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all the links to the Indonesian TEDx talks
# links = []
# for a in soup.find_all('a', href=True):
#     if '/talks/' in a['href'] and '/lang/id' in a['href']:
#         links.append('https://www.ted.com' + a['href'])

# # Print the links to the Indonesian TEDx talks
# for link in links:
#     print(link)


# import os
# from googleapiclient.discovery import build
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from a .env file

# # Set up the YouTube Data API client
# api_key = os.getenv('YOUTUBE_API_KEY')
# youtube = build('youtube', 'v3', developerKey=api_key)

# # Set the playlist ID
# playlist_id = 'PLsRNoUx8w3rN_K4Y7lysWBQQVayAbf8DP'

# # Get the playlist items
# next_page_token = None
# video_links = []
# while True:
#     playlist_items = youtube.playlistItems().list(
#         part='contentDetails',
#         playlistId=playlist_id,
#         maxResults=50,
#         pageToken=next_page_token
#     ).execute()

#     # Get the video IDs and construct the video links
#     video_ids = [item['contentDetails']['videoId'] for item in playlist_items['items']]
#     for video_id in video_ids:
#         video_links.append(f'https://www.youtube.com/watch?v={video_id}')

#     # Check if there are more items in the playlist
#     next_page_token = playlist_items.get('nextPageToken')
#     if not next_page_token:
#         break

# # Print the video links
# for video_link in video_links:
#     print(video_link)


# import os
# from googleapiclient.discovery import build
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from a .env file

# # Set up the YouTube Data API client
# api_key = os.getenv('YOUTUBE_API_KEY')
# youtube = build('youtube', 'v3', developerKey=api_key)

# # Set the search query for TedEx videos in Indonesian
# search_query = 'TedEx Bahasa Indonesia'

# # Set the parameters for the search request
# search_params = {
#     'q': search_query,
#     'part': 'id',
#     'type': 'video',
#     'videoDefinition': 'high',
#     'regionCode': 'ID',
#     'relevanceLanguage': 'id',
#     'videoCaption': 'closedCaption',
#     'maxResults': 50
# }

# # Execute the search request and get the video IDs
# search_response = youtube.search().list(**search_params).execute()
# video_ids = [item['id']['videoId'] for item in search_response['items']]

# # Construct the video links
# video_links = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids]

# # Print the video links
# for video_link in video_links:
#     print(video_link)

# # Save the video links to a text file
# with open('tedex_indonesia_links.txt', 'w') as file:
#     for video_link in video_links:
#         file.write(video_link + '\n')




import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

# Set up the YouTube Data API client
api_key = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

# Set the search query to "TedEx Indonesia"
search_query = "TedEx Indonesia"

# Search for the videos
next_page_token = None
video_links = []
while True:
    search_request = youtube.search().list(
        q=search_query,
        type='video',
        part='id',
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    # Get the video IDs and construct the video links
    video_ids = [item['id']['videoId'] for item in search_request['items']]
    for video_id in video_ids:
        video_links.append(f'https://www.youtube.com/watch?v={video_id}')

    # Check if there are more videos in the search results
    next_page_token = search_request.get('nextPageToken')
    if not next_page_token:
        break

# Print the video links
for video_link in video_links:
    print(video_link)


# Save the video links to a text file
with open('tedex_indonesia_links2.txt', 'w') as file:
    for video_link in video_links:
        file.write(video_link + '\n')