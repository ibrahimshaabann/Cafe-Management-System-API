# Coffee Management System API

The Coffee Management System API is a comprehensive backend system that handles various aspects of coffee shop management. This API is designed to support four main industries within the coffee business:

1. **Authentication**: Manage user authentication, user roles, and provide JWT (JSON Web Tokens) for secure access.

2. **Financials**: Keep track of costs, benefits, calculate net profit, manage shift benefits, and update order total prices on benefits for users.

3. **Human Resources**: Handle employee management, including worker details, salaries, deductions, attendance, and leaving records. Track shift start and end times, as well as customer data.

4. **Sales**: Manage orders, order items, menus, categories, and table assignments to streamline the coffee shop's daily operations.

## Features

### Authentication

- **User Management**: Create and manage user accounts with different roles, such as admin, staff, and manager.
- **JWT Authentication**: Securely authenticate users and generate JWT tokens for API access.
- **User Roles**: Assign specific permissions and access levels based on user roles.
   - #### Roles included in our project: Admin, User.  

### Financials

- **Cost Tracking**: Record and manage various costs incurred in the coffee shop allow user to add costs during his shift.
- **Benefits Management**: Monitor benefits and profits over time bt calculating ptofits, costs and net profits.
- **Net Profit Calculation**: Automatically calculate net profits by subtracting costs from benefits.
- **Shift Benefits**: Track benefits specific to each shift by adding the benefits oll orders processed in that shift.
- **Order Total Updates**: Automatically update order total prices based on menu items and quantities.

### Human Resources

- **Employee Management**: Maintain employee records, including personal information, salary and contact details.
   - #### Note that we provied some epmloyees with user accounts, only the ones respnsible for shifts. 
- **Salary Management**: Record and manage employee salaries, and deductions.
- **Attendance Records**: Keep track of employee attendance and leaves times.
- **Shift Management**: Record user shift start and end times for employees.
- **Customer Data**: Store customer information and preferences for better service.

### Sales

- **Order Management**: Create and manage customer orders.
- **Order Items**: List and customize order items, including menu items, quantities, and prices.
- **Menu and Categories**: Organize menu items into categories for easy access.
- **Table Management**: Assign tables to orders for efficient service.


## Getting Started

To run the Coffee Management System API locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ibrahimshaabann/Cafe-Management-System-API
   cd Coffee-Management-System-API
   ```

2. **Set up a virtual environment and install dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure your postgres database settings in `settings.py`:**

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'your_database_host',
           'PORT': 'your_database_port',
       }
   }
   ```

4. **Run database migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser account for admin access:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

The API should now be accessible at `http://localhost:8000/`. You can use the Django admin panel to manage users, roles, and other data.

#### Authentication
- `POST /token/`: Obtain a JSON Web Token (JWT) for authentication by providing valid user credentials.
   >>> Roles: User, Admin 
- `POST /token/refresh/`: Refresh an expired JWT to obtain a new one.
    >>> Roles: User, Admin
- `GET /authentication/users/`: List all users records.
   >>> Roles: Admin
- `POST /authentication/users/`: Create a new user.
   >>> Roles: Admin
- `GET /authentication/users/{id}/`: Retrieve details of a specific cost record.
  >>> Roles: User, Admin
- `PUT /authentication/users/{id}/`: Update a specific cost record.
  >>> Roles: Admin
- `DELETE /authentication/users/{id}/`: Delete a specific cost record.
  >>> Roles: Admin

#### Financials
- `GET /financials/costs/`: List all cost records.
  >>> Roles: Admin
- `POST /financials/costs/`: Create a new cost record.
  >>> Roles: User or Admin
- `GET /financials/costs/{id}/`: Retrieve details of a specific cost record.
  >>> Roles: Admin   
- `PUT /financials/costs/{id}/`: Update a specific cost record.
  >>> Roles: Admin
- `DELETE /financials/costs/{id}/`: Delete a specific cost record.
  >>> Roles: Admin
- `GET /financials/benefits/`: List all benefit records.
  >>> Roles: Admin
- `POST /financials/benefits/`: Create a new benefit record.
  >>> Roles: Admin
- `GET /financials/benefits/{id}/`: Retrieve details of a specific benefit record.
  >>> Roles: Admin
- Note that neither Admin nor user are allowed to delete benefit object or update it.

#### Human Resources
- `GET /humanresources/employees/`: List all employee records.
- >>> Roles: Admin
- `POST /humanresources/employees/`: Create a new employee record.
   >>> Roles: Admin
- `GET /humanresources/employees/{id}/`: Retrieve details of a specific employee record.
   >>> Roles: Admin
- `PUT /humanresources/employees/{id}/`: Update a specific employee record.
  >>> Roles: Admin
- `DELETE /humanresources/employees/{id}/`: Delete a specific employee record.
  >>> Roles: Admin
- `GET /humanresources/deductions/`: List all salary deductions records.
  >>> Roles: Admin
- `POST /humanresources/deductions/`: Create a new salary deduction record.
  >>> Roles: Admin
- `GET /humanresources/deductions/{id}/`: Retrieve details of a specific salary deduction record.
  >>> Roles: Admin
- `PUT /humanresources/deductions/{id}/`: Update a specific salary deduction record.
  >>> Roles: Admin
- `DELETE /humanresources/deductions/{id}/`: Delete a specific salary deduction record.
  >>> Roles: Admin

#### Sales
- `GET /sales/menu/`: List all menu items.
  >>> Roles: Admin, User
- `POST /sales/menu/`: Create a new menu item.
  >>> Roles: Admin
- `GET /sales/menu/{id}/`: Retrieve details of a specific menu item.
  >>> Roles: Admin, User
- `PUT /sales/menu/{id}/`: Update a specific menu item.
  >>> Roles: Admin, User
- `DELETE /sales/menu/{id}/`: Delete a specific menu item.
  >>> Roles: Admin
- `GET /sales/tables/`: List all tables.
  >>> Roles: Admin, User
- `POST /sales/tables/`: Create a new table.
  >>> Roles: Admin
- `GET /sales/tables/{id}/`: Retrieve details of a specific table.
  >>> Roles: Admin, User
- `PUT /sales/tables/{id}/`: Update a specific table.
  >>> Roles: Admin
- `DELETE /sales/tables/{id}/`: Delete a specific table.
  >>> Roles: Admin
- `GET /sales/categories/`: List all categories.
  >>> Roles: Admin
- `POST /sales/categories/`: Create a new category.
  >>> Roles: Admin
- `GET /sales/categories/{id}/`: Retrieve details of a specific category.
  >>> Roles: Admin
- `PUT /sales/categories/{id}/`: Update a specific category.
  >>> Roles: Admin
- `DELETE /sales/categories/{id}/`: Delete a specific category.
  >>> Roles: Admin
- `GET /sales/orders/`: List all orders.
  >>> Roles: Admin, User
- `POST /sales/orders/`: Create a new order.
  >>> Roles: Admin, User
- `GET /sales/orders/{id}/`: Retrieve details of a specific order.
  >>> Roles: Admin, User
- `PUT /sales/orders/{id}/`: Update a specific order.
  >>> Roles: Admin
- `DELETE /sales/orders/{id}/`: Delete a specific order.
  >>> Roles: Admin
- `GET /sales/orderitems/`: List all order items.
  >>> Roles: Admin, User
- `POST /sales/orderitems/`: Create a new order item.
  >>> Roles: Admin
- `GET /sales/orderitems/{id}/`: Retrieve details of a specific order item.
  >>> Roles: Admin, User
- `PUT /sales/orderitems/{id}/`: Update a specific order item.
  >>> Roles: Admin
- `DELETE /sales/orderitems/{id}/`: Delete a specific order item.
  >>> Roles: Admin, User
- `GET /sales/active_orders/`: List the last order in every table.
 >>> Roles: Admin, User
You can use these endpoints to interact with the Coffee Management System API.
### Technologies Used
- **Django**: The backend framework used for building the API.
- **Django Rest Framework (DRF)**: An extension for Django that simplifies building RESTful APIs.
- **JWT Authentication**: JSON Web Tokens are used for secure user authentication.
- **PostgreSQL**: The relational database management system used to store data.
- **Python**: The programming language in which the application is developed.
- **Git Terminal**: Version control system for tracking changes in the project.


