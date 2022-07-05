user_dict = {}

class ROI:
    def __init__(self):
        pass

    def income(self):
        self.username = input('Please enter a username to calculate your ROI!: ')
        print(f'Hi, {self.username.title()}! Thank you for using my calculator.')
        user_dict[self.username] = self
        self.income = int(input('How much is your monthly rental income?: $'))
        self.full_income = (int(self.income))
        continue_on = input('Would you like to continue to expenses? Type yes to continue or quit to exit. ')
        if continue_on == 'yes':
            self.expenses()
        elif continue_on == 'quit':
            exit
        else:
            print('Sorry, invalid input!')

    def expenses(self):
        self.taxes = float(input('Please input how much you pay for taxes: '))
        self.insurance = int(input('How much does your insurance cost you?: '))
        self.utilites = int(input('Enter your total utilities cost: '))
        self.hoa = int(input('How much does the HOA cost you? '))
        self.lawn_service = int(input('How much will lawn services cost you? '))
        self.vacancy = int(input('How much do you want to set aside monthly to account for vacancy? '))
        self.repairs = int(input('How much are you putting away monthly for repairs? '))
        self.mortgage = int(input('How much is your mortgage payment? '))
        self.total_expenses = (self.taxes) + (self.utilites) + (self.hoa) + (self.lawn_service) + (self.vacancy) + (
            self.repairs) + (self.mortgage) + (self.insurance)
        print(f"Your monthly expenses are: ${self.total_expenses} a month.")
        continue1 = input('Would you like to view your cash flow? Type yes to continue or quit to exit. ')
        if continue1 == 'yes':
            self.cashflow()
        elif continue1 == 'quit':
            exit

    def cashflow(self):
        self.incomes = int(self.full_income) - int(self.total_expenses)
        print(f" Here is your total cash flow: {self.incomes}")
        continue2 = input('Would you like to find your cash on cash return? Type yes to continue or quit to exit. ')
        if continue2 == 'yes':
            self.cash_roi()
        elif continue2 == 'quit':
            exit

    def cash_roi(self):
        self.down_payment = input('How much was your down payment?: ')
        self.closing_cost = input('How much was your closing costs?: ')
        self.repair_budget = input('How much did you put in to repair this property?: ')
        self.total_investment = int(self.down_payment) + int(self.closing_cost) + int(self.repair_budget)
        print(f"Great! Your total investments have totaled: {self.total_investment} !")
        self.annual_cash_flow = 12 * int(self.total_expenses)
        print(f" Here is your annual cash flow: ${self.annual_cash_flow}")
        self.cash_roi = float(self.annual_cash_flow) / float(self.total_investment)
        self.cash_roi = float(self.cash_roi) * float(100)
        print(f'Your R.O.I. is: {self.cash_roi}%!')


cash = ROI()
cash.income()