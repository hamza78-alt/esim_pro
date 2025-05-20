from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from phonenumbers import geocoder, carrier, parse
import qrcode
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import datetime

class EsimLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.add_widget(Label(text='[b]Esim Pro – Developed by Guessar ISKANDAR[/b]', markup=True, font_size=18))
        self.number_input = TextInput(hint_text='أدخل الرقم الدولي (+213...)', multiline=False)
        self.add_widget(self.number_input)
        self.result = Label(text='')
        self.add_widget(self.result)
        self.btn = Button(text='تحليل الرقم')
        self.btn.bind(on_press=self.analyze)
        self.add_widget(self.btn)

    def analyze(self, instance):
        num = self.number_input.text.strip()
        try:
            parsed = parse(num)
            country = geocoder.description_for_number(parsed, "en")
            sim = carrier.name_for_number(parsed, "en")
            result = f"الرقم: {num}\nالدولة: {country}\nالمشغل: {sim}"
            self.result.text = result

            with open("history.txt", "a") as f:
                f.write(f"{datetime.datetime.now()} - {result}\n")

            img = qrcode.make(num)
            img.save("qr.png")
        except:
            self.result.text = "رقم غير صالح!"

class EsimApp(App):
    def build(self):
        return EsimLayout()

if __name__ == '__main__':
    EsimApp().run()