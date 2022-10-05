from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QWidget,
    QLabel,
    QComboBox,
    QPushButton,
    QMessageBox)

from PySide6.QtCore import QSize, Qt

from yt_downl import yt_downl

from os import path


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arnaud's YT Downloader")

        self.setMinimumSize(QSize(700, 300))

        self.layout = QVBoxLayout()

        # label for youtube url box
        self.url_label = QLabel("YouTube URL:")
        self.layout.addWidget(self.url_label)

        # text box to enter the url of the youtube video
        self.url_box = QLineEdit(
            "https://www.youtube.com/watch?v=SVcsDDABEkM&ab_channel=Vox")
        self.url_box.setPlaceholderText("URL of youtube video...")
        self.url_box.textChanged.connect(self.is_downloadable)
        self.layout.addWidget(self.url_box)

        # label for the file name box
        self.filename_label = QLabel("File Name:")
        self.layout.addWidget(self.filename_label)

        # text box to enter the name of the exported file
        self.filename_box = QLineEdit("untitled_video")
        self.filename_box.setPlaceholderText("Name of your file...")
        self.filename_box.textChanged.connect(self.is_downloadable)
        self.layout.addWidget(self.filename_box)

        # label for the export path box
        self.path_label = QLabel("Export Path:")
        self.layout.addWidget(self.path_label)

        # text box to enter the name of the export path
        self.path_box = QLineEdit(path.normpath(path.expanduser("~/Desktop")))
        self.path_box.setPlaceholderText("Path for export...")
        self.path_box.textChanged.connect(self.is_downloadable)
        self.layout.addWidget(self.path_box)

        # label for the file type combo box
        self.filetype_label = QLabel("File Type:")
        self.layout.addWidget(self.filetype_label)

        # combo box to choose either audio or video
        self.filetype_box = QComboBox()
        self.filetype_box.addItem("Video")
        self.filetype_box.addItem("Audio")
        self.layout.addWidget(self.filetype_box)

        # button to start the downlaod
        self.downl_button = QPushButton("Downl")
        self.downl_button.clicked.connect(self.downlbutton_pressed)
        self.layout.addWidget(self.downl_button)

        # label with current status of downloading video
        self.status_label = QLabel()
        self.layout.addWidget(self.status_label)

        # attaching the widgets to the window
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setMenuWidget(self.widget)

        self.cancel_downl = False

    # method is called anytime the url_box, filename_box and path_box are edited
    def is_downloadable(self):
        # checks the following:
        # 1. the url box is non-empty
        # 2. the path box is non-empty and contains a valid path
        # 3. the filename box is non-empty
        if self.url_box.text() and path.exists(self.path_box.text()) and self.filename_box.text():
            # enalbles user to press button if all conditions are met
            self.downl_button.setEnabled(True)
        else:
            self.downl_button.setEnabled(False)

    def downlbutton_pressed(self):
        self.status_label.setText(None)
        # initializing the download object
        to_downl = yt_downl(self.url_box.text(),
                            export_path=self.path_box.text(), file_type=self.filetype_box.currentText().lower(), file_name=self.filename_box.text())

        if path.exists(str(to_downl.export_path+"/"+to_downl.file_name)):
            overwrite_pop = QMessageBox()
            overwrite_pop.setWindowTitle("Overwrite?")
            overwrite_pop.setText(
                "A file already exists at this path, do you want to overwrite it?")
            overwrite_pop.setIcon(QMessageBox.Warning)
            overwrite_pop.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            overwrite_pop.setDefaultButton(QMessageBox.No)
            overwrite_pop.buttonClicked.connect(self.overwrite_pop)
            overwrite_pop.exec()

        # will check if url is valid, if not it will no export
        if not to_downl.url_valid:
            self.status_label.setText("Invalid YouTube URL, please try again.")
            return

        if self.cancel_downl:
            self.status_label.setText(
                "Filename already exists, pick another one.")
            self.cancel_downl = False
            return

        # else downloading the video
        self.status_label.setText("Exporting the video...")
        to_downl.downl()
        self.status_label.setText(
            "Video exported at : " + to_downl.export_path+"/"+to_downl.file_name)

    def overwrite_pop(self, i):
        if (i.text()) == "&No":
            self.cancel_downl = True


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
