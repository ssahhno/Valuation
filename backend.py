class Compound_intr:
    #pvalue = input()

    def __init__(self,pvalue,interest,friq,time):
        self.pvalue = pvalue
        self.interest = interest
        self.friq = friq
        self.time = time

    def set_pvalue(self,pv):
        if type(pv) in (int, float):
            self.pvalue = pv
        else:
            raise ValueError("It has to be a number")

    def set_interest(self,i):
        if type(i) in (int, float):
            self.interest = i
        else:
            raise ValueError("It has to be a number")

    def set_friq(self,f):
        if type(f) in (int, float):
            self.friq = f
        else:
            raise ValueError("It has to be an integer")

    def set_time(self,t):
        if type(t) in (int, float):
            self.time = t
        else:
            raise ValueError("It has to be a number")

    def get_coump_int(self):
        return self.pvalue*(1+(self.interest/100)/(self.friq))**self.time

person_1 = Compound_intr(1,1,1,1)

person_1.set_pvalue(1000)
person_1.set_interest(30)
person_1.set_friq(1)
person_1.set_time(3)

print(person_1.get_coump_int())

class WACC:
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

    def set_tl_debt(self, debt):
        self.tl_debt = debt

    def set_i_tax_expense(self, tax):
        self.i_tax_expense = tax

    def set_i_before_tax(self, bef_tax):
        self.i_before_tax = bef_tax

    def set_i_expense(self,i):
        self.i_expense = i

    def set_cap(self,c):
        self.cap = c

    def cost_of_debt(self):
        return self.i_expense/self.tl_debt

    def effective_t_rate(self):
        return self.i_tax_expense/self.i_before_tax

    def get_cost_of_debt_aftTax(self):
        return self.cost_of_debt()*(1 - self.effective_t_rate()) * 100

    def get_cost_of_equity(self):
        return (self.beta + self.rfr) * (self.market_rtrn - self.rfr)

    def debt_to_total(self):
        return self.tl_debt / (self.tl_debt + self.cap)

    def cap_to_total(self):
        return self.cap / (self.tl_debt + self.cap)

    def get_wacc(self):
        return (self.get_cost_of_debt_aftTax() * self.debt_to_total())+ (self.get_cost_of_equity() * self.cap_to_total()) * 100

Debt = WACC(1,1,1,1,1,1)

Debt.set_beta(2)
Debt.set_tl_debt(212000)
Debt.set_i_before_tax(777000)
Debt.set_i_tax_expense(121000)
Debt.set_i_expense(29000)
Debt.set_cap(2387000)

print(Debt.get_wacc())

class Discount(Compound_intr, WACC):
    def __init__(self):
        pass

    def get(self):
        return self.get_wacc()

disc = Discount()

print(disc.get())




          





