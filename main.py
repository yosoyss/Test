from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import random
from kivy.core.text import LabelBase

# Define the version
__version__ = "1.0.123"

# Configure the size of the window
Window.size = (350, 500)


# Class for the loading screen
class SplashScreen(Screen):
    # Main function of the splash screen
    def on_enter(self, *args):
        Clock.schedule_once(self.home, 3)

    # Function to redirect to the home screen
    def home(self, load):
        self.manager.current = "Home"


class Home(Screen):
    def fun(self):
        print("clicked")
        # icon = ico.Icon('delete')
        # print(icon)


class ImageGen(Screen):
    pass


class PassGen(Screen):
    text1 = StringProperty()
    icon_name = "gear"

    # @property
    # def icon_string(self):
    #     return f"[font=FontAwesome]{fa.icons.get(self.icon_name, '')}[/font]"

    def generator(self):
        my_list = "abcdefghijklmnopqrstuvwxyz1234567890"
        length = 6
        rand = "".join(random.sample(my_list, length))
        self.text1 = rand


class Main(ScreenManager):
    pass


# Load the my.kivy file
presentation = Builder.load_file("my.kv")


# Main function to load all the content
class Apps(App):
    def build(self):
        return presentation


if __name__ == "__main__":
    Apps().run()
