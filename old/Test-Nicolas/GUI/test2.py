import tkinter as tk

def show_entry_fields():
    print("Path to the exe %s\nPath to the infected exe %s\nName of the section %s" % (e1.get(), e2.get(), e3.get()))

master = tk.Tk()
tk.Label(master, 
         text="Path to the exe").grid(row=0)
tk.Label(master, 
         text="Path to the infected exe").grid(row=1)
tk.Label(master, 
         text="Name of the section").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Infect', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()
