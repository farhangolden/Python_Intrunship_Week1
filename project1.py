# print("="*40)
# print("     RETAIL INVENTORY MANAGER")
# print("="*40)

# print("\n1.Add Product")
# print("2.Display Products")
# print("3.Search Product")
# print("4.Update Product")
# print("5.Delete Product")
# print("6.Low Stock Report")
# print("7.Inventory Summary")
# print("8.Exit")

# choice=input("\nEnter your choice: ")
# print("Your choice is:",choice)


# RETAIL INVENTORY MANAGER

products=[]
def add_product():

    print("\n========== ADD PRODUCT ==========")

    # Product ID
    product_id=input("Enter Product ID: ")

    # Duplicate ID check
    for product in products:
        if product["id"]==product_id:
            print("Error:Product ID already exists!")
            return

    # Product Name
    name=input("Enter Product Name: ").strip()

    if not name:
        print("Error: Product name cannot be empty!")
        return

    # Category
    category=input("Enter Category: ").strip()

    if not category:
        print("Error:Category cannot be empty!")
        return

    # Selling Price
    try:
        price=float(input("Enter Selling Price: "))

        if price<=0:
            print("Error:Price must be positive!")
            return

    except ValueError:
        print("Error:Enter a valid price!")
        return

    # Stock Quantity
    try:
        stock=int(input("Enter Stock Quantity: "))

        if stock<0:
            print("Error:Stock cannot be negative!")
            return

    except ValueError:
        print("Error:Enter a valid quantity!")
        return

    # Reorder Level
    try:
        reorder=int(input("Enter Reorder Level: "))

        if reorder<0:
            print("Error:Reorder level cannot be negative!")
            return

    except ValueError:
        print("Error:Enter a valid reorder level!")
        return

    # Save Product
    product={
        "id":product_id,
        "name":name,
        "category":category,
        "price":price,
        "stock":stock,
        "reorder":reorder
    }
    products.append(product)
    print("\nSUCCESS: Product added successfully!")

def display_products():

    if len(products)==0:
        print("No Products Available")
    else:
        for p in products:
            print("\nProduct ID:",p["id"])
            print("Name:",p["name"])
            print("Category:",p["category"])
            print("Price:",p["price"])
            print("Stock:",p["stock"])
            print("Reorder Level:",p["reorder"])


def search_product():

    pid=input("Enter Product ID to Search: ")
    for p in products:

        if p["id"]==pid:

            print("\nProduct Found!")
            print("ID:", p["id"])
            print("Name:", p["name"])
            print("Category:", p["category"])
            print("Price:", p["price"])
            print("Stock:", p["stock"])
            print("Reorder Level:", p["reorder"])
            return

    print("Product Not Found!")


def update_product():

    pid=input("Enter Product ID: ")
    for p in products:

        if p["id"]==pid:
            print("\nProduct Found!")
            print("\nWhat do you want to edit?")
            print("1.Product Name")
            print("2.Category")
            print("3.Price")
            print("4.Stock")
            print("5.Reorder Level")
            choice=input("\nEnter your choice: ")

            if choice=="1":
                p["name"]=input("Enter New Name: ")

            elif choice=="2":
                p["category"]=input("Enter New Category: ")

            elif choice=="3":
                p["price"]=float(input("Enter New Price: "))

            elif choice=="4":
                p["stock"]=int(input("Enter New Stock: "))

            elif choice=="5":
                p["reorder"]=int(input("Enter New Reorder Level: "))

            else:
                print("Invalid Choice!")
                return

            print("\nProduct Updated Successfully!")
            return

    print("Product Not Found!")


def delete_product():

    pid=input("Enter Product ID to Delete: ")
    for p in products:

        if p["id"]==pid:
            print("Product Found!")
            print("Product Name:", p["name"])

            confirm=input("Are you sure you want to delete? (yes/no): ")

            if confirm.lower()=="yes":
                products.remove(p)
                print("Product Deleted Successfully!")

            else:
                print("Delete Cancelled!")
            return

    print("Product Not Found!")


def low_stock_report():

    print("\n===== LOW STOCK REPORT =====")
    found=False
    for p in products:
        if p["stock"]<=p["reorder"]:
            print("\nProduct ID:",p["id"])
            print("Product Name:",p["name"])
            print("Stock:",p["stock"])
            print("Reorder Level:",p["reorder"])
            found=True

    if not found:
        print("No Low Stock Products!")
    
def inventory_summary():

    total_products=len(products)
    total_stock=0
    total_value=0
    for p in products:
        total_stock+=p["stock"]
        total_value+=p["price"]*p["stock"]

    print("\n===== INVENTORY SUMMARY =====")
    print("Total Products:",total_products)
    print("Total Stock:",total_stock)
    print("Total Inventory Value: Rs.",total_value)

# Main Menu
while True:

    print("\n===== RETAIL INVENTORY MANAGER =====")
    print("1.Add Product")
    print("2.Display Products")
    print("3.Search Product")
    print("4.Update Product")
    print("5.Delete Product")
    print("6.Low Stock Report")
    print("7.Inventory Summary")
    print("8.Exit")
    choice=input("\nEnter your choice: ")

    if choice=="1":
        add_product()

    elif choice=="2":
        display_products()

    elif choice=="3":
        search_product()

    elif choice=="4":
        update_product()

    elif choice=="5":
        delete_product()

    elif choice=="6":
        low_stock_report()

    elif choice=="7":
        inventory_summary()

    elif choice=="8":
        print("Thank you for using Inventory Manager!")
        break

    else:
        print("Enter Valid Opptions!")
