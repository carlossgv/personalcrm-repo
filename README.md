# Welcome to your Personal CRM!

Hi! If you use free CRM's found online you probably notice that the most important features are behind a pay wall. In my case I use free Hubspot to do most of my CRM needs, but one of the paid key features is the possibility to have a library of products for them to be used when creating quotations. This is the first thing tackled with **PersonalCRM**!

With your **PersonalCRM** you will have a way to create, edit and print quotes using the database of your products with part number, description, prices, etc. All of your quotes are going to be stored with custom information if you decide to change it (for example a different description to match your customer needs).

**PersonalCRM** has MIT Licence so you can clone it, tinker it and change it any way you want! If you make some improvements to the app let me know I would love to apply your changes :).

# Requirements

Since this is a very early stage app you are going to be required to have basic knowledge of **SQL** to change and modify the tables so you can add your own Clients, Contacts and Products.

Also, you should know basic **Django** in order to make it run locally.

# Installation

As mentioned before, **PersonalCRM** can only run for the time being locally through Django. So the steps to make it run are the following:

 1. Clone the repo: `git clone https://github.com/carlossgv/personalcrm-repo.git`
 2. Create an environment to run your app: this step is not 100% required but it is strongly recommended, you should run the app in a controlled environment. If you don't know how to create one you can learn how-to [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
 3. Set up your environment variable for the `SECRET_KEY` within `settings.py`.
 4. Install the requirements with pip: run the following command inside the cloned folder `pip install -r requirements.txt`
 5. Make database migrations: go to `PARENT_FOLDER/personalcrm` and run `python manage.py makemigrations` and `python manage.py migrate`
 6. Run the server: run `python manage.py runserver`
 7. Since not everything is implemented you should go to the following site [http://127.0.0.1:8000/quote/](http://127.0.0.1:8000/quote/)


# Usage

## Quote Index
You will be received with a table with all of your quotes, you can sort the table by ID and by Customer name; also, you will see a short description of the quote, reference number and creator (users and currently not implemented, you are free to create new users directly into User table or use the generic admin user with the following info:

`Username: admin`
`Password: admin`

There is also a "New Quote" button, guess what it does!

##  Create Quote
As the title says, in this page you will be able to create a new quote. It is basically a form with the following items:


 ### Customer (Required): 
Select the customer; you can only select customers defined in the **Company** table within the database, else you will get an error.

### Contact (Required):
Same as customers, only contacts defined in **Contact** table can be selected. 

### Reference #:
Optional reference; for example, quote request ID from your customer.

### Date:
"Today" by default, can be changed.

### Description:
Short description of the quote, option.

### Products Table (At least one required):
Here you can add the quoted items, the table contains the following information:

 - **#:** row number, it will automatically update.
 - **Description:** it has two fields, the product field (datalist) and the description field (textarea). When you select an item from the product field it will autofill the information with the data contained within the **Product** table in your database. You can edit the information in the description area, it will not change the description in the master item info, it will change the description just for this specific quote.
 - **Qty:** quantity of products.
 - **Price:** unit price of the product.
 - **Discount:** fill this field with the percentage of discount granted for the product (0% by default).
 - **Amount:** total price for each product (qty * price), it will automatically fill.
 - **Hidden:** this selector is turned off ("No") by default. If for some reason you want the quote to contain certain items from your products database but you don't want it to be shown in the printed quote turn the selector to "Yes".
 - **"X" button:** deletes current row.
 - **"Add new item" button**: creates a new row for another product.


### Terms & conditions: 

Notes for your client to see, usually lead times, delivery terms and payment terms.

### Tax:
Tax used in your quote, input it as percentage.

### Notes:
This notes are for your personal consumption, your client won't be able to see them.

After pressing "Create Quote" you will be taken to the quote index and you'll see your brand new quote in the table!

## Edit Quote
If you press any of the ID's within the quote index you will be taken to the "Edit Quote" site of the quote clicked. There you can make changes to your quote and saved them or you can view the quote for printing using the proper button at the bottom of the quote.

## Print Quote (View Quote)
After pressing "View Quote" button you will be taken to a site where you can preview how your quote is going to look like. If you think it's OK press Ctrl+P or right click + Print... and you will have your quote ready to send to your customer!


# Short term future features

Because of the short time I didn't manage to feature the CRM as complete as I would want it, but definitely is something that is coming!

## Users
User register and login is going to be implemented soon. Remember, in the meantime everything should be done through users made in the data base or with the superuser:
`Username: admin`
`Password: admin`

## Inventory

There is going to be a product inventory handler with these features:

 - Creating, editing and deleted products from the app.
 - Product index with sorting and searching.
 - Automatically information about stock of quoted items.

## Companies (Customers)

 - Creating, editing and deleted companies from the app.

## Contacts

 - Creating, editing and deleted contacts from the app.

# Long term future features
Hopefully the app is going to have support for a long time; if so, many CRM stuff can be implemented.

 - Reports of quotes made, status of each, customer response, etc.
 - Invoicing system.
 - Beefier inventory system: automate stock management integrated to the CRM (example: deal invoiced automatically update the stock availability for the items sold).
 - Online team integration.

Created by Carlos Gonzalez carlossgv@gmail.com
