# Step 1: Initialize an empty dictionary to store salaries by department
# Structure: { dept_no: [salary1, salary2, ...] }
dept_data = {}

print("--- Employee Data Entry ---")
print("Enter 'done' at any time to finish.\n")

while True:
    dept = input("Enter Department No: ")
    if dept.lower() == 'done':
        break
        
    try:
        roll_no = input("Enter Employee Roll No: ")
        salary = float(input("Enter Salary: "))
        
        # Step 2: Grouping logic
        # If the department doesn't exist yet, create an empty list for it
        if dept not in dept_data:
            dept_data[dept] = []
        
        # Append the salary to that department's list
        dept_data[dept].append(salary)
        print("Data added successfully!\n")
        
    except ValueError:
        print("Invalid input. Please enter numbers for Roll No and Salary.")

# Step 3: Calculate and display Min/Max per department
print("\n--- Department Wise Salary Report ---")
if not dept_data:
    print("No data recorded.")
else:
    for dept, salaries in dept_data.items():
        min_sal = min(salaries)
        max_sal = max(salaries)
        print(f"Dept {dept}: Min Salary = {min_sal}, Max Salary = {max_sal}")
