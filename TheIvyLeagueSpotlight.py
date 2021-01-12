import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import *
from kivy.config import Config
from kivy.uix.label import Label

from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarkerPopup

from csv import *

import webbrowser

# ------------------------ LIBRARY INITIALIZATION ------------------------#


Window.size = (1600, 900)
Config.set('graphics', 'width', 'height')
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Window.top = 0
Window.left = 0


# class for running program
class IvyPage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #initialize the mapview module
        self.mapview = MapView(zoom=3, lat=30, lon=20, double_tap_zoom=False, snap_to_zoom=True)
        self.add_widget(self.mapview)

        self.name = []
        self.searching = []
        self.latitude = []
        self.longitude = []
        self.websites = []
        self.tag = []

        # Append all datas to a specific list
        with open("College.csv") as f:
            data = reader(f)
            for row in data:
                self.name.append(row[0])
                self.searching.append(row[5])
                self.latitude.append(float(row[1]))
                self.longitude.append(float(row[2]))
                self.websites.append(row[3])
                self.tag.append(row[4])
                print(row)

        # To make a loop of declaration
        self.marker = self.name
        self.bt = self.tag

        # Add all the pins to the maps
        for i in range(len(self.marker)):
            self.marker[i] = MapMarkerPopup(lat=self.latitude[i],
                                            lon=self.longitude[i],
                                            source=self.image(self.name[i]))
            self.mapview.add_widget(self.marker[i])
            self.bt[i] = Button(text=self.tag[i],
                                size_hint=(2.7, 0.8),
                                background_color=(1, 0, 0, 1))
            self.marker[i].add_widget(self.bt[i])

        # Call back the button that links to the university's website
        self.callback_list = [
            self.callback_mit, self.callback_stanford, self.callback_harvard,
            self.callback_oxford, self.callback_caltech, self.callback_zurich,
            self.callback_cambridge, self.callback_ucl, self.callback_imperial,
            self.callback_chicago, self.callback_nanyang, self.callback_national,
            self.callback_princeton, self.callback_cornell, self.callback_upenn,
            self.callback_tsinghua, self.callback_yale, self.callback_columbia,
            self.callback_epfl, self.callback_edinburgh, self.callback_michigan,
            self.callback_peking, self.callback_tokyo, self.callback_hopkins,
            self.callback_duke, self.callback_hongkong, self.callback_manchester,
            self.callback_berkely, self.callback_brown, self.callback_dartmouth,
            self.callback_toronto, self.callback_northwestern, self.callback_kcl,
            self.callback_kyoto, self.callback_ucla, self.callback_seoul,
            self.callback_melbourne, self.callback_nyu, self.callback_fudan,
            self.callback_kaist, self.callback_sydney, self.callback_newsouthwales,
            self.callback_sandiego, self.callback_kmitl, self.callback_chula,
            self.callback_mahidol, self.callback_thammasat, self.callback_lse,
            self.callback_queensland, self.callback_carnegie, self.callback_bristol,
            self.callback_delft, self.callback_tokyotech, self.callback_glasgow,
            self.callback_rice, self.callback_warwick, self.callback_amsterdam,
            self.callback_texas, self.callback_british, self.callback_zhejiang,
            self.callback_munich, self.callback_georgia, self.callback_illinois,
            self.callback_heidenberg, self.callback_lund, self.callback_monash,
            self.callback_malaya, self.callback_wuhan, self.callback_oregon,
            self.callback_georgetown
        ]

        # Add function to each buttons
        for callback in range(len(self.callback_list)):
            self.bt[callback].bind(on_press=self.callback_list[callback])
            self.bt[callback].size_hint = (2.5, 0.7)

        # Extra widgets
        self.floating = FloatLayout()
        self.add_widget(self.floating)

        # Transit the mapview to North American Zone
        self.button1 = Button(
            text="North America",
            background_color=(0 / 255, 56 / 255, 101 / 255, 1),
            # font_size=35,
            on_press=self.american
        )

        # Transit the mapview to European Zone
        self.button2 = Button(
            text="Europe",
            background_color=(0 / 255, 56 / 255, 101 / 255, 1),
            # font_size=35,
            on_press=self.europe,
        )

        # Transit the mapview to Asian Zone
        self.button3 = Button(
            text="Asia",
            background_color=(0 / 255, 56 / 255, 101 / 255, 1),
            on_press=self.asia
        )

        self.top_bar = BoxLayout(
            padding=15,
            spacing=15,
            size_hint=(1, 0.08),
            pos_hint={"y": 0.92},
        )

        self.centralize = Button(
            size_hint=(0.1, 0.05),
            pos_hint={"x": 0.4, "y": 0.01},
            text = "Centralize",
        )


        self.name_input = TextInput(
            text="",
            size_hint=(0.3, 0.05),
            font_size=40,
            multiline=False,
            pos_hint={"x": 0.01, "y": 0.01},
            halign="center"
        )
 
        self.show = Button(
            text="Search",
            size_hint=(0.1, 0.05),
            pos_hint={"x": 0.3, "y": 0.01},
            on_press = self.zoom_location
        )

        self.floating.add_widget(self.name_input)
        self.floating.add_widget(self.show)
        self.floating.add_widget(self.top_bar)
        self.top_bar.add_widget(self.button1)
        self.top_bar.add_widget(self.button2)
        self.top_bar.add_widget(self.button3)

    @staticmethod
    def image(name):
        return f"/Users/markkypanc/Desktop/TestKivy3.1/IvyLogo/{name}.png"

    def callback_mit(self, instance):
        webbrowser.open(self.websites[0])

    def callback_stanford(self, instance):
        webbrowser.open(self.websites[1])

    def callback_harvard(self, instance):
        webbrowser.open(self.websites[2])

    def callback_oxford(self, instance):
        webbrowser.open(self.websites[3])

    def callback_caltech(self, instance):
        webbrowser.open(self.websites[4])

    def callback_zurich(self, instance):
        webbrowser.open(self.websites[5])

    def callback_cambridge(self, instance):
        webbrowser.open(self.websites[6])

    def callback_ucl(self, instance):
        webbrowser.open(self.websites[7])

    def callback_imperial(self, instance):
        webbrowser.open(self.websites[8])

    def callback_chicago(self, instance):
        webbrowser.open(self.websites[9])

    def callback_nanyang(self, instance):
        webbrowser.open(self.websites[10])

    def callback_national(self, instance):
        webbrowser.open(self.websites[11])

    def callback_princeton(self, instance):
        webbrowser.open(self.websites[12])

    def callback_cornell(self, instance):
        webbrowser.open(self.websites[13])

    def callback_upenn(self, instance):
        webbrowser.open(self.websites[14])

    def callback_tsinghua(self, instance):
        webbrowser.open(self.websites[15])

    def callback_yale(self, instance):
        webbrowser.open(self.websites[16])

    def callback_columbia(self, instance):
        webbrowser.open(self.websites[17])

    def callback_epfl(self, instance):
        webbrowser.open(self.websites[18])

    def callback_edinburgh(self, instance):
        webbrowser.open(self.websites[19])

    def callback_michigan(self, instance):
        webbrowser.open(self.websites[20])

    def callback_peking(self, instance):
        webbrowser.open(self.websites[21])

    def callback_tokyo(self, instance):
        webbrowser.open(self.websites[22])

    def callback_hopkins(self, instance):
        webbrowser.open(self.websites[23])

    def callback_duke(self, instance):
        webbrowser.open(self.websites[24])

    def callback_hongkong(self, instance):
        webbrowser.open(self.websites[25])

    def callback_manchester(self, instance):
        webbrowser.open(self.websites[26])

    def callback_berkely(self, instance):
        webbrowser.open(self.websites[27])

    def callback_brown(self, instance):
        webbrowser.open(self.websites[28])

    def callback_dartmouth(self, instance):
        webbrowser.open(self.websites[29])

    def callback_toronto(self, instance):
        webbrowser.open(self.websites[30])

    def callback_northwestern(self, instance):
        webbrowser.open(self.websites[31])

    def callback_kcl(self, instance):
        webbrowser.open(self.websites[32])

    def callback_kyoto(self, instance):
        webbrowser.open(self.websites[33])

    def callback_ucla(self, instance):
        webbrowser.open(self.websites[34])

    def callback_seoul(self, instance):
        webbrowser.open(self.websites[35])

    def callback_melbourne(self, instance):
        webbrowser.open(self.websites[36])

    def callback_nyu(self, instance):
        webbrowser.open(self.websites[37])

    def callback_fudan(self, instance):
        webbrowser.open(self.websites[38])

    def callback_kaist(self, instance):
        webbrowser.open(self.websites[39])

    def callback_sydney(self, instance):
        webbrowser.open(self.websites[40])

    def callback_newsouthwales(self, instance):
        webbrowser.open(self.websites[41])

    def callback_sandiego(self, instance):
        webbrowser.open(self.websites[42])

    def callback_kmitl(self, instance):
        webbrowser.open(self.websites[43])

    def callback_chula(self, instance):
        webbrowser.open(self.websites[44])

    def callback_mahidol(self, instance):
        webbrowser.open(self.websites[45])

    def callback_thammasat(self, instance):
        webbrowser.open(self.websites[46])

    def callback_lse(self, instance):
        webbrowser.open(self.websites[47])

    def callback_queensland(self, instance):
        webbrowser.open(self.websites[48])

    def callback_carnegie(self, instance):
        webbrowser.open(self.websites[49])

    def callback_bristol(self, instance):
        webbrowser.open(self.websites[50])

    def callback_delft(self, instance):
        webbrowser.open(self.websites[51])

    def callback_tokyotech(self, instance):
        webbrowser.open(self.websites[52])

    def callback_glasgow(self, instance):
        webbrowser.open(self.websites[53])

    def callback_rice(self, instance):
        webbrowser.open(self.websites[54])

    def callback_warwick(self, instance):
        webbrowser.open(self.websites[55])

    def callback_amsterdam(self, instance):
        webbrowser.open(self.websites[56])

    def callback_texas(self, instance):
        webbrowser.open(self.websites[57])

    def callback_british(self, instance):
        webbrowser.open(self.websites[58])

    def callback_zhejiang(self, instance):
        webbrowser.open(self.websites[59])

    def callback_munich(self, instance):
        webbrowser.open(self.websites[60])

    def callback_georgia(self, instance):
        webbrowser.open(self.websites[61])

    def callback_illinois(self, instance):
        webbrowser.open(self.websites[62])

    def callback_heidenberg(self, instance):
        webbrowser.open(self.websites[63])

    def callback_lund(self, instance):
        webbrowser.open(self.websites[64])

    def callback_monash(self, instance):
        webbrowser.open(self.websites[65])

    def callback_malaya(self, instance):
        webbrowser.open(self.websites[66])

    def callback_wuhan(self, instance):
        webbrowser.open(self.websites[67])

    def callback_oregon(self, instance):
        webbrowser.open(self.websites[68])

    def callback_georgetown(self, instance):
        webbrowser.open(self.websites[69])

    def zoom_location(self, instance):
        for n in range(len(self.searching)):
            if self.name_input.text.lower() == "mit":
                self.mapview.center_on(self.latitude[0], self.longitude[0])
                self.mapview.zoom = 8
            elif self.name_input.text.lower() in self.searching[n].lower():
                self.mapview.center_on(self.latitude[n], self.longitude[n])
                self.mapview.zoom = 8


    def american(self, instance):
        self.mapview.center_on(40, -90)
        self.mapview.zoom = 5

    def europe(self, instance):
        self.mapview.center_on(52.5, 0)
        self.mapview.zoom = 6

    def asia(self, instance):
        self.mapview.center_on(8, 100)
        self.mapview.zoom = 4

    def center(self, instance):
        self.mapview.center_on(30, 20)
        self.mapview.zoom = 3


class MyApp(App):
    def build(self):
        return IvyPage()

    def on_start(self):
        print(" \" The program has started \" ")

    def on_stop(self):
        print(" \" The program has ended \" ")


if __name__ == '__main__':
    MyApp().run()
