Blogging Platform API
Overview
Welcome to the Blogging Platform API! This is a dynamic content management system designed for both bloggers and readers. The platform allows users to manage blog posts, interact with content, and enjoy features like commenting, liking, sharing posts, and subscribing to other bloggers or categories.

Built using Django REST Framework, this platform provides a user-friendly and scalable solution for managing blog content. Whether you're a blogger looking to share posts or a reader exploring content, this platform offers a great experience.

Features
1. User Authentication and Profile Management
Secure user registration, login, and profile management.

Users can personalize their profiles with a bio and profile picture.

Authentication is token-based via Django REST Framework’s Token Authentication.

2. Post Creation and Management
Bloggers can create, update, and delete blog posts.

Posts can be categorized and tagged for better discoverability.

Each post has an author, title, content, and publish date.

3. Categories and Tags
Content is organized into categories for easy browsing.

Posts can be tagged with keywords to make them easily searchable.

Categories and tags provide better filtering options for the posts.

4. Commenting and Liking
Users can comment on posts and like them.

Full CRUD functionality is available for comments.

Users can like posts, with a unique like system that ensures they can like a post only once.

5. Subscriptions
Users can subscribe to bloggers or categories to stay updated on new posts and content.

Subscriptions help users keep track of content they're interested in.

6. Post Sharing
Posts can be shared via email, extending their reach beyond the platform.

Easily share posts with other users by providing their email address.

7. Search and Filtering
Advanced search and filter features allow users to find posts based on categories, tags, and keywords.

Users can sort posts based on various criteria such as published date and category name.

8. Full-Featured REST API
A fully integrated REST API to handle the above features.

Enables third-party integrations and mobile app support.

Endpoints
Root Endpoint
GET /
Displays a welcome message and information about the platform.

Authentication
POST /api/token/
Get a token by providing your username and password.

Blog Posts
GET /posts/
List all published posts.

POST /posts/
Create a new post (authenticated users only).

GET /posts/{post_id}/
Get detailed information about a single post.

PUT /posts/{post_id}/
Update an existing post (authenticated users only).

DELETE /posts/{post_id}/
Delete a post (authenticated users only).

Comments
GET /posts/{post_id}/comments/
List all comments for a specific post.

POST /posts/{post_id}/comments/
Create a new comment on a post (authenticated users only).

Likes
POST /posts/{post_id}/like/
Like a post (authenticated users only).

DELETE /posts/{post_id}/unlike/
Unlike a post (authenticated users only).

Subscriptions
POST /subscribe/
Subscribe to a blogger or category (authenticated users only).

Categories
GET /categories/
List all categories.

POST /categories/
Create a new category (authenticated users only).

GET /categories/{category_id}/
Get details about a specific category.

Post Sharing
POST /posts/{post_id}/share/
Share a post with a given email address (authenticated users only).

Project Setup
Prerequisites
Python 3.x

Django 3.x or higher

Django REST Framework

Django markdownify for rendering markdown content

A working email backend for sending email (e.g., Gmail or an SMTP server)



Installation
Clone the repository:

git clone https://github.com/IjalusiMargaret/Alx_BloggingPlatform.git
cd blogging-platform-api


Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate



Install the required dependencies:

pip install -r requirements.txt


Apply the migrations:

python manage.py migrate


Create a superuser for the admin panel:
python manage.py createsuperuser


Start the development server:

Start the development server:The API should now be running at http://127.0.0.1:8000/.


Testing the API with Postman

Get an Authentication Token
To interact with protected endpoints (like posting comments or creating new posts), you'll need to authenticate using a token.

Send a POST request to /api/token/ with your username and password to get the token.

Add the Token to Your Headers
Once you have the token, you need to include it in your request headers as follows:

Authorization: Token <your_token_here>
Create new post - http://127.0.0.1:8000/Blog/posts/
update a post - http://127.0.0.1:8000/Blog/posts/5/
Delete a post -http://127.0.0.1:8000/Blog/posts/7/
create new category - http://127.0.0.1:8000/Blog/categories/
list all categories - http://127.0.0.1:8000/Blog/categories/
add comment - http://127.0.0.1:8000/Blog/posts/1/comments/
list all comments - http://127.0.0.1:8000/Blog/posts/1/comments/
like a post - http://127.0.0.1:8000/Blog/posts/1/like/
unlike a post - http://127.0.0.1:8000/Blog/posts/1/unlike/
share a post - http://127.0.0.1:8000/Blog/posts/1/share/
suscribe - http://127.0.0.1:8000/Blog/subscribe/

The endpoints below do not need token authentication
Test get all post - http://127.0.0.1:8000/Blog/posts/
Test get post by ID -http://127.0.0.1:8000/Blog/posts/2
Test list all categories - http://127.0.0.1:8000/Blog/categories/
Test get category by ID -http://127.0.0.1:8000/Blog/categories/1/
