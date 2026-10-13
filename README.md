# Glassmorphism Login

A Django login page with a glassmorphism design.

## Setup

1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver

# Glassmorphism Login

A login page built with Django and styled with a glassmorphism design: a frosted-glass card over a mountain background image.

## Features

- Glassmorphism login card (blurred, semi-transparent glass effect)
- Floating labels on the username and password fields
- Responsive layout that works on desktop and mobile
- Django templates and static files setup
- Login logic with Django's built-in authentication (in progress)

## Tech Stack

- Python 3
- Django 6.1
- HTML5 and CSS3
- SQLite (default Django database)

## Project Structure

```
glassmorphism/                  # project root (contains manage.py)
├── accounts/                   # the app that holds the login page
│   ├── migrations/
│   │   └── __init__.py
│   ├── static/
│   │   └── accounts/
│   │       ├── css/
│   │       │   └── style.css       # glassmorphism styles
│   │       └── images/
│   │           └── hero-bg.jpg     # background image
│   ├── templates/
│   │   └── accounts/
│   │       └── login.html          # login page template
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py                     # app URL routes
│   └── views.py                    # login logic
├── glassmorphism/              # project configuration package
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                 # project settings
│   ├── urls.py                     # root URL routing
│   └── wsgi.py
├── .gitignore
├── LICENSE
├── manage.py                   # command-line utility
├── README.md
└── requirements.txt            # Python dependencies
```

## Getting Started

1. Clone the repository:

```bash
   git clone https://github.com/Maxwel12744/glassmorphism-login.git
   cd glassmorphism-login
```

2. (Recommended) Create and activate a virtual environment:

```bash
   python -m venv venv
   source venv/Scripts/activate
```

3. Install the dependencies:

```bash
   pip install -r requirements.txt
```

4. Apply the database migrations:

```bash
   python manage.py migrate
```

5. Create a user to log in with:

```bash
   python manage.py createsuperuser
```

6. Start the development server:

```bash
   python manage.py runserver
```

7. Open http://127.0.0.1:8000 in your browser.

## Roadmap

- [x] Frontend login page
- [ ] Backend login logic (authenticate and redirect)
- [ ] Dashboard page
- [ ] Registration page
- [ ] Forgot password flow

## Credits

The login form design is based on a tutorial by [CodingNepal](https://www.codingnepalweb.com).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
