import customtkinter
from tkinter import filedialog
from os import path
from visualizacion import PredictApp

class MyCodeFrame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.code = ''
        
        # Label
        self.title = customtkinter.CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        # Code
        self.textbox = customtkinter.CTkTextbox(master=self, height=250, font=('consolas', 18), wrap = 'none')
        self.textbox.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")

        # Select Java File
        self.button = customtkinter.CTkButton(self, fg_color="teal", text="Seleccionar Archivo", command=self.select_java_file)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=1)

    def select_java_file(self):
        self.file_path = filedialog.askopenfilename(
            initialdir="/", 
            title="Selecciona un código en Java", 
            filetypes=(("archivos .java", "*.java"),)
        )
        
        if self.file_path == '':
            return
        
        head, self.filename = path.split(self.file_path)

        with open(self.file_path) as java_code:
            self.code = java_code.read()
            self.title.configure(text=self.filename)
            self.textbox.delete("0.0", "end")
            self.textbox.insert(index="0.0", text=self.code)

    def getCode(self):
        self.code = self.textbox.get("0.0", "end")
        return self.code

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title("Detector de Plagio")
        self.geometry("750x450+550+200")
        self.minsize(1000, 755)
        self.maxsize(1000, 755)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Code 1
        self.code1_frame = MyCodeFrame(self, "Código 1")
        self.code1_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
        # Code 2
        self.code2_frame = MyCodeFrame(self, "Código 2")
        self.code2_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

        # Identifier
        self.title_id = customtkinter.CTkLabel(self, text="Segmentos en común", fg_color="gray30", corner_radius=6)
        self.title_id.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)

        self.identifier = customtkinter.CTkTextbox(self, height=250, font=('consolas', 18), wrap = 'none', state="disabled")
        self.identifier.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)

        # Detect Plagiarism
        self.button = customtkinter.CTkButton(self, text="Detectar Plagio", command=self.detect_plagiarism)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        # Veredict
        self.label = customtkinter.CTkLabel(self, text="Veredicto", fg_color="gray30", corner_radius=6)
        self.label.grid(row=4, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def detect_plagiarism(self):
        self.code1 = predictApp.process_code(self.code1_frame.getCode())
        self.code2 = predictApp.process_code(self.code2_frame.getCode())

        self.code3 = predictApp.process_code2(self.code1_frame.getCode())
        self.code4 = predictApp.process_code2(self.code2_frame.getCode())
        
        self.label.configure(text="Detectando Plagio...")
        self.predictions = predictApp.predict_plagiarism(self.code1, self.code2)    
        self.veredict = predictApp.determine_plagiarism(self.predictions)
        self.label.configure(text=self.veredict)

        if self.veredict == "Sí es plagio":
            self.label.configure(fg_color="#d94040")
        else:
            self.label.configure(fg_color="green")
        
        segments = predictApp.identify_plagiarized_segments(self.code3, self.code4)
        
        self.identifier.configure(state="normal")
        self.identifier.delete("0.0", "end")

        for segment1, segment2  in segments:
            self.identifier.configure(state="normal")
            self.identifier.insert("end", '\n'.join(segment1) + '\n')
            self.identifier.configure(state="disabled")

predictApp = PredictApp()
app = App()

app.mainloop()
