import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("My First PyQt5 GUI")
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

        layout = QVBoxLayout()

        # Label
        self.static_text_label = QLabel("Enter your name:")
        layout.addWidget(self.static_text_label)  # Add label to layout

        # Input Box
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Type your name here...")
        layout.addWidget(self.name_input)

        # Button
        self.process_button = QPushButton("Process Text")
        layout.addWidget(self.process_button)

        # Connect the button "clicked" signal to "process_text" slot
        self.process_button.clicked.connect(self.process_text)

        self.setLayout(layout)

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
