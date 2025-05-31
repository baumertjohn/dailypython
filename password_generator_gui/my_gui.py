import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
)
from PyQt5.QtCore import Qt  # Import Qt for alignment
from PyQt5.QtGui import QFont, QColor, QPalette  # For styling


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("My Styled PyQt5 GUI")
        self.setGeometry(100, 100, 500, 300)  # (x, y, width, height)

        # Style the window background
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor("#E0FFFF"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(15)

        # Label
        self.static_text_label = QLabel("Enter your name:")
        font = QFont("Arial", 14)
        self.static_text_label.setFont(font)
        self.static_text_label.setStyleSheet("color: #333333;")
        main_layout.addWidget(
            self.static_text_label, alignment=Qt.AlignHCenter
        )  # Add label to layout

        # Input Box
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Type your name here...")
        self.name_input.setFixedSize(300, 35)
        self.name_input.setStyleSheet(
            "QLineEdit {"
            "   border: 2px solid #007BFF;"  # Blue border
            "   border-radius: 8px;"  # Rounded corners
            "   padding: 5px;"  # Inner padding
            "   background-color: white;"
            "   color: #333333;"
            "   font-size: 14px;"
            "}"
            "QLineEdit:focus {"  # Style when the input field is focused
            "   border: 2px solid #0056b3;"
            "}"
        )
        input_layout = QHBoxLayout()
        input_layout.addStretch(1)
        input_layout.addWidget(self.name_input)
        input_layout.addStretch(1)
        main_layout.addLayout(input_layout)

        # Button
        self.process_button = QPushButton("Process Text")
        self.process_button.setFixedSize(180, 40)
        self.process_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #28a745;"  # Green background
            "   color: white;"  # White text
            "   border: none;"
            "   border-radius: 10px;"  # More rounded corners
            "   font-size: 16px;"
            "   font-weight: bold;"
            "}"
            "QPushButton:hover {"  # Style when mouse hovers over the button
            "   background-color: #218838;"  # Slightly darker green on hover
            "}"
            "QPushButton:pressed {"  # Style when button is pressed
            "   background-color: #1e7e34;"  # Even darker green on press
            "}"
        )
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.process_button)
        button_layout.addStretch(1)
        main_layout.addLayout(button_layout)

        # Connect the button "clicked" signal to "process_text" slot
        self.process_button.clicked.connect(self.process_text)

        main_layout.addStretch(1)  # This pushes all content towards the top
        self.setLayout(main_layout)

    def process_text(self):
        # Slot function
        input_text = self.name_input.text()
        print(f"Processed text: {input_text}")


def main():
    # Create an application object
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()  # Show the window
    sys.exit(app.exec_())  # Start the event application's event loop


if __name__ == "__main__":
    main()
