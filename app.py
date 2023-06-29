import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb

root = ttkb.Window(themename='darkly', size=(400, 200))
root.title('Metric Convertert')

main_frame = ttk.Frame(root)
main_frame.grid()

feet_value = tk.StringVar()
meters_value = tk.StringVar()

feet_label = ttkb.Label(main_frame,
                        text='Feet:',
                        font=('Helvetica', 18))
feet_label.grid(column=0, row=1, padx=5, pady=5)

feet_display = ttkb.Label(main_frame,
                          textvariable=feet_value,
                          font=('Helvetica', 18))
feet_display.grid(column=1, row=1, padx=5, pady=5)

meters_label = ttkb.Label(main_frame,
                          text='Meters:',
                          font=('Helvetica', 18))
meters_label.grid(column=0, row=0, padx=5, pady=5)

meters_input = ttkb.Entry(main_frame,
                          textvariable=meters_value,
                          bootstyle='success',
                          font=('Helvetica', 18))
meters_input.grid(column=1, row=0, padx=5, pady=5)
meters_input.focus()


def convert():
    try:
        value = float(meters_value.get())
        feet_value.set('%.3f' % (value * 3.28084))
    except ValueError:
        pass


btn_convert = ttk.Button(main_frame,
                         text='Convert',
                         command=convert,
                         bootstyle='danger')
btn_convert.grid(column=0, row=2, columnspan=2)

root.mainloop()
