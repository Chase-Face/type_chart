import tkinter as tk
from tkinter import messagebox
from subprocess import Popen, PIPE

def run_main_file(pokemon_name):
    try:
        process = Popen(['python', 'type_chart.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate(input=pokemon_name.encode())
        if error:
            messagebox.showerror("Error", error.decode())
        else:
            messagebox.showinfo("Results", output.decode())
    except Exception as e:
        messagebox.showerror("Error", str(e))

def submit_pokemon():
    pokemon_name = entry.get()
    if pokemon_name:
        run_main_file(pokemon_name)
    else:
        messagebox.showwarning("Warning", "Please enter a Pokémon name.")

# Create main window
root = tk.Tk()
root.title("Pokémon Type Chart")

# Create input field
entry = tk.Entry(root)
entry.pack(pady=10)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_pokemon)
submit_button.pack(pady=5)

# Run the main loop
root.mainloop()
