import sys
import hashlib
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit


class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("MD5 Hash Generator")

        # Create a central widget and set it as the main widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a QVBoxLayout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a QLabel for the text input
        input_label = QLabel("Input Text:")
        layout.addWidget(input_label)

        # Create a QLineEdit for text input
        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        # Create a QLabel for the MD5 hash output
        output_label = QLabel("MD5 Hash:")
        layout.addWidget(output_label)

        # Create a QLineEdit for the MD5 hash output (read-only)
        self.md5_output = QLineEdit(self)
        self.md5_output.setReadOnly(True)
        layout.addWidget(self.md5_output)

        # Connect the text changed signal of the input field to the hash generation slot
        self.text_input.textChanged.connect(self.generate_md5_hash)

    def generate_md5_hash(self):
        text = self.text_input.text()
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        self.md5_output.setText(md5_hash)


def main():
    app = QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
