# Portfolio Website

A professional portfolio website built with Django, featuring a contact form with database integration and responsive design using Bootstrap.

## Features

- Responsive design using Bootstrap
- Contact form with database storage
- Admin interface for managing contact submissions
- Multiple pages (Home, About, Projects, Contact)

## Requirements

- Python 3.8+
- Django 4.2+
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd portfolio_project
```

2. Create and activate virtual environment

````bash
# Windows
python -m venv venv
venv\Scripts\activate

3. Install dependencies
```bash
pip install -r requirements.txt
````

4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (for admin access)

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to view the website.

## Project Structure

```
portfolio_project/
├── portfolio_project/    # Project configuration
├── main/               # Main application
├── static/             # Static files (images)
├── templates/         # HTML templates
└── media/           # User-uploaded files
```

## Usage

- Access the admin interface at `/admin` to manage contact form submissions
- Customize the templates in the `templates/` directory
- Add your projects and information in the respective template files

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
