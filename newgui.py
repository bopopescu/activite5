import tkinter as tk


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.shared_data = {
            "choice": tk.StringVar(),
        }
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.value1 = tk.StringVar()
        self.user_choice = ""
        self.frames = {}
        self.all_frames = (StartPage, ChooseCate, ChooseFood)# Results, Substitute, SaveSubs)

        for F in self.all_frames:

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    # def get_page(self, page_class):
    #     return self.frames[page_class]

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Substituer un aliment",
                            command=lambda: controller.show_frame(ChooseCate))
        button.pack()

        button2 = tk.Button(self, text="Retrouver mes aliments substitués.",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class ChooseCate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # self.controller = controller
        label = tk.Label(self, text="Choix de l'aliment a substituer", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        vals = ["jambon", "chocolat", "biscuit"]
        etiqs = ["jambon", "chocolat", "biscuit"]

        self.varCatch = tk.StringVar()    #define type of variable catching

        self.choice = None
        def get_value():
            controller.user_choice = self.varCatch.get()
            frame = ChooseFood(parent,controller)
            controller.frames[ChooseFood] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        for i in range(3):
            b = tk.Radiobutton(self, variable = self.varCatch, text= etiqs[i], value = vals[i], command= lambda : [get_value(), controller.show_frame(ChooseFood)] )
            b.pack(side="top", expand=1)

        button1 = tk.Button(self, text="Retour au menu",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()





        # self.controller.show_frame(ChooseFood)


class ChooseFood(tk.Frame):

    def __init__(self, parent, controller):
        self.controller =controller
        # page1 = self.controller.get_page(ChooseCate)
        self.toto = self.controller.user_choice
        print(self.toto)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=str(self.toto), font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()





app = SeaofBTCapp()
app.mainloop()
