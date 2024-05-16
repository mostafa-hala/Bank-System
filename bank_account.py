import tkinter as tk
from tkinter import messagebox

accounts = [{"account_no": "1234", "balance": 12}, {"account_no": "2345", "balance": 200}]
choice = ""

def check(x):
    if len(x) == 4 and x.isdigit():
        return True
    else:
        messagebox.showerror("Invalid Input", "Invalid number. Please enter 4 integer numbers.")
        return False

def main():
    root = tk.Tk()
    root.title("Banking Application")

    def clear_frame():
        for widget in root.winfo_children():
            widget.destroy()

    def show_menu():
        clear_frame()
        tk.Label(root, text="****Welcome****", font=("Helvetica", 16)).pack()
        tk.Label(root, text="1-Create Account\n2-View Account\n3-Review Balance\n4-Update Account\n"
                            "5-Deposit\n6-Withdraw\n7-Transfer\n8-Delete Account\n0-Exit\n", font=("Helvetica", 14)).pack()

        options = ["Create Account", "View Account", "Review Balance", "Update Account", "Deposit", "Withdraw", "Transfer", "Delete Account", "Exit"]

        def handle_choice(choice):
            clear_frame()
            if choice == "Create Account":
                create_account_gui()
            elif choice == "View Account":
                view_account_gui()
            elif choice == "Review Balance":
                view_balance_gui()
            elif choice == "Update Account":
                update_account_gui()
            elif choice == "Deposit":
                deposit_gui()
            elif choice == "Withdraw":
                withdraw_gui()
            elif choice == "Transfer":
                transfer_gui()
            elif choice == "Delete Account":
                delete_account_gui()
            elif choice == "Exit":
                root.quit()

        for option in options:
            tk.Button(root, text=option, command=lambda option=option: handle_choice(option)).pack(fill='x')

    def create_account(accounts, new_account, balance=0):
        if not check(new_account):
            return
        for account in accounts:
            if new_account == account["account_no"]:
                messagebox.showerror("Error", "This account number is already present.")
                return
        accounts.append({"account_no": new_account, "balance": balance})
        messagebox.showinfo("Success", f"Account created successfully: {accounts[-1]}")

    def view_account(accounts, account_number):
        if not check(account_number):
            return
        for account in accounts:
            if account["account_no"] == account_number:
                messagebox.showinfo("Account Info", f"{account}")
                return
        messagebox.showerror("Error", "This account cannot be found.")

    def view_balance(accounts, number):
        if not check(number):
            return
        for account in accounts:
            if account["account_no"] == number:
                messagebox.showinfo("Balance", f'Your balance is {str(account["balance"])} $')
                return
        messagebox.showerror("Error", "This account cannot be found.")

    def update_account(accounts, numberu, new_name):
        if not check(numberu) or not check(new_name):
            return
        for account in accounts:
            if numberu == account["account_no"]:
                if any(acc["account_no"] == new_name for acc in accounts):
                    messagebox.showerror("Error", "The new account number is already present. Try again.")
                    return
                account.update({"account_no": new_name})
                messagebox.showinfo("Success", f"Account updated successfully: {account}")
                return
        messagebox.showerror("Error", "This account cannot be found.")

    def deposit(accounts, numberd, deposite):
        if not check(numberd):
            return
        for account in accounts:
            if account["account_no"] == numberd:
                account["balance"] += deposite
                messagebox.showinfo("Success", f'Your balance now is {str(account["balance"])} $')
                return
        messagebox.showerror("Error", "This account cannot be found.")

    def withdraw(accounts, numberw, withdraw):
        if not check(numberw):
            return
        for account in accounts:
            if account["account_no"] == numberw:
                if withdraw <= account["balance"]:
                    account["balance"] -= withdraw
                    messagebox.showinfo("Success", f'Your balance now is {str(account["balance"])} $')
                else:
                    messagebox.showerror("Error", f'Your balance is not enough. Current balance: {str(account["balance"])} $')
                return
        messagebox.showerror("Error", "This account cannot be found.")

    def transfer(accounts, no1, no2, amount):
        if not check(no1) or not check(no2):
            return
        for acc1 in accounts:
            if no1 == acc1["account_no"]:
                for acc2 in accounts:
                    if no2 == acc2["account_no"]:
                        if amount <= acc1["balance"]:
                            acc1["balance"] -= amount
                            acc2["balance"] += amount
                            messagebox.showinfo("Success", f'Transfer completed successfully. Your current balance: {str(acc1["balance"])} $')
                        else:
                            messagebox.showerror("Error", "Your balance is not enough.")
                        return
                messagebox.showerror("Error", "The second account cannot be found.")
                return
        messagebox.showerror("Error", "Your account number cannot be found.")

    def delete_account(accounts, numberd):
        if not check(numberd):
            return
        for i, account in enumerate(accounts):
            if account["account_no"] == numberd:
                del accounts[i]
                messagebox.showinfo("Success", "Your account has been deleted.")
                return
        messagebox.showerror("Error", "This account cannot be found.")

    def create_account_gui():
        tk.Label(root, text="Enter Your Account Number:").pack()
        account_entry = tk.Entry(root)
        account_entry.pack()

        def submit():
            account_no = account_entry.get()
            create_account(accounts, account_no)
            show_menu()

        tk.Button(root, text="Submit", command=submit).pack()
        tk.Button(root, text="Back to Menu", command=show_menu).pack()

    def view_account_gui():
        tk.Label(root, text="Enter Your Account Number:").pack()
        account_entry = tk.Entry(root)
        account_entry.pack()

        def submit():
            account_no = account_entry.get()
            view_account(accounts, account_no)
            show_menu()

        tk.Button(root, text="Submit", command=submit).pack()
        tk.Button(root, text="Back to Menu", command=show_menu).pack()

    def view_balance_gui():
        tk.Label(root, text="Enter Your Account Number:").pack()
        account_entry = tk.Entry(root)
        account_entry.pack()

        def submit():
            account_no = account_entry.get()
            view_balance(accounts, account_no)
            show_menu()

        tk.Button(root, text="Submit", command=submit).pack()
        tk.Button(root, text="Back to Menu", command=show_menu).pack()

    def update_account_gui():
        tk.Label(root, text="Enter Your Account Number:").pack()
        account_entry = tk.Entry(root)
        account_entry.pack()
        tk.Label(root, text="Enter the New Account Number:").pack()
        new_account_entry = tk.Entry(root)
        new_account_entry.pack()

        def submit():
            account_no = account_entry.get()
            new_account_no = new_account_entry.get()
            update_account(accounts, account_no, new_account_no)
            show_menu()

        tk.Button(root, text="Submit", command=submit).pack()
        tk.Button(root, text="Back to Menu", command=show_menu).pack()

    def deposit_gui():
        tk.Label(root, text="Enter Your Account Number:").pack()
        account_entry = tk.Entry(root)
        account_entry.pack()
        tk.Label(root, text="Enter the Amount to Deposit:").pack()
        amount_entry = tk.Entry(root)
        amount_entry.pack()

        def submit():
            account_no = account_entry.get()
            amount = float(amount_entry.get())
            deposit(accounts, account_no, amount)
            show_menu()

        tk.Button(root, text="Submit", command=submit).pack()
        tk.Button(root, text="Back to Menu", command=show_menu).pack()

    def withdraw_gui():
        tk.Label(root, text="Enter Your Account Number:").pack()
        account_entry = tk.Entry(root)
        account_entry.pack()
        tk.Label(root, text="Enter the Amount to Withdraw:").pack()
        amount_entry = tk.Entry(root)
        amount_entry.pack()

        def submit():
            account_no = account_entry.get()
            amount = float(amount_entry.get())
            withdraw(accounts, account_no, amount)
            show_menu()

        tk.Button(root, text="Submit", command=submit).pack()
        tk.Button(root, text="Back to Menu", command=show_menu).pack()

    def transfer_gui():
        tk.Label(root, text="Enter Your Account Number:").pack()
        from_account_entry = tk.Entry(root)
        from_account_entry.pack()
        tk.Label(root, text="Enter the Account Number to Transfer To:").pack()
        to_account_entry = tk.Entry(root)
        to_account_entry.pack()
        tk.Label(root, text="Enter the Amount to Transfer:").pack()
        amount_entry = tk.Entry(root)
        amount_entry.pack()

        def submit():
            from_account_no = from_account_entry.get()
            to_account_no = to_account_entry.get()
            amount = float(amount_entry.get())
            transfer(accounts, from_account_no, to_account_no, amount)
            show_menu()

        tk.Button(root, text="Submit", command=submit).pack()
        tk.Button(root, text="Back to Menu", command=show_menu).pack()

    def delete_account_gui():
        tk.Label(root, text="Enter Your Account Number:").pack()
        account_entry = tk.Entry(root)
        account_entry.pack()

        def submit():
            account_no = account_entry.get()
            delete_account(accounts, account_no)
            show_menu()

        tk.Button(root, text="Submit", command=submit).pack()
        tk.Button(root, text="Back to Menu", command=show_menu).pack()

    show_menu()
    root.mainloop()

main()
