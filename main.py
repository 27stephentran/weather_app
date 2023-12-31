# main.py
### Imports ###
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel,
                             QPushButton, QLineEdit, QGroupBox)
from PyQt5.QtCore import Qt

from rich import print
from rich.traceback import install
install(show_locals=True)
from rich.console import Console
console = Console()

from tools import get_weather, get_local_time, get_celsius, get_icon, validate_string_format

### Varaibles ###

### Main Win Class ###
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.event_handlers()

    def setup_ui(self):
        ### Window Setup ###
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 330, 260)

        ### UI Setup ###
        ## Search UI
        # Widgets
        self.txt_search = QLineEdit(self, placeholderText="eg Hanoi, VN")
        self.btn_search = QPushButton("Search", self)

        # Layouts
        lyt_main_search = QHBoxLayout()

        # Setup
        lyt_main_search.addWidget(self.txt_search)
        lyt_main_search.addWidget(self.btn_search)

        ## Info 1 UI
        # Widgets
        self.lbl_city = QLabel("City:", self)
        self.lbl_country = QLabel("Country:", self)

        # Layouts
        lyt_main_info_1 = QHBoxLayout()

        # Setup
        lyt_main_info_1.addWidget(self.lbl_city, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_main_info_1.addWidget(self.lbl_country, alignment=Qt.AlignmentFlag.AlignCenter)

        ## Info 2 UI
        # Widgets
        self.lbl_time = QLabel("Time:", self)
        self.lbl_date = QLabel("Date:", self)

        # Layouts
        lyt_main_info_2 = QHBoxLayout()

        # Setup
        lyt_main_info_2.addWidget(self.lbl_time, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_main_info_2.addWidget(self.lbl_date, alignment=Qt.AlignmentFlag.AlignCenter)

        ## Weather UI
        # Widgets
        self.grpb_weather = QGroupBox("Weather", self)

        self.lbl_icon = QLabel("'Icon'", self)
        self.lbl_temp = QLabel("'Temp'", self)
        self.lbl_description = QLabel("'Description'", self)

        self.lbl_feels = QLabel("Feels:", self)
        self.lbl_max = QLabel("Max:", self)
        self.lbl_min = QLabel("Min:", self)
        self.lbl_humidity = QLabel("Humidity:", self)
        self.lbl_wind = QLabel("Wind:", self)

        # Layouts
        lyt_main_weather = QHBoxLayout()
        lyt_weather_main = QHBoxLayout()
        lyt_weather_info = QVBoxLayout()
        lyt_weather_detail = QVBoxLayout()
        
        # Setup
        lyt_weather_info.addWidget(self.lbl_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_info.addWidget(self.lbl_temp, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_info.addWidget(self.lbl_description, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_weather_detail.addWidget(self.lbl_feels, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_detail.addWidget(self.lbl_max, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_detail.addWidget(self.lbl_min, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_detail.addWidget(self.lbl_humidity, alignment=Qt.AlignmentFlag.AlignCenter)
        lyt_weather_detail.addWidget(self.lbl_wind, alignment=Qt.AlignmentFlag.AlignCenter)

        lyt_weather_main.addLayout(lyt_weather_info)
        lyt_weather_main.addLayout(lyt_weather_detail)

        self.grpb_weather.setLayout(lyt_weather_main)

        lyt_main_weather.addWidget(self.grpb_weather)


        #TODO: Add Forcast UI
        ## Forcast UI
        # Widgets
        # Layouts
        # Setup

        ## Main Win Layout
        # Widgets
        central_widget = QWidget()

        # Layouts
        lyt_main = QVBoxLayout()

        # Setup
        lyt_main.addLayout(lyt_main_search)
        lyt_main.addLayout(lyt_main_info_1)
        lyt_main.addLayout(lyt_main_info_2)
        lyt_main.addLayout(lyt_main_weather)
        #TODO: Add Forcast Layout

        central_widget.setLayout(lyt_main)
        self.setCentralWidget(central_widget)


    def event_handlers(self):
        self.btn_search.clicked.connect(self.update_ui)


    def update_ui(self):
        if validate_string_format(self.txt_search.text()):
            try:
                # Get Weather & Location Data
                city_name, country_code = self.txt_search.text().split(", ")
                weather_data = get_weather(city_name, country_code)
                if isinstance(weather_data, dict):
                    today's work 
            except:
                console.print_exception()
                self.txt_search.clear()
                self.txt_search.setPlaceholderText("Check format > Hanoi, VN")
        else:
            self.txt_search.clear()
            self.txt_search.setPlaceholderText("Check format > Hanoi, VN")
        

### App Execution ###
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
