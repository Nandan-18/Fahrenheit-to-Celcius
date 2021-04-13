import tkinter as tk


def FtoC():
    fahrenheit = temperature_input.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    converted_value["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


# Setting-up the window
window = tk.Tk()
window.title("Temperature Converter")

frm_entry = tk.Frame(master=window)

temperature_input = tk.Entry(master=frm_entry,
                             width=10
                             )

temp_label = tk.Label(master=frm_entry,
                      text="\N{DEGREE FAHRENHEIT}"
                      )

temperature_input.grid(row=0,
                       column=0
                       )

temp_label.grid(row=0,
                column=1,
                )

# Creating the conversion Button and result display Label
convert_button = tk.Button(master=window,
                           text="\N{RIGHTWARDS BLACK ARROW}",
                           command=FtoC
                           )

converted_value = tk.Label(master=window,
                           text="\N{DEGREE CELSIUS}"
                           )

frm_entry.grid(row=0,
               column=0,
               padx=10
               )

convert_button.grid(row=0,
                    column=1,
                    pady=10
                    )

converted_value.grid(row=0,
                     column=2,
                     padx=10
                     )

window.mainloop()
