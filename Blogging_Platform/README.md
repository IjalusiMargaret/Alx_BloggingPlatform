# Blogging Platform API

A fully-featured Blogging Platform API built with Django and Django REST Framework. This API supports user authentication, post management, comments, likes, subscriptions, sharing posts via email, filtering, search, and ordering.

---

## Features

- **User Authentication** with DRF Token Authentication.
- **CRUD operations for Posts** (Create, Retrieve, Update, Delete).
- **CRUD operations for Comments** under each post.
- **Like system** for posts (with optional rating support).
- **Subscriptions** to authors or categories.
- **Post sharing** via email.
- **Categories** and **tags** management.
- **Filtering**, **searching**, and **ordering** for posts.
- **Profile model** for user bios and profile pictures.
- Fully RESTful API following best practices.

---

## Technologies Used

- Python 3.x
- Django 5.x
- Django REST Framework
- django-taggit (for tagging)
- DRF Token Authentication
- SQLite (default, can be swapped with PostgreSQL, MySQL, etc.)
- Markdownify (optional for markdown rendering)
- SMTP for email sharing (configure your own email backend)

---

## Models Overview

### User
- Provided by Django's built-in User model.

### Profile
- `user` (OneToOne to User)
- `bio`
- `profile_picture`

### Category
- `name`

### Post
- `title`
- `slug`
- `content`
- `author` (ForeignKey to User)
- `category` (ForeignKey)
- `tags` (via django-taggit)
- `status` (draft/published)
- `published_date`

### Comment
- `post` (ForeignKey to Post)
- `user` (ForeignKey to User)
- `content`
- `created_at`
- `updated_at`

### Like
- `post` (ForeignKey to Post)
- `user` (ForeignKey to User)
- `rating` (optional)

### Subscription
- `user` (subscriber)
- `author` (optional)
- `category` (optional)

---

## API Endpoints

| Endpoint | Method | Description |
| -------- | ------ | ----------- |
| `/api-token-auth/` | POST | Obtain auth token |
| `/posts/` | GET, POST | List all posts / Create a new post |
| `/posts/<int:pk>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a post |
| `/posts/<int:post_id>/comments/` | GET, POST | List or create comments for a post |
| `/posts/<int:post_id>/like/` | POST | Like a post |
| `/subscribe/` | POST | Subscribe to an author or category |
| `/posts/<int:post_id>/share/` | POST | Share a post via email |

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo


2 Create a virtual environment


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3 Install dependencies
   pip install -r requirements.txt

4 Apply migrations

    python manage.py makemigrations
    python manage.py migrate

5  Create a superuser


    python manage.py createsuperuser


6  Run the development server
     python manage.py runserver





Authentication
The API uses DRF's token-based authentication.

Obtain token using:

POST /api-token-auth/
{
    "username": "your_username",
    "password": "your_password"
}
Use the token in subsequent requests via the Authorization: Token <token> header.

Email Setup
To enable the post sharing feature, configure your SMTP settings in settings.py:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourprovider.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@blog.com'
Filtering, Search & Ordering
Search fields: title, content, tags, author username

Ordering fields: published_date, category name

Example usage:

GET /posts/?search=django&ordering=-published_date
Contributing
Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -m 'Add new feature').

Push to your branch (git push origin feature-branch).

Open a Pull Request.

License
This project is licensed under the MIT License.

TODOs
Implement user registration & login views.

Add pagination to Post and Comment listings.

Enhance permissions (e.g., users can only edit/delete their own posts/comments).

Add email notifications for new comments or new posts by subscribed authors.

