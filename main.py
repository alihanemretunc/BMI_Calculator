import tkinter
import tkinter.messagebox as messagebox

# Settings
bmi_window = tkinter.Tk()
bmi_window.title("BMI Calculator")
bmi_window.minsize(width=600, height=600)
FONT = ("Calibri", 16, 'normal')

# Label
my_label = tkinter.Label(text="Enter Your Weight (kg)", font=FONT)
my_label.place(x=210, y=200)

my_label2 = tkinter.Label(text="Enter Your Height (cm)", font=FONT)
my_label2.place(x=210, y=265)

# Entry
my_entry = tkinter.Entry(width=20)
my_entry.place(x=300-50, y=300-62)
my_entry.focus()

my_entry2 = tkinter.Entry(width=20)
my_entry2.place(x=300-50, y=365-62)

# Label for BMI message
bmi_label = tkinter.Label(text="", font=('Calibri', 16, 'italic'))
bmi_label.place(x=130, y=380)

# Button and showing the final message
def get_bmi(weight, height):
    bmi = round(weight / ((height/100) ** 2), 1)
    return bmi

def click_button():
    weight_str = my_entry.get()
    height_str = my_entry2.get()

    if not weight_str or not height_str:
        messagebox.showerror("Error", 'Please enter both weight and height.')
        return None

    try:
        weight = float(weight_str)
        height = float(height_str)

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", 'Weight and height must be positive.')
            return None

        bmi = get_bmi(weight, height)

        if bmi < 18.5:
            bmi_label.config(text=f'Your BMI is {bmi}. You are under weight.')
        elif bmi >= 18.5 and bmi < 25:
            bmi_label.config(text=f'Your BMI is {bmi}. You have normal weight.')
        elif bmi >= 25 and bmi < 30:
            bmi_label.config(text=f'Your BMI is {bmi}. You are over weight.')
        elif bmi >= 30 and bmi < 35:
            bmi_label.config(text=f'Your BMI is {bmi}. You are in obesity class 1.')
        elif bmi >= 35 and bmi < 40:
            bmi_label.config(text=f'Your BMI is {bmi}. You are in obesity class 2.')
        else:
            bmi_label.config(text=f'Your BMI is {bmi}. You are in extreme obesity class.')

    except ValueError:
        messagebox.showerror('Error', 'Invalid input. Please enter valid numbers.')

my_button = tkinter.Button(text='Calculate', command=click_button)
my_button.place(x=280, y=340)

bmi_window.mainloop()