from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QWidget,
    QLabel,
    QComboBox,
    QPushButton)

from PySide6.QtCore import QSize, Qt

from yt_downl import yt_downl


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.user_url = None
        self.user_path = None
        self.user_filetype = None

        self.setWindowTitle("Arnaud's YT Downloader")

        self.setMinimumSize(QSize(700, 300))

        self.layout = QVBoxLayout()

        self.url_label = QLabel("YouTube URL:")
        self.layout.addWidget(self.url_label)

        self.url_box = QLineEdit()
        self.url_box.setPlaceholderText("URL of youtube video...")
        self.url_box.textChanged.connect(self.url_edited)
        self.layout.addWidget(self.url_box)

        self.filename_label = QLabel("File Name:")
        self.layout.addWidget(self.filename_label)

        self.filename_box = QLineEdit()
        self.filename_box.setPlaceholderText("Name of your file...")
        self.layout.addWidget(self.filename_box)

        self.path_label = QLabel("Export Path:")
        self.layout.addWidget(self.path_label)

        self.path_box = QLineEdit()
        self.path_box.setPlaceholderText("Path for export...")

        self.layout.addWidget(self.path_box)

        self.filetype_label = QLabel("File Type:")
        self.layout.addWidget(self.filetype_label)

        self.filetype_box = QComboBox()
        self.filetype_box.addItem("Video")
        self.filetype_box.addItem("Audio")
        self.filetype_box.currentIndexChanged.connect(self.filetype_edited)
        self.layout.addWidget(self.filetype_box)

        self.downl_button = QPushButton("Downl")
        self.downl_button.clicked.connect(self.downlbutton_pressed)
        self.layout.addWidget(self.downl_button)

        self.status_label = QLabel()
        self.layout.addWidget(self.status_label)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setMenuWidget(self.widget)

    def url_edited(self, url):
        self.user_url = url

    def path_edited(self, path):
        self.user_path = path

    def filetype_edited(self):
        self.user_filetype = self.filetype_box.currentText().lower()
        print(self.user_filetype)

    def downlbutton_pressed(self):
        self.status_label.setText("Exporting the video...")
        to_downl = yt_downl(self.url_box.text(),
                            export_path=self.path_box.text(), file_type=self.filetype_box.currentText().lower(), file_name=self.filename_box.text())
        to_downl.downl()
        self.status_label.setText(
            "Video exported at : " + to_downl.export_path+"/"+to_downl.file_name)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
