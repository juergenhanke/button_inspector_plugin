class ButtonInspectorPlugin:
    def __init__(self, controller):
        self.controller = controller
        print("ButtonInspectorPlugin: Plugin wurde geladen!")  # Debug-Ausgabe

    def on_ready(self):
        print("ButtonInspectorPlugin: Plugin ist bereit!")  # Debug-Ausgabe
        self.list_buttons()

    def list_buttons(self):
        print("ButtonInspectorPlugin: Liste der Tasten wird abgerufen...")  # Debug-Ausgabe
        try:
            buttons = self.controller.get_buttons()  # Beispiel-Methode
            if not buttons:
                print("Keine Tasten gefunden.")
                return
            output_file = "/tmp/button_list.txt"  # Speicherort für die Ausgabe

            with open(output_file, "w") as file:
                for button in buttons:
                    file.write(f"Taste gefunden: ID={button.id}, Name={button.name}\n")
                    print(f"Taste gefunden: ID={button.id}, Name={button.name}")  # Terminal-Ausgabe

            print(f"Tasten-Liste erfolgreich in {output_file} gespeichert.")

        except Exception as e:
            print(f"Fehler beim Abrufen der Tasten: {e}")
