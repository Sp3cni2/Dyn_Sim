import tkinter
from tkinter import ttk

from prototype.Builders.PayloadBuilder import PayloadBuilder
from prototype.Builders.TankBuilder import TankBuilder
from prototype.Builders.FuelBuilder import FuelBuilder
from prototype.Builders.EngineBuilder import EngineBuilder
from prototype.Builders.ManifoldBuilder import ManifoldBuilder


def make_window():
    fuels = tkinter.Tk()
    frame = ttk.Frame(fuels, padding=10)
    frame.grid()
    ttk.Button(frame, text="Quit", command=fuels.destroy).grid(column=1, row=0)
    fuels.mainloop()
    pass

x=[]
root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Fuel Setup", command=make_window).grid(column=1, row=1)
ttk.OptionMenu(frm, variable=x).grid(column=2, row=0)
root.mainloop()
# build fuel button:

