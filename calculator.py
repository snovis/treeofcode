#!/usr/bin/env python3
"""
Simple Calculator Application
Currently supports: Addition and Subtraction
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QLabel, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.first_number = None
        self.operation = None
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(100, 100, 400, 500)

        # Main layout
        layout = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFont(QFont('Arial', 24))
        self.display.setMinimumHeight(60)
        layout.addWidget(self.display)

        # Number pad (0-9 and decimal)
        numbers_layout = QVBoxLayout()

        # Rows 7-8-9, 4-5-6, 1-2-3
        for row in [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]:
            row_layout = QHBoxLayout()
            for num in row:
                btn = QPushButton(num)
                btn.setFont(QFont('Arial', 18))
                btn.setMinimumHeight(60)
                btn.clicked.connect(lambda checked, n=num: self.number_clicked(n))
                row_layout.addWidget(btn)
            numbers_layout.addLayout(row_layout)

        # Bottom row: 0 and decimal
        bottom_row = QHBoxLayout()
        btn_0 = QPushButton('0')
        btn_0.setFont(QFont('Arial', 18))
        btn_0.setMinimumHeight(60)
        btn_0.clicked.connect(lambda: self.number_clicked('0'))
        bottom_row.addWidget(btn_0)

        btn_decimal = QPushButton('.')
        btn_decimal.setFont(QFont('Arial', 18))
        btn_decimal.setMinimumHeight(60)
        btn_decimal.clicked.connect(lambda: self.number_clicked('.'))
        bottom_row.addWidget(btn_decimal)

        numbers_layout.addLayout(bottom_row)
        layout.addLayout(numbers_layout)

        # Operations
        operations_layout = QHBoxLayout()

        # Add button (enabled)
        self.btn_add = QPushButton('+')
        self.btn_add.setFont(QFont('Arial', 18, QFont.Bold))
        self.btn_add.setMinimumHeight(60)
        self.btn_add.setStyleSheet("background-color: #4CAF50; color: white;")
        self.btn_add.clicked.connect(lambda: self.operation_clicked('add'))
        operations_layout.addWidget(self.btn_add)

        # Subtract button (enabled)
        self.btn_subtract = QPushButton('-')
        self.btn_subtract.setFont(QFont('Arial', 18, QFont.Bold))
        self.btn_subtract.setMinimumHeight(60)
        self.btn_subtract.setStyleSheet("background-color: #FF9800; color: white;")
        self.btn_subtract.clicked.connect(lambda: self.operation_clicked('subtract'))
        operations_layout.addWidget(self.btn_subtract)

        # Multiply button (disabled - coming soon)
        self.btn_multiply = QPushButton('×')
        self.btn_multiply.setFont(QFont('Arial', 18, QFont.Bold))
        self.btn_multiply.setMinimumHeight(60)
        self.btn_multiply.setEnabled(False)
        self.btn_multiply.setStyleSheet("background-color: #cccccc;")
        operations_layout.addWidget(self.btn_multiply)

        # Divide button (disabled - coming soon)
        self.btn_divide = QPushButton('÷')
        self.btn_divide.setFont(QFont('Arial', 18, QFont.Bold))
        self.btn_divide.setMinimumHeight(60)
        self.btn_divide.setEnabled(False)
        self.btn_divide.setStyleSheet("background-color: #cccccc;")
        operations_layout.addWidget(self.btn_divide)

        layout.addLayout(operations_layout)

        # Control buttons
        control_layout = QHBoxLayout()

        btn_clear = QPushButton('Clear')
        btn_clear.setFont(QFont('Arial', 14))
        btn_clear.setMinimumHeight(50)
        btn_clear.setStyleSheet("background-color: #f44336; color: white;")
        btn_clear.clicked.connect(self.clear_clicked)
        control_layout.addWidget(btn_clear)

        btn_equals = QPushButton('=')
        btn_equals.setFont(QFont('Arial', 18, QFont.Bold))
        btn_equals.setMinimumHeight(50)
        btn_equals.setStyleSheet("background-color: #2196F3; color: white;")
        btn_equals.clicked.connect(self.equals_clicked)
        control_layout.addWidget(btn_equals)

        layout.addLayout(control_layout)

        # Status label
        self.status_label = QLabel('Currently supports: Addition and Subtraction')
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont('Arial', 10))
        self.status_label.setStyleSheet("color: #666;")
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def number_clicked(self, number):
        """Handle number button clicks"""
        current = self.display.text()
        if current == '0' or current == 'Error':
            self.display.setText(number)
        else:
            self.display.setText(current + number)

    def operation_clicked(self, op):
        """Handle operation button clicks"""
        try:
            self.first_number = float(self.display.text())
            self.operation = op
            self.display.setText('0')
        except ValueError:
            self.display.setText('Error')

    def equals_clicked(self):
        """Handle equals button click"""
        if self.first_number is None or self.operation is None:
            return

        try:
            second_number = float(self.display.text())

            if self.operation == 'add':
                result = self.add(self.first_number, second_number)
                self.display.setText(str(result))
            elif self.operation == 'subtract':
                result = self.subtract(self.first_number, second_number)
                self.display.setText(str(result))

            # Reset for next calculation
            self.first_number = None
            self.operation = None

        except ValueError:
            self.display.setText('Error')

    def clear_clicked(self):
        """Handle clear button click"""
        self.display.setText('0')
        self.first_number = None
        self.operation = None

    def add(self, a, b):
        """Add two numbers together"""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers"""
        return a - b


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
