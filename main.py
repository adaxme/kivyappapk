import socket
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.core.window import Window
Window.size = (400, 600)
Window.clearcolor = (0.07, 0.09, 0.13, 1)  # Dark navy background

class PortScanner(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        self.target_input = TextInput(
            hint_text='Enter IP or domain',
            size_hint=(1, None),
            height=50,
            multiline=False,
            padding_y=(10, 10),
            font_size=18,
            background_color=(0.15, 0.2, 0.25, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )

        self.scan_button = Button(
            text='🔍 Scan Common Ports',
            size_hint=(1, None),
            height=50,
            background_color=(0.2, 0.6, 0.3, 1),
            color=(1, 1, 1, 1),
            font_size=18,
            bold=True
        )
        self.scan_button.bind(on_press=self.scan_ports)

        self.result_label = Label(
            text='Scan results will appear here.',
            font_size=16,
            size_hint=(1, 1),
            halign='left',
            valign='top',
            text_size=(self.width, None),
            color=(0.9, 0.9, 0.9, 1)
        )

        self.scroll = ScrollView()
        self.scroll.add_widget(self.result_label)

        self.add_widget(Label(text='🛡️ PortScan Lite', font_size=24, color=(1, 1, 1, 1), size_hint=(1, None), height=40))
        self.add_widget(self.target_input)
        self.add_widget(self.scan_button)
        self.add_widget(self.scroll)

    def scan_ports(self, instance):
        target = self.target_input.text.strip()
        if not target:
            popup = Popup(title='Input Error', content=Label(text='Please enter a valid IP or domain.'), size_hint=(0.8, 0.3))
            popup.open()
            return

        open_ports = []
        self.result_label.text = "🔄 Scanning...\n"
        common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306]

        for port in common_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.3)
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except:
                continue

        if open_ports:
            self.result_label.text = f"✅ Open Ports on {target}:\n" + "\n".join([f"• Port {p}" for p in open_ports])
        else:
            self.result_label.text = f"❌ No common ports open or host unreachable."

class PortScannerApp(App):
    def build(self):
        self.title = "PortScan Lite"
        return PortScanner()

if __name__ == '__main__':
    PortScannerApp().run()
