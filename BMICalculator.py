import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=300)

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        sonuc_label.config(text="Enter your weight and height!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            sonuc_label.config(text=result_string)
        except:
            sonuc_label.config(text="Enter a valid number")
# first label
your_weight = tkinter.Label(text="Enter your weight (kg)", font=('Arial', 10, "bold"))
your_weight.config(fg="blue")
your_weight.pack()
weight_input = tkinter.Entry(width=7)
weight_input.pack()

#second label
your_height = tkinter.Label(text="Enter your height(cm)", font=('Arial', 10, "bold"))
your_height.config(fg="blue")
your_height.pack()
height_input = tkinter.Entry(width=7)
height_input.pack()

#button
hesapla_button = tkinter.Button(text="Calculate!", width=15,command=calculate_bmi)
hesapla_button.pack()

sonuc_label = tkinter.Label()
sonuc_label.pack()

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string

window.mainloop()
