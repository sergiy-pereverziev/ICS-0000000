import sys, tkinter as tk
from tkinter import Toplevel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def main():
    canvas_width = 420
    canvas_height = 250

    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <measurements_file_name>")
        return

    try:
        file_name = sys.argv[1]

        with open(file_name, "r") as file:
            contents = file.read()
            data = list(map(lambda line: line.split(" "), filter(len, contents.split("\n"))))
            if not len(data):
                print("Empty list of measurements")
                return
            
            measurements = []
            for line in data:
                if (len(line) < 2):
                    raise ValueError(f"Please provide at least one measurement for the axis {line[0]}")
                
                measurements.append((line[0], list(map(lambda value: float(value), line[1:]))))
        
    except Exception as e:
        print(f"File error: {e}")
        return

    root = tk.Tk()
    root.geometry(f"{canvas_width}x{canvas_height}")
    root.title("Measurement chart")
    root.configure(bg="orange")

    fig, ax = plt.subplots(figsize=(4, 2))

    for (resistor, currents) in measurements:
        ax.plot(range(1, len(currents) + 1), currents, marker='o', label=resistor)

    ax.set_title("Current measurements chart for resistors")
    ax.set_xlabel("Measurement No.")
    ax.set_ylabel("Amperage")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().place(x=10, y=10)

    root.mainloop()

if __name__ == "__main__":
    main()