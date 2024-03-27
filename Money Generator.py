import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

    if freq != 0:
        return freq
    else:
       tk.messagebox.showinfo("Error", ("Frequency cannot be zero"))

def get_compoun_interest():
    future_value = set_present_v()*(1 + set_interest()/set_freq())**set_time()
    return future_value

def result_compoun_int():
    result['text'] = f"The Future value over {round(set_time())} years is: {round(get_compoun_interest())}$"
    return result


def set_IntrExpense():
    inter_expense = float(Enter_InterExpense.get())
    return inter_expense

def set_Total_debt():
    total_debt = float(Enter_TlDebt.get())
    return total_debt

def set_IncomeTaxExpense():
    income_t_expense = float(Enter_IncomeTaxExp.get())
    return income_t_expense

def set_IncBefTax():
    income_bef_tax = float(Enter_IncBefTax.get())
    return income_bef_tax

def set_cap():
    cap = float(Enter_Cap.get())
    return cap

def set_beta():
    beta = float(Enter_Beta.get())
    return beta

def set_RiskFreeRate():
    risk_f_rate = float(Enter_RiskFRate.get())
    return risk_f_rate/100

def set_MarketReturn():
    market_return = float(Enter_MReturn.get())
    return market_return/100

def get_cost_of_debt():
    return set_IntrExpense()/set_Total_debt()

def get_effective_tax_rate():
    return set_IncomeTaxExpense()/set_IncBefTax()

def get_debt_total():
    return set_Total_debt()/(set_Total_debt() + set_cap())

def get_cap_to_total():
    return set_cap()/(set_Total_debt() + set_cap())

def get_cost_of_debt_aft_tax():
    return get_cost_of_debt()*(1 - get_effective_tax_rate())

def get_cost_of_equity():
    return(set_beta() + set_RiskFreeRate()) * (set_MarketReturn() - set_RiskFreeRate())

def get_wacc():
    wacc = (get_cost_of_debt_aft_tax() * get_debt_total()) + (get_cost_of_equity() * get_cap_to_total())*100
    Wacc_result['text'] = f"WACC is: {round(wacc)}%"

    return Wacc_result

def get_rate_of_disc():
    discount  = float(Enter_DiscRate.get())
    return (1 + discount/100)**set_time()

def get_disc_pv():
    present_value = get_compoun_interest()/get_rate_of_disc()
    discount_result['text'] = f"Present value is: {round(present_value)}"

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

Calculate_FV = tk.Button(window, text = "Calculate",command = result_compoun_int, width = 15 , height = 2)
Calculate_FV.place(x = 500, y = 75)

result = tk.Label(window)
result.place(x = 70, y = 110)


wacc_lable = tk.Label(window, text = "WACC", font = ("Arial Bald", 13), fg = "black")
wacc_lable.place(x = 900 , y = 25)

InterestExpense = tk.Label(window, text = "Interest Expense", font = ("Arial Bald", 9), fg = "black")
InterestExpense.place(x = 910 , y = 70)

Enter_InterExpense = tk.Entry(fg = "black", width = "12",)
Enter_InterExpense.place(x = 1035, y = 72)

TotalDebt = tk.Label(window, text = "Total Debt", font = ("Arial Bald", 9), fg = "black")
TotalDebt.place(x = 910 , y = 105)

Enter_TlDebt = tk.Entry(fg = "black", width = "12",)
Enter_TlDebt.place(x = 1035, y = 107)

IncomeTaxExpense = tk.Label(window, text = "Income Tax Expense", font = ("Arial Bald", 9), fg = "black")
IncomeTaxExpense.place(x = 910 , y = 135)

Enter_IncomeTaxExp = tk.Entry(fg = "black", width = "12",)
Enter_IncomeTaxExp.place(x = 1035, y = 137)

IncomeBeforeTAx = tk.Label(window, text = "Income Before Tax", font = ("Arial Bald", 9), fg = "black")
IncomeBeforeTAx.place(x = 910 , y = 165)

Enter_IncBefTax = tk.Entry(fg = "black", width = "12",)
Enter_IncBefTax.place(x = 1035, y = 167)

Cap = tk.Label(window, text = "Capitalisation", font = ("Arial Bald", 9), fg = "black")
Cap.place(x = 910, y = 195)

Enter_Cap = tk.Entry(fg = "black", width = "12",)
Enter_Cap.place(x = 1035, y = 197)

BetaLable = tk.Label(window, text = "Beta", font = ("Arial Bald", 9), fg = "black")
BetaLable.place(x = 910, y = 220)

Enter_Beta = tk.Entry(fg = "black", width = "12",)
Enter_Beta.place(x = 1035, y = 222)

RiskFreeRate = tk.Label(window, text = "Risk Free Rate", font = ("Arial Bald", 9), fg = "black")
RiskFreeRate.place(x = 910 , y = 245)

Enter_RiskFRate = tk.Entry(fg = "black", width = "12",)
Enter_RiskFRate.place(x = 1035, y = 247)

MarketReturn = tk.Label(window, text = "Market Return", font = ("Arial Bald", 9), fg = "black")
MarketReturn.place(x = 910 , y = 270)

Enter_MReturn = tk.Entry(fg = "black", width = "12",)
Enter_MReturn.place(x = 1035, y = 272)

btn_WACC = tk.Button(window,text= "Find WACC", command = get_wacc ,width = 10, height = 1 )
btn_WACC.place(x = 910, y = 300)

Wacc_result = tk.Label(window)
Wacc_result.place(x = 1035, y = 300)

Discounting_lable = tk.Label(window, text = "Discounting", font = ("Arial Bald", 13), fg = "black")
Discounting_lable.place(x = 630 , y = 25)

DiscoutLable = tk.Label(window, text = "Discount Rate", font = ("Arial Bald", 9), fg = "black")
DiscoutLable.place(x = 640 , y = 70)

Enter_DiscRate = tk.Entry(window, fg = "black", width = "12")
Enter_DiscRate.place(x = 740, y = 72)

btn_discount = tk.Button(window, text= "Discount it!", command = get_disc_pv,width = 10, height = 1 )
btn_discount.place(x = 645, y = 100)

discount_result = tk.Label(window, text = "Result:" , font = ("Arial Bald", 9), fg = "black")
discount_result.place(x = 740, y = 100)




window.mainloop()
