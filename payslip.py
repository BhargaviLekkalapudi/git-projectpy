class Earnings: 
 def __init__(self, basic_salary): 
    self.basic_salary = basic_salary 
    self.da = 0.15 * basic_salary 
    self.hra = 0.45 * basic_salary 
    self.conveyance = 0.10 * basic_salary 
    self.gross_salary = self.basic_salary + self.da + self.hra + self.conveyance 
class Deductions:
 def __init__(self, basic_salary): 
    self.pf = 0.0833 * basic_salary 
    self.esi = 0.006 * basic_salary 
    self.pt = 200 
    self.monthly_tds = 0 # To be calculated later 
class SalaryCalculation:
 def __init__(self, basic_salary): 
    self.earnings = Earnings(basic_salary) 
    self.deductions = Deductions(basic_salary)
 # Calculate Monthly TDS 
    annual_gross_salary = self.earnings.gross_salary * 12 
    tds_limit = 700000 if basic_salary <= 700000 else 0 
    taxable_amount = max(annual_gross_salary - tds_limit, 0) 
    self.deductions.monthly_tds = (taxable_amount * 0.10) / 12
 # Calculate Net Salary 
    self.net_salary = self.earnings.gross_salary - ( 
    self.deductions.pf + self.deductions.esi + self.deductions.pt
    + self.deductions.monthly_tds) 
class PayslipGeneration:
 def __init__(self, basic_salary): 
    self.salary_calculation = SalaryCalculation(basic_salary)
 def generate_payslip(self): 
    print("Basic Salary:", self.salary_calculation.earnings.basic_salary)
    print("DA:", self.salary_calculation.earnings.da)
    print("HRA:", self.salary_calculation.earnings.hra)
    print("Conveyance:", self.salary_calculation.earnings.conveyance)
    print("Gross Salary:", self.salary_calculation.earnings.gross_salary)
    print("\nDeductions:")
    print("PF:", self.salary_calculation.deductions.pf)
    print("ESI:", self.salary_calculation.deductions.esi)
    print("PT:", self.salary_calculation.deductions.pt)
    print("Monthly TDS:", self.salary_calculation.deductions.monthly_tds)
    print("\nNet Salary:", self.salary_calculation.net_salary)
# Example Usage 
basic_salary = 50000 
payslip = PayslipGeneration(basic_salary)
payslip.generate_payslip()