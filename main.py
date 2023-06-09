import customtkinter
from visualizacion import PredictApp

class MyCodeFrame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.code = ''
        
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        self.textbox = customtkinter.CTkTextbox(master=self, height=280, font=('consolas', 18))
        self.textbox.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")

    def getCode(self):
        self.code = self.textbox.get("0.0", "end")
        return self.code

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title("Detector de Plagio")
        self.geometry("750x450+550+200")
        self.minsize(750, 450)
        self.maxsize(750, 450)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Code 1
        self.code1_frame = MyCodeFrame(self, "Código 1")
        self.code1_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
        # Code 2
        self.code2_frame = MyCodeFrame(self, "Código 2")
        self.code2_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

        # Detect Plagiarism
        self.button = customtkinter.CTkButton(self, text="Detectar Plagio", command=self.detect_plagiarism)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        # Veredict
        self.label = customtkinter.CTkLabel(self, text="Veredicto", fg_color="gray30", corner_radius=6)
        self.label.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)


    def detect_plagiarism(self):
        self.code1 = predictApp.process_code(self.code1_frame.getCode())
        self.code2 = predictApp.process_code(self.code2_frame.getCode())
        
        self.label.configure(text="Detectando Plagio...")
        self.predictions = predictApp.predict_plagiarism(self.code1, self.code2)    
        self.veredict = predictApp.determine_plagiarism(self.predictions)
        self.label.configure(text=self.veredict)

predictApp = PredictApp()
app = App()

app.mainloop()
