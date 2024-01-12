from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.core.window import Window

class ChatInterface(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatInterface, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.chat_history = ScrollView()
        self.messages_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, padding=(10, 10))
        self.chat_history.add_widget(self.messages_layout)
        self.add_widget(self.chat_history)

        self.message_input = TextInput(size_hint_y=None, height=40)
        self.send_button = Button(text="Отправить", size_hint_y=None, height=40)
        self.send_button.bind(on_press=self.send_message)

        input_box = BoxLayout(size_hint_y=None, height=40, padding=(10, 10))
        input_box.add_widget(self.message_input)
        input_box.add_widget(self.send_button)

        self.add_widget(input_box)

    def send_message(self, instance):
        message = self.message_input.text
        if message:
            self.add_user_message(message)
            # Проверяем, если сообщение - "привет", то добавляем ответ от бота
            if message.lower() == 'привет':
                self.add_bot_response("Привет, как дела?")

            self.message_input.text = ''
            self.chat_history.scroll_y = 0

    def add_user_message(self, message):
        # Создаем BoxLayout для сообщения пользователя
        user_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30, spacing=10)

        # Добавляем пустой виджет с фиксированной шириной, чтобы выровнять текст по правому краю
        user_layout.add_widget(Label(size_hint_x=None, width=200))

        # Добавляем Label для отображения текста сообщения с выравниванием по правому краю
        user_label = Label(text=f"[b]Вы:[/b] {message}", markup=True, halign='right')
        user_layout.add_widget(user_label)

        # Добавляем BoxLayout с сообщением пользователя в общий макет сообщений
        self.messages_layout.add_widget(user_layout)
        self.chat_history.scroll_y = 0

    def add_bot_response(self, response):
        # Создаем BoxLayout для ответа бота
        bot_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30, spacing=10)

        # Добавляем Label для отображения ответа бота с выравниванием по левому краю
        bot_label = Label(text=f"[b]Бот:[/b] {response}", markup=True)
        bot_layout.add_widget(bot_label)

        # Добавляем пустой виджет с фиксированной шириной, чтобы выровнять текст по левому краю
        bot_layout.add_widget(Label(size_hint_x=None, width=200))

        # Добавляем BoxLayout с ответом бота в общий макет сообщений
        self.messages_layout.add_widget(bot_layout)
        self.chat_history.scroll_y = 0

class ChatApp(App):
    def build(self):
        Window.size = (400, 600)
        return ChatInterface()

if __name__ == '__main__':
    ChatApp().run()
