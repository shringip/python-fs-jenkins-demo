class EmployeeServcie:
 
    def calculate_annual_salary(self,monthly_salary):
        if monthly_salary==0:
            raise ValueError("monthly salary must be greater than 0")
        return monthly_salary *12
 
    def calculate_bonus(self,monthly_salary,bonus_percentage):
        if monthly_salary<=0:
            raise ValueError("monthly salary must be greater than 0")
 
        if bonus_percentage<0:
            raise ValueError("bonus percentage cannot be -ve")
        return monthly_salary * bonus_percentage/100
 
    def validate_employee(self,emp_id):
        return isinstance(emp_id,int) and emp_id >0