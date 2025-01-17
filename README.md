# Django Blog Application

A full-featured blog application built with Django that allows users to create, read, update and delete blog posts, manage user profiles, and interact through comments.

## Features

- User Authentication (Login/Logout)
- Blog Post Management
  - Create new posts
  - Read posts
  - Delete posts (for authors and admins)
  - File attachments support
- Comment System
  - Add comments on posts
  - Delete comments (for comment authors, post authors, and admins)
- User Profiles
  - Customizable profile information
  - Profile picture upload
  - View user's posts
  - Edit profile details (hobbies, skills, profession)
- Search Functionality
  - Search posts by title

## Technology Stack

- Python 
- Django 
- Bootstrap 
- SQLite3

## Installation

1. Clone the repository
```bash
git clone https://github.com/anevski-stefan/django-blogapp.git
cd django-blogapp
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  
```

3. Install dependencies
```bash
pip install django
pip install Pillow  
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

6. Start the development server
```bash
python manage.py runserver
```

## Project Structure

The main application components are:

- `blogApp/` - Main application directory
  - `models.py` - Contains UserInfo, BlogPost, and PostComment models
  - `views.py` - Contains all view functions
  - `forms.py` - Contains forms for post creation and profile editing
  - `templates/` - Contains all HTML templates
  - `admin.py` - Admin panel configuration

## Usage

1. Access the application at `http://localhost:8000/posts/`
2. Login with your credentials
3. Create new posts, comment on existing posts
4. Edit your profile information
5. Search for posts using the search bar

