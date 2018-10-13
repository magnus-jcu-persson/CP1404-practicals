from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class VerySimpleApp(App):
    def build(self, **kwargs):
        super().__init__(**kwargs)
        self.labels = ['Steve', 'Memes', 'Magnus']
        self.title = "Very Simple App"
        self.root = Builder.load_file('very_simple_app.kv')

        self.create_labels()
        return self.root

    def create_labels(self):
        for label in self.labels:
            label_field = Label(text=label, id='test_' + label)
            self.root.ids.labels_box.add_widget(label_field)

VerySimpleApp().run()