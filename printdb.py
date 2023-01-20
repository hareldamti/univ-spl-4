from persistence import *

def main():
    output = ""
    output += "Activities\n"
    activityCursor = repo._conn.cursor()
    stmt = "SELECT * FROM activities ORDER BY date"
    activityCursor.execute(stmt)
    for activity in activityCursor:
        output += str(activity) + "\n"
    
    output += "Branches\n"
    brancheCursor = repo._conn.cursor()
    stmt = "SELECT * FROM branches ORDER BY id"
    brancheCursor.execute(stmt)
    for branche in brancheCursor:
        output += str(branche) + "\n"
    
    output += "Employees\n"
    employeeCursor = repo._conn.cursor()
    stmt = "SELECT * FROM employees ORDER BY id"
    employeeCursor.execute(stmt)
    for employee in employeeCursor:
        output += str(employee) + "\n"

    output += "Products\n"
    productCursor = repo._conn.cursor()
    stmt = "SELECT * FROM products ORDER BY id"
    productCursor.execute(stmt)
    for product in productCursor:
        output += str(product) + "\n"

    output += "Suppliers\n"
    supplierCursor = repo._conn.cursor()
    stmt = "SELECT * FROM suppliers ORDER BY id"
    supplierCursor.execute(stmt)
    for supplier in supplierCursor:
        output += str(supplier) + "\n"
        
    output += "\n"
    output += "Employers report\n"
    employerReportCursor = repo._conn.cursor()
    stmt = """SELECT employees.name, employees.salary, branches.location, IFNULL( SUM(-activities.quantity * products.price), 0) AS total_income
    FROM employees
    LEFT JOIN branches ON employees.branche = branches.id
    LEFT JOIN activities ON employees.id = activities.activator_id
    LEFT JOIN products ON activities.product_id = products.id
    GROUP BY employees.id
    ORDER BY employees.name ASC
    """

    employerReportCursor.execute(stmt)
    for employerReport in employerReportCursor:
        output += " ".join(map(str,employerReport)) + "\n"


    output += "\n"
    output += "Activities report\n"
    activityReportCursor = repo._conn.cursor()
    stmt = """SELECT activities.date, products.description, activities.quantity, employees.name as employee_name, suppliers.name as supplier_name
    FROM activities
    JOIN products ON activities.product_id = products.id
    LEFT JOIN employees ON activities.activator_id = employees.id AND employees.id IS NOT NULL
    LEFT JOIN suppliers ON activities.activator_id = suppliers.id AND suppliers.id IS NOT NULL
    ORDER BY activities.date;
    """
    activityReportCursor.execute(stmt)
    for activityReport in activityReportCursor:
        output += str(activityReport) + "\n"
    
    output = output[:-1]
    print(output)

    with open('res.txt','w') as f:
        f.write(output)
    

if __name__ == '__main__':
    main()