# Food Billing System

This project is a **Food Billing System** built using Python's `Tkinter` library. It provides a graphical user interface for calculating and managing bills in a food shop or restaurant. The system categorizes food items and generates receipts based on user selections.

### Features
- **Graphical User Interface (GUI)**: Built using the `Tkinter` library, providing an easy-to-use interface for the cashier or billing personnel.
- **Food Categories**: The system organizes food into categories like Sweets and Namkeens.
- **Bill Calculation**: Automatically calculates the total cost based on selected items.
- **Receipts**: Displays a receipt with itemized costs and total amount.
- **Time and Date**: Displays the current time and date on the receipt.
  
### Prerequisites
Make sure you have Python installed on your system. This project uses the following libraries:
- `tkinter` (comes pre-installed with Python)
- `random`
- `time`
- `datetime`

### How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/AishwaryaBhargava/food_billing_system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd food_billing_system
   ```
3. Run the Python script:
   ```bash
   python food_billing_system.py
   ```

### How it Works
1. When the program is run, it opens a GUI window with different sections:
   - **Menu**: A list of available food items, separated into categories like Sweets and Namkeens.
   - **Receipt**: Shows the items selected and their respective prices.
   - **Total Cost**: Automatically calculates the total cost as items are selected.
2. The cashier can select items and quantities, and the system will display the final bill with the date and time of purchase.
3. There are buttons for generating receipts, clearing selections, and exiting the application.

### Future Improvements
- Add more food categories or customize existing ones.
- Integrate a database to store sales data.
- Include discount options or additional features like coupons.
