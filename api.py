import sys
import requests
from PyQt5.QtWidgets import *


id = x
class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowsTitle("Cos tam nie apie")
        self.resize(600,400)
        
        self.lyt_main = QHBoxLayout()
        self.lyt_left = QHBoxLayout()
        self.lyt_right = QHBoxLayout()
        self.lyt_form = QFormLayout()


        self.btn1 = QPushButton("daj dane stacji")
        self.btn1.resize(100,50)
        self.btn1.click.connect(self.pobierz_dane)
        self.btn2 = QPushButton("machnt")
        self.lyt_left.addWidget(self.btn2)
        self.lyt_left.addWidget(self.btn1)

        self.lbl1 = QLabel("to bede dane stacji")
        self.lbl2 = QLabel("tu tu pusto jest")
        self.lyt_right.addWidget(self.lbl1)
        self.lyt_left.addWidget(self.lbl2)

        self.lyt_main.addLayout(self.lyt_left)
        self.lyt_main.addLayout(self.lyt_right)

        self.setLayout(self.lyt_main)

        def pobierz_dane(self):
            res = requests.get(url="http://api.open-notify.org/iss-now.json")
            res.raise_for_status()

            dane = res.json()
            lat = dane['iss_position']['latitude']
            long = dane['iss_position']['longitude']
            self.lbl1.setText(f" {lat =}, {long =}")
            
        def nowe_dane(self):
            res = requests.get(url="htpp://swapi.dev/api/people/1")
            data = res.json()
            print(data)
            name = data['name']
            height = data["height"]
            mass = data["mass"]
            