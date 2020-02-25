import tkinter as tk
import  random
from sql import SqlInject

LARGE_FONT = ("Verdana", 12)
data = SqlInject()


class GuiFood(tk.Tk):

    def __init__(self, data=data, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.database = data
        self.value1 = tk.StringVar()
        self.user_choice = "purée"
        self.user_product_name = "Purée de Pois Cassés "
        self.user_product_data = []
        self.subs_product_data = []
        self.frames = {}
        self.all_frames = (StartPage, ChooseCate, ChooseFood, FoodInfo, SubsFood, SaveSearch)

        for F in self.all_frames:
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Substituer un aliment",
                           command=lambda: controller.show_frame(ChooseCate))
        button.pack()

        button2 = tk.Button(self, text="Retrouver mes aliments substitués.",
                            command=lambda: controller.show_frame(SaveSearch))
        button2.pack()


class ChooseCate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choix de l'aliment a substituer", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        vals = controller.database.get_category()
        etiqs = controller.database.get_category()

        self.varCatch = tk.StringVar()  # define type of variable catching

        self.choice = None

        def get_value():
            controller.user_choice = self.varCatch.get()
            frame = ChooseFood(parent, controller)
            controller.frames[ChooseFood] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        for i in range(len(vals)):
            b = tk.Radiobutton(self, variable=self.varCatch, text=etiqs[i], value=vals[i],
                               command=lambda: [get_value(), controller.show_frame(ChooseFood)])
            b.pack(side="top", expand=1)

        button1 = tk.Button(self, text="Retour au menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class ChooseFood(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        self.choice_cate = self.controller.user_choice
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=str(self.choice_cate), font=LARGE_FONT)
        label.pack(side="top")
        food_data = controller.database.get_categorized_food(self.choice_cate)
        list = tk.Listbox(self)
        for i in food_data:
            list.insert(i[0], i[2])
        list.pack()

        button2 = tk.Button(self, text="Afficher les infos",
                            command=lambda:[info_food(), controller.show_frame(FoodInfo)])
        button2.pack()
        button1 = tk.Button(self, text="Retour au Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        def info_food():
            controller.user_product_name = list.get(list.curselection())
            frame = FoodInfo(parent, controller)
            controller.frames[FoodInfo] = frame
            frame.grid(row=0, column=0, sticky="nsew")

class FoodInfo(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.choice_info = self.controller.user_product_name
        tk.Frame.__init__(self, parent)
        food_data = controller.database.get_data_product(column="product_name", search=self.choice_info)
        column_name = ["nutriscore","nom du produit","Nom générique","Magasin","Marques","url"]
        for col, data in zip(column_name, food_data[0][1:-1]):
            label = tk.Label(self, text=str(col)+" : "+str(data)+"\n", font=LARGE_FONT)
            label.pack(side="top")
        button1 = tk.Button(self, text="Retour au Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Substituer cet aliment",
                            command=lambda:[substitute_food(), controller.show_frame(SubsFood)])
        button2.pack()
        def substitute_food():
            controller.user_product_data = food_data
            frame = SubsFood(parent, controller)
            controller.frames[SubsFood] = frame
            frame.grid(row=0, column=0, sticky="nsew")
class SubsFood(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.cate = self.controller.user_choice
        tk.Frame.__init__(self, parent)
        food_data = controller.database.get_substitute(self.cate)[random.randrange(0,2)]
        column_name = ["nutriscore", "nom du produit", "Nom générique", "Magasin", "Marques", "url"]
        for col, data in zip(column_name, food_data[1:-1]):
            label = tk.Label(self, text=str(col)+" : "+str(data)+"\n", font=LARGE_FONT)
            label.pack(side="top")
        button1 = tk.Button(self, text="Retour au Menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Sauvegarder?",
                            command= lambda: save_search())
        button2.pack()
        def save_search():
            prod_id = controller.user_product_data[0][0]
            controller.database.save_substitute(product_id=int(prod_id), substitute_id=int(food_data[0]))
            frame = StartPage(parent, controller)
            controller.frames[StartPage] = frame
            frame.grid(row=0, column=0, sticky="nsew")

class SaveSearch(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        self.save = controller.database.get_save_substitute()
        print(str(self.save))
        tk.Frame.__init__(self, parent)
        for i in self.save:
            product_name = controller.database.get_data_product(search=i[1])[0][2]
            substitute_name = controller.database.get_data_product(search=i[2])[0][2]
            label = tk.Label(self, text=str(product_name)+" ==> "+str(substitute_name)+"\n", font=LARGE_FONT)
            label.pack(side="top")

if __name__ == '__main__':
    app = GuiFood()
    app.mainloop()
