import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.font import Font
from tkinter import ttk
import pygame

class Question:
    def __init__(self, prompt, options, answer, explanation):
        self.prompt = prompt
        self.options = options
        self.answer = answer
        self.explanation = explanation


questions = [

    Question("Was ist ein Bilanzkreis?", ["ein virtuelles Energiemengenkonto",
                                          "der Jahresabschluss eines Energieunternehmens",
                                          "ein Diagramm, in dem der Energiemix eines Stromerzeugers dargestellt ist"],
             [0],
             "Der Bilanzkreis ist ein virtuelles Energiemengenkonto, welches Erzeugung und Verbrauch von Energie gegenüberstellt"),
    Question("Wo befindet sich eine Marktlokation?", ["dort, wo Strom eingespeist wird",
                                                      "dort, wo Strom gehandelt wird",
                                                      "dort, wo Strom ausgespeist wird"], [0, 2],
             "Marktlokationen befinden sich überall dort, wo Strom eingespeist oder bezogen wird."),
    Question("Was ist Ausgleichsenergie?",
             ["der Unterschied zwischen dem prognostizierten und dem realen Verbrauch an Energie",
              "das bilanzielle Pendant zur Regelenergie",
              "physischer Strom, der eingespeist wird, um die Stabilität des Stromnetzes zu gewährleisten"], [0, 1],
             "Unter Ausgleichsenergie versteht man die elektrische Energie, "
             "um die der Verbrauch eines Bilanzkreises vom prognostizierten Verbrauch abweicht. Sie ist das Pendant auf dem Abrechnungsmarkt zur Regelleistung."),
    Question("Bilanzkreisüberdeckung, Netzunterspeisung. Wer zahlt?",
             ["Der BIKO an den BKV ",
              "Der BKV an den BIKO",
              "Der Verteilnetzbetreiber an den Übertragungsnetzbetreiber"], [0],
             "Das Netz ist unterspeist, es muss also Regelenergie hinzugefügt werden. Der BKV hat einen Beitrag dazu geleistet und bekommt dementsprechend Geld"),


    Question("Was regelt ein Bilanzkreisvertrag?",
             ["Vertragsgegenstand",
              "Rechte, Pflichten und Leistungen des Betreibers von Übertragungsnetzen",
              "Rechte und Pflichten des Bilanzkreisverantwortlichen"
              ], [0, 1, 2],
             "Ein Bilanzkreisvertrag regelt  all diese Punkte."),
    Question("Wer ist für die Beschaffung und den Einsatz von Regelenergie verantwortlich?",
             ["Bilanzkreisverantwortlicher (BKV)",
              "Übertragungsnetzbetreiber (ÜNB)",
              "Verteilnetzbetreiber (VNB)"], [1],
             "Der Übertragungsnetzbetreiber (ÜNB) ist dafür verantwortlich, Regelenergie zu beschaffen und einzusetzen."),
    Question("Wann erfolgt die Abrechnung der Bilanzabweichungen der Bilanzkreise?",
             ["täglich gemäß den Regeln der Bundesnetzagentur",
              "wöchentlich gemäß den Regeln der Bundesnetzagentur",
              "monatlich gemäß den Regeln der Bundesnetzagentur"], [2],
             "Die Abrechnung der Bilanzabweichungen der Bilanzkreise erfolgt monatlich gemäß den Regeln der Bundesnetzagentur."),
    Question("Was ist eine der Hauptverantwortlichkeiten des Bilanzkreisverantwortlichen (BKV)?",
             ["durch die Spekulation mit Ausgleichsenergie möglichst gewinnbringend zu arbeiten",
              "Beschaffung und Einsatz von Regelenergie",
              "Bestreben, Bilanzabweichungen möglichst gering zu halten",
              "Stromhandel an der Börse"], [2],
             "Eine der Hauptverantwortlichkeiten des BKV ist es, Bilanzabweichungen möglichst gering zu halten. Es ist verboten die Ausgleichsenergie als Mittel zum Gewinn zu nutzen"),
    Question("Was kann der BKV nutzen, um vorhersehbare Abweichungen auszugleichen?",
             ["Ausgleichsenergie",
              "Regelenergie",
              "Stromhandel an der Börse"], [2],
             "Der BKV kann durch Stromhandel an der Börse seine Bilanzkreisabweichung zu verringern."),
    Question("Warum ist die Einhaltung der Datenaustauschvorgaben für beide Parteien entscheidend?",
             ["um Kosten zu sparen",
              "um die Integrität und Genauigkeit der Daten sicherzustellen",
              "um ein stabiles Stromnetz zu gewährleisten"], [0,1,2],
             "All diese Punkte werden direkt oder indirekt durch Einhaltung der Vorgaben erreicht"),
    Question("Welche Funktion hat der reBAP im deutschen Energiemarkt?",
             ["Anleitung zur Vorgehensweise nach Blackout",
              "bezeichnet den geringsten Preis bei der Merit-Order",
              "dient der Berechnung von Ausgleichsenergie bei Bilanzkreisabweichung"], [2],
             "Der reBAP hat neben seiner Funktion als Abrechnungspreis eine grundlegende Bedeutung im deutschen Energiemarkt. Seine Aufgabe besteht darin, "
             "die richtigen Anreize zu setzen,"
             " damit der BKV offene Positionen im Handel schließt, bevor die Übertragungsnetzbetreiber (ÜNB) diese mit Regelenergie ausgleichen müssen."),
    Question("Welche Funktion haben die Strombörsen EEX in Leipzig und EPEX in Paris?",
             ["Die EEX ist für den Intradayhandel von essenzieler Bedeutung",
              "Die EPEX bitet hauptsächlich kurzfristige Produkte an.",
              "Die Produkte an der EEX sind günstiger, da sie hauptsächlich kurzfristige handelsprodukte anbietet"],
             [1],
             "Die EEX handelt hauptsächlich langfristige Produkte, während die EPEX den kurzfristigen Handel abdeckt."),
    Question(
        "Was geschieht, wenn nach der CutOffTime Unstimmigkeiten in den Fahrplänen sind?",
        ["Es greifen die Matchingregeln",
         "Der niedrigere Wert aus den beiden Zeitreihen wird genommen",
         "Beide Fahrpläne werden abgelehnt"],
        [0,1],
        "Es greifen die Matchingregeln. Dazu gehört die Minimumregel"),
    Question(
        "Was passiert, wenn bei der BK-SZR Differenzen auftreten) ",
        ["Der ÜNB fordert eine Clearingliste beim BKV",
         "Der BKV fordert eine Clearingliste beim ÜNB",
         "Der NB fordert eine Clearingliste beim BKV"],
        [2],
        "Antwort 3 ist korrekt"),
    Question(
        "Welche 3 Prognosen erhalten EInzug bei einem Fahrplan ",
        ["Erzeugung, Verbrauch und Art der Erzeugung/Verbrauch",
         "Erzeugung, Verbrauch und Redispatch",
         "Lastgangprofil, Marktlokation und Messlokation"],
        [2],
        "Erzeugungsprognose, Verbrauchsprognose und Redispatchprognose sind richtig")



]



class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.current_question = 0
        self.score = 0
        self.question_label = tk.Label(root, text="")
        self.question_label.config(font=Font(family="Arial", size=25, weight="bold"))
        self.question_label.pack()
        self.options_var = []
        self.option_checkbuttons = []
        for i in range(len(questions[0].options)):
            var = tk.IntVar()
            self.options_var.append(var)
            option_checkbox = tk.Checkbutton(root, text="", variable=var)
            option_checkbox.config(font=("Calibri", 27))
            option_checkbox.pack()
            self.option_checkbuttons.append(option_checkbox)

        self.submit_button = tk.Button(root, text="Antwort überprüfen")
        self.submit_button.config(font=("Arial", 20))
        self.submit_button.config(command=self.check_answer)
        self.submit_button.pack()
        self.progress_label = tk.Label(root, text="")
        self.progress_label.pack()
        self.progress_bar = ttk.Progressbar(root, length=400, mode="determinate")
        self.progress_bar.pack()
        self.update_question()

        image_path = r"C:\Users\josef\Desktop\Lea.png"
        image = Image.open(image_path)
        image = image.resize((1000, 200))
        self.image_label = tk.Label(root, image=None)
        self.image_label.image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.image_label.image)
        self.image_label.pack()
        self.volume_label = tk.Label(root, text="Lautstärke")
        self.volume_label.config(font=("Arial", 12))
        self.volume_label.pack()
        self.volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
        self.volume_slider.set(50)
        self.volume_slider.pack()

        pygame.init()
        self.correct_sound = pygame.mixer.Sound("richtig.wav")
        self.incorrect_sound = pygame.mixer.Sound("falsch.wav")

    def check_answer(self):
        selected_options = []

        for i, var in enumerate(self.options_var):
            if var.get() == 1:
                selected_options.append(i)

        if not selected_options:
            messagebox.showinfo("Fehler", "Bitte wähle mindestens eine Antwort aus.")
            return

        correct_options = questions[self.current_question].answer
        self.current_question += 1
        if set(selected_options) == set(correct_options):
            self.score += 1
            volume = self.volume_slider.get() / 100
            self.correct_sound.set_volume(volume)
            self.correct_sound.play()
        else:
            volume = self.volume_slider.get() / 100
            self.incorrect_sound.set_volume(volume)
            self.incorrect_sound.play()
            self.show_explanation_window(questions[self.current_question].explanation)
              # Stop here if the answer is incorrect

        # Proceed to the next question if the answer is correct

        if self.current_question < len(questions):
            self.update_question()
        else:
            messagebox.showinfo("Quiz beendet", "Deine Punktzahl: {}/{}".format(self.score, len(questions)))
            self.root.quit()
        return

    def show_explanation_window(self, explanation):
        window = tk.Toplevel(self.root)
        window.title("Erklärung")
        window.attributes("-topmost", True)
        explanation_label = tk.Label(window, text=explanation, font=("Arial", 25), wraplength=800)
        explanation_label.pack()
        window.update_idletasks()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        position_x = int((screen_width - window_width) / 2)
        position_y = int((screen_height - window_height) / 2)
        window.geometry(f"+{position_x}+{position_y}")
        ok_button = tk.Button(window, text="OK", command=window.destroy)
        ok_button.pack()

    def show_explanation_window(self, explanation):
        window = tk.Toplevel(self.root)
        window.title("Erklärung")
        window.attributes("-topmost", True)
        explanation_label = tk.Label(window, text=explanation, font=("Arial", 25), wraplength=800)
        explanation_label.pack()
        window.update_idletasks()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        position_x = int((screen_width - window_width) / 2)
        position_y = int((screen_height - window_height) / 2)
        window.geometry(f"+{position_x}+{position_y}")
        ok_button = tk.Button(window, text="OK", command=window.destroy)
        ok_button.pack()

    def update_question(self):
        question = questions[self.current_question]
        question_text = question.prompt
        self.question_label.config(text=question_text)

        for i, option_checkbox in enumerate(self.option_checkbuttons):
            option_checkbox.config(text=question.options[i])
            self.options_var[i].set(0)

        progress_percentage = (self.current_question + 1) / len(questions) * 100
        self.progress_bar["value"] = progress_percentage


root = tk.Tk()
root.title("Quiz")
root.attributes("-fullscreen", True)
quiz_gui = QuizGUI(root)
root.mainloop()
