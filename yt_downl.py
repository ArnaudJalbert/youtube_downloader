from pytube import YouTube
from os import path

deft_export_path = path.normpath(path.expanduser("~/Desktop"))

deft_file_type = 'video'

deft_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'


class yt_downl(YouTube):

    def __init__(self, url, export_path=deft_export_path, file_name=None, file_type=deft_file_type):

        super().__init__(url)

        self.set_export_path(export_path)

        self.set_file_type(file_type)

        self.set_name(file_name)

    def set_export_path(self, export_path):
        if path.isdir(export_path):
            self.export_path = export_path
        else:
            print("Not a valid path! Will set the desktop as the export path.")
            self.export_path = path.normpath(path.expanduser("~/Desktop"))

    def set_name(self, file_name):
        if isinstance(file_name, str):
            if self.file_type == 'video':
                self.file_name = file_name+".mp4"
            else:
                self.file_name = file_name+".mp3"
        else:
            print("Not a string! Default will be applied.")
            self.file_name = self.title

    def set_file_type(self, file_type):
        if file_type == "audio" or file_type == "video":
            self.file_type = file_type
        else:
            print("Not a string! Default will be applied.")
            self.file_type = 'video'

    def to_string(self):
        return "Name : " + self.file_name + ", file type : " + self.file_type + " and export path : " + self.export_path + "."

    def downl(self):
        if self.file_type == 'audio':
            to_downl = self.streams.get_audio_only()
        else:
            to_downl = self.streams.get_highest_resolution()

        to_downl.download(output_path=self.export_path,
                          filename=self.file_name)
