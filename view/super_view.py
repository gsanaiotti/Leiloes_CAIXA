import customtkinter as ctk

class SuperView:
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("utils/themes/yellow.json")

        self.app = ctk.CTk()
        self.app.title("Webscraping - Leilões CAIXA")
        