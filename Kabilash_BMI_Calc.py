import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

def calc_bmi(weight,height):
    """
    Calculating the BMI based on weight and height.
    Returns the value.
    """
    bmi=weight/(height**2)
    return bmi


def bmi_conditions(bmi):
    """
    Using Conditional Structures to determine the type ,your BMI value has.
    Returns as string.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def animate_widget(widget, animation, duration=0.1, repeat=5):
    """
    Animates a tkinter widget by applying a sequence of styles repeatedly.
    """
    for _ in range(repeat):
        for style, value in animation:
            widget.configure(**{style: value})
            root.update()
            time.sleep(duration)


def calculate():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    if weight_unit_var.get() == "lbs":
        weight = weight * 0.453592

    if height_unit_var.get() == "feet":
        height = height * 0.3048

    bmi = calc_bmi(weight, height)
    bmi_category = bmi_conditions(bmi)

    bmi_label.config(text="BMI: {:.2f}".format(bmi))
    category_label.config(text="Category: {}".format(bmi_category))

    weight__range = weight_range(height)
    height__range = height_range(weight)

    weight_range_label.config(text="Suggested Weight Range: {:.2f} - {:.2f} kg".format(weight_range[0], weight_range[1]))
    height_range_label.config(text="Suggested Height Range: {:.2f} - {:.2f} meters".format(height_range[0], height_range[1]))

    animate_widget(bmi_label, [("background", "#7C3AED"), ("background", "#1E1B4B")])
    animate_widget(category_label, [("background", "#2563EB"), ("background", "#1E1B4B")])
    animate_widget(weight_range_label, [("background", "#0EA5E9"), ("background", "#1E1B4B")])
    animate_widget(height_range_label, [("background", "#06B6D4"), ("background", "#1E1B4B")])

    animate_widget(calculate_button, [("background", "#7C3AED"), ("background", "#4F46E5")])


def weight_range(height):
    """
    weight based on the height.
    """
    lower_limit = 18.5 * (height**2)
    upper_limit = 24.9 * (height**2)
    return lower_limit, upper_limit


def height_range(weight):
    """
    range based on the weight.
    """
    lower_limit = (weight / 24.9) ** 0.5
    upper_limit = (weight / 18.5) ** 0.5
    return lower_limit, upper_limit


root = tk.Tk()
root.title("BMI Calculator By Kabilash_L_R")
root.geometry("600x400")
root.configure(bg="#f7baba")

style = ttk.Style()
style.configure('TButton', background='#4F46E5', foreground='#B8C9FF', font=("Helvetica", 12, "bold"))
style.map('TButton', background=[('active', '#7C3AED')])
style.configure('TFrame', background='#1E1B4B')
style.configure('TLabel', background='#1E1B4B', foreground="#8AA5FF", font=("Helvetica", 12))
style.configure('TEntry', fieldbackground='#2D2A6E', foreground='#A5C8F0', insertcolor='#7C3AED')
style.configure('TCombobox', fieldbackground='#2D2A6E', foreground='#A5C8F0', background='#2D2A6E')
style.map('TCombobox', fieldbackground=[('readonly', '#2D2A6E')], foreground=[('readonly', '#A5C8F0')])
root.configure(bg='#1E1B4B')

main_frame = ttk.Frame(root, padding="20", style='TFrame')
main_frame.pack(expand=True, fill="both")

weight_label = ttk.Label(main_frame, text="Weight:", font=("Helvetica", 12), style='TLabel')
weight_label.grid(row=0, column=0, sticky="w")

weight_entry = ttk.Entry(main_frame, style='TEntry')
weight_entry.grid(row=0, column=1)
weight_entry_animation = [("background", "#7C3AED"), ("background", "#2D2A6E")]

weight_unit_var = tk.StringVar(value="kgs")
weight_unit_combo = ttk.Combobox(main_frame, textvariable=weight_unit_var, values=("kgs", "lbs"), state="readonly", width=5)
weight_unit_combo.grid(row=0, column=2, padx=5)
weight_unit_combo_animation = [("background", "#7C3AED"), ("background", "#2D2A6E")]

height_label = ttk.Label(main_frame, text="Height:", font=("Helvetica", 12), style='TLabel')
height_label.grid(row=1, column=0, sticky="w")

height_entry = ttk.Entry(main_frame, style='TEntry')
height_entry.grid(row=1, column=1)
height_entry_animation = [("background", "#7C3AED"), ("background", "#2D2A6E")]

height_unit_var = tk.StringVar(value="meters")
height_unit_combo = ttk.Combobox(main_frame, textvariable=height_unit_var, values=("meters", "feet"), state="readonly", width=5)
height_unit_combo.grid(row=1, column=2, padx=5)
height_unit_combo_animation = [("background", "#7C3AED"), ("background", "#2D2A6E")]

calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate, style='TButton')
calculate_button.grid(row=2, column=0, columnspan=3, pady=10)


category_label = ttk.Label(main_frame, text="Category: ", font=("Helvetica", 12), style='TLabel')
category_label.grid(row=4, column=0, sticky="w")

bmi_label = ttk.Label(main_frame, text="BMI: ", font=("Helvetica", 12), style='TLabel')
bmi_label.grid(row=3, column=0, sticky="w")


weight_range_label = ttk.Label(main_frame, text="Suggested Weight Range: ", font=("Helvetica", 12), style='TLabel')
weight_range_label.grid(row=5, column=0, sticky="w")

height_range_label = ttk.Label(main_frame, text="Suggested Height Range: ", font=("Helvetica", 12), style='TLabel')
height_range_label.grid(row=6, column=0, sticky="w")

root.mainloop()