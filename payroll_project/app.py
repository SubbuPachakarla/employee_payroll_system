from flask import Flask, render_template, request, redirect, url_for
from abc import ABC, abstractmethod

app = Flask(__name__)

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

employee_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    emp_id = int(request.form['emp_id'])
    emp_type = request.form['type']

    if emp_type == 'fulltime':
        salary = float(request.form['salary'])
        employee = FullTimeEmployee(name, emp_id, salary)
    else:
        hours = int(request.form['hours'])
        rate = float(request.form['rate'])
        employee = PartTimeEmployee(name, emp_id, hours, rate)

    employee_list.append(employee)
    return redirect(url_for('list_employees'))

@app.route('/employees')
def list_employees():
    return render_template('employees.html', employees=employee_list)

if __name__ == '__main__':
    app.run(debug=True)
