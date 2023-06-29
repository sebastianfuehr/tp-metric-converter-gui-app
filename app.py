import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Metric Convertert')

main_frame = ttk.Frame(root)
main_frame.grid()

feet_value = tk.StringVar()
meters_value = tk.StringVar()

feet_label = ttk.Label(main_frame, text='feet')
feet_label.grid(column=0, row=1)

feet_display = ttk.Label(main_frame, textvariable=feet_value)
feet_display.grid(column=1, row=1)

meters_label = ttk.Label(main_frame, text='meters')
meters_label.grid(column=0, row=0)

meters_input = ttk.Entry(main_frame, textvariable=meters_value)
meters_input.grid(column=1, row=0)
meters_input.focus()

def convert():
    try:
        value = float(meters_value.get())
        feet_value.set('%.3f' % (value * 3.28084))
    except ValueError:
        pass

btn_convert = ttk.Button(main_frame, text='Convert', command=convert)
btn_convert.grid(column=0, row=2, columnspan=2)

root.mainloop()