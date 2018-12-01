from floatingactionsbuttons import FloatingActionButtons


class BaseScreen(Screen):
    def on_enter(self):

        self.add_widget(FloatingActionButtons(
            icon = 'lead-pencil',
            floating_data={
                'Python': 'language-python',
                'Php': 'language-php',
                'C++': 'language-cpp'},
            callback=self.set_my_language))