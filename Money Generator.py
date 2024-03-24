import tkinter as tk
from tkinter import ttk

def set_interest():
    interest = float(Enter_Interest.get())/100
    return interest

def set_present_v():
    present_value = float(Enter_Pvalue.get())
    return present_value

def set_time():
    time = float(Enter_Time.get())
    return time

def set_freq():
    freq = float(Enter_Freq.get())
    return freq

def get_result():
    future_value = set_present_v()*(1 + set_interest()/set_freq())**set_time()
    result['text'] = f"The Future value over {set_time()} is: {future_value}$"

    return result

window = tk.Tk()

window.geometry("1200x600")

window.resizable(width = False, height = False)

window.title("Money Generator")


compound_lable = tk.Label(window, text = "Compound Interest", font = ("Arial Bald", 13), fg = "black")
compound_lable.place(x = 70 , y = 25)

PresentValue = tk.Label(window, text = "Present Value", font = ("Arial Bald", 9), fg = "black")
PresentValue.place(x = 90 , y = 70)

Enter_Pvalue = tk.Entry(fg = "black", width = "10",)
Enter_Pvalue.place(x = 95, y = 90)

Interest = tk.Label(window, text = "Interest", font = ("Arial Bald", 9), fg = "black")
Interest.place(x = 200 , y = 70)

Enter_Interest = tk.Entry(fg = "black", width = "10",)
Enter_Interest.place(x = 193, y = 90)

Time = tk.Label(window, text = "Time(In years)", font = ("Arial Bald", 9), fg = "black")
Time.place(x = 275 , y = 70)

Enter_Time = tk.Entry(fg = "black", width = "10",)
Enter_Time.place(x = 283, y = 90)

Frequency = tk.Label(window, text = "Times per year", font = ("Arial Bald", 9), fg = "black")
Frequency.place(x = 390 , y = 70)

Enter_Freq = tk.Entry(fg = "black", width = "10",)
Enter_Freq.place(x = 400, y = 90)

Calculate_FV = tk.Button(window, text = "Calculate",command = get_result, width = 15 , height = 2)
Calculate_FV.place(x = 500, y = 75)



result = tk.Label(window)
result.place(x = 650, y = 85)




window.mainloop()
