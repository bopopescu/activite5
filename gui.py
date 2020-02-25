# from tkinter import *
#
# class GuiApi(Tk):
#     def __init__(self, food):
#         Tk.__init__(self)
#         self.title("Alimentation saine")
#         self.firstframe = Frame(self)
#         self.choicesframe = Frame(self)
#         self.foodchoicesframe = Frame(self)
#         self.food = food
#
#
#     def firstScreen(self):
#         self.firstframe.pack()
#         self.value =StringVar()
#         self.tick1 = Radiobutton(self.firstframe, text="Substituer un aliment", variable=self.value, value=1)
#         self.tick2 = Radiobutton(self.firstframe, text="Retrouver mes aliments substitués.", variable=self.value, value=2)
#         Button(self.firstframe, text ="Quitter", command =self.exit).pack(side = BOTTOM)
#         Button(self.firstframe, text ="OK", command =self.research_food).pack(side = BOTTOM)
#         self.tick1.pack()
#         self.tick2.pack()
#         test = self.value.get()
#         if test != "":
#             print(test)
#
#     def research_food(self):
#         self.firstframe.pack_forget()
#         self.choicesframe.pack()
#         self.listbox = Listbox(self.choicesframe)
#         self.listbox.insert(1,"chocolat")
#         self.listbox.insert(2,"jambon")
#         self.listbox.insert(3,"bonbon")
#         self.listbox.pack()
#         Button(self.choicesframe, text ="OK", command =self.showchoices).pack(side = BOTTOM)
#
#     def showchoices(self):
#         self.choicesframe.pack_forget()
#         self.foodchoicesframe.pack()
#         self.listbox = Listbox(self.foodchoicesframe)
#         index = 1
#         for i in self.food:
#             self.listbox.insert(index, i[2])
#             index += 1
#         self.listbox.pack(fill=X)
#
#
#     def substitute(self):
#         self.research_food
#
#     def exit(self):
#         self.destroy()
#
#
# if __name__ == "__main__":
#     from sql import SqlInject
#     from request_api import ApiOpenFoodFact
#     test = ApiOpenFoodFact("chocolat")
#     tata = SqlInject(test.bdd_dict_list, 'chocolat')
#     food = tata.get_product()
#     toto = GuiApi(food)
#     toto.firstScreen()
#     test=toto.value.get()
#     if test != "":
#         print(test)
#     toto.mainloop()
