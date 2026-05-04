# CS253 Web Development Projects

This repository contains web development projects and assignments for the CS253 Web Development course from Udacity. The projects are built using Google App Engine with Python 2.7 and demonstrate various web development concepts and techniques.

## Course Information
- **Course Page**: https://www.udacity.com/wiki/cs253
- **Original Web App**: https://yaoyaohust2.appspot.com/ (outdated)
- **App Engine Dashboard**: https://appengine.google.com/dashboard?app_id=s~yaoyaohust (outdated)

## Project Structure

```
CS253-Web-Development/
├── README.md                    # This file
├── test.py                      # SQLite practice exercises
├── helloworld/                  # Multi-feature web application
│   ├── app.yaml                 # Google App Engine configuration
│   ├── helloworld.py            # Main application with multiple handlers
│   ├── calculate_and_rot13.py   # Calculator and ROT13 encryption handlers
│   ├── userlogin.py             # User login module (imported by helloworld)
│   ├── happyfish.jpg            # Sample image
│   ├── happyfish.png            # Sample image
│   └── templates/               # HTML templates
│       ├── ascii_chan.html      # ASCII art gallery
│       ├── ascii_chan_sub.html  # Individual ASCII art page
│       ├── calculate.html       # Calculator form
│       ├── rot13.html           # ROT13 encryption form
│       ├── submit.html          # ASCII art submission form
│       └── mainpage.html        # Main landing page
├── hw3/                         # Blog application (Homework 3)
│   ├── app.yaml                 # Google App Engine configuration
│   ├── index.yaml               # Datastore index configuration
│   ├── blog.py                  # Blog application with user authentication
│   ├── static/
│   │   └── main.css             # CSS styles for the blog
│   └── templates/               # Blog templates
│       ├── base.html            # Base template
│       ├── front.html           # Blog front page
│       ├── newpost.html         # New post form
│       ├── permalink.html       # Individual post page
│       ├── post.html            # Post template
│       ├── rot13-form.html      # ROT13 encryption form
│       ├── signup-form.html     # User signup form
│       └── welcome.html         # Welcome page after signup
└── userlogin/                   # Standalone user login application
    ├── app.yaml                 # Google App Engine configuration
    └── userlogin.py             # Simple user registration/login
```

## Applications Overview

### 1. Helloworld Application (`helloworld/`)
A multi-feature web application demonstrating various web development concepts:

**Features:**
- **Main Page**: Landing page with navigation
- **Calculator**: Simple expression calculator (uses `eval()` - security warning)
- **ROT13 Encryption**: Text encryption/decryption using ROT13 cipher
- **ASCII Art Gallery**: User-submitted ASCII art with data persistence
- **User Login**: Basic user registration and login functionality

**Key Components:**
- `helloworld.py`: Main application with URL routing
- `calculate_and_rot13.py`: Calculator and ROT13 handlers
- `userlogin.py`: User authentication module
- Data model: `Art` for storing ASCII art submissions

### 2. Blog Application (`hw3/`)
A fully-featured blog application with user authentication:

**Features:**
- **Blog Front Page**: Displays latest posts (10 most recent)
- **New Post Creation**: Form for creating new blog posts
- **Individual Post Pages**: Permanent links to each post
- **User Registration**: Form validation for username, password, and email
- **ROT13 Tool**: Separate ROT13 encryption utility

**Key Components:**
- `blog.py`: Main application with blog and authentication handlers
- Data model: `Post` for blog posts with subject, content, and timestamps
- Form validation for user registration
- CSS styling for professional appearance

### 3. User Login Application (`userlogin/`)
A standalone user registration application:

**Features:**
- **Registration Form**: Username, password, and email validation
- **Form Validation**: Client-side validation with error messages
- **Success Page**: Redirect to thank you page upon successful registration

**Key Components:**
- `userlogin.py`: Simple registration form with validation logic
- HTML embedded in Python code (no separate templates)

### 4. Test File (`test.py`)
SQLite practice exercises with link data:
- Demonstrates SQLite database operations
- Contains sample link data with votes, titles, and URLs
- Includes query functions for data retrieval

## Technology Stack

- **Runtime**: Python 2.7
- **Framework**: webapp2 (Google App Engine web framework)
- **Template Engine**: Jinja2
- **Database**: Google App Engine Datastore
- **Deployment**: Google App Engine
- **Frontend**: HTML, CSS, JavaScript (basic)

## How to Run

### Prerequisites
1. Google App Engine SDK for Python (or Cloud SDK)
2. Python 2.7
3. Google Cloud Platform account (for deployment)

### Local Development
1. Install Google App Engine SDK or Cloud SDK
2. Navigate to any application directory:
   ```bash
   cd helloworld/  # or hw3/ or userlogin/
   ```
3. Start the development server:
   ```bash
   python helloworld.py app.yaml
   ```

4. Access the application at `http://localhost:8080`

### Deployment to Google App Engine

#### Using Google App Engine SDK (Legacy)
1. Install the Google App Engine SDK for Python
2. Configure your application ID in `app.yaml` (replace "yaoyaohust2" or "udacity-cs253" with your own app ID)
3. Deploy 

## Application URLs

### Helloworld Application
- `/` - Main page
- `/calculate` - Calculator
- `/rot13` - ROT13 encryption
- `/asciichan` - ASCII art gallery
- `/submit` - Submit new ASCII art
- `/userlogin` - User registration
- `/thanks` - Thank you page

### Blog Application
- `/` - Simple hello page
- `/blog/` - Blog front page
- `/blog/newpost` - Create new post
- `/blog/[post_id]` - Individual post
- `/unit2/rot13` - ROT13 tool
- `/unit2/signup` - User registration
- `/unit2/welcome` - Welcome page

### User Login Application
- `/` - Registration form
- `/thanks` - Thank you page

## Security Notes

⚠️ **Security Warning**: The calculator in `helloworld` application uses Python's `eval()` function, which is a security risk in production environments. This is for educational purposes only.

## Data Models

### ASCII Art (`helloworld/`)
```python
class Art(db.Model):
    title = db.StringProperty(required=True)
    art = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
```

### Blog Post (`hw3/`)
```python
class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
```

## Form Validation

Both applications include form validation:
- Username: 3-20 characters, alphanumeric and underscores
- Password: 3-20 characters
- Email: Valid email format (optional in some forms)
- Required fields validation

## Notes

- This project uses Python 2.7, which is deprecated. For new projects, consider migrating to Python 3.
- The applications are designed for Google App Engine and use its specific APIs and data storage.
- Some URLs and application IDs in the original README are outdated.
- The project demonstrates progressive web development concepts from simple forms to full applications with data persistence.

## License

Educational project for CS253 Web Development course.