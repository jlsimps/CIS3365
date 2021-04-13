from tkinter import *
import pyodbc
from tkinter import ttk

WIDTH = 1068
HEIGHT = 838

#Function that executes when log in button is clicked
def login():
    un = username_entry.get()
    pw = pw_entry.get()
    cursor = conn.cursor()
    query = f"SELECT * FROM system_users WHERE username='{un}' AND password='{pw}'"
    cursor.execute(query)
    results = cursor.fetchone()
    if results:
        is_admin = results[3]
        if is_admin:
            print("User found!" + str(results) )
            #The lift method brings the admin page to the front, it will not be visible until a successful login occurs
            admin_logged_in.lift()
            un_admin_text.set(f"Welcome, {un}!")
        else:
            print("User found!" + str(results) )
            user_logged_in.lift()
            un_user_text.set(f"Welcome, {un}!")
    else:
        invalid_login = Label(login_container, fg='red', text="INVALID USER CREDENTIALS", font=('Helvetica 10 bold'))
        invalid_login.grid(row=4, columnspan=2)


#Function that executes when logout button is clicked
def logout_clicked():
    admin_logged_in.lower()
    user_logged_in.lower()
    username_entry.delete(0, last='end')
    pw_entry.delete(0, last='end')

#function that executes when add new store is clicked
def add_store():
    add_store_frame.lift()

#function that executes when submit is clicked on add new store frame
def submit_new_store():
    state_id = state_id_entry.get()
    city = city_entry.get()
    address = address_entry.get()
    cursor = conn.cursor()
    query = f"INSERT INTO blockhouse_stores (state_id, city, address) VALUES ({int(state_id)}, '{city}', '{address}')"
    cursor.execute(query)
    update_stores()
    add_store_frame.lower()

#function that executes when edit selected store button is clicked 
def edit_store():
    if store_tree.focus():
        update_store_frame.lift()
        selected_store = store_tree.item(store_tree.focus())
        values = selected_store['values']
        store_id_text.set(values[0])
        state_id_entry_update.delete(0, last='end')
        state_id_entry_update.insert(0, str(values[1]))
        city_entry_update.delete(0, last='end')
        city_entry_update.insert(0, values[2])
        address_entry_update.delete(0, last='end')
        address_entry_update.insert(0, values[3])


    print(values)
    # values = store_tree.item(selected_store)

#function that executes when submit is clicked on update store frame
def update_store():
    store_id = int(store_id_label2.cget("text"))
    state_id = int(state_id_entry_update.get())
    city = city_entry_update.get()
    address = address_entry_update.get()
    cursor = conn.cursor()
    query = f"UPDATE blockhouse_stores SET state_id = {state_id}, city = '{city}', address = '{address}' WHERE store_id = {store_id}"
    cursor.execute(query)
    update_stores()
    update_store_frame.lower()


#function to update store list in the store treeview
def update_stores():
    store_tree.delete(*store_tree.get_children())
    cursor = conn.cursor()
    query = f"SELECT * FROM blockhouse_stores"
    cursor.execute(query)
    stores = cursor.fetchall()
    for store in stores:
        store_tree.insert("", index="end", values=(store[0], store[1], store[2], store[3]))

#function to update user list in the system users treeview
def update_users():
    users_tree.delete(*users_tree.get_children())
    cursor = conn.cursor()
    query = "SELECT * FROM system_users"
    cursor.execute(query)
    users = cursor.fetchall()
    for user in users:
        users_tree.insert("", index="end", values=(user[0], user[1], user[3]))

def manage_products_clicked():
    products_main_frame.lift()

def cb_product_selected(event):
    selection = products_cb.get()
    products_tree.delete(*products_tree.get_children())
    cursor = conn.cursor()
    product_bottom_container.lift()
    details_form_cover.lift()
    if selection == "Bread":
        query = "SELECT * FROM suppliers_bread_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Cleaning":
        query = "SELECT * FROM suppliers_cleaning_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Coffee":
        query = "SELECT * FROM suppliers_coffee_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Dairy":
        query = "SELECT * FROM suppliers_dairy_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Meat":
        query = "SELECT * FROM suppliers_meat_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Other":
        query = "SELECT * FROM suppliers_other_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Paper":
        query = "SELECT * FROM suppliers_paper_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Produce":
        query = "SELECT * FROM suppliers_produce_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Retail":
        query = "SELECT * FROM suppliers_retail_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))
    if selection == "Sugars, Spices, Seasonings":
        query = "SELECT * FROM suppliers_sss_products"
        cursor.execute(query)
        products = cursor.fetchall()
        for product in products:
            products_tree.insert("", index="end", values=(product[0], product[1], product[2], product[3], product[4], product[5]))

def add_product_clicked():
    new_product_details_form.lift()

def edit_product_clicked():
    edit_product_details_form.lift()

#DB Connection
DB_USERNAME = "Your Username"
DB_PASSWORD = "Your Password"
DB_SERVER = "Your Server Address"
DB_NAME = "Your Database Name"
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={DB_SERVER};DATABASE={DB_NAME};UID={DB_USERNAME};PWD={DB_PASSWORD}')

root = Tk()
root.title("Blockhouse Management System")

#Using canvas to set initial window size
canvas = Canvas(root, bg='white', height=HEIGHT, width=WIDTH)

#This label sets the background image
bg_img = PhotoImage(file="coffee.png")
bg_label = Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas.pack()

#The container that holds the log in screen
login_container = Frame(root, bg='#454040', bd=25, highlightbackground="#332e2d", highlightthickness=2)
login_container.place(relx=.5, rely=.5, anchor='c')
title_label = Label(login_container, text="Welcome to the Blockhouse Inventory System!", bg='#454040', fg='white', font=('Helvetica 12 bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=15)
username_label = Label(login_container, text="Username", bg='#454040', fg='white')
username_label.grid(row=1, column=0, padx=10, pady=15)
username_entry = Entry(login_container)
username_entry.grid(row=1, column=1, pady=15)
pw_label = Label(login_container, text="Password", bg='#454040', fg='white')
pw_label.grid(row=2, column=0)
pw_entry = Entry(login_container, show="*")
pw_entry.grid(row=2, column=1)
login_button = Button(login_container, text="Log In", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=25)

#This frame is brought to the front after a successful admin login
admin_logged_in = Frame(root, bg='#454040', highlightbackground="#332e2d", highlightthickness=1)
admin_logged_in.place(relx=.5, rely=.5, anchor='c', width=968, height=738)

#This code styles the font on the notebook tabs
s = ttk.Style()
s.configure('TNotebook.Tab', padding=5, bg='black', fg='grey', font=('Helvetica 12') )

##BEGIN ADMIN NOTEBOOK##
#Using a notebook for simplified navigation
admin_notebook = ttk.Notebook(admin_logged_in)
admin_notebook.pack(fill="both", expand=True)

#Creating a frame for each tab of the notebook
admin_main_frame = Frame(admin_notebook, width=968, height=738)
admin_store_frame = Frame(admin_notebook, width=968, height=738)
admin_system_users_frame = Frame(admin_notebook, width=968, height=738)
admin_inventory_frame = Frame(admin_notebook, width=968, height=738)
admin_orders_frame = Frame(admin_notebook, width=968, height=738)
admin_catering_frame = Frame(admin_notebook, width=968, height=738)
admin_reports_frame = Frame(admin_notebook, width=968, height=738)
admin_main_frame.pack(fill="both", expand=1)
admin_store_frame.pack(fill="both", expand=1)
admin_system_users_frame.pack(fill="both", expand=1)
admin_inventory_frame.pack(fill="both", expand=1)
admin_orders_frame.pack(fill="both", expand=1)
admin_catering_frame.pack(fill="both", expand=1)
admin_reports_frame.pack(fill="both", expand=1)

#BEGIN WELCOME TAB
admin_notebook.add(admin_main_frame, text="Welcome Page")
un_admin_text = StringVar()
welcome_un = Label(admin_main_frame, textvariable=un_admin_text, font=('Arial 14'))
welcome_un.pack(anchor="center", pady=20)
welcome_label = Label(admin_main_frame, font=('Arial 14'), text=f"You are logged in to the Blockhouse Inventory Management System with admin privileges.\n Use the tabs above to see all available options.")
welcome_label.pack(anchor="center", pady=25)
logout_button = Button(admin_main_frame, text="Logout", command=logout_clicked, font=('Arial 10'))
logout_button.pack(anchor="center")
#END WELCOME TAB

#BEGIN STORES TAB
admin_notebook.add(admin_store_frame, text="Stores")

store_tree = ttk.Treeview(admin_store_frame)
store_tree['show'] = 'headings'
store_tree['columns'] = ("Store ID", "State ID", "City", "Address")
store_tree.column("#0", width=0, anchor=W)
store_tree.column("Store ID", anchor=W, width=20)
store_tree.column("State ID", anchor=W, width=20)
store_tree.column("City", anchor=W, width=50)
store_tree.column("Address", anchor=W, width=200)

store_tree.heading("#0")
store_tree.heading("Store ID", text="Store ID", anchor=W)
store_tree.heading("State ID", text="State ID", anchor=W)
store_tree.heading("City", text="City", anchor=W)
store_tree.heading("Address", text="Address", anchor=W)

store_tree.pack(fill="x", side="top")
update_stores()

store_button_container = Frame(admin_store_frame)
store_button_container.pack(anchor=CENTER, pady=20)
add_store_button = Button(store_button_container, text="Add a new store", command=add_store, pady=10)
add_store_button.grid(column=0, row=0, padx=10)
edit_store_button = Button(store_button_container, text="Edit Selected Store", command=edit_store, pady=10)
edit_store_button.grid(column=1, row=0, padx=10)

add_store_frame = Frame(root)
add_store_frame.place(relx=.4, rely=.5)
state_id_label = Label(add_store_frame, text="State ID:")
state_id_label.grid(column=0, row=0)
state_id_entry = Entry(add_store_frame)
state_id_entry.grid(column=1, row=0)
city_label = Label(add_store_frame, text="City:")
city_label.grid(column=0, row=1)
city_entry = Entry(add_store_frame)
city_entry.grid(column=1, row=1)
address_label = Label(add_store_frame, text="Address:")
address_label.grid(column=0, row=2)
address_entry = Entry(add_store_frame)
address_entry.grid(column=1, row=2)
submit_button = Button(add_store_frame, text="Submit", command=submit_new_store)
submit_button.grid(row=3, column=0, pady=15)
cancel_button = Button(add_store_frame, text="Cancel", command=add_store_frame.lower)
cancel_button.grid(row=3, column=1,  pady=15)
add_store_frame.lower()

update_store_frame = Frame(root)
update_store_frame.place(relx=.4, rely=.5)
store_id_text = StringVar()
store_id_label = Label(update_store_frame, text="Store ID:")
store_id_label.grid(column=0, row=0)
store_id_label2 = Label(update_store_frame, textvariable=store_id_text)
store_id_label2.grid(column=1, row=0)
state_id_label = Label(update_store_frame, text="State ID:")
state_id_label.grid(column=0, row=1)
state_id_entry_update = Entry(update_store_frame)
state_id_entry_update.grid(column=1, row=1)
city_label = Label(update_store_frame, text="City:")
city_label.grid(column=0, row=2)
city_entry_update = Entry(update_store_frame)
city_entry_update.grid(column=1, row=2)
address_label = Label(update_store_frame, text="Address:")
address_label.grid(column=0, row=3)
address_entry_update = Entry(update_store_frame)
address_entry_update.grid(column=1, row=3)
submit_button = Button(update_store_frame, text="Submit", command=update_store,)
submit_button.grid(row=4, column=0,  pady=15)
cancel_button = Button(update_store_frame, text="Cancel", command=update_store_frame.lower)
cancel_button.grid(row=4, column=1,  pady=15)
update_store_frame.lower()
#END STORES TAB

#BEGIN SYSTEM USERS TAB
admin_notebook.add(admin_system_users_frame, text="System Users")

users_tree = ttk.Treeview(admin_system_users_frame, selectmode='browse')
users_tree['show'] = 'headings'
users_tree['columns'] = ("User ID", "Username", "Admin")

users_tree.column("#0", width=0)
users_tree.column("User ID", anchor=W, width=20)
users_tree.column("Username", anchor=W, width=50)
users_tree.column("Admin", anchor=W, width=30)

users_tree.heading("#0")
users_tree.heading("User ID", text="User ID", anchor=W)
users_tree.heading("Username", text="Username", anchor=W)
users_tree.heading("Admin", text="Admin Privileges", anchor=W)

users_tree.pack(fill='x', side='top')

users_vsb = ttk.Scrollbar(admin_system_users_frame, orient="vertical", command=users_tree.yview)
users_vsb.place(x=940, y=2, height=222)
users_tree.configure(yscrollcommand=users_vsb.set)

update_users()
#END SYSTEM USERS TAB

#BEGIN ADMIN INVENTORY TAB
admin_notebook.add(admin_inventory_frame, text="Inventory")
inventory_button_container = Frame(admin_inventory_frame, bg='grey')
inventory_button_container.pack(side="left", fill="y")
manage_products_button = Button(inventory_button_container, text="Manage Products", command=manage_products_clicked)
manage_products_button.pack(pady=10)
manage_suppliers_button = Button(inventory_button_container, text="Manage Suppliers")
manage_suppliers_button.pack(pady=10)
update_counts_button = Button(inventory_button_container, text="Update Counts")
update_counts_button.pack(pady=10)
button4 = Button(inventory_button_container, text="Button 4")
button4.pack(pady=10)
button5 = Button(inventory_button_container, text="Button 5")
button5.pack(pady=10)
inventory_data_container = Frame(admin_inventory_frame)
inventory_data_container.pack(fill='both', expand=True)


inventory_main_frame = Frame(inventory_data_container)
inventory_main_frame.place(relwidth=1, relheight=1)
main_frame_message = Label(inventory_main_frame, text="Please select an option from the left", font=('Helvetica 20 bold'))
main_frame_message.place(relx=.25, rely=.3)

products_main_frame = Frame(inventory_data_container)
products_main_frame.place(relwidth=1, relheight=1)
products_frame = Frame(products_main_frame)
products_frame.place(relwidth=1, relheight=.5)
products_header = Label(products_frame, text="Select a product category below", font=('Helvetica 12 bold'))
products_header.pack()
options = ["Bread", "Cleaning", "Coffee", "Dairy", "Meat", "Other", "Paper", "Produce", "Retail", "Sugars, Spices, Seasonings"]
options_svar = StringVar()
options_svar.set("")
products_cb = ttk.Combobox(products_frame, textvariable=options_svar, values=options)
products_cb.pack(pady=5, fill='x', padx=30)
products_cb.bind("<<ComboboxSelected>>", cb_product_selected)

products_tree = ttk.Treeview(products_frame)
products_tree['show'] = 'headings'
products_tree['columns'] = ("Product ID", "Supplier ID", "Product Name", "Manufacturer", "Price per case", "Case Quantity")
products_tree.pack(fill='x')
products_main_frame.lower()

products_tree.column("Product ID", width=10, anchor='center')
products_tree.column("Supplier ID", width=10, anchor='center')
products_tree.column("Product Name", width=50)
products_tree.column("Manufacturer", width=50)
products_tree.column("Price per case", width=50, anchor='center')
products_tree.column("Case Quantity", width=50, anchor='w')

products_tree.heading("Product ID", text="Product ID")
products_tree.heading("Supplier ID", text="Supplier ID")
products_tree.heading("Product Name", text="Product Name")
products_tree.heading("Manufacturer", text="Manufacturer")
products_tree.heading("Price per case", text="Price per Case")
products_tree.heading("Case Quantity", text="Case Quantity")

products_vsb = ttk.Scrollbar(products_frame, orient="vertical", command=products_tree.yview)
products_vsb.place(x=835, y=60, height=222)
products_tree.configure(yscrollcommand=products_vsb.set)

bottom_container_cover = Frame(products_main_frame)
bottom_container_cover.place(relheight=.5, relwidth=1, rely=.4)
product_bottom_container = Frame(products_main_frame)
product_bottom_container.place(relheight=.5, relwidth=1, rely=.4)
product_buttons_container = Frame(product_bottom_container)
product_buttons_container.place(relheight=1, relwidth=.2)
add_product_button = Button(product_buttons_container, text="Add New Product", command=add_product_clicked)
add_product_button.pack(pady=20, padx=20, fill='x')
edit_product_button = Button(product_buttons_container, text="Edit Selected Product", command=edit_product_clicked)
edit_product_button.pack(pady=20, padx=20, fill='x')
delete_product_button = Button(product_buttons_container, text="Delete Selected Product")
delete_product_button.pack(pady=20, padx=20, fill='x')
product_bottom_container.lower()

details_form_cover = Frame(product_bottom_container)
details_form_cover.place(relheight=1, relwidth=.8, relx=.2)

new_product_details_form = Frame(product_bottom_container)
new_product_details_form.place(relheight=1, relwidth=.77, relx=.23)
product_title = Label(new_product_details_form, text="Enter the details for the new product:", font=('Arial 12'))
product_title.grid(row=0, column=0, columnspan=2, pady=13)
supplier_id_label = Label(new_product_details_form, text="Supplier ID:")
supplier_id_label.grid(row=1, column=0, pady=10, padx=10)
supplier_id_entry = Entry(new_product_details_form, width=75)
supplier_id_entry.grid(row=1, column=1, pady=10, padx=10)
product_name_label = Label(new_product_details_form, text="Product Name:")
product_name_label.grid(row=2, column=0, pady=10, padx=10)
product_name_entry = Entry(new_product_details_form, width=75)
product_name_entry.grid(row=2, column=1, pady=10, padx=10)
manufacturer_label = Label(new_product_details_form, text="Manufacturer:")
manufacturer_label.grid(row=3, column=0, pady=10, padx=10)
manufacturer_entry = Entry(new_product_details_form, width=75)
manufacturer_entry.grid(row=3, column=1, pady=10, padx=10)
ppc_label = Label(new_product_details_form, text="Price per Case:")
ppc_label.grid(row=4, column=0, pady=10, padx=10)
ppc_entry = Entry(new_product_details_form, width=75)
ppc_entry.grid(row=4, column=1, pady=10, padx=10)
case_qty_label = Label(new_product_details_form, text="Quantity in Case:")
case_qty_label.grid(row=5, column=0, pady=10, padx=10)
case_qty_entry = Entry(new_product_details_form, width=75)
case_qty_entry.grid(row=5, column=1, pady=10, padx=10)
new_product_submit_button = Button(new_product_details_form, text="Submit", width=20)
new_product_submit_button.grid(row=6, column=1)
new_product_details_form.lower()

edit_product_details_form = Frame(product_bottom_container)
edit_product_details_form.place(relheight=1, relwidth=.77, relx=.23)
product_title = Label(edit_product_details_form, text="Edit details for existing product:", font=('Arial 12'))
product_title.grid(row=0, column=0, columnspan=2, pady=13)
supplier_id_label = Label(edit_product_details_form, text="Supplier ID:")
supplier_id_label.grid(row=1, column=0, pady=10, padx=10)
supplier_id_entry = Entry(edit_product_details_form, width=75)
supplier_id_entry.grid(row=1, column=1, pady=10, padx=10)
product_name_label = Label(edit_product_details_form, text="Product Name:")
product_name_label.grid(row=2, column=0, pady=10, padx=10)
product_name_entry = Entry(edit_product_details_form, width=75)
product_name_entry.grid(row=2, column=1, pady=10, padx=10)
manufacturer_label = Label(edit_product_details_form, text="Manufacturer:")
manufacturer_label.grid(row=3, column=0, pady=10, padx=10)
manufacturer_entry = Entry(edit_product_details_form, width=75)
manufacturer_entry.grid(row=3, column=1, pady=10, padx=10)
ppc_label = Label(edit_product_details_form, text="Price per Case:")
ppc_label.grid(row=4, column=0, pady=10, padx=10)
ppc_entry = Entry(edit_product_details_form, width=75)
ppc_entry.grid(row=4, column=1, pady=10, padx=10)
case_qty_label = Label(edit_product_details_form, text="Quantity in Case:")
case_qty_label.grid(row=5, column=0, pady=10, padx=10)
case_qty_entry = Entry(edit_product_details_form, width=75)
case_qty_entry.grid(row=5, column=1, pady=10, padx=10)
product_id_label1 = Label(edit_product_details_form, text="Product ID:")
product_id_label1.grid(row=6, column=0, pady=10, padx=10)
product_id_label2 = Label(edit_product_details_form, text="Product ID will be here")
product_id_label2.grid(row=6, column=1, pady=10, padx=10)
edit_product_submit_button = Button(edit_product_details_form, text="Submit", width=20)
edit_product_submit_button.grid(row=7, column=1)
edit_product_details_form.lower()
#END INVENTORY TAB

#BEGIN ORDERS TAB
admin_notebook.add(admin_orders_frame, text="Orders")
#END ORDERS TAB

#BEGIN CATERING TAB
admin_notebook.add(admin_catering_frame, text="Catering")
#END CATERING TAB

#BEGIN REPORTS TAB
admin_notebook.add(admin_reports_frame, text="Reports")
#END REPORTS TAB

##END ADMIN NOTEBOOK##


#This frame is brought to the front after a successful user login
user_logged_in = Frame(root, bg='#454040', highlightbackground="#332e2d", highlightthickness=1)
user_logged_in.place(relx=.5, rely=.5, anchor='c', width=968, height=738)

##BEGIN USER NOTEBOOK##
#Using a notebook for simplified navigation
user_notebook = ttk.Notebook(user_logged_in)
user_notebook.pack(fill="both", expand=True)


#Creating a frame for each tab of the notebook
user_main_frame = Frame(user_notebook, width=968, height=738)

#BEGIN WELCOME TAB
user_notebook.add(user_main_frame, text="Welcome Page")
un_user_text = StringVar()
welcome_un = Label(user_main_frame, textvariable=un_user_text)
welcome_un.pack(anchor="center", pady=20)
welcome_label = Label(user_main_frame, text=f"You are logged in to the Blockhouse Inventory Management System.\n Use the tabs above to see all available options.")
welcome_label.pack(anchor="center", pady=25)
logout_button = Button(user_main_frame, text="Logout", command=logout_clicked)
logout_button.pack(anchor="center")
#END WELCOME TAB

##END USERS NOTEBOOK##

#Lowering the admin/user page so that it is invisible until a successful login occurs
admin_logged_in.lower()
user_logged_in.lower()

root.mainloop()