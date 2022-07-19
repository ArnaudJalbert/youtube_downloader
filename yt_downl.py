from pytube import YouTube


class yt_downl(YouTube):

    def __init__(self, url, export_path, name, file_type):
        super().__init__(url)

        self.export_path = export_path

        self.name = name

        self.file_type = file_type
