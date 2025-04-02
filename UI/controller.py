import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def filldd(self):
        for corso in self._model.getAllCorsi():
            self._view.dd.options.append(ft.dropdown.Option(key = corso.codins,
                                                            text = corso.__str__()))

    def handleb1(self, e):
        self._view.lvTxtOut.controls.clear()
        corso = self._view.dd.value
        if corso is None:
            self._view.create_alert("Attenzione, selezionare un corso!")
            self._view.update_page()
        else:
            studenti = self._model.getIscrittiCorso(corso)
            self._view.lvTxtOut.controls.append(ft.Text(f"Studenti del corso ({len(studenti)} in totale):"))
            for s in studenti:
                self._view.lvTxtOut.controls.append(ft.Text(s))
            self._view.update_page()

    def handleb2(self, e):
        self._view.txtNome.value = ""
        self._view.txtCognome.value = ""

        matricola = self._view.txtMatricola.value
        if matricola == "":
            self._view.create_alert("Attenzione, inserire un matricola!")
            self._view.update_page()
        else:
            studente = self._model.getStudente(matricola)
            if not studente:
                self._view.create_alert("Studente non esistente!")
                self._view.update_page()
            else:
                self._view.txtNome.value = studente[0].nome
                self._view.txtCognome.value = studente[0].cognome
                self._view.update_page()

    def handleb3(self, e):
        self._view.lvTxtOut.controls.clear()
        matricola = self._view.txtMatricola.value
        if matricola == "":
            self._view.create_alert("Attenzione, inserire un matricola!")
            self._view.update_page()
        else:
            studente = self._model.getStudente(matricola)
            if not studente:
                self._view.create_alert("Studente non esistente!")
                self._view.update_page()
            else:
                corsi = self._model.getCorsiStudente(matricola)
                self._view.lvTxtOut.controls.append(ft.Text(f"Corsi seguiti dallo studente {matricola}:"))
                for c in corsi:
                    self._view.lvTxtOut.controls.append(ft.Text(c))
                self._view.update_page()


