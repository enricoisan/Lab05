import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT

        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # Elementi grafici
        self._title = None
        self.dd = None
        self.btn1 = None
        self.txtMatricola = None
        self.txtNome = None
        self.txtCognome = None
        self.btn2 = None
        self.btn3 = None
        self.btn4 = None
        self.lvTxtOut = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # Titolo
        self._title = ft.Text("App Gestione Studenti", color = "blue", size = 24)
        self._page.controls.append(self._title)

        # Riga 1
        self.dd = ft.Dropdown(label = "Corso", width = 600)
        self._controller.filldd()

        self.btn1 = ft.ElevatedButton(text = "Cerca iscritti",
                                      on_click=self._controller.handleb1)
        row1 = ft.Row([self.dd, self.btn1], alignment=ft.MainAxisAlignment.CENTER)

        # Riga 2
        self.txtMatricola = ft.TextField(label = "Matricola", width = 250)
        self.txtNome = ft.TextField(label = "Nome", width = 250, read_only = True)
        self.txtCognome = ft.TextField(label = "Cognome", width = 250, read_only = True)
        row2 = ft.Row([self.txtMatricola, self.txtNome, self.txtCognome], alignment=ft.MainAxisAlignment.CENTER)

        # Riga 3
        self.btn2 = ft.ElevatedButton(text = "Cerca studente",
                                      on_click = self._controller.handleb2)
        self.btn3 = ft.ElevatedButton(text = "Cerca corsi",
                                      on_click = self._controller.handleb3)
        self.btn4 = ft.ElevatedButton(text = "Iscrivi")
        row3 = ft.Row([self.btn2, self.btn3, self.btn4], alignment=ft.MainAxisAlignment.CENTER)

        # List View
        self.lvTxtOut = ft.ListView(expand = True)

        # Composizione interfaccia
        self._page.add(row1, row2, row3, self.lvTxtOut )


        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
