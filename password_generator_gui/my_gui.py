import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


def main():
    # Create an application object
    app = QApplication(sys.argv)

    # Create a basic window (QWidget)
    window = QWidget()
    window.setWindowTitle("My First PyQt5 GUI")
    window.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

    # Create and position a QLabel widget
    static_text_label = QLabel("Enter your name:", window)
    static_text_label.move(50, 50)  # (x, y) coords relative to the windows top-left

    # Create and position a QLineEdit widget
    name_input = QLineEdit(window)
    name_input.move(180, 50)
    name_input.setFixedWidth(150)

    # Create and position QPushButton
    process_button = QPushButton("Process Test", window)
    process_button.move(150, 100)

    # 3. Show the window
    window.show()

    # 4. Start the application's event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
