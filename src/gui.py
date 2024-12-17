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
        super().__init__()
        self.zoo = zoo
        self.title("Djurparken")
        self.geometry("800x600")
        self.frames = {}


        # Container för alla sidor
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")  # Ändra från pack till grid

        # Gör att container expanderar
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Öppna i fullskärm
        self.state('zoomed')


        # Lägg till sidor
        for Page in (StartPage, RegisterVisitorPage, ManageVisitorsPage, ZooInfoPage, AddAddonsPage, SelectVisitorPage, ExploreParkPage, DetailedAnimalPage, SearchAnimalPage, InteractAnimalPage, FeedAnimalPage):
            page_name = Page.__name__
            frame = Page(parent=container, controller=self, zoo=self.zoo)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_page("StartPage")

    def get_page(self, page_name):
        return self.frames[page_name]

    def show_page(self, page_name):
        """Visa en specifik sida och uppdatera innehåll vid behov."""
        frame = self.frames[page_name]

        if page_name == "ManageVisitorsPage":
            frame.update_visitor_list()  # Uppdatera listan med besökare
        elif page_name == "SelectVisitorPage":
            frame.update_visitors()  # Uppdatera besökarknappar
        frame.tkraise()


# Klass för Startsida
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
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Huvudinnehåll i mitten
        content_frame = tk.Frame(self, bg="lightblue")
        content_frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        # Titel för startsidan
        tk.Label(content_frame, text="Välkommen till Eggis Zoo", font=("Arial", 24, "bold"), bg="#1A3636").pack(pady=20)

        # Bildruta med bild från assets/images/bild.png
        image_frame = tk.Frame(content_frame, bg="white", relief="ridge", bd=3)
        image_frame.pack(pady=10)

        try:
            image_path = "../assets/images/bridge.jpg"  # bild sökväg
            image = Image.open(image_path)
            image = image.resize((500, 150))  # Anpassa bildens storlek
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(image_frame, image=photo, bg="white")
            image_label.image = photo  # Håll en referens för att undvika att bilden försvinner
            image_label.pack()
        except Exception as e:
            tk.Label(image_frame, text="Bild kunde inte laddas", bg="lightcoral", font=("Arial", 14)).pack(expand=True)
            print(f"Fel: {e}")

        # Menyram för knappar
        menu_frame = tk.Frame(content_frame, bg="lightgray", relief="groove", bd=5, padx=10, pady=10)
        menu_frame.pack(pady=20)

        # Knappar i grid-layout med 2 knappar per rad
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
            tk.Button(menu_frame, text=text, font=("Arial", 14, "bold"), bg="red", fg="white", width=20, height=2,
                      command=cmd).grid(row=row, column=col, padx=10, pady=10)

        # Sidfot med info
        footer_label = tk.Label(self, text="Sidfot med info", bg="lightgray", font=("Arial", 12))
        footer_label.grid(row=2, column=0, columnspan=3, sticky="ew")





class RegisterVisitorPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att registrera en ny besökare."""
        super().__init__(parent, bg="#ffffff")  # Vit bakgrundsfärg
        self.controller = controller
        self.zoo = zoo

        # Tillbaka-knapp
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939", command=lambda: controller.show_page("StartPage"))
        back_button.place(x=10, y=10)

        # Titel
        title_label = tk.Label(self, text="Registrera ny besökare", font=("Arial", 26, "bold"),
                               bg="#ffffff", fg="#b30000")
        title_label.pack(pady=20)

        # Ram för inmatningsfält
        input_frame = tk.Frame(self, bg="#f9f9f9", bd=2, relief="ridge")  # Ljusgrå bakgrund
        input_frame.pack(pady=20, padx=20)

        # Namn-input
        tk.Label(input_frame, text="Ange namn:", font=("Arial", 12, "bold"), bg="#f9f9f9", fg="#333333").grid(
            row=0, column=0, pady=10, padx=10)
        self.name_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#ffffff", fg="#333333",
                                   bd=2, relief="solid", insertbackground="#333333")
        self.name_entry.grid(row=0, column=1, pady=10, padx=10)

        # Budget-input
        tk.Label(input_frame, text="Ange budget:", font=("Arial", 12, "bold"), bg="#f9f9f9", fg="#333333").grid(
            row=1, column=0, pady=10, padx=10)
        self.budget_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#ffffff", fg="#333333",
                                     bd=2, relief="solid", insertbackground="#333333")
        self.budget_entry.grid(row=1, column=1, pady=10, padx=10)

        # Registrera-knapp
        register_button = tk.Button(self, text="Registrera", font=("Arial", 14, "bold"), bg="#ff4d4d",
                                    fg="white", activebackground="#e63939", activeforeground="white",
                                    bd=2, relief="raised", command=self.register_visitor)
        register_button.pack(pady=20)

        # Meddelanderuta för att visa feedback
        self.message_label = tk.Label(self, text="", font=("Arial", 14), bg="#ffffff", fg="green")
        self.message_label.pack(pady=10)

        # Informationsetikett för biljettkostnad
        ticket_info_label = tk.Label(self, text="En biljett till djurparken kostar 150 SEK och dras från din budget.",
                                     font=("Arial", 12), bg="#ffffff", fg="#b30000")
        ticket_info_label.pack(pady=(5, 0))  # Liten padding ovanför

    def register_visitor(self):
        """Registrerar en ny besökare och visar bekräftelse."""
        name = self.name_entry.get()
        budget_text = self.budget_entry.get()

        # Validera inmatning
        if not name or not budget_text.isdigit() or float(budget_text) < 150:
            self.show_message("Ange ett giltigt namn och budget (minst 150 SEK)!", error=True)
            return

        # Dra av biljettkostnaden (150 SEK)
        budget = float(budget_text) - 150

        # Skapa besökare
        visitor = Visitor(name, budget)
        result = self.zoo.add_visitor(visitor)

        if "har lagts till" in result:
            # Visa bekräftelsemeddelande
            self.show_message(f"{name} har registrerats med biljett (150 SEK) och budget {visitor.budget:.2f} SEK.",
                              error=False)

            # Rensa inmatningsfälten, men lämna meddelandet kvar
            self.reset_fields(keep_message=True)

            # Gå automatiskt till tillvalsidan efter 2 sekunder
            self.after(2000, lambda: self.next_page(visitor))
        else:
            self.show_message(result, error=True)  # Felmeddelande vid maxgräns

    def reset_fields(self, keep_message=False):
        """Nollställer alla inmatningsfält och meddelanderuta om inte annat anges."""
        self.name_entry.delete(0, tk.END)
        self.budget_entry.delete(0, tk.END)
        if not keep_message:
            self.message_label.config(text="")

    def show_message(self, text, error=False):
        """Visar ett meddelande på sidan."""
        color = "red" if error else "green"
        self.message_label.config(text=text, fg=color)

    def next_page(self, visitor):
        """Navigerar till AddAddonsPage och sätter aktuell besökare."""
        addons_page = self.controller.get_page("AddAddonsPage")
        addons_page.set_visitor(visitor)
        self.controller.show_page("AddAddonsPage")



class ManageVisitorsPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att hantera besökare."""
        super().__init__(parent, bg="#ffffff")  # Vit bakgrund
        self.controller = controller
        self.zoo = zoo
        self.selected_visitor = tk.StringVar()  # För att hålla markerad besökare

        # Tillbaka-knapp
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939",
                                command=lambda: controller.show_page("StartPage"))
        back_button.place(x=10, y=10)

        # Titel
        title_label = tk.Label(self, text="Hantera Besökare", font=("Arial", 26, "bold"),
                               bg="#ffffff", fg="#b30000")
        title_label.pack(pady=20)

        # Ram för besökarlista
        list_frame = tk.Frame(self, bg="#f9f9f9", bd=2, relief="ridge")
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Listbox för att visa besökare
        self.visitor_listbox = tk.Listbox(list_frame, font=("Arial", 12), bg="#ffffff", fg="#333333",
                                          selectbackground="#ff4d4d", selectforeground="white",
                                          bd=0, relief="flat", height=15)
        self.visitor_listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Scrollbar kopplad till listbox
        scrollbar = tk.Scrollbar(list_frame, command=self.visitor_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.visitor_listbox.config(yscrollcommand=scrollbar.set)

        # Ta bort-knapp
        remove_button = tk.Button(self, text="Ta bort markerad besökare", font=("Arial", 12, "bold"),
                                  bg="#ff4d4d", fg="white", activebackground="#e63939",
                                  command=self.remove_selected_visitor)
        remove_button.pack(pady=10)

        # Uppdatera listan med besökare
        self.update_visitor_list()

    def update_visitor_list(self):
        """Uppdaterar listan över registrerade besökare."""
        self.visitor_listbox.delete(0, tk.END)  # Rensa listan först

        # Hämta besökare som en lista
        visitors = self.zoo.list_visitors()  # Returnerar redan en lista av strängar
        for visitor in visitors:
            if visitor.strip():  # Kontrollera att strängen inte är tom
                self.visitor_listbox.insert(tk.END, visitor)

    def remove_selected_visitor(self):
        """Tar bort markerad besökare."""
        selected_index = self.visitor_listbox.curselection()
        if selected_index:
            visitor_name = self.visitor_listbox.get(selected_index).split(" - ")[0]
            result = self.zoo.remove_visitor(visitor_name)  # Använder remove_visitor() för att ta bort besökaren

            if "har tagits bort" in result:  # Kontrollera om borttagning lyckades
                self.update_visitor_list()
                messagebox.showinfo("Besökare borttagen", result)
            else:
                messagebox.showwarning("Fel", result)
        else:
            messagebox.showwarning("Ingen markerad", "Vänligen markera en besökare att ta bort.")


class AddAddonsPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att lägga till tillval."""
        super().__init__(parent, bg="#ffffff")  # Vit bakgrund
        self.controller = controller
        self.zoo = zoo
        self.visitor = None  # Håller den aktuella besökaren
        self.cart = []  # Kundvagn för valda tillval

        # Tillbaka-knapp
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939",
                                command=lambda: controller.show_page("StartPage"))
        back_button.place(x=10, y=10)

        # Titel
        title_label = tk.Label(self, text="Lägg till tillval", font=("Arial", 26, "bold"),
                               bg="#ffffff", fg="#b30000")
        title_label.pack(pady=20)

        # Info-ruta
        self.info_label = tk.Label(self, text="", font=("Arial", 14), bg="#f9f9f9", fg="#333333",
                                   bd=2, relief="ridge", padx=10, pady=5)
        self.info_label.pack(pady=10, padx=20)

        # Ram för tillval
        self.addons_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="flat")
        self.addons_frame.pack(pady=10, padx=20, fill="x", expand=True)

        # Kundvagn för att visa valda tillval
        cart_label = tk.Label(self, text="Din kundvagn:", font=("Arial", 14, "bold"), bg="#ffffff", fg="#b30000")
        cart_label.pack(pady=10)
        self.cart_listbox = tk.Listbox(self, font=("Arial", 12), bg="#f9f9f9", height=5, width=50)
        self.cart_listbox.pack(pady=10)

        # Bekräfta-knapp längst ner
        confirm_button = tk.Button(self, text="Bekräfta och gå tillbaka till startsidan", bg="#ff4d4d",
                                   fg="white", font=("Arial", 12, "bold"),
                                   activebackground="#e63939",
                                   command=self.confirm_and_go_back)
        confirm_button.pack(pady=20)

    def set_visitor(self, visitor):
        """Sätter aktuell besökare och uppdaterar sidan."""
        print("set_visitor anropades!")  # Lägg till denna för att se om den körs
        self.visitor = visitor
        self.cart = []  # Töm kundvagnen
        self.cart_listbox.delete(0, tk.END)  # Rensa
        print(f"Tillval: {self.zoo._addons}")  # Debug: Skriv ut tillval
        self.info_label.config(text=f"Välkommen {visitor.name}! Din budget är {visitor.budget:.2f} SEK.")
        self.display_addons()

    def display_addons(self):
        """Visar alla tillval som knappar."""
        # Kontrollera om addons finns
        if not self.zoo._addons:
            self.info_label.config(text="Inga tillval tillgängliga!", fg="red")
            return

        # Rensa gamla widgets
        for widget in self.addons_frame.winfo_children():
            widget.destroy()

        # Skapa knappar för tillval
        for addon, price in self.zoo._addons.items():
            addon_frame = tk.Frame(self.addons_frame, bg="#ffcccc", bd=1, relief="ridge")
            addon_frame.pack(fill="x", pady=5, padx=5)

            # Label som visar tillvalets namn och pris
            addon_label = tk.Label(addon_frame, text=f"{addon} - {price:.2f} SEK",
                                   font=("Arial", 12), bg="#ffcccc", fg="#b30000")
            addon_label.pack(side="left", padx=10, pady=5)

            # Knappar för att lägga till tillval i kundvagnen
            buy_button = tk.Button(addon_frame, text="Lägg till", bg="#ff4d4d", fg="white",
                                   activebackground="#e63939",
                                   font=("Arial", 10, "bold"),
                                   command=lambda a=addon, p=price: self.add_to_cart(a, p))
            buy_button.pack(side="right", padx=10, pady=5)

    def add_to_cart(self, addon, price):
        """Lägger till tillval i kundvagnen och visar uppdaterad info."""
        if self.visitor.budget >= price:
            self.visitor.budget -= price  # Dra av priset från budgeten
            self.cart.append((addon, price))  # Lägg till i kundvagnen
            self.cart_listbox.insert(tk.END, f"{addon} - {price:.2f} SEK")  # Visa i kundvagnslistan
            self.info_label.config(text=f"Välkommen {self.visitor.name}! Din budget är {self.visitor.budget:.2f} SEK.")
        else:
            self.info_label.config(text="Otillräcklig budget för detta tillval!", fg="red")

    def confirm_and_go_back(self):
        """Bekräftar kundvagnens innehåll och navigerar tillbaka till startsidan."""
        if not self.cart:
            # Informera att inga tillval valdes, men gå ändå tillbaka
            self.info_label.config(text="Inga tillval valdes. Går tillbaka till startsidan...", fg="blue")
        else:
            # Lägg till valda tillval i besökarens kundvagn
            for addon, price in self.cart:
                self.visitor.add_to_cart(addon, price)  # Använd visitor-metoden för att hantera tillval
            self.info_label.config(text="Tillvalen har bekräftats! Går tillbaka till startsidan...", fg="green")

        # Vänta 2 sekunder och gå tillbaka till startsidan
        self.after(2000, lambda: self.controller.show_page("StartPage"))


class ZooInfoPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        super().__init__(parent, bg="#ffe6e6")
        self.controller = controller
        self.zoo = zoo

        # Centrera huvudlayout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Tillbaka-knapp
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939",
                                command=lambda: controller.show_page("StartPage"))
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Huvudram i mitten
        center_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="ridge", width=1200, height=600)
        center_frame.grid(row=1, column=1, padx=40, pady=20, sticky="nsew")
        center_frame.grid_columnconfigure(0, weight=1)

        # Stoppa automatisk anpassning
        center_frame.grid_propagate(False)

        # Titel
        title = tk.Label(center_frame, text="Parkens Information", font=("Arial", 26, "bold"),
                         bg="#ffffff", fg="#b30000")
        title.grid(row=0, column=0, pady=10, padx=10, sticky="n")

        # Canvas och scrollbar
        canvas = tk.Canvas(center_frame, bg="#ffe6e6", highlightthickness=0, width= 500)
        scrollbar = ttk.Scrollbar(center_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#ffe6e6")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Centrera scrollable_frame
        canvas.create_window((0, 0), window=scrollable_frame, anchor="n", width=780)
        canvas.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")

        # Grid layout för centrering
        scrollable_frame.grid_columnconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(2, weight=1)

        # Titel
        tk.Label(scrollable_frame, text="Djur i parken:", font=("Arial", 18, "bold", "underline"),
                 bg="#ffe6e6", fg="#b30000").grid(row=0, column=1, pady=10)

        # Djur-information centreras i kolumn 1
        row_index = 1
        for animal in self.zoo.list_animals():
            frame = tk.Frame(scrollable_frame, bg="#f9f9f9", bd=2, relief="ridge")
            frame.grid(row=row_index, column=1, pady=10, padx=20, sticky="ew")
            row_index += 1

            try:
                img = Image.open(animal.image_path).resize((200, 130), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame, image=photo, bg="#f9f9f9")
                img_label.image = photo
                img_label.pack(side="left", padx=10, pady=10)
            except Exception:
                tk.Label(frame, text="[Bild saknas]", bg="#f9f9f9", font=("Arial", 12, "italic")).pack(side="left",
                                                                                                       padx=10)

            age_text = f"Ålder: {animal.get_age_in_month()} månader" if isinstance(animal,
                                                                                   LionCub) else f"Ålder: {animal.age} år"
            info_text = (f"Art: {animal.get_species()}\n"
                         f"Namn: {animal.name}\n"
                         f"{age_text}\n"
                         )
            tk.Label(frame, text=info_text, font=("Arial", 12), bg="#f9f9f9", fg="#333333",
                     justify="left", anchor="w").pack(side="left", padx=10)

        # Sektion för öppettider, biljettkostnad och tillval
        info_section = tk.Frame(center_frame, bg="#ffe6e6", bd=2, relief="ridge")
        info_section.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        tk.Label(info_section, text="Parkens Öppettider:", font=("Arial", 16, "bold"), bg="#ffe6e6", fg="#b30000").pack(pady=5)
        tk.Label(info_section, text=f"{self.zoo.show_opening_hours()}", font=("Arial", 12), bg="#ffe6e6").pack(pady=2)

        tk.Label(info_section, text="Biljettkostnad:", font=("Arial", 16, "bold"), bg="#ffe6e6", fg="#b30000").pack(pady=5)
        tk.Label(info_section, text=f"{self.zoo.show_ticket_price()}", font=("Arial", 12), bg="#ffe6e6").pack(pady=2)

        tk.Label(info_section, text="Tillval:", font=("Arial", 16, "bold"), bg="#ffe6e6", fg="#b30000").pack(pady=5)
        addon_prices = self.zoo.show_addon_prices()
        for line in addon_prices.split("\n"):
            tk.Label(info_section, text=line, font=("Arial", 12), bg="#ffe6e6").pack(pady=2)

        # Sidfot
        footer = tk.Label(self, text="Sidfot med info", bg="#ff4d4d", fg="white", font=("Arial", 12))
        footer.grid(row=3, column=1, sticky="ew")




class ExploreParkPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att utforska djurparken."""
        super().__init__(parent, bg="#ffffff")
        self.controller = controller
        self.zoo = zoo
        self.visitor = None  # För att hålla aktuell besökare

        # Tillbaka-knapp
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939",
                                command=lambda: controller.show_page("StartPage"))
        back_button.place(x=10, y=10)

        # Titel
        self.title_label = tk.Label(self, text="Utforska djurparken", font=("Arial", 26, "bold"),
                                    bg="#ffffff", fg="#b30000")
        self.title_label.pack(pady=20)

        # Knapp-container
        self.button_frame = tk.Frame(self, bg="#ffffff")
        self.button_frame.pack(pady=30)

        # Knappar
        self.search_button = tk.Button(self.button_frame, text="Sök efter ett djur",
                                       font=("Arial", 14, "bold"), bg="#ff4d4d", fg="white",
                                       command=lambda: controller.show_page("SearchAnimalPage"))
        self.interact_button = tk.Button(self.button_frame, text="Interagera med ett djur (kräver tillval)",
                                         font=("Arial", 14, "bold"), bg="#ff4d4d", fg="white",
                                         command=self.go_to_interact_page)
        self.feed_button = tk.Button(self.button_frame, text="Mata ett djur (kräver tillval)",
                                     font=("Arial", 14, "bold"), bg="#ff4d4d", fg="white",
                                     command=self.go_to_feed_page)
        self.details_button = tk.Button(self.button_frame, text="Visa detaljerad information om djur",
                                        font=("Arial", 14, "bold"), bg="#ff4d4d", fg="white",
                                        command=self.go_to_detailed_page)

        # Packa knappar
        for btn in [self.search_button, self.interact_button, self.feed_button, self.details_button]:
            btn.pack(pady=10)

    def set_visitor(self, visitor):
        """Uppdaterar sidan med besökarens namn och tillgänglighet för knappar."""
        self.visitor = visitor
        self.title_label.config(text=f"Utforska djurparken - {visitor.name}")
        self.update_button_states()

    def update_button_states(self):
        """Aktiverar/inaktiverar knappar baserat på besökarens tillval."""
        if not self.visitor:
            return
        cart = [item[0] for item in self.visitor.cart]
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





class SelectVisitorPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att välja en besökare."""
        super().__init__(parent, bg="white")
        self.controller = controller
        self.zoo = zoo

        # Tillbaka-knapp
        tk.Button(self, text="←", bg="lightgray", font=("Arial", 16),
                  command=lambda: controller.show_page("StartPage")).place(x=10, y=10)

        # Titel
        tk.Label(self, text="Välj en besökare att logga in som:", font=("Arial", 20), bg="white").pack(pady=10)

        # Info-meddelande
        self.message_label = tk.Label(self, text="", font=("Arial", 14), fg="red", bg="white")
        self.message_label.pack()

        # Ram för besökarknappar
        self.visitor_buttons_frame = tk.Frame(self, bg="white")
        self.visitor_buttons_frame.pack(pady=20)

    def update_visitors(self):
        """Uppdaterar besökarlistan och skapar knappar."""
        self.visitor_buttons_frame.destroy()  # Rensa tidigare knappar
        self.visitor_buttons_frame = tk.Frame(self, bg="white")
        self.visitor_buttons_frame.pack(pady=20)

        for visitor in self.zoo._visitors:  # Direkt åtkomst till besökarlistan
            name = visitor.name
            addons = ", ".join(item[0] for item in visitor.cart) if visitor.cart else "Inga tillval"



            # Skapa en stor knapp med röd bakgrund och vit text
            button_text = f"{name}\nTillval: {addons}"
            tk.Button(self.visitor_buttons_frame,
                      text=button_text,
                      bg="red",  # Bakgrundsfärg
                      fg="white",  # Textfärg för synlighet
                      font=("Arial", 14),  # Större textstorlek
                      width=30,  # Justera bredd
                      height=3,  # Justera höjd
                      command=lambda v=name: self.select_visitor(v)
                      ).pack(pady=10)  # Extra avstånd mellan knappar

    def select_visitor(self, visitor_name):
        """Loggar in vald besökare och navigerar till Utforska-sidan."""
        # Hämta den valda besökaren baserat på namn
        for visitor in self.zoo._visitors:  # Direkt åtkomst till besökarlistan
            if visitor.name == visitor_name:  # Jämför bara namn
                self.controller.frames["ExploreParkPage"].set_visitor(visitor)
                self.controller.show_page("ExploreParkPage")
                return

        # Om besökaren inte hittades
        self.message_label.config(text=f"Besökaren '{visitor_name}' kunde inte hittas.", fg="red")



class DetailedAnimalPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för detaljerad information om djur."""
        super().__init__(parent, bg="#ffffff")  # Vit bakgrund
        self.controller = controller
        self.zoo = zoo

        # Tillbaka-knapp
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939",
                                command=lambda: controller.show_page("ExploreParkPage"))
        back_button.place(x=10, y=10)

        # Titel
        tk.Label(self, text="Detaljerad info om djur", font=("Arial", 26, "bold"),
                 bg="#ffffff", fg="#b30000").pack(pady=20)

        # Frame för att hålla detaljer om djur
        self.animal_frame = tk.Frame(self, bg="#ffffff")
        self.animal_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.display_animals() #Anropar metoden.

    def display_animals(self):
        """Visar alla djur i detaljerad vy med större bilder och vänsterställd information."""
        # Rensa tidigare widgets
        for widget in self.animal_frame.winfo_children():
            widget.destroy()

        # Hämta djur från zoo med list_animals()
        for animal in self.zoo.list_animals():  # Säker åtkomst till __animals
            # Ram för varje djur
            frame = tk.Frame(self.animal_frame, bg="#f9f9f9", bd=2, relief="ridge")
            frame.pack(pady=15, padx=10, fill="x")

            # Huvudram med horisontell layout
            content_frame = tk.Frame(frame, bg="#f9f9f9")
            content_frame.pack(fill="both", expand=True, padx=20, pady=15)

            # Ladda och visa en större bild
            try:
                img = Image.open(animal.image_path).resize((150, 150), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(content_frame, image=photo, bg="#f9f9f9")
                img_label.image = photo  # Håll referensen
                img_label.pack(side="left", padx=10)
            except Exception:
                tk.Label(content_frame, text="[Bild saknas]", bg="#f9f9f9", font=("Arial", 14, "italic"),
                         width=15, height=7).pack(side="left", padx=10)

            # Vänsterställd djurinformation
            info_frame = tk.Frame(content_frame, bg="#f9f9f9")
            info_frame.pack(side="left", fill="both", expand=True, padx=20)

            info_text = (f"Art: {animal.get_species()}\n"
                         f"Namn: {animal.name}\n"
                         f"Ålder: {animal.age} år\n"
                         f"Favoritmat: {animal.favorite_food}")
            tk.Label(info_frame, text=info_text, font=("Arial", 14), bg="#f9f9f9", fg="#333333",
                     justify="left", anchor="w").pack(anchor="w")

            # Knappar för mata och interagera
            button_frame = tk.Frame(content_frame, bg="#f9f9f9")
            button_frame.pack(side="right", padx=10)

            tk.Button(button_frame, text="Mata djur", bg="#ff4d4d", fg="white", font=("Arial", 12, "bold"),
                      command=lambda a=animal: self.feed_animal(a)).pack(pady=5)
            tk.Button(button_frame, text="Interagera", bg="#ff4d4d", fg="white", font=("Arial", 12, "bold"),
                      command=lambda a=animal: self.interact_with_animal(a)).pack(pady=5)

    def feed_animal(self, animal):
        """Funktion för att mata djuret."""
        food = simpledialog.askstring("Mata djur", f"Vad vill du mata {animal.name} med?")
        if food:
            result = animal.eat(food)  # Använd animal-metoden för att hantera matning
            messagebox.showinfo("Matningsresultat", result)

    def interact_with_animal(self, animal):
        """Funktion för att interagera med djuret."""
        result = animal.interact()  # Använd animal-metoden för interaktion
        messagebox.showinfo("Interaktion", result)



class SearchAnimalPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att söka efter djur."""
        super().__init__(parent, bg="white")
        self.controller = controller
        self.zoo = zoo

        # Titel
        tk.Label(self, text="Sök efter djur", font=("Arial", 20, "bold"), bg="white").pack(pady=10)

        # Sökfält
        search_frame = tk.Frame(self, bg="white")
        search_frame.pack(pady=10)
        tk.Label(search_frame, text="Ange djurnamn:", font=("Arial", 14), bg="white").grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=20)
        self.search_entry.grid(row=0, column=1, padx=5)

        # Sök-knapp
        tk.Button(search_frame, text="Sök", font=("Arial", 12), bg="#ff4d4d", fg="white",
                  command=self.search_animal).grid(row=0, column=2, padx=5)

        # Ram för att visa djurdetaljer
        self.result_frame = tk.Frame(self, bg="#f9f9f9", bd=2, relief="ridge")
        self.result_frame.pack(pady=20, fill="both", expand=True)

        # Tillbaka-knapp
        tk.Button(self, text="← Tillbaka", font=("Arial", 12), bg="#ff4d4d", fg="white",
                  command=lambda: controller.show_page("ExploreParkPage")).pack(pady=5)

    def search_animal(self):
        """Söker efter djuret och visar detaljerad information inklusive bild."""
        search_name = self.search_entry.get().lower()

        # Rensa tidigare resultat
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        # Sök efter djuret via list_animals()
        for animal in self.zoo.list_animals():  # Säker åtkomst till __animals
            if animal.name.lower() == search_name:
                # Visa detaljerad info
                tk.Label(self.result_frame, text="Djurets Detaljer", font=("Arial", 18, "bold"),
                         bg="#f9f9f9", fg="#b30000").pack(pady=5)

                # Ladda och visa bilden
                try:
                    image = Image.open(animal.image_path)
                    image = image.resize((340, 200), Image.Resampling.LANCZOS)  # Ändra storlek på bilden
                    photo = ImageTk.PhotoImage(image)
                    image_label = tk.Label(self.result_frame, image=photo, bg="#f9f9f9")
                    image_label.image = photo  # Håll referensen
                    image_label.pack(pady=5)
                except Exception:
                    tk.Label(self.result_frame, text="[Bild saknas]", font=("Arial", 12, "italic"),
                             bg="#f9f9f9", fg="red").pack(pady=5)

                # Detaljerad information
                details = (f"Art: {animal.get_species()}\n"
                           f"Namn: {animal.name}\n"
                           f"Ålder: {animal.age} år\n"
                           f"Favoritmat: {animal.favorite_food}\n"
                           f"Hungerstatus: {'Hungrig' if animal.hungry else 'Mätt'}")
                tk.Label(self.result_frame, text=details, font=("Arial", 14), bg="#f9f9f9", fg="#333333",
                         justify="left", anchor="w").pack(pady=5, padx=10)

                return

        # Om djuret inte hittas
        tk.Label(self.result_frame, text="Inget djur med det namnet hittades.", font=("Arial", 14, "italic"),
                 bg="#f9f9f9", fg="red").pack(pady=10)


class InteractAnimalPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Skapar sidan för att interagera med djur."""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.zoo = zoo

        # Konfigurera fönstret för att centrera widgets
        self.grid_rowconfigure(0, weight=1)  # Överst
        self.grid_rowconfigure(4, weight=1)  # Nederst
        self.grid_columnconfigure(0, weight=1)  # Vänster
        self.grid_columnconfigure(2, weight=1)  # Höger

        # Rubrik
        label = tk.Label(self, text="Interagera med ett djur", font=("Arial", 18, "bold"))
        label.grid(row=1, column=1, pady=(10, 20), sticky="n")

        # Input för djurnamn
        self.animal_name_var = tk.StringVar()
        animal_label = tk.Label(self, text="Ange djurets namn:")
        animal_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        animal_entry = tk.Entry(self, textvariable=self.animal_name_var)
        animal_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Bekräfta-knapp
        interact_button = tk.Button(self, text="Interagera", command=self.interact_with_animal)
        interact_button.grid(row=3, column=1, pady=10)

        # Feedback-meddelande
        self.feedback_label = tk.Label(self, text="", fg="green")
        self.feedback_label.grid(row=4, column=1, pady=10)

        # Tillbaka-knapp (placerad i övre vänstra hörnet)
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939",
                                command=lambda: controller.show_page("ExploreParkPage"))
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    def interact_with_animal(self):
        """Interagerar med djuret."""
        animal_name = self.animal_name_var.get()
        animals = self.zoo.list_animals()
        animal = next((a for a in animals if a.name == animal_name), None)

        if animal:
            result = animal.interact()
            self.feedback_label.config(text=result, fg="green")
        else:
            self.feedback_label.config(text="Djuret finns inte i zoo.", fg="red")


import tkinter as tk
from tkinter import ttk

class FeedAnimalPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.zoo = zoo
        self.animal = None

        # Grundkonfiguration av layout
        self.config(bg="#f0f8ff")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)

        # Header
        self.create_header()

        # Sökningssektion
        self.create_search_section()

        # Djurets detaljer
        self.create_animal_info_section()

        # Mata-sektion
        self.create_feed_section()

        # Footer
        self.create_footer()

    def create_header(self):
        """Header-sektionen."""
        header = tk.Label(self, text="Mata ett djur", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="#333")
        header.grid(row=0, column=1, pady=(10, 20), sticky="n")

    def create_search_section(self):
        """Sökningssektionen."""
        search_label = tk.Label(self, text="Ange djurets namn:", font=("Arial", 12), bg="#f0f8ff")
        search_label.grid(row=1, column=0, sticky="e", padx=10)

        self.animal_name_var = tk.StringVar()
        self.animal_entry = tk.Entry(self, textvariable=self.animal_name_var, width=20)
        self.animal_entry.grid(row=1, column=1, sticky="w", padx=10)

        self.search_button = ttk.Button(self, text="Sök", command=self.search_animal)
        self.search_button.grid(row=1, column=2, padx=10)

    def create_animal_info_section(self):
        """Visar djurets detaljer."""
        self.animal_info_frame = tk.Frame(self, bg="#e6f7ff", bd=2, relief="ridge")
        self.animal_info_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="nsew")

        self.animal_info_label = tk.Label(self.animal_info_frame, text="Inget djur valt", font=("Arial", 12), bg="#e6f7ff", justify="left")
        self.animal_info_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    def create_feed_section(self):
        """Input för mat och mata-knapp."""
        tk.Label(self, text="Ange maten:", font=("Arial", 12), bg="#f0f8ff").grid(row=3, column=0, sticky="e", padx=10)

        self.food_var = tk.StringVar()
        self.food_entry = tk.Entry(self, textvariable=self.food_var, width=20)
        self.food_entry.grid(row=3, column=1, sticky="w", padx=10)

        self.feed_button = ttk.Button(self, text="Mata", command=self.feed_animal)
        self.feed_button.grid(row=3, column=2, padx=10)
        self.feed_button.config(state="disabled")

    def create_footer(self):
        """Footer med tillbaka-knapp och feedback."""
        self.feedback_label = tk.Label(self, text="", fg="green", bg="#f0f8ff", font=("Arial", 10))
        self.feedback_label.grid(row=4, column=0, columnspan=3, pady=10)

        back_button = ttk.Button(self, text="← Tillbaka", command=lambda: self.controller.show_page("ExploreParkPage"))
        back_button.grid(row=5, column=0, columnspan=3, pady=10)

    def search_animal(self):
        """Söker efter djuret och uppdaterar information."""
        animal_name = self.animal_name_var.get().strip()
        animals = self.zoo.list_animals()
        self.animal = next((a for a in animals if a.name.lower() == animal_name.lower()), None)

        if self.animal:
            self.animal_info_label.config(
                text=f"Namn: {self.animal.name}\nArt: {type(self.animal).__name__}\nHungerstatus: {'Hungrig' if self.animal.hungry else 'Mätt'}\nFavoritmat: {self.animal.favorite_food}"
            )
            self.feed_button.config(state="normal")
        else:
            self.animal_info_label.config(text="Djuret hittades inte.")
            self.feed_button.config(state="disabled")

    def feed_animal(self):
        """Hantera matning av djuret."""
        food_item = self.food_var.get().strip()
        if self.animal:
            result = self.animal.eat(food_item)
            self.feedback_label.config(text=result, fg="green")
            self.search_animal()  # Uppdatera hungerstatus
        else:
            self.feedback_label.config(text="Sök efter ett djur först.", fg="red")


