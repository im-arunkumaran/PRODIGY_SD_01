import tkinter as tk
from tkinter import messagebox

# -------- Main Logic --------

def convert():  #Button
    try:
        t = float(entry.get())  # get temperature
        u = unit.get()  # get selected unit

        if u == "Celsius":
            result = f"Fahrenheit: {(t*9/5)+32:.2f} °F\nKelvin: {t+273.15:.2f} K"

        elif u == "Fahrenheit":
            c = (t-32)*5/9
            result = f"Celsius: {c:.2f} °C\nKelvin: {c+273.15:.2f} K"

        else:  # Kelvin
            c = t-273.15
            result = f"Celsius: {c:.2f} °C\nFahrenheit: {(c*9/5)+32:.2f} °F"

        output.config(text=result)  # shows result

    except:
        messagebox.showerror("Error", "Enter a valid number")


# -------- GUI setup --------

root = tk.Tk()
root.title("Temp Converter")
root.geometry("350x300")
root.configure(bg="black")

# main body frame
body = tk.Frame(root, bg="white", padx=20, pady=20)
body.pack(expand=True, fill="both", padx=5, pady=5)

tk.Label(body, text="Temperature Converter", 
         font=("Arial", 16, "bold"), bg="white").pack(pady=10)

entry = tk.Entry(body, font=("Arial", 12), justify="center")
entry.pack(pady=5)

unit = tk.StringVar(value="Celsius")

for i in ["Celsius", "Fahrenheit", "Kelvin"]:
    tk.Radiobutton(body, text=i, variable=unit, value=i,
                   bg="white").pack(anchor="w")

tk.Button(body, text="Convert", command=convert,
          bg="black", fg="white", width=15).pack(pady=10)

output = tk.Label(body, text="", font=("Arial", 12),
                  bg="white", fg="black")
output.pack()

root.mainloop()
