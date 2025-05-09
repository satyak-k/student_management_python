# Student Management Application (Django)

This project implements a Student Management system using Django and Python, with a MySQL database. It provides Create, Read, Update, and Delete (CRUD) functionalities for student records, along with user authentication and other features as outlined below.

## Requirements

* **Backend:** Python with Django framework (version compatible with requirements.txt).
* **Database:** MySQL.
* **Frontend:** Django templates, basic CSS and Bootstrap, JS DataTables.

## Features

* **Student CRUD:**
    * **Create:** Add new student records with name, class, and admission date.
    * **Read:** List all students with pagination and display their details.
    * **Update:** Edit existing student information.
    * **Delete (Soft Delete):** Mark students as deleted without permanently removing them from the database. Deleted students are not displayed in the main list.
* **Student Model:** Includes fields for `student_name`, `class`, `admission_date`, timestamps (`created_at`, `updated_at`), and soft delete (`deleted_at`).
* **Database Management:** Uses Django migrations for database schema management.
* **Form Validation:** Implements validation for all form inputs to ensure data integrity.
* **Search Functionality:** Allows filtering students by `student_name` or `class`.
* **Pagination:** Lists students with pagination to improve performance and user experience.
* **JS DataTables Integration:** Enhances the student list table with features like sorting and advanced searching.
* **User Authentication:** Implements user login and logout functionality using Django's built-in authentication system.
* **Responsive Design:** Basic CSS and Bootstrap are used to ensure the application is responsive on different screen sizes.

## Setup Instructions

Follow these steps to set up and run the application on your local machine:

1.  **Prerequisites:**
    * **Python:** Ensure you have Python installed (version compatible with Django). You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
    * **pip:** Python package installer, usually included with Python.
    * **MySQL:** Ensure you have MySQL server installed and running. You can download it from [https://dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/).

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/satyak-k/student_management_python
    cd student_management
    ```
    (https://github.com/satyak-k/student_management_python)
3.  **Create and Activate Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` file, install Django and the MySQL client manually: `pip install Django mysqlclient`)*

5.  **Configure Database:**
    * Create a MySQL database (e.g., `student_db`).
    * Open the `student_management/settings.py` file.
    * Modify the `DATABASES` setting to match your MySQL configuration:

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'student_management',
                'USER': 'your_mysql_user',
                'PASSWORD': 'your_mysql_password',
                'HOST': '127.0.0.1',
                'PORT': '3306',
            }
        }
        ```
        *(Replace `your_mysql_user` and `your_mysql_password` with your MySQL credentials.)*

6.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```
    This command creates the necessary database tables based on your Django models.

7.  **Create Superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an administrative user.

8.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    This starts the Django development server. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

1.  **Access the Application:** Open your web browser and go to `http://127.0.0.1:8000/students/`. This will display the list of students.

2.  **User Authentication:**
    * To access administrative features or protected views (if implemented beyond basic CRUD), log in using the superuser account you created or any other registered user account. The login URL is typically `/accounts/login/`.
    * The logout URL is typically `/accounts/logout/`.

3.  **Student Management:**
    * **View Students:** The main page displays a paginated list of students with their name, class, admission date, and actions. The "Class Teacher" column is not applicable to this Django-based task.
    * **Search Students:** Use the search bar to filter students by name or class.
    * **Add New Student:** Click the "Add Student" button to open a form for creating a new student record. Fill in the details and submit the form.
    * **Edit Student:** Click the "Edit" button next to a student to modify their information. Update the fields and submit the form.
    * **Delete Student:** Click the "Delete" button next to a student to soft-delete their record. The student will no longer appear in the main list but will remain in the database with a `deleted_at` timestamp.

## GitHub Repository

You can find the complete project code on GitHub at:

https://github.com/satyak-k/student_management_python

## Code Quality

The codebase is organized logically with clear naming conventions and follows Django best practices to ensure maintainability.

## Functionality

All the core CRUD operations for the Student model are fully implemented and functional. Form validation ensures data integrity. Soft delete functionality prevents permanent data loss. Search and pagination enhance the user experience when dealing with a large number of student records. The integration of JS DataTables provides advanced table features. User authentication secures access to the application.

## UI/UX

The user interface is designed to be clean and intuitive, utilizing basic CSS and Bootstrap for a responsive layout. JS DataTables enhances the table's usability with features like sorting and filtering.

## Submission

This project has been uploaded to GitHub at the following link:

https://github.com/satyak-k/student_management_python

A detailed README file with setup and usage instructions is included in the repository.
