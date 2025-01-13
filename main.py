    def list_buttons(self):
        print("ButtonInspectorPlugin: Liste der Tasten wird abgerufen...")
        try:
            buttons = self.controller.get_buttons()
            if not buttons:
                print("Keine Tasten gefunden.")
                return

            for button in buttons:
                print(f"Taste gefunden: ID={button.id}, Name={button.name}")

        except Exception as e:
            print(f"Fehler beim Abrufen der Tasten: {e}")
