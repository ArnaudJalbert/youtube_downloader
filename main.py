from yt_downl import yt_downl

url = 'https://www.youtube.com/watch?v=g9xvkAnfh0w&ab_channel=iJustine'
export_path = '/Users/arnaudjalbert/Projects/youtube_downloader/dump'
name = 'test'
file_type = 'video'

test = yt_downl(url, export_path, name, file_type)

print(test.get_author())
