# Project Overview
You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## About
This project is a RESTful web application utilizing the Flask framework which accesses a SQL database that populates categories and their items. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

## In This Repo
This project has one main Python module `app.py` 
A SQL database is created using the `database_setup.py` module and `database_init.py`.
The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application.

## You must instull
Here's what you should do:

1. Install Vagrant and VirtualBox
2. Clone the fullstack-nanodegree-vm
3. Launch the Vagrant VM (vagrant up) then (vagrant ssh)
4. Write your Flask application locally in the vagrant/catalog directory (which will automatically be synced to /vagrant/catalog within the VM).
5. Run database_setup then to fill data base run database_init
6. Run your application within the VM (python /vagrant/catalog/app.py)
7. Access and test your application by visiting http://localhost:5000 locally


## links you needs 
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)


## Google Login
To get the Google login working there are a few additional steps:

1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'Item-Catalog'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory that you cloned from here
14. Run application using `python /item-catalog/app.py`

## JSON Endpoints

Catalog JSON: `/catalog/JSON` - Displays the whole catalog. Categories and all items.

Categories JSON: `/catalog/categories/JSON` - Displays all categories

Category Items JSON: `/catalog/<path:category_name>/items/JSON`- Displays items for a specific category

Category Item JSON: `/catalog/<path:category_name>/<path:item_name>/JSON` - Displays a specific category item.

