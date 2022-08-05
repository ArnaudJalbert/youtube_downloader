from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QWidget,
    QLabel,
    QComboBox,
    QPushButton)

from PySide6.QtCore import QSize


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arnaud's YT Downloader")

        self.setMinimumSize(QSize(500, 500))

        layout = QVBoxLayout()

        url_label = QLabel("YouTube URL:")
        layout.addWidget(url_label)

        url_box = QLineEdit()
        url_box.setPlaceholderText("URL of youtube video...")
        layout.addWidget(url_box)

        path_label = QLabel("Export Path:")
        layout.addWidget(path_label)

        path_box = QLineEdit()
        path_box.setPlaceholderText("Path for export...")
        layout.addWidget(path_box)

        filetype_label = QLabel("File Type:")
        layout.addWidget(filetype_label)

        filetype_box = QComboBox()
        filetype_box.addItem("Video")
        filetype_box.addItem("Audio")
        layout.addWidget(filetype_box)

        downl_button = QPushButton("Downl")
        layout.addWidget(downl_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setMenuWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
