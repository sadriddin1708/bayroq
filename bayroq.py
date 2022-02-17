import tkinter as tk
oyna = tk.Tk()
frame1 = tk.Frame(master = oyna, width = 500, height = 100, bg = "blue")
frame1.pack()

frame2 = tk.Frame(master = oyna, width = 500, height = 15, bg = "red")
frame2.pack()

frame3 = tk.Frame(master = oyna, width = 500, height = 100, bg = "white")
frame3.pack()

frame4 = tk.Frame(master = oyna, width = 500, height = 15, bg = "red")
frame4.pack()

frame5 = tk.Frame(master = oyna, width = 500, height = 100, bg = "green")
frame5.pack()

oyna.mainloop()