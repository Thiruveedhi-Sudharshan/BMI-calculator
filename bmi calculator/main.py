import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert height from cm to meters

        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numeric values for weight and height.")

# GUI setup
app = tk.Tk()
app.title("BMI Calculator")

weight_label = tk.Label(app, text="Weight (kg):",width=30,bg='orange')
weight_label.pack(pady=10)

weight_entry = tk.Entry(app)
weight_entry.pack(pady=10)

height_label = tk.Label(app, text="Height (cm):",width=30,bg='green')
height_label.pack(pady=10)

height_entry = tk.Entry(app)
height_entry.pack(pady=10)

calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi,width=30,bg='pink')
calculate_button.pack(pady=10)

result_label = tk.Label(app, text="",width=30,bg='yellow')
result_label.pack(pady=10)

app.mainloop()
