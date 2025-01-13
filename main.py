class ButtonInspectorPlugin:
    def __init__(self, controller):
        self.controller = controller

    def on_ready(self):
        """Wird aufgerufen, wenn das Plugin geladen ist."""
        self.list_buttons()

    def list_buttons(self):
        """Liste alle verfügbaren Tasten und speichere sie in einer Datei."""
        try:
            # Button-Liste abrufen
            buttons = self.controller.get_buttons()  # Beispiel für Button-Methode
            output_file = "/tmp/button_list.txt"  # Speicherort für die Ausgabe

            with open(output_file, "w") as file:
                for button in buttons:
                    file.write(f"Taste gefunden: ID={button.id}, Name={button.name}\n")
                    print(f"Taste gefunden: ID={button.id}, Name={button.name}")  # Auch im Terminal ausgeben

            print(f"Tasten-Liste erfolgreich in {output_file} gespeichert.")

        except Exception as e:
            print(f"Fehler beim Abrufen der Tasten: {e}")