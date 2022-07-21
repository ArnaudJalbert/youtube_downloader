from yt_downl import yt_downl

url = 'https://www.youtube.com/watch?v=g9xvkAnfh0w&ab_channel=iJustine'
export_path = '/Users/arnaudjalbert/Projects/youtube_downloader/dump'
file_name = "Arno"
file_type = 'video'

test = yt_downl(url, export_path=export_path,
                file_name=file_name, file_type=file_type)

print(test.to_string())

test.downl_video()
