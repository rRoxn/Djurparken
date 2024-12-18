from PIL import Image, ImageTk  # Pillow-biblioteket för att hantera bilder
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from zoo.zoo import Zoo
from zoo.visitor import Visitor
from animals.lion import Lion
from animals.lioncub import LionCub
from animals.giraffe import Giraffe
from animals.elephant import Elephant

class MainApp(tk.Tk):
    def __init__(self, zoo):
        """Initialiserar huvudapplikationen."""
        super().__init__()
        self.zoo = zoo
        self.title("Djurparken")  # Titel för fönstret
        self.state('zoomed')  # Starta i fullskärmsläge
        self.frames = {}

        # Container för alla sidor
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")  # Använd grid-layout

        # Gör container expanderbart
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Lägg till sidor
        for Page in (StartPage, RegisterVisitorPage, ManageVisitorsPage, ZooInfoPage, AddAddonsPage,
                     SelectVisitorPage, ExploreParkPage, DetailedAnimalPage, SearchAnimalPage,
                     InteractAnimalPage, FeedAnimalPage):
            page_name = Page.__name__
            frame = Page(parent=container, controller=self, zoo=self.zoo)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Placera varje sida i samma grid

        # Visa startsidan
        self.show_page("StartPage")


    def show_page(self, page_name):
        """Visa en specifik sida och uppdatera innehåll vid behov."""
        frame = self.frames[page_name]
        # Uppdatera dynamiska sidor
        if page_name == "ManageVisitorsPage":
            frame.update_visitor_list()  # Uppdatera besökar listan
        elif page_name == "SelectVisitorPage":
            frame.update_visitors()  # Uppdatera besökarknappar
        frame.tkraise()  # Lyft sidan till toppen

    def get_page(self, page_name):
        """Returnerar en instans av en specifik sida."""
        return self.frames[page_name]


# Startsidan
class StartPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar startsidan för djurparken."""
        super().__init__(parent, bg="#1A3636")
        self.controller = controller
        self.zoo = zoo

        # Gör sidan expanderbar
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)  # Mittenkolumn
        self.grid_columnconfigure(2, weight=1)

        # Centralt innehållsram (center_frame)
        center_frame = tk.Frame(self, bg="#D6BD98", bd=2, relief="ridge")
        center_frame.place(relx=0.24, rely=0.14, relwidth=0.5, relheight=0.7)

        # Gör center_frame flexibelt
        center_frame.grid_rowconfigure(0, weight=0)  # Titel
        center_frame.grid_rowconfigure(1, weight=1)  # Bildruta
        center_frame.grid_rowconfigure(2, weight=1)  # Menyram
        center_frame.grid_rowconfigure(3, weight=0)  # Sidfot
        center_frame.grid_columnconfigure(0, weight=1)

        # Titel
        tk.Label(center_frame, text="Välkommen till Eggis Zoo", font=("Arial", 24, "bold"),
                 bg="#677D6A", fg="#ffffff").grid(row=0, column=0, pady=10, sticky="n")

        # Bildruta
        image_frame = tk.Frame(center_frame, bg="white", relief="ridge", bd=3)
        image_frame.grid(row=1, column=0, pady=10)
        try:
            image_path = "../assets/images/bridge.jpg"  # Bildens sökväg
            image = Image.open(image_path).resize((500, 150))  # Ändra storlek
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(image_frame, image=photo, bg="white")
            image_label.image = photo  # Håll en referens
            image_label.pack()
        except Exception as e:
            tk.Label(image_frame, text="Bild kunde inte laddas", bg="lightcoral", font=("Arial", 14)).pack(expand=True)
            print(f"Fel: {e}")

        # Menyram
        menu_frame = tk.Frame(center_frame, bg="#677D6A", relief="groove", bd=5, padx=10, pady=10)
        menu_frame.grid(row=2, column=0, pady=10)
        buttons = [
            ("Se info", "ZooInfoPage"),
            ("Köp biljett", "RegisterVisitorPage"),
            ("Hantera besökare", "ManageVisitorsPage"),
            ("Utforska djurparken", "SelectVisitorPage"),
            ("Avsluta Program", "quit")
        ]
        for idx, (text, page) in enumerate(buttons):
            if page == "quit":
                cmd = controller.quit  # Avsluta programmet
            else:
                cmd = lambda p=page: controller.show_page(p)
            row, col = divmod(idx, 2)  # Dela upp i rader och kolumner
            tk.Button(menu_frame,
                      text=text,
                      font=("Arial", 14, "bold"),
                      bg="#D6BD98", fg="#000000",
                      width=20, height=2,
                      command=cmd).grid(row=row, column=col, padx=10, pady=10)

        # Sidfot
        footer_label = tk.Label(center_frame, text="Sidfot med info", bg="lightgray", font=("Arial", 12))
        footer_label.grid(row=3, column=0, pady=5, sticky="ew")



class ZooInfoPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att visa information om djurparken."""
        super().__init__(parent, bg="#1A3636")
        self.controller = controller
        self.zoo = zoo

        # Gör sidan expanderbar
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

        # Huvudinnehåll i mitten
        center_frame = tk.Frame(self, bg="#D6BD98", bd=2, relief="ridge")
        center_frame.place(relx=0.24, rely=0.14, relwidth=0.5, relheight=0.73)

        # Layout för center_frame
        center_frame.grid_rowconfigure(0, weight=0)  # Tillbaka-knappen
        center_frame.grid_rowconfigure(1, weight=0)  # Info-rutan
        center_frame.grid_rowconfigure(2, weight=1)  # Djurlista
        center_frame.grid_columnconfigure(0, weight=1)
        center_frame.grid_columnconfigure(1, weight=1)

        # Tillbaka-knapp i vänstra hörnet
        back_button = tk.Button(center_frame, text="←", font=("Arial", 24, "bold"),
                                bg="#677D6A", fg="white", width=5, height=1,
                                command=lambda: controller.show_page("StartPage"))
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Rutan för parkens information
        info_section = tk.Frame(center_frame, bg="#677D6A", bd=2, relief="ridge")
        info_section.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        info_section.grid_columnconfigure(0, weight=1)  # För öppettider och biljett
        info_section.grid_columnconfigure(1, weight=1)  # För tillval

        # Titel
        tk.Label(info_section, text="Parkens Information", font=("Arial", 20, "bold"),
                 bg="#677D6A", fg="white").grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

        # Kolumn 1: Öppettider och biljettkostnad
        tk.Label(info_section, text=f"{self.zoo.show_opening_hours()}",
                 font=("Arial", 14), bg="#677D6A", fg="white").grid(row=1, column=0, pady=5, sticky="n")
        tk.Label(info_section, text=f"{self.zoo.show_ticket_price()}",
                 font=("Arial", 14), bg="#677D6A", fg="white").grid(row=2, column=0, pady=5, sticky="n")

        # Kolumn 2: Tillval i parken
        addons_text = "Tillval i parken:\n" + "\n".join(f"{addon} - {price} SEK"
                                                        for addon, price in self.zoo._addons.items())
        tk.Label(info_section, text=addons_text, font=("Arial", 14), bg="#677D6A", fg="white",
                 justify="left").grid(row=1, column=1, rowspan=2, pady=5, padx=10, sticky="n")

        # Djurlista med större bilder och text
        animal_list = self.zoo.list_animals()
        for index, animal in enumerate(animal_list):
            row = index // 2 + 2  # Starta från rad 2
            col = index % 2  # Växla mellan kolumn 0 och 1

            frame = tk.Frame(center_frame, bg="#f9f9f9", bd=2, relief="ridge")
            frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            frame.grid_columnconfigure(0, weight=1)

            # Bild som fyller ramen
            try:
                img = Image.open(animal.image_path).resize((200, 150), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame, image=photo, bg="#f9f9f9")
                img_label.image = photo  # Behåll referens
                img_label.grid(row=0, column=0, pady=5, sticky="nsew")
            except Exception:
                tk.Label(frame, text="[Bild saknas]", font=("Arial", 12), bg="#f9f9f9", fg="red").grid(row=0, column=0)

            # Text för djuret
            tk.Label(frame, text=f"Namn: {animal.name}\nArt: {animal.get_species()}",
                     font=("Arial", 12), bg="#f9f9f9", fg="#333333", justify="center").grid(row=1, column=0, pady=5)


class RegisterVisitorPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att registrera en ny besökare."""
        super().__init__(parent, bg="#1A3636")
        self.controller = controller
        self.zoo = zoo

        # Huvudram (center_frame) för innehållet
        center_frame = tk.Frame(self, bg="#D6BD98", bd=2, relief="ridge")
        center_frame.place(relx=0.24, rely=0.14, relwidth=0.5, relheight=0.7)

        # Layout för center_frame
        center_frame.grid_rowconfigure(0, weight=0)  # Rad för tillbaka-knapp
        center_frame.grid_rowconfigure(1, weight=0)  # Rad för titel
        center_frame.grid_rowconfigure(2, weight=0)  # Rad för formulär
        center_frame.grid_rowconfigure(3, weight=0)  # Rad för informationsruta
        center_frame.grid_columnconfigure(0, weight=1)

        # Tillbaka-knapp i övre vänstra hörnet
        back_button = tk.Button(center_frame, text="←", font=("Arial", 24, "bold"),
                                bg="#677D6A", fg="white", width=5, height=1,
                                command=lambda: controller.show_page("StartPage"))
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Titel
        title_label = tk.Label(center_frame, text="Registrera ny besökare", font=("Arial", 18, "bold"),
                               bg="#677D6A", fg="#000000")
        title_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Formulär-container med ram
        form_frame_container = tk.Frame(center_frame, bg="#ffffff", bd=2, relief="ridge")
        form_frame_container.grid(row=2, column=0, padx=20, pady=(10, 5), sticky="n")
        form_frame_container.grid_rowconfigure(0, weight=1)
        form_frame_container.grid_columnconfigure(0, weight=1)

        # Själva formulärramen
        form_frame = tk.Frame(form_frame_container, bg="#f9f9f9")
        form_frame.grid(row=0, column=0, padx=20, pady=(5, 10), sticky="n")

        # Namn-input
        tk.Label(form_frame, text="Ange namn:", font=("Arial", 12, "bold"), bg="#f9f9f9").grid(row=0, column=0, pady=10, padx=10, sticky="e")
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12), bg="#ffffff", fg="#333333", bd=2)
        self.name_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        # Budget-input
        tk.Label(form_frame, text="Ange budget:", font=("Arial", 12, "bold"), bg="#f9f9f9").grid(row=1, column=0, pady=10, padx=10, sticky="e")
        self.budget_entry = tk.Entry(form_frame, font=("Arial", 12), bg="#ffffff", fg="#333333", bd=2)
        self.budget_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        # Registrera-knapp
        register_button = tk.Button(form_frame, text="Registrera", font=("Arial", 14, "bold"),
                                    bg="#677D6A", fg="white", command=self.register_visitor)
        register_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Informationsruta längst ner
        info_section = tk.Frame(center_frame, bg="#e6e6e6", bd=2, relief="ridge")
        info_section.grid(row=3, column=0, padx=10, pady=(4, 10), sticky="n")
        self.message_label = tk.Label(info_section, text="En biljett till djurparken kostar 150 SEK och dras från din budget efter registrering.",
                                      font=("Arial", 15), bg="#e6e6e6", fg="#000000", wraplength=400)
        self.message_label.pack(pady=10)

    def register_visitor(self):
        """Registers a new visitor and resets the form."""
        name = self.name_entry.get().strip()
        budget_text = self.budget_entry.get().strip()

        # Validate input
        if not name or not budget_text.isdigit() or float(budget_text) < 150:
            self.show_message("Skriv in ett godtagbar namn och nummer, du måste sätta in minst 150kr!", error=True)
            return

        # Create and register the visitor
        budget = float(budget_text) - 150
        visitor = Visitor(name, budget)
        result = self.zoo.add_visitor(visitor)

        if "har lagts till" in result:
            # Show success message
            self.show_message(
                f"{name} har blivit registrerat (150 SEK) och har kvar av sin budget: {visitor.budget:.2f} SEK.",
                error=False)

            # Reset the form fields
            self.name_entry.delete(0, tk.END)
            self.budget_entry.delete(0, tk.END)

            # Rensa meddelandet efter 3 sekunder
            self.after(3000, lambda: self.message_label.config(text=""))

            # Navigate to the next page
            addons_page = self.controller.get_page("AddAddonsPage")
            addons_page.set_visitor(visitor)
            self.controller.show_page("AddAddonsPage")
        else:
            self.show_message(result, error=True)

    def show_message(self, text, error=False):
        """Visar ett meddelande i informationsrutan."""
        color = "red" if error else "green"
        self.message_label.config(text=text, fg=color)

        # Hantera synlighet baserat på meddelandets innehåll
        if not text:
            self.message_label.grid_remove()  # Göm rutan om text är tom
        else:
            self.message_label.grid()  # Visa rutan igen om text finns


class AddAddonsPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att lägga till tillval."""
        super().__init__(parent, bg="#1A3636")
        self.controller = controller
        self.zoo = zoo
        self.visitor = None  # Besökaren som läggs till tillval
        self.cart = []  # Kundvagn för valda tillval

        # Huvudram för sidan (centrerad)
        center_frame = tk.Frame(self, bg="#D6BD98", bd=2, relief="ridge")
        center_frame.place(relx=0.24, rely=0.14, relwidth=0.5, relheight=0.7)

        # Konfigurera layout för center_frame
        center_frame.grid_rowconfigure(0, weight=0)  # Tillbaka-knapp
        center_frame.grid_rowconfigure(1, weight=0)  # Titel
        center_frame.grid_rowconfigure(2, weight=0)  # Info-ruta
        center_frame.grid_rowconfigure(3, weight=0)  # Tillval
        center_frame.grid_rowconfigure(4, weight=0)  # Kundvagnstitel
        center_frame.grid_rowconfigure(5, weight=1)  # Kundvagnslista
        center_frame.grid_rowconfigure(6, weight=0)  # Bekräfta-knapp
        center_frame.grid_columnconfigure(0, weight=1)
        center_frame.grid_columnconfigure(1, weight=1)

        # Titel för sidan
        title_label = tk.Label(center_frame, text="Lägg till tillval", font=("Arial", 24, "bold"),
                               bg="#677D6A", fg="#000000")
        title_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Informationsruta (besökarens info och budget)
        self.info_label = tk.Label(center_frame, text="", font=("Arial", 14), bg="#f9f9f9", fg="#333333",
                                   bd=2, relief="ridge", padx=10, pady=5)
        self.info_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        # Ram för tillval (två kolumner)
        self.addons_frame = tk.Frame(center_frame, bg="#ffffff")
        self.addons_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.addons_frame.grid_columnconfigure(0, weight=1)
        self.addons_frame.grid_columnconfigure(1, weight=1)

        # Kundvagnstitel
        cart_label = tk.Label(center_frame, text="Din kundvagn:", font=("Arial", 14, "bold"),
                              bg="#ffffff", fg="#000000")
        cart_label.grid(row=4, column=0, columnspan=2, pady=(2, 0))

        # Lista för att visa valda tillval
        self.cart_listbox = tk.Listbox(center_frame, font=("Arial", 12), bg="#f9f9f9", height=5,
                                       bd=2, relief="ridge")
        self.cart_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 2), sticky="nsew")

        # Bekräfta-knapp längst ner
        confirm_button = tk.Button(center_frame, text="Bekräfta och gå tillbaka till startsidan", bg="#677D6A",
                                   fg="white", font=("Arial", 12, "bold"), command=self.confirm_and_go_back)
        confirm_button.grid(row=6, column=0, columnspan=2, pady=10)

    def set_visitor(self, visitor):
        """Sätter aktuell besökare och uppdaterar sidan."""
        self.visitor = visitor  # Spara besökaren
        self.cart = []  # Töm kundvagnen
        self.cart_listbox.delete(0, tk.END)  # Rensa listan i kundvagnen
        self.info_label.config(text=f"Välkommen {visitor.name}! Din budget är {visitor.budget:.2f} SEK.")
        self.display_addons()  # Visa tillgängliga tillval

    def display_addons(self):
        """Visar tillvalen i två kolumner."""
        for widget in self.addons_frame.winfo_children():
            widget.destroy()  # Rensa tidigare widgets

        row, col = 0, 0  # Startposition för tillvalen
        for addon, price in self.zoo._addons.items():
            # Ram för varje tillval
            frame = tk.Frame(self.addons_frame, bg="#677D6A", bd=1, relief="ridge")
            frame.grid(row=row, column=col, padx=10, pady=5, sticky="nsew")

            # Text för tillval och pris
            tk.Label(frame, text=f"{addon} - {price:.2f} SEK", font=("Arial", 12), bg="#ffffff",
                     fg="#000000").pack(side="left", padx=10, pady=5)

            # Knapp för att lägga till tillval
            tk.Button(frame, text="Lägg till", bg="#1A3636", fg="white", font=("Arial", 10, "bold"),
                      command=lambda a=addon, p=price: self.add_to_cart(a, p)).pack(side="right", padx=10, pady=5)

            # Byt kolumn eller rad
            col += 1
            if col > 1:  # När två kolumner är fyllda, byt rad
                col = 0
                row += 1

    def add_to_cart(self, addon, price):
        """Lägger till tillval i kundvagnen om budgeten räcker."""
        if self.visitor.budget >= price:
            self.visitor.budget -= price  # Minska budget
            self.cart.append((addon, price))  # Lägg till i kundvagnen
            self.cart_listbox.insert(tk.END, f"{addon} - {price:.2f} SEK")
            self.info_label.config(text=f"Välkommen {self.visitor.name}! Din budget är {self.visitor.budget:.2f} SEK.")
        else:
            self.info_label.config(text="Otillräcklig budget för detta tillval!", fg="red")

    def confirm_and_go_back(self):
        """Bekräftar valda tillval och navigerar tillbaka till startsidan."""
        if not self.cart:
            self.info_label.config(text="Inga tillval valdes. Går tillbaka till startsidan...", fg="blue")
        else:
            # Lägg till alla valda tillval i besökarens kundvagn
            for addon, price in self.cart:
                self.visitor.add_to_cart(addon, price)
            self.info_label.config(text="Tillvalen har bekräftats! Går tillbaka till startsidan...", fg="green")
        self.after(1000, lambda: self.controller.show_page("StartPage"))



class ManageVisitorsPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att hantera besökare."""
        super().__init__(parent, bg="#1A3636")
        self.controller = controller
        self.zoo = zoo

        # Variabel för markerad besökare
        self.selected_visitor = tk.StringVar()

        # Huvudram för sidan (centrerad)
        center_frame = tk.Frame(self, bg="#D6BD98", bd=2, relief="ridge")
        center_frame.place(relx=0.24, rely=0.14, relwidth=0.5, relheight=0.7)

        # Layout för center_frame
        center_frame.grid_rowconfigure(0, weight=0)  # Tillbaka-knapp
        center_frame.grid_rowconfigure(1, weight=0)  # Titel
        center_frame.grid_rowconfigure(2, weight=1)  # Listbox (expanderbar)
        center_frame.grid_rowconfigure(3, weight=0)  # Ta bort-knapp
        center_frame.grid_columnconfigure(0, weight=1)

        # Tillbaka-knapp (vänstra hörnet)
        back_button = tk.Button(center_frame, text="←", font=("Arial", 24, "bold"),
                                bg="#677D6A", fg="white", width=5, height=1,
                                command=lambda: controller.show_page("StartPage"))
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Titel för sidan
        title_label = tk.Label(center_frame, text="Hantera besökare", font=("Arial", 24, "bold"),
                               bg="#677D6A", fg="#000000")
        title_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Ram för listbox med scrollbar
        visitor_frame = tk.Frame(center_frame, bg="#f9f9f9", bd=2, relief="ridge")
        visitor_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Listbox för att visa besökare
        self.visitor_listbox = tk.Listbox(visitor_frame, font=("Arial", 14), bg="#ffffff",
                                          fg="#000000", selectbackground="#ff4d4d", height=12)
        self.visitor_listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Scrollbar kopplad till listbox
        scrollbar = tk.Scrollbar(visitor_frame, command=self.visitor_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.visitor_listbox.config(yscrollcommand=scrollbar.set)

        # Ta bort-knapp
        remove_button = tk.Button(center_frame, text="Ta bort markerad besökare", font=("Arial", 12, "bold"),
                                  bg="#677D6A", fg="white", activebackground="#e63939",
                                  command=self.remove_selected_visitor)
        remove_button.grid(row=3, column=0, pady=10)

        # Uppdatera listan med besökare
        self.update_visitor_list()

    def update_visitor_list(self):
        """Uppdaterar listan över registrerade besökare."""
        self.visitor_listbox.delete(0, tk.END)  # Rensar listan
        visitors = self.zoo.list_visitors()  # Hämtar besökarlistan
        for visitor in visitors:
            if visitor.strip():  # Lägg endast till icke-tomma strängar
                self.visitor_listbox.insert(tk.END, visitor)

    def remove_selected_visitor(self):
        """Tar bort markerad besökare från listan."""
        # Kontrollera om en besökare är markerad
        selected_index = self.visitor_listbox.curselection()
        if selected_index:
            # Hämta besökarens namn
            visitor_name = self.visitor_listbox.get(selected_index).split(" - ")[0]
            result = self.zoo.remove_visitor(visitor_name)

            # Visa resultat och uppdatera listan
            if "har tagits bort" in result:
                self.update_visitor_list()
                messagebox.showinfo("Besökare borttagen", result)
            else:
                messagebox.showwarning("Fel", result)
        else:
            messagebox.showwarning("Ingen markerad", "Vänligen markera en besökare att ta bort.")

class SelectVisitorPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att välja en besökare."""
        super().__init__(parent, bg="#1A3636")
        self.controller = controller
        self.zoo = zoo

        # Gör sidan flexibel
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

        # Huvudram (center_frame)
        center_frame = tk.Frame(self, bg="#D6BD98", bd=2, relief="ridge")
        center_frame.place(relx=0.24, rely=0.14, relwidth=0.5, relheight=0.7)

        # Layout för center_frame
        center_frame.grid_rowconfigure(0, weight=0)  # Tillbaka-knappen
        center_frame.grid_rowconfigure(1, weight=0)  # Titel
        center_frame.grid_rowconfigure(2, weight=1)  # Knapp-rad
        center_frame.grid_columnconfigure(0, weight=1)
        center_frame.grid_columnconfigure(1, weight=1)

        # Tillbaka-knapp
        back_button = tk.Button(center_frame, text="←", font=("Arial", 24, "bold"),
                                bg="#677D6A", fg="white", width=5, height=1,
                                command=lambda: controller.show_page("StartPage"))
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Titel
        title_label = tk.Label(center_frame, text="Välj en besökare att logga in som:",
                               font=("Arial", 24, "bold"), bg="#677D6A", fg="#000000")
        title_label.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

        # Ram för knappar
        self.visitor_buttons_frame = tk.Frame(center_frame, bg="#ffffff")
        self.visitor_buttons_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

        # Info-meddelande
        self.message_label = tk.Label(center_frame, text="", font=("Arial", 14), bg="#D6BD98", fg="red")
        self.message_label.grid(row=3, column=0, columnspan=2, pady=5)

    def update_visitors(self):
        """Uppdaterar besökarlistan och skapar knappar."""
        # Rensa tidigare knappar
        for widget in self.visitor_buttons_frame.winfo_children():
            widget.destroy()

        # Skapa nya knappar i två kolumner
        for index, visitor in enumerate(self.zoo._visitors):
            name = visitor.name
            addons = ", ".join(item[0] for item in visitor.cart) if visitor.cart else "Inga tillval"
            button_text = f"{name}\nTillval: {addons}"

            col = index % 2  # Växla mellan kolumn 0 och 1
            row = index // 2  # Öka radnummer efter två kolumner

            # Skapa knappen med korrekt lambda-bindning
            button = tk.Button(self.visitor_buttons_frame, text=button_text,
                               font=("Arial", 14), bg="#677D6A", fg="#000000",
                               activebackground="#4CAF50", height=3, width=20,
                               command=lambda v=visitor: self.select_visitor(v))
            button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Flexibel layout för knappar
        self.visitor_buttons_frame.grid_columnconfigure(0, weight=1)
        self.visitor_buttons_frame.grid_columnconfigure(1, weight=1)

    def select_visitor(self, visitor):
        """Loggar in vald besökare och navigerar till Utforska-sidan."""
        self.controller.frames["ExploreParkPage"].set_visitor(visitor)
        self.controller.show_page("ExploreParkPage")



class ExploreParkPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att utforska djurparken."""
        super().__init__(parent, bg="#1A3636")
        self.controller = controller
        self.zoo = zoo
        self.visitor = None  # Aktuell besökare

        # Layoutkonfiguration för sidan
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Huvudram (center_frame) för innehållet
        center_frame = tk.Frame(self, bg="#D6BD98", bd=2, relief="ridge")
        center_frame.place(relx=0.24, rely=0.14, relwidth=0.5, relheight=0.7)

        # Layoutkonfiguration för center_frame
        center_frame.grid_rowconfigure(0, weight=0)  # Rad för tillbaka-knappen
        center_frame.grid_rowconfigure(1, weight=0)  # Titelrad
        center_frame.grid_rowconfigure(2, weight=1)  # Ram för knappar
        center_frame.grid_columnconfigure(0, weight=1)

        # Tillbaka-knapp i vänstra hörnet
        back_button = tk.Button(center_frame, text="←", font=("Arial", 24, "bold"),
                                bg="#677D6A", fg="white", width=5, height=1,
                                command=lambda: controller.show_page("SelectVisitorPage"))
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Titel för sidan
        self.title_label = tk.Label(center_frame, text="Utforska djurparken",
                                    font=("Arial", 20, "bold"), bg="#677D6A", fg="#000000")
        self.title_label.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

        # Ram för navigationsknappar
        button_frame = tk.Frame(center_frame, bg="#f9f9f9")
        button_frame.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")

        # Definiera knappar och deras kommandon
        buttons = [
            ("Sök efter ett djur", lambda: controller.show_page("SearchAnimalPage")),
            ("Interagera med ett djur (kräver tillval)", self.go_to_interact_page),
            ("Mata ett djur (kräver tillval)", self.go_to_feed_page),
            ("Visa detaljerad information om djur", self.go_to_detailed_page)
        ]

        # Skapa och placera knappar
        for index, (text, command) in enumerate(buttons):
            btn = tk.Button(button_frame, text=text, font=("Arial", 14),
                            bg="#677D6A", fg="#000000", activebackground="#4CAF50",
                            command=command)
            btn.grid(row=index, column=0, pady=10, padx=10, sticky="nsew")

        # Gör knapparna flexibla i layouten
        button_frame.grid_rowconfigure(tuple(range(len(buttons))), weight=1)
        button_frame.grid_columnconfigure(0, weight=1)

        # Knappar som ska uppdateras i update_button_states
        self.interact_button = tk.Button(button_frame, text="Interagera med ett djur (kräver tillval)",
                                         font=("Arial", 14),
                                         bg="#677D6A", fg="#000",  # Standardfärg (grå-grön)
                                         activebackground="#4CAF50",  # Grön färg vid klick
                                         activeforeground="white",  # Vit text vid klick
                                         command=self.go_to_interact_page)
        self.interact_button.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

        self.feed_button = tk.Button(button_frame, text="Mata ett djur (kräver tillval)",
                                     font=("Arial", 14),
                                     bg="#677D6A", fg="#000000",  # Standardfärg (grå-grön)
                                     activebackground="#4CAF50",  # Grön färg vid klick
                                     activeforeground="white",  # Vit text vid klick
                                     command=self.go_to_feed_page)
        self.feed_button.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

    def set_visitor(self, visitor):
        """Uppdaterar sidan med besökarens namn och knapparnas tillgänglighet."""
        self.visitor = visitor
        self.title_label.config(text=f"Utforska djurparken - {visitor.name}")
        self.update_button_states()

    def update_button_states(self):
        """Aktiverar/inaktiverar knappar baserat på besökarens tillval."""
        if not self.visitor:
            return
        cart = [item[0] for item in self.visitor.cart]
        # Aktivera/inaktivera knappar beroende på tillval
        self.interact_button.config(state=tk.NORMAL if "Interagera med djur" in cart else tk.DISABLED)
        self.feed_button.config(state=tk.NORMAL if "Mata djur" in cart else tk.DISABLED)

    def go_to_interact_page(self):
        """Navigerar till sidan för att interagera med djur."""
        if "Interagera med djur" in [item[0] for item in self.visitor.cart]:
            self.controller.show_page("InteractAnimalPage")
        else:
            messagebox.showwarning("Tillval saknas", "Du har inte köpt tillvalet för att interagera med djur.")

    def go_to_feed_page(self):
        """Navigerar till sidan för att mata djur."""
        if "Mata djur" in [item[0] for item in self.visitor.cart]:
            self.controller.show_page("FeedAnimalPage")
        else:
            messagebox.showwarning("Tillval saknas", "Du har inte köpt tillvalet för att mata djur.")

    def go_to_detailed_page(self):
        """Navigerar till sidan med detaljerad information om djur."""
        self.controller.show_page("DetailedAnimalPage")



class DetailedAnimalPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för detaljerad information om djur."""
        super().__init__(parent, bg="#1A3636")  # Bakgrundsfärg
        self.controller = controller
        self.zoo = zoo

        # Huvudram för allt innehåll (centrerad och bredare)
        center_frame = tk.Frame(self, bg="#D6BD98", bd=2, relief="ridge")
        center_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

        # Tillbaka-knapp i övre vänstra hörnet
        back_button = tk.Button(center_frame, text="←", font=("Arial", 24, "bold"),
                                bg="#677D6A", fg="white", width=5, height=1,
                                command=lambda: controller.show_page("ExploreParkPage"))
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Titel för sidan
        tk.Label(center_frame, text="Detaljerad info om djur", font=("Arial", 20, "bold"),
                 bg="#677D6A", fg="#000000").grid(row=1, column=0, pady=20, sticky="n")

        # Skapa en Canvas med scrollbar
        canvas = tk.Canvas(center_frame, bg="#f9f9f9")
        scrollbar = tk.Scrollbar(center_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg="#f9f9f9")

        # Koppla scrollfunktion
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Placera canvas och scrollbar i center_frame
        canvas.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)
        scrollbar.grid(row=2, column=1, sticky="ns")

        # Anpassa center_frame för att tillåta expandering
        center_frame.grid_rowconfigure(2, weight=1)
        center_frame.grid_columnconfigure(0, weight=1)

        # Visa djurdetaljer
        self.display_animals()

    def display_animals(self):
        """Visar alla djur i en detaljerad vy."""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()  # Rensa tidigare widgets

        for index, animal in enumerate(self.zoo.list_animals()):
            animal_frame = tk.Frame(self.scrollable_frame, bg="#ffffff", bd=4, relief="groove")
            animal_frame.pack(pady=20, padx=20, fill="x")

            # Bild
            try:
                img = Image.open(animal.image_path).resize((200, 200), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                tk.Label(animal_frame, image=photo, bg="#ffffff").grid(row=0, column=0, padx=20, pady=10)
                animal_frame.image = photo  # Håll referens
            except:
                tk.Label(animal_frame, text="[Bild saknas]", font=("Arial", 14, "italic"),
                         bg="#ffffff", fg="red").grid(row=0, column=0, padx=20, pady=10)

            # Djurets detaljer
            info_text = (f"Art: {animal.get_species()}\n"
                         f"Namn: {animal.name}\n"
                         f"Ålder: {animal.age} år\n"
                         f"Favoritmat: {animal.favorite_food}\n"
                         f"Hungerstatus: {'Hungrig' if animal.hungry else 'Mätt'}")
            tk.Label(animal_frame, text=info_text, font=("Arial", 14, "bold"), bg="#ffffff",
                     anchor="w", justify="left").grid(row=0, column=1, padx=20, pady=10, sticky="w")




class SearchAnimalPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att söka efter djur."""
        super().__init__(parent, bg="#1A3636")
        self.controller = controller
        self.zoo = zoo

        # Huvudram för innehåll
        center_frame = tk.Frame(self, bg="#D6BD98", bd=2, relief="ridge")
        center_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.8)

        # Tillbaka-knapp i övre vänstra hörnet
        back_button = tk.Button(center_frame, text="←", font=("Arial", 24, "bold"),
                                bg="#677D6A", fg="white", width=5, height=1,
                                command=lambda: controller.show_page("ExploreParkPage"))
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Titel
        tk.Label(center_frame, text="Sök efter djur", font=("Arial", 24, "bold"),
                 bg="#677D6A", fg="#000000").grid(row=1, column=0, pady=20, sticky="n")

        # Sökfält
        search_frame = tk.Frame(center_frame, bg="#D6BD98")
        search_frame.grid(row=2, column=0, pady=10)
        tk.Label(search_frame, text="Ange djurets namn:", font=("Arial", 14, "bold"),
                 bg="#D6BD98").grid(row=0, column=0, padx=5, pady=10)
        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=20)
        self.search_entry.grid(row=0, column=1, padx=5)
        tk.Button(search_frame, text="Sök", font=("Arial", 12, "bold"), bg="#1A3636", fg="#ffffff",
                  command=self.search_animal).grid(row=0, column=2, padx=5)

        # Resultatram
        self.result_frame = tk.Frame(center_frame, bg="#f9f9f9", bd=2, relief="ridge")
        self.result_frame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")

        # Justera center_frame layout
        center_frame.grid_rowconfigure(3, weight=1)
        center_frame.grid_columnconfigure(0, weight=1)

    def search_animal(self):
        """Söker efter djuret och visar detaljerad information med större bild."""
        search_name = self.search_entry.get().strip().lower()

        # Rensa tidigare resultat
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        # Visa djurets detaljer
        for animal in self.zoo.list_animals():
            if animal.name.lower() == search_name:
                # Större ram för djuret
                animal_frame = tk.Frame(self.result_frame, bg="#ffffff", bd=6, relief="ridge")
                animal_frame.pack(pady=20, padx=20, fill="both", expand=True)

                # Större bild
                try:
                    img = Image.open(animal.image_path).resize((300, 300), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    tk.Label(animal_frame, image=photo, bg="#ffffff").grid(row=0, column=0, rowspan=2, padx=20, pady=20)
                    animal_frame.image = photo  # Håll referens
                except:
                    tk.Label(animal_frame, text="[Bild saknas]", font=("Arial", 18, "italic"),
                             bg="#ffffff", fg="red").grid(row=0, column=0, rowspan=2, padx=20, pady=20)

                # Information i större text
                info_text = (f"Art: {animal.get_species()}\n"
                             f"Namn: {animal.name}\n"
                             f"Ålder: {animal.age} år\n"
                             f"Favoritmat: {animal.favorite_food}")
                tk.Label(animal_frame, text=info_text, font=("Arial", 16, "bold"), bg="#ffffff",
                         fg="#333333", anchor="w", justify="left").grid(row=0, column=1, padx=20, pady=20, sticky="w")
                return

        # Om djuret inte hittas
        tk.Label(self.result_frame, text="Inget djur med det namnet hittades.",
                 font=("Arial", 14, "italic"), bg="#f9f9f9", fg="red").pack(padx=10, pady=10)


class InteractAnimalPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att interagera med djur."""
        super().__init__(parent, bg="#1A3636")
        self.controller = controller
        self.zoo = zoo
        self.selected_animal = None

        # Back button
        tk.Button(self, text="←", font=("Arial", 18, "bold"), bg="#677D6A", fg="white",
                  command=lambda: controller.show_page("ExploreParkPage")).place(relx=0.05, rely=0.05, width=50, height=50)

        # Title
        tk.Label(self, text="Interagera med djur", font=("Arial", 20, "bold"),
                 bg="#D6BD98", fg="black").place(relx=0.5, rely=0.1, anchor="center")

        # Search Frame
        search_frame = tk.Frame(self, bg="#D6BD98")
        search_frame.place(relx=0.5, rely=0.18, anchor="center")
        tk.Label(search_frame, text="Ange djurets namn:", font=("Arial", 14), bg="#D6BD98").pack(side="left")
        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=20)
        self.search_entry.pack(side="left", padx=5)
        tk.Button(search_frame, text="Sök", font=("Arial", 12), bg="#677D6A", fg="white",
                  command=self.search_animal).pack(side="left")

        # Result Frame
        self.result_frame = tk.Frame(self, bg="white", bd=2, relief="groove")
        self.result_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.7, relheight=0.5)

        # Interact Button
        self.interact_button = tk.Button(self, text="Interagera", font=("Arial", 14, "bold"),
                                         bg="#677D6A", fg="white", state="disabled",
                                         command=self.interact_with_animal)
        self.interact_button.place(relx=0.5, rely=0.82, anchor="center", width=120)

    def search_animal(self):
        """Söker efter djuret och uppdaterar resultatfältet."""
        animal_name = self.search_entry.get().strip()
        self.selected_animal = next((a for a in self.zoo.list_animals() if a.name.lower() == animal_name.lower()), None)

        # Clear previous results
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        if self.selected_animal:
            # Display Image
            try:
                img = Image.open(self.selected_animal.image_path).resize((200, 200), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(self.result_frame, image=photo, bg="white")
                img_label.image = photo  # Keep reference
                img_label.pack(side="left", padx=10)
            except:
                tk.Label(self.result_frame, text="[Bild saknas]", bg="white", font=("Arial", 12)).pack(side="left", padx=10)

            # Display Animal Info
            info_text = (f"Art: {type(self.selected_animal).__name__}\n"
                         f"Namn: {self.selected_animal.name}\n"
                         f"Ålder: {self.selected_animal.age} år\n"
                         f"Favoritmat: {self.selected_animal.favorite_food}")
            tk.Label(self.result_frame, text=info_text, font=("Arial", 12), bg="white", anchor="w", justify="left").pack(side="left", padx=10)
            self.interact_button.config(state="normal")
        else:
            tk.Label(self.result_frame, text="Inget djur hittades.", font=("Arial", 12, "italic"),
                     fg="red", bg="white").pack()
            self.interact_button.config(state="disabled")

    def interact_with_animal(self):
        """Interagerar med djuret och visar resultat."""
        if self.selected_animal:
            result = self.selected_animal.interact()
            messagebox.showinfo("Interaktionsresultat", result)
            self.interact_button.config(state="disabled")




class FeedAnimalPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initializes the 'Feed an Animal' page."""
        super().__init__(parent, bg="#1A3636")
        self.controller = controller
        self.zoo = zoo
        self.selected_animal = None

        # Back button
        tk.Button(self, text="←", font=("Arial", 18, "bold"), bg="#677D6A", fg="white",
                  command=lambda: controller.show_page("ExploreParkPage")).place(relx=0.05, rely=0.05, width=50, height=50)

        # Title
        tk.Label(self, text="Mata ett djur", font=("Arial", 20, "bold"), bg="#D6BD98", fg="black").place(relx=0.5, rely=0.1, anchor="center")

        # Search Frame
        search_frame = tk.Frame(self, bg="#D6BD98")
        search_frame.place(relx=0.5, rely=0.18, anchor="center")

        tk.Label(search_frame, text="Ange djurets namn:", font=("Arial", 14), bg="#D6BD98").pack(side="left")
        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=20)
        self.search_entry.pack(side="left", padx=5)
        tk.Button(search_frame, text="Sök", font=("Arial", 12), bg="#677D6A", fg="white",
                  command=self.search_animal).pack(side="left")

        # Result Frame
        self.result_frame = tk.Frame(self, bg="white", bd=2, relief="groove")
        self.result_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.7, relheight=0.5)

        # Feed Button
        self.feed_button = tk.Button(self, text="Mata", font=("Arial", 14, "bold"), bg="#677D6A",
                                     fg="white", state="disabled", command=self.feed_animal)
        self.feed_button.place(relx=0.5, rely=0.82, anchor="center", width=100)

    def search_animal(self):
        """Searches for the animal by name and updates the result frame."""
        animal_name = self.search_entry.get().strip()
        self.selected_animal = next((a for a in self.zoo.list_animals() if a.name.lower() == animal_name.lower()), None)

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        if self.selected_animal:
            # Display Image
            try:
                img = Image.open(self.selected_animal.image_path).resize((200, 200), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(self.result_frame, image=photo, bg="white")
                img_label.image = photo  # Keep reference
                img_label.pack(side="left", padx=10)
            except:
                tk.Label(self.result_frame, text="[Bild saknas]", bg="white", font=("Arial", 12)).pack(side="left", padx=10)

            # Display Animal Info
            info_text = (f"Art: {type(self.selected_animal).__name__}\n"
                         f"Namn: {self.selected_animal.name}\n"
                         f"Ålder: {self.selected_animal.age} år\n"
                         f"Favoritmat: {self.selected_animal.favorite_food}")
            tk.Label(self.result_frame, text=info_text, font=("Arial", 12), bg="white", anchor="w", justify="left").pack(side="left", padx=10)
            self.feed_button.config(state="normal")
        else:
            tk.Label(self.result_frame, text="Inget djur hittades.", font=("Arial", 12, "italic"), fg="red", bg="white").pack()

    def feed_animal(self):
        """Feeds the animal and shows the result."""
        if self.selected_animal:
            result = self.selected_animal.eat(self.selected_animal.favorite_food)
            messagebox.showinfo("Matningsresultat", result)
            self.feed_button.config(state="disabled")