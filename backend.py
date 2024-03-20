
class Compound_intr:
    #pvalue = input()
    def __init__(self,pvalue,interest,friq,time):
        self.pvalue = pvalue
        self.interest = interest
        self.friq = friq
        self.time = time

    def set_pvalue(self,pv):#present value
        if type(pv) in (int, float):
            self.pvalue = pv
        else:
            raise ValueError("It has to be a number")

    def set_interest(self,i):#growt rate
        if type(i) in (int, float):
            self.interest = i
        else:
            raise ValueError("It has to be a number")

    def set_friq(self,f):#friquentcy
        if type(f) in (int, float):
            self.friq = f
        else:
            raise ValueError("It has to be an integer")

    def set_time(self,t):#time(period)
        if type(t) in (int, float):
            self.time = t
        else:
            raise ValueError("It has to be a number")

    def get_coump_int(self): # finds compound interest
        return self.pvalue*(1+(self.interest/100)/(self.friq))**self.time


class WACC:# waighted average cost fo capital
    def __init__(self, i_expense, tl_debt, i_tax_expense, i_before_tax, cap, beta, rfr = 0.0345, market_rtrn = 0.09, ):
        self.i_expense = i_expense
        self.tl_debt = tl_debt
        self.i_tax_expense = i_tax_expense
        self.i_before_tax = i_before_tax
        self.cap = cap
        self.beta = beta
        self.rfr = rfr
        self.market_rtrn = market_rtrn

    def set_beta(self,b):
        self.beta = b

    def set_tl_debt(self, debt):# total debt
        self.tl_debt = debt

    def set_i_tax_expense(self, tax):#income tax expense
        self.i_tax_expense = tax

    def set_i_before_tax(self, bef_tax):#income before tax
        self.i_before_tax = bef_tax

    def set_i_expense(self,i):#interest expense
        self.i_expense = i

    def set_cap(self,c):#capitalisation
        self.cap = c

    def cost_of_debt(self):#find cost of debt
        return self.i_expense/self.tl_debt

    def effective_t_rate(self):
        return self.i_tax_expense/self.i_before_tax

    def get_cost_of_debt_aftTax(self):#cost of debt after tax
        return self.cost_of_debt()*(1 - self.effective_t_rate())

    def get_cost_of_equity(self):
        return (self.beta + self.rfr) * (self.market_rtrn - self.rfr)

    def debt_to_total(self):
        return self.tl_debt / (self.tl_debt + self.cap)

    def cap_to_total(self):
        return self.cap / (self.tl_debt + self.cap)

    def get_wacc(self): # returns waighted average cost of capital
        return (self.get_cost_of_debt_aftTax() * self.debt_to_total())+ (self.get_cost_of_equity() * self.cap_to_total())


class Discount(WACC, Compound_intr):
#discounting future value (compound interest) by wacc
    def rate_of_d(self):#discount rate (1+wacc)^period
        return (1 + self.get_wacc())**self.time

    def discounting(self):#FV/discount rate
        return self.get_coump_int() / self.rate_of_d()

disc = Discount(1,1,1,1,1,1)

disc.set_beta(2)
disc.set_tl_debt(212000)
disc.set_i_before_tax(777000)
disc.set_i_tax_expense(121000)
disc.set_i_expense(29000)
disc.set_cap(2387000)

disc.set_pvalue(1000)
disc.set_interest(30)
disc.set_friq(1)
disc.set_time(3)

print(f"Future value is {disc.get_coump_int()}$")

print(f"WACC is {disc.get_wacc()*100}%")

print(f"Discounted cash flow is: {disc.discounting()}$ over: {disc.time} years")






