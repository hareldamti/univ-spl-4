from persistence import *

def main():
    #TODO: implement
    print("Activities")
    activityCursor = repo._conn.cursor()
    stmt = "SELECT * FROM activities ORDER BY date"
    activityCursor.execute(stmt)
    for activity in activityCursor:
        print(activity)
    
    print("Branches")
    brancheCursor = repo._conn.cursor()
    stmt = "SELECT * FROM branches ORDER BY id"
    brancheCursor.execute(stmt)
    for branche in brancheCursor:
        print(branche)
    
    print("Employees")
    employeeCursor = repo._conn.cursor()
    stmt = "SELECT * FROM employees ORDER BY id"
    employeeCursor.execute(stmt)
    for employee in employeeCursor:
        print(employee)

    print("Products")
    productCursor = repo._conn.cursor()
    stmt = "SELECT * FROM products ORDER BY id"
    productCursor.execute(stmt)
    for product in productCursor:
        print(product)

    print("Suppliers")
    supplierCursor = repo._conn.cursor()
    stmt = "SELECT * FROM suppliers ORDER BY id"
    supplierCursor.execute(stmt)
    for supplier in supplierCursor:
        print(supplier)
        
    print()
    print("Employers report")
    employerReportCursor = repo._conn.cursor()
    stmt = """SELECT employees.name, employees.salary, branches.location, IFNULL(SUM(ABS(activities.quantity) * products.price),'0') AS total_income
    FROM employees
    LEFT JOIN branches ON employees.branche = branches.id
    LEFT JOIN activities ON employees.id = activities.activator_id
    LEFT JOIN products ON activities.product_id = products.id
    GROUP BY employees.name, employees.salary, branches.location
    ORDER BY employees.name ASC
    """
    employerReportCursor.execute(stmt)
    for employerReport in employerReportCursor:
        print(employerReport)

    print()
    print("Activities report")
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
        print(activityReport)
    

    

if __name__ == '__main__':
    main()