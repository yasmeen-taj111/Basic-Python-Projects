def calculate_salary( basic, hra, ded):
    hra_amt = basic * hra / 100
    ded_amt = basic * ded / 100
    gross = basic + hra_amt
    net = gross - ded_amt
    return gross, net


print("Employee Payroll Calculator")
print("-" * 40)

n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"\nEnter details for Employee {i+1}")
    name = input("Enter employee name: ")
    basic = float(input("Enter basic salary: ₹"))
    hra = float(input("Enter HRA percentage: "))
    ded = float(input("Enter deduction percentage: "))

    gross, net = calculate_salary( basic, hra, ded)

    print("\n" + "=" * 40)
    print("Salary Slip - Taj Company")
    print("=" * 40)
    print(f"Employee Name     : {name}")
    print(f"Basic Salary      : ₹{basic:.2f}")
    print(f"HRA ({hra}%)        : ₹{(basic * hra / 100):.2f}")
    print(f"Deductions ({ded}%) : ₹{(basic * ded / 100):.2f}")
    print(f"Gross Salary      : ₹{gross:.2f}")
    print(f"Net Salary        : ₹{net:.2f}")
    print("=" * 40)

print("\nAll employee salary slips generated successfully!")
