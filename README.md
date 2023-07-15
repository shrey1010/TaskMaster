# TaskMaster
Your ultimate todo companion. Stay organized, boost productivity, and manage tasks effortlessly. With secure authentication and easy CRUD functionality.
It is a web-based todo application built with Django that allows users to create, manage, and organize their tasks. It provides user authentication, CRUD functionality, and the ability to track task status and priority.

## Features
User Authentication: Users can create an account, log in, and securely authenticate themselves to access their todo lists.

Create Todo: Users can create new tasks by providing a title, description, due date, and priority level.

Read Todo: Users can view their existing tasks, including the title, description, due date, status (pending or complete), and priority level.

Update Todo: Users can update task details, such as title, description, due date, status, and priority.

Delete Todo: Users can remove tasks they no longer need.

Task Status: Users can change the status of a task to mark it as pending or complete.

Task Priority: Users can assign priority levels (e.g., high, medium, low) to tasks.


## Installation
Clone the repository: git clone https://github.com/shrey1010/TaskMaster.git

Navigate to the project directory: cd TaskMaster

Install the dependencies: pip install -r requirements.txt

Set up the database:

Run database migrations: python manage.py migrate

(Optional) Create a superuser: python manage.py createsuperuser

Start the development server: python manage.py runserver

Open your web browser and visit: http://localhost:8000

## Usage
Create an account or log in to your existing account.

On the dashboard, you can view your existing tasks and create new tasks.

Click on a task to view its details and make updates.

To mark a task as complete, click the "Complete" button.

To change the task priority, select the desired priority level from the dropdown menu.

To delete a task, click the "Delete" button.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgements
This project was inspired by the need for a simple and efficient todo application.
Thanks to the Django community for their excellent documentation and resources.
Feel free to customize this README file to match your project's specific details, requirements, and guidelines.
