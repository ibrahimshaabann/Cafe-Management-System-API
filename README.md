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

### Financials

- **Cost Tracking**: Record and manage various costs incurred in the coffee shop, including inventory, utilities, and employee salaries.
- **Benefits Management**: Monitor benefits and profits over time.
- **Net Profit Calculation**: Automatically calculate net profits by subtracting costs from benefits.
- **Shift Benefits**: Track benefits specific to each shift.
- **Order Total Updates**: Automatically update order total prices based on menu items and quantities.

### Human Resources

- **Employee Management**: Maintain employee records, including personal information and contact details.
- **Salary Management**: Record and manage employee salaries, and deductions.
- **Attendance Records**: Keep track of employee attendance and leaves.
- **Shift Management**: Record shift start and end times for employees.
- **Customer Data**: Store customer information and preferences for better service.

### Sales

- **Order Management**: Create and manage customer orders.
- **Order Items**: List and customize order items, including menu items, quantities, and prices.
- **Menu and Categories**: Organize menu items into categories for easy access.
- **Table Management**: Assign tables to orders for efficient service.

Certainly! Here's the "Getting Started" section of the README.md in full Markdown code:

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


