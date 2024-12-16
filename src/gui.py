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
        container.pack(fill="both", expand=True)

        # Lägg till sidor
        for Page in (StartPage, RegisterVisitorPage, ManageVisitorsPage, ZooInfoPage, AddAddonsPage, SelectVisitorPage, ExploreParkPage, DetailedAnimalPage, SearchAnimalPage):
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

class StartPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar startsidan för djurparken."""
        super().__init__(parent, bg="white")
        self.controller = controller
        self.zoo = zoo

        # Titel för startsidan
        tk.Label(self, text="Välkommen till Eggis Zoo", font=("Arial", 24), bg="white").pack(pady=20)

        # Bildruta - här kan en bild läggas in senare
        image_frame = tk.Frame(self, bg="lightcoral", width=700, height=150)
        image_frame.pack(pady=10)
        tk.Label(image_frame, text="Någon bild här", bg="lightcoral", font=("Arial", 14)).pack(expand=True)

        # Menyram för knappar
        menu_frame = tk.Frame(self, bg="lightgray", width=700, height=150)
        menu_frame.pack(pady=10)
        tk.Label(menu_frame, text="Meny", font=("Arial", 16), bg="lightgray").pack(pady=5)

        # Första raden med knappar
        button_row1 = tk.Frame(menu_frame, bg="lightgray")
        button_row1.pack()

        tk.Button(button_row1, text="Visa enkel information om djurparken", font=("Arial", 14), bg="red", fg="white",
                  width=30, command=lambda: controller.show_page("ZooInfoPage")).pack(side="left", padx=10, pady=5)

        tk.Button(button_row1, text="Registrera ny besökare och köp biljett", font=("Arial", 14), bg="red", fg="white",
                  width=30, command=lambda: controller.show_page("RegisterVisitorPage")).pack(side="left", padx=10, pady=5)

        # Andra raden med knappar
        button_row2 = tk.Frame(menu_frame, bg="lightgray")
        button_row2.pack()

        tk.Button(button_row2, text="Visa och hantera besökare", font=("Arial", 14), bg="red", fg="white",
                  width=30, command=lambda: controller.show_page("ManageVisitorsPage")).pack(side="left", padx=10, pady=5)

        tk.Button(button_row2, text="Utforska djurparken", font=("Arial", 14), bg="red", fg="white",
                  width=30, command=lambda: controller.show_page("SelectVisitorPage")).pack(side="left", padx=10, pady=5)

        # Sökfält för att söka efter djur
        search_frame = tk.Frame(self, bg="white")
        search_frame.pack(pady=20)
        tk.Label(search_frame, text="Sök", font=("Arial", 14), bg="white").grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame, font=("Arial", 14), width=30)
        self.search_entry.grid(row=0, column=1, padx=5)

        # Sidfot med ytterligare information
        footer_label = tk.Label(self, text="Sidfot med info", bg="lightgray", font=("Arial", 12))
        footer_label.pack(side="bottom", fill="x")



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

    def register_visitor(self):
        """Registrerar en ny besökare och visar bekräftelse."""
        name = self.name_entry.get()
        budget_text = self.budget_entry.get()

        # Validera inmatning
        if not name or not budget_text.isdigit():
            self.show_message("Ange ett giltigt namn och budget!", error=True)
            return

        # Skapa besökare
        visitor = Visitor(name, float(budget_text))
        result = self.zoo.add_visitor(visitor)  # Använder add_visitor() istället för direktåtkomst

        if "har lagts till" in result:  # Kontrollera om besökaren lades till framgångsrikt
            self.show_message(f"{name} har registrerats med budget {visitor.budget:.2f} SEK.", error=False)
            # Byt sida automatiskt efter 2 sekunder
            self.after(2000, lambda: self.next_page(visitor))
        else:
            self.show_message(result, error=True)  # Visa felmeddelande om maxgränsen nåddes

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
        self.visitor = visitor
        self.cart = []  # Töm kundvagnen
        self.cart_listbox.delete(0, tk.END)  # Rensa listbox
        self.info_label.config(text=f"Välkommen {visitor.name}! Din budget är {visitor.budget:.2f} SEK.")
        self.display_addons()

    def display_addons(self):
        """Visar alla tillval som knappar."""
        # Rensa gamla widgets
        for widget in self.addons_frame.winfo_children():
            widget.destroy()

        # Skapa knappar för tillval
        for addon, price in self.zoo._addons.items():  # Hämtar tillval via addons
            addon_frame = tk.Frame(self.addons_frame, bg="#ffcccc", bd=1, relief="ridge")
            addon_frame.pack(fill="x", pady=5, padx=5)

            addon_label = tk.Label(addon_frame, text=f"{addon} - {price:.2f} SEK",
                                   font=("Arial", 12), bg="#ffcccc", fg="#b30000")
            addon_label.pack(side="left", padx=10, pady=5)

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
            self.info_label.config(text="Du har inte valt några tillval att bekräfta.", fg="red")
            return

        # Lägg till valda tillval i besökarens kundvagn
        for addon, price in self.cart:
            self.visitor.add_to_cart(addon, price)  # Använd visitor-metoden för att hantera tillval

        self.info_label.config(text="Tillvalen har bekräftats! Går tillbaka till startsidan...", fg="green")
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

        # Huvudram i mitten
        center_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="ridge")
        center_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        # Titel
        title = tk.Label(center_frame, text="Parkens Information", font=("Arial", 26, "bold"),
                         bg="#ffffff", fg="#b30000")
        title.grid(row=0, column=0, pady=10, padx=10, sticky="n")

        # Canvas och scrollbar för innehållet
        canvas = tk.Canvas(center_frame, bg="#ffe6e6", highlightthickness=0)
        scrollbar = ttk.Scrollbar(center_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#ffe6e6")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
        canvas.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")

        # Öppettider och biljettpriser
        info_frame = tk.Frame(scrollable_frame, bg="#ffcccc", bd=2, relief="ridge")
        info_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(info_frame, text="Öppettider: 09:00 - 18:00.", font=("Arial", 14),
                 bg="#ffcccc", fg="#b30000").pack(pady=5)
        tk.Label(info_frame, text="Biljettpris: 150.0 SEK.", font=("Arial", 14),
                 bg="#ffcccc", fg="#b30000").pack(pady=5)

        # Tillval
        tk.Label(info_frame, text="Tillval:", font=("Arial", 14, "bold"), bg="#ffcccc", fg="#b30000").pack(pady=5)
        for addon in self.zoo.show_addon_prices().split("\n"):
            tk.Label(info_frame, text=addon, font=("Arial", 12), bg="#ffcccc", fg="#333333").pack()

        # Djur-information
        tk.Label(scrollable_frame, text="Djur i parken:", font=("Arial", 18, "bold", "underline"),
                 bg="#ffe6e6", fg="#b30000").pack(pady=10)

        for animal in self.zoo.list_animals():
            animal_frame = tk.Frame(scrollable_frame, bg="#ffffff", bd=2, relief="solid")
            animal_frame.pack(pady=5, padx=10, fill="x")

            # Djurbild
            try:
                img = Image.open(animal.image_path).resize((80, 80), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(animal_frame, image=photo, bg="#ffffff")
                img_label.image = photo  # Håll referens
                img_label.pack(side="right", padx=10, pady=10)
            except Exception:
                tk.Label(animal_frame, text="[Bild saknas]", bg="#ffffff", font=("Arial", 12, "italic")).pack(side="right", padx=10)

            # Djurets info
            details = (f"Art: {animal.get_species()}\n"
                       f"Namn: {animal.name}\n"
                       f"Ålder: {animal.age} år\n"
                       f"Favoritmat: {animal.favorite_food}")
            tk.Label(animal_frame, text=details, font=("Arial", 12), bg="#ffffff", fg="#333333",
                     justify="left").pack(side="left", padx=10, pady=10)

        # Sidfot
        footer = tk.Label(self, text="Sidfot med info", bg="#ff4d4d", fg="white", font=("Arial", 12))
        footer.grid(row=3, column=1, sticky="ew")




# Sida för att utforska djurparken
class ExploreParkPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        """Initialiserar sidan för att utforska djurparken."""
        super().__init__(parent, bg="#ffffff")  # Vit bakgrund
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
        button_frame = tk.Frame(self, bg="#ffffff")
        button_frame.pack(pady=30)

        # Knappar
        buttons = [
            ("Sök efter ett djur", lambda: controller.show_page("SearchAnimalPage")),
            ("Interagera med ett djur (kräver tillval)", lambda: controller.show_page("InteractAnimalPage")),
            ("Mata ett djur (kräver tillval)", lambda: controller.show_page("FeedAnimalPage")),
            ("Visa detaljerad information om djur", lambda: controller.show_page("DetailedAnimalPage"))
        ]

        for text, command in buttons:
            btn = tk.Button(button_frame, text=text, font=("Arial", 14, "bold"), bg="#ff4d4d",
                            fg="white", activebackground="#e63939", activeforeground="white",
                            bd=2, relief="raised", width=30, height=2, command=command)
            btn.pack(pady=10)

    def set_visitor(self, visitor):
        """Uppdaterar sidan med besökarens namn."""
        self.visitor = visitor
        self.title_label.config(text=f"Utforska djurparken - {visitor.name}")

    def show_animal_info(self):
        """Visar detaljerad information om djuren."""
        animal_info = "\n".join([str(animal) for animal in self.zoo.list_animals()])  # Använd list_animals()
        messagebox.showinfo("Djurinformation", animal_info)

    def search_animals(self):
        """Söker efter djur baserat på namn."""
        search = simpledialog.askstring("Sök djur", "Ange namnet på djuret:")
        if not search:
            return

        for animal in self.zoo.list_animals():  # Använd list_animals()
            if animal.name.lower() == search.lower():
                messagebox.showinfo("Hittat djur", f"Art: {animal.get_species()}\n"
                                                   f"Namn: {animal.name}\n"
                                                   f"Ålder: {animal.age} år\n"
                                                   f"Favoritmat: {animal.favorite_food}")
                return
        messagebox.showerror("Fel", "Inget djur hittades.")

    def interact_with_animal(self):
        """Simulerar interaktion med ett djur."""
        if not self.visitor or "Interagera med djur" not in [item[0] for item in self.visitor.cart]:
            messagebox.showwarning("Tillval saknas", "Du har inte köpt tillvalet för att interagera med djur.")
            return
        messagebox.showinfo("Interaktion", "Du har interagerat med ett djur!")

    def feed_animal(self):
        """Simulerar att mata ett djur."""
        if not self.visitor or "Mata djur" not in [item[0] for item in self.visitor.cart]:
            messagebox.showwarning("Tillval saknas", "Du har inte köpt tillvalet för att mata djur.")
            return
        messagebox.showinfo("Matning", "Du har matat ett djur!")


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
            budget = f"{visitor.budget:.2f}"

            # Skapa en knapp för varje besökare och skicka endast namnet
            tk.Button(self.visitor_buttons_frame, text=f"{name} - Budget: {budget} SEK",
                      bg="lightblue", font=("Arial", 12),
                      command=lambda v=name: self.select_visitor(v)).pack(pady=5)

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

    def display_animals(self):
        """Visar alla djur i detaljerad vy."""
        # Rensa tidigare widgets
        for widget in self.animal_frame.winfo_children():
            widget.destroy()

        # Hämta djur från zoo med list_animals()
        for animal in self.zoo.list_animals():  # Säker åtkomst till __animals
            # Ram för varje djur
            frame = tk.Frame(self.animal_frame, bg="#f9f9f9", bd=2, relief="ridge")
            frame.pack(pady=10, fill="x")

            # Försök ladda bilden
            try:
                img = Image.open(animal.image_path).resize((80, 80), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame, image=photo, bg="#f9f9f9")
                img_label.image = photo  # Håll referensen
                img_label.pack(side="left", padx=10, pady=10)
            except Exception:
                tk.Label(frame, text="[Bild saknas]", bg="#f9f9f9", font=("Arial", 12, "italic")).pack(side="left",
                                                                                                      padx=10, pady=10)

            # Information om djuret
            info_text = (f"Art: {animal.get_species()}\n"
                         f"Namn: {animal.name}\n"
                         f"Ålder: {animal.age} år\n"
                         f"Favoritmat: {animal.favorite_food}")
            tk.Label(frame, text=info_text, font=("Arial", 12), bg="#f9f9f9", fg="#333333",
                     justify="left", anchor="w").pack(side="left", padx=10)

            # Knappar för mata och interagera
            button_frame = tk.Frame(frame, bg="#f9f9f9")
            button_frame.pack(side="right", padx=10, pady=10)

            tk.Button(button_frame, text="Mata djur", bg="#ff4d4d", fg="white", font=("Arial", 10, "bold"),
                      command=lambda a=animal: self.feed_animal(a)).pack(pady=5)
            tk.Button(button_frame, text="Interagera", bg="#ff4d4d", fg="white", font=("Arial", 10, "bold"),
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


