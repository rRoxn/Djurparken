import tkinter as tk
from tkinter import messagebox, simpledialog
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
        for Page in (StartPage, RegisterVisitorPage, ManageVisitorsPage, ZooInfoPage, AddAddonsPage, SelectVisitorPage, ExploreParkPage, DetailedAnimalPage):
            page_name = Page.__name__
            frame = Page(parent=container, controller=self, zoo=self.zoo)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_page("StartPage")

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
        super().__init__(parent, bg="white")
        self.controller = controller
        self.zoo = zoo

        # Titel
        tk.Label(self, text="Välkommen till Eggis Zoo", font=("Arial", 24), bg="white").pack(pady=20)

        # Bildruta
        image_frame = tk.Frame(self, bg="lightcoral", width=700, height=150)
        image_frame.pack(pady=10)
        tk.Label(image_frame, text="Någon bild här", bg="lightcoral", font=("Arial", 14)).pack(expand=True)

        # Menyruta
        menu_frame = tk.Frame(self, bg="lightgray", width=700, height=150)
        menu_frame.pack(pady=10)
        tk.Label(menu_frame, text="Meny", font=("Arial", 16), bg="lightgray").pack(pady=5)

        # Knappar i två rader
        button_row1 = tk.Frame(menu_frame, bg="lightgray")
        button_row1.pack()
        tk.Button(button_row1, text="Visa enkel information om djurparken", font=("Arial", 14), bg="red", fg="white",
                  width=30, command=lambda: controller.show_page("ZooInfoPage")).pack(side="left", padx=10, pady=5)
        tk.Button(button_row1, text="Registrera ny besökare och köp biljett", font=("Arial", 14), bg="red", fg="white",
                  width=30, command=lambda: controller.show_page("RegisterVisitorPage")).pack(side="left", padx=10, pady=5)

        button_row2 = tk.Frame(menu_frame, bg="lightgray")
        button_row2.pack()
        tk.Button(button_row2, text="Visa och hantera besökare", font=("Arial", 14), bg="red", fg="white",
                  width=30, command=lambda: controller.show_page("ManageVisitorsPage")).pack(side="left", padx=10, pady=5)
        tk.Button(button_row2, text="Utforska djurparken", font=("Arial", 14), bg="red", fg="white",
                  width=30, command=lambda: controller.show_page("SelectVisitorPage")).pack(side="left", padx=10, pady=5)

        # Sökfält längst ner
        search_frame = tk.Frame(self, bg="white")
        search_frame.pack(pady=20)
        tk.Label(search_frame, text="Sök", font=("Arial", 14), bg="white").grid(row=0, column=0, padx=5)
        tk.Entry(search_frame, font=("Arial", 14), width=30).grid(row=0, column=1, padx=5)

        # Sidfot
        footer_label = tk.Label(self, text="Sidfot med info", bg="lightgray", font=("Arial", 12))
        footer_label.pack(side="bottom", fill="x")

class RegisterVisitorPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        super().__init__(parent, bg="#ffe6e6")  # Ljus rödaktig bakgrundsfärg
        self.controller = controller
        self.zoo = zoo

        # Tillbaka-knapp (pil)
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939", command=lambda: controller.show_page("StartPage"))
        back_button.place(x=10, y=10)

        # Titel
        title_label = tk.Label(self, text="Registrera ny besökare", font=("Arial", 26, "bold"),
                               bg="#ffe6e6", fg="#b30000")
        title_label.pack(pady=20)

        # Ram för input-fält
        input_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="solid")
        input_frame.pack(pady=20, padx=20)

        # Namn-input
        tk.Label(input_frame, text="Ange namn:", font=("Arial", 12), bg="#ffffff", fg="#b30000").grid(row=0, column=0, pady=10, padx=10)
        self.name_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#ffcccc", fg="#b30000", bd=1, relief="solid")
        self.name_entry.grid(row=0, column=1, pady=10, padx=10)

        # Budget-input
        tk.Label(input_frame, text="Ange budget:", font=("Arial", 12), bg="#ffffff", fg="#b30000").grid(row=1, column=0, pady=10, padx=10)
        self.budget_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#ffcccc", fg="#b30000", bd=1, relief="solid")
        self.budget_entry.grid(row=1, column=1, pady=10, padx=10)

        # Registrera-knapp
        register_button = tk.Button(self, text="Registrera", font=("Arial", 14, "bold"), bg="#ff4d4d",
                                    fg="white", activebackground="#e63939", command=self.register_visitor)
        register_button.pack(pady=20)

    def register_visitor(self):
        """Registrera en ny besökare."""
        name = self.name_entry.get()
        budget_text = self.budget_entry.get()
        if not name or not budget_text.isdigit():
            messagebox.showerror("Fel", "Ange ett giltigt namn och budget!")
            return

        visitor = Visitor(name, float(budget_text))
        self.zoo.visitors.append(visitor)
        messagebox.showinfo("Registrerad", f"{name} har registrerats med budget {visitor.budget} SEK.")
        self.controller.show_page("StartPage")




class ManageVisitorsPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        super().__init__(parent, bg="#ffe6e6")  # Ljus rödaktig bakgrundsfärg
        self.controller = controller
        self.zoo = zoo

        # Tillbaka-knapp
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939",
                                command=lambda: controller.show_page("StartPage"))
        back_button.place(x=10, y=10)

        # Titel
        title_label = tk.Label(self, text="Hantera Besökare", font=("Arial", 26, "bold"),
                               bg="#ffe6e6", fg="#b30000")
        title_label.pack(pady=20)

        # Frame för besökarlistan
        self.visitors_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="solid")
        self.visitors_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Listbox för att visa besökare
        self.visitor_listbox = tk.Listbox(self.visitors_frame, font=("Arial", 12), bg="#ffcccc",
                                          fg="#b30000", selectbackground="#ff6666", height=10)
        self.visitor_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Ta bort-knapp
        remove_button = tk.Button(self, text="Ta bort markerad besökare", bg="#ff4d4d", fg="white",
                                  font=("Arial", 12, "bold"),
                                  activebackground="#e63939",
                                  command=self.remove_selected_visitor)
        remove_button.pack(pady=20)

    def update_visitor_list(self):
        """Uppdaterar listan över registrerade besökare."""
        self.visitor_listbox.delete(0, tk.END)
        for visitor in self.zoo.visitors:
            self.visitor_listbox.insert(tk.END, f"{visitor.name} - Budget: {visitor.budget:.2f} SEK")

    def remove_selected_visitor(self):
        """Tar bort markerad besökare."""
        selected_index = self.visitor_listbox.curselection()
        if selected_index:
            visitor_name = self.visitor_listbox.get(selected_index).split(" - ")[0]
            self.zoo.remove_visitor(visitor_name)
            self.update_visitor_list()
            messagebox.showinfo("Besökare borttagen", f"{visitor_name} har tagits bort.")
        else:
            messagebox.showwarning("Ingen markerad", "Vänligen markera en besökare att ta bort.")


# Sida för tillval
class AddAddonsPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        super().__init__(parent, bg="#ffe6e6")  # Ljus rödaktig bakgrundsfärg
        self.controller = controller
        self.zoo = zoo
        self.visitor = None
        self.buttons = []

        # Tillbaka-knapp
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939",
                                command=lambda: controller.show_page("StartPage"))
        back_button.place(x=10, y=10)

        # Titel
        title_label = tk.Label(self, text="Lägg till tillval", font=("Arial", 26, "bold"),
                               bg="#ffe6e6", fg="#b30000")
        title_label.pack(pady=20)

        # Info-ruta
        self.info_label = tk.Label(self, text="", font=("Arial", 14), bg="#ffcccc", fg="#b30000",
                                   bd=2, relief="ridge", padx=10, pady=5)
        self.info_label.pack(pady=10, padx=20)

        # Frame för tillval
        addons_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="solid")
        addons_frame.pack(pady=10, padx=20, fill="x", expand=True)

        # Bekräfta-knapp längst ner
        confirm_button = tk.Button(self, text="Bekräfta och gå tillbaka till startsidan", bg="#ff4d4d",
                                   fg="white", font=("Arial", 12, "bold"),
                                   activebackground="#e63939",
                                   command=self.confirm_and_go_back)
        confirm_button.pack(pady=20)

        # Lagra tillvalsknappar
        self.addons_frame = addons_frame

    def set_visitor(self, visitor):
        """Sätter aktuell besökare och uppdaterar sidan."""
        self.visitor = visitor
        self.info_label.config(text=f"Välkommen {visitor.name}! Din budget är {visitor.budget:.2f} SEK.")
        self.display_addons()

    def display_addons(self):
        """Visar alla tillval som knappar."""
        # Rensa gamla knappar
        for widget in self.addons_frame.winfo_children():
            widget.destroy()

        # Skapa knappar för tillval
        for addon, price in self.zoo.addons.items():
            addon_frame = tk.Frame(self.addons_frame, bg="#ffcccc", bd=1, relief="ridge")
            addon_frame.pack(fill="x", pady=5, padx=5)

            addon_label = tk.Label(addon_frame, text=f"{addon} - {price:.2f} SEK",
                                   font=("Arial", 12), bg="#ffcccc", fg="#b30000")
            addon_label.pack(side="left", padx=10, pady=5)

            buy_button = tk.Button(addon_frame, text="Köp", bg="#ff4d4d", fg="white",
                                   activebackground="#e63939",
                                   font=("Arial", 10, "bold"),
                                   command=lambda a=addon, p=price: self.add_to_cart(a, p))
            buy_button.pack(side="right", padx=10, pady=5)

    def add_to_cart(self, addon, price):
        """Lägger till tillval i besökarens kundvagn."""
        if self.visitor.add_to_cart(addon, price):
            messagebox.showinfo("Tillval tillagt",
                                f"{addon} har lagts till!\nÅterstående budget: {self.visitor.budget:.2f} SEK")
            self.info_label.config(text=f"Välkommen {self.visitor.name}! Din budget är {self.visitor.budget:.2f} SEK.")
        else:
            messagebox.showwarning("Otillräcklig budget", f"Du har inte råd med {addon}.")

    def confirm_and_go_back(self):
        """Bekräftar tillval och går tillbaka till startsidan."""
        messagebox.showinfo("Bekräftelse", "Dina tillval har bekräftats!")
        self.controller.show_page("StartPage")


class ZooInfoPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        super().__init__(parent, bg="#ffe6e6")  # Ljus rödaktig bakgrundsfärg
        self.controller = controller
        self.zoo = zoo

        # Tillbaka-knapp
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="#ff4d4d", fg="white",
                                activebackground="#e63939",
                                command=lambda: controller.show_page("StartPage"))
        back_button.place(x=10, y=10)

        # Titel
        title = tk.Label(self, text="Parkens Information", font=("Arial", 26, "bold"),
                         bg="#ffe6e6", fg="#b30000")
        title.pack(pady=20)

        # Information om öppettider och biljettpris
        info_frame = tk.Frame(self, bg="#ffcccc", bd=2, relief="ridge")
        info_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(info_frame, text=f"Parkens öppettider: {self.zoo.opening_hours}",
                 font=("Arial", 14), bg="#ffcccc", fg="#b30000").pack(pady=5)
        tk.Label(info_frame, text=f"Biljettkostnad: {self.zoo.ticket_price} SEK",
                 font=("Arial", 14), bg="#ffcccc", fg="#b30000").pack(pady=5)

        # Djur-information
        animals_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="solid")
        animals_frame.pack(pady=20, padx=20, fill="both", expand=True)

        tk.Label(animals_frame, text="Djur i parken:", font=("Arial", 18, "bold", "underline"),
                 bg="#ffffff", fg="#ff4d4d").pack(pady=10)

        for animal in self.zoo.animals:
            tk.Label(animals_frame, text=f"Art: {animal.get_species()}, Namn: {animal.name}",
                     font=("Arial", 12), bg="#ffffff", fg="#4d4d4d").pack(pady=5)

        # Sidfot
        footer = tk.Label(self, text="Sidfot med info", bg="#ff4d4d", fg="white",
                          font=("Arial", 12))
        footer.pack(side="bottom", fill="x")


#Sida för att utforska djurparken
class ExploreParkPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.zoo = zoo
        self.visitor = None  # Placeholder för den inloggade besökaren

        # Titel
        self.title_label = tk.Label(self, text="Utforska djurparken", font=("Arial", 20), bg="white")
        self.title_label.pack(pady=10)

        # Meddelande
        self.info_label = tk.Label(self, text="", font=("Arial", 14), bg="white")
        self.info_label.pack(pady=5)

        # Knapp för att gå tillbaka
        tk.Button(self, text="←", font=("Arial", 16), bg="lightgray",
                  command=lambda: controller.show_page("StartPage")).place(x=10, y=10)

        # Menyval
        self.menu_frame = tk.Frame(self, bg="white")
        self.menu_frame.pack(pady=10)

        tk.Button(self, text="Visa detaljerad information om djur", bg="red", fg="white",
                  command=lambda: [controller.frames["DetailedAnimalPage"].display_animals(),
                                   controller.show_page("DetailedAnimalPage")]).pack(pady=5)
        tk.Button(self.menu_frame, text="Sök efter ett djur", bg="red", fg="white", font=("Arial", 12),
                  command=self.search_animals).pack(pady=5)
        tk.Button(self.menu_frame, text="Interagera med ett djur (kräver tillval)", bg="red", fg="white", font=("Arial", 12),
                  command=self.interact_with_animal).pack(pady=5)
        tk.Button(self.menu_frame, text="Mata ett djur (kräver tillval)", bg="red", fg="white", font=("Arial", 12),
                  command=self.feed_animal).pack(pady=5)

    def set_visitor(self, visitor):
        """Sätter den aktuella besökaren och uppdaterar sidan."""
        self.visitor = visitor
        self.title_label.config(text=f"Utforska djurparken - {visitor.name}")
        self.info_label.config(text=f"Välkommen {visitor.name}! Din budget är {visitor.budget:.2f} SEK.")

    def show_animal_info(self):
        """Visar detaljerad information om djuren."""
        animal_info = "\n".join([str(animal) for animal in self.zoo.animals])
        messagebox.showinfo("Djurinformation", animal_info)

    def search_animals(self):
        """Simulerar sökning av djur."""
        search = simpledialog.askstring("Sök djur", "Ange namnet på djuret:")
        for animal in self.zoo.animals:
            if animal.name.lower() == search.lower():
                messagebox.showinfo("Hittat djur", str(animal))
                return
        messagebox.showerror("Fel", "Inget djur hittades.")

    def interact_with_animal(self):
        """Simulerar interaktion med djur."""
        if not self.visitor or "Interagera med djur" not in [item[0] for item in self.visitor.cart]:
            messagebox.showwarning("Tillval saknas", "Du har inte köpt tillvalet för att interagera med djur.")
            return
        messagebox.showinfo("Interaktion", "Du har interagerat med ett djur!")

    def feed_animal(self):
        """Simulerar att mata djur."""
        if not self.visitor or "Mata djur" not in [item[0] for item in self.visitor.cart]:
            messagebox.showwarning("Tillval saknas", "Du har inte köpt tillvalet för att mata djur.")
            return
        messagebox.showinfo("Matning", "Du har matat ett djur!")

class SelectVisitorPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
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

        # Besökarknappar
        self.visitor_buttons_frame = tk.Frame(self, bg="white")
        self.visitor_buttons_frame.pack(pady=20)

    def update_visitors(self):
        """Uppdaterar vyn med besökarknappar."""
        # Rensa gamla knappar
        for widget in self.visitor_buttons_frame.winfo_children():
            widget.destroy()

        # Om inga besökare finns
        if not self.zoo.visitors:
            self.message_label.config(text="Inga besökare har registrerats.")
            return
        else:
            self.message_label.config(text="")

        # Skapa knappar för varje besökare
        for visitor in self.zoo.visitors:
            tk.Button(self.visitor_buttons_frame, text=f"{visitor.name} - Budget: {visitor.budget:.2f} SEK",
                      bg="lightblue", font=("Arial", 12),
                      command=lambda v=visitor: self.select_visitor(v)).pack(pady=5)

    def select_visitor(self, visitor):
        """Logga in vald besökare och gå till utforskningssidan."""
        self.controller.frames["ExploreParkPage"].set_visitor(visitor)
        self.controller.show_page("ExploreParkPage")


class DetailedAnimalPage(tk.Frame):
    def __init__(self, parent, controller, zoo):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.zoo = zoo

        # Tillbaka-knapp (pil)
        back_button = tk.Button(self, text="←", font=("Arial", 16), bg="lightgray",
                                command=lambda: controller.show_page("ExploreParkPage"))
        back_button.place(x=10, y=10)

        # Titel
        tk.Label(self, text="Detaljerad info om djur", font=("Arial", 20), bg="white").pack(pady=10)

        # Frame för att hålla detaljer om djur
        self.animal_frame = tk.Frame(self, bg="white")
        self.animal_frame.pack(fill="both", expand=True)

    def display_animals(self):
        """Visar alla djur i detaljerad vy."""
        for widget in self.animal_frame.winfo_children():
            widget.destroy()  # Rensa tidigare widgets

        for animal in self.zoo.animals:
            # Ram för varje djur
            frame = tk.Frame(self.animal_frame, bg="lightcoral", pady=10, padx=10)
            frame.pack(pady=10, fill="x", padx=20)

            # Bild på djuret
            try:
                image = tk.PhotoImage(file=animal.image_path).subsample(4)  # Anpassa storleken
                image_label = tk.Label(frame, image=image, bg="lightcoral")
                image_label.image = image  # Förhindra garbage collection
                image_label.pack(side="left", padx=10)
            except Exception as e:
                print(f"Fel att ladda bild för {animal.name}: {e}")
                tk.Label(frame, text="[Bild saknas]", bg="lightcoral").pack(side="left", padx=10)

            # Information om djuret
            info_text = f"Art: {animal.get_species()}\nNamn: {animal.name}\nÅlder: {animal.age}\nFavoritmat: {animal.favorite_food}"
            tk.Label(frame, text=info_text, font=("Arial", 12), bg="lightcoral", justify="left").pack(side="left",
                                                                                                      padx=10)

            # Knappar för mata och interagera
            button_frame = tk.Frame(frame, bg="lightcoral")
            button_frame.pack(side="right", padx=10)

            tk.Button(button_frame, text="Mata djur", bg="red", fg="white",
                      command=lambda a=animal: self.feed_animal(a)).pack(pady=5)
            tk.Button(button_frame, text="Interagera", bg="red", fg="white",
                      command=lambda a=animal: self.interact_with_animal(a)).pack(pady=5)

    def feed_animal(self, animal):
        """Funktion för att mata djuret."""
        food = simpledialog.askstring("Mata djur", f"Vad vill du mata {animal.name} med?")
        if food:
            result = animal.eat(food)
            messagebox.showinfo("Matningsresultat", result)

    def interact_with_animal(self, animal):
        """Funktion för att interagera med djuret."""
        result = animal.interact()
        messagebox.showinfo("Interaktion", result)
