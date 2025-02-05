SOCIAL WEBSITE

Overview
A social website that allows users to log in using their Google, Facebook, or Twitter accounts.

Features
Multi-authentication support:
Google OAuth 2.0
Facebook OAuth 2.0
Twitter OAuth 1.0a
User profile management
Friend/follow system
Posting and commenting system

Google, Facebook, and Twitter API keys (hidden for security)

Installation
Clone the repository: git clone https://github.com/Cchimjiokem/social_website.git
Navigate into the project directory: cd bookmarks
Install dependencies: pip install -r requirements.txt
Set environment variables for API keys (see below)
Run migrations: python manage.py migrate
Start the development server: python manage.py runserver

Environment Variables
To keep your API keys secure, set the following environment variables:
GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
FACEBOOK_APP_ID
FACEBOOK_APP_SECRET
TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET

Usage
Open your web browser and navigate to http://localhost:8000
Log in using your Google, Facebook, or Twitter account
Explore the website's features and connect with others

Contributing
Contributions are welcome! If you'd like to report a bug or suggest a feature, please open an issue on this repository.

Acknowledgments
Special thanks to the Django community and the developers of the Google, Facebook, and Twitter APIs for making this project possible.