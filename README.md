# Retail Inventory Manager

## Project Overview
Retail Inventory Manager is a Python-based console application designed to manage products and stock in a shop. It helps users add, display, search, update, and delete products, monitor low stock, and calculate inventory value.

## Setup
- Install Python 3 on your computer.
- Download or clone this repository.
- Open the project folder in VS Code.
- No external Python libraries are required.

## How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:
   `python project1.py`
4. Select an option from the main menu to use the system.

## Input Rules
- Product ID must be unique.
- Product name and category cannot be empty.
- Price must be a positive number.
- Stock quantity must be a non-negative integer.
- Reorder level must be a non-negative integer.
- Enter a valid menu option.

## Features
- Add Product
- Display Products
- Search Product
- Update Product
- Delete Product
- Low Stock Report
- Inventory Summary

## Known Limitations
- Product data is stored in memory and is lost when the program closes.
- The application is console-based and has no graphical interface.
- No database is connected.
- Only one user can operate the system at a time.

## Test Cases
- Add a product with valid details.
- Try adding a duplicate Product ID.
- Search for an existing and a non-existing product.
- Update product details.
- Delete a product.
- Check the Low Stock Report.
- Check the Inventory Summary.
- Enter invalid values such as negative price or stock.

## Project Details
- Language: Python
- Project Type: Console Application
- Version: 1.0
- Author: Farhan Anjum
