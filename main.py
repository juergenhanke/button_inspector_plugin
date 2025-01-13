    def debug_controller(self):
        """Liste alle Methoden und Attribute des Controllers."""
        try:
            with open("/tmp/controller_debug.txt", "w") as file:
                for attr in dir(self.controller):
                    file.write(f"{attr}\n")
                print("Controller-Debugging abgeschlossen. Ergebnisse in /tmp/controller_debug.txt gespeichert.")
        except Exception as e:
            print(f"Fehler beim Debuggen des Controllers: {e}")

    def on_ready(self):
        """Wird aufgerufen, wenn das Plugin geladen ist."""
        self.debug_controller()
