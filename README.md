# Calories Tracker

This is a Calories Tracker application built with Streamlit. The application allows users to log their meals, track their daily calorie and macronutrient intake, and visualize their progress.

## Features

- User authentication via username/password or Google login
- Log meals manually or by uploading/taking a photo
- Track daily calorie, protein, carbs, fats, and fiber intake
- Visualize progress with custom progress bars
- Store user data and meal logs in a MySQL database

## Libraries Used

- [Streamlit](https://streamlit.io/) - Web application framework for creating interactive web apps
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) - MySQL database connector
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Read environment variables from a `.env` file
- [openai](https://pypi.org/project/openai/) - OpenAI API client
- [pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and settings management using Python type annotations
- [st-paywall](https://pypi.org/project/st-paywall/) - Streamlit component for adding authentication


## File Structure

- [app.py](http://_vscodecontentref_/3): Main application file
- [login_screen.py](http://_vscodecontentref_/4): Handles user login and authentication
- [database.py](http://_vscodecontentref_/5): Database connection and query functions
- [ai_func.py](http://_vscodecontentref_/6): Functions for interacting with OpenAI API
- [table_creation.sql](http://_vscodecontentref_/7): SQL script for creating database tables
- [requirements.txt](http://_vscodecontentref_/8): List of required Python packages
- [.devcontainer](http://_vscodecontentref_/9): Configuration for VS Code Dev Containers
- [.streamlit](http://_vscodecontentref_/10): Streamlit configuration files
- [packages.txt](http://_vscodecontentref_/11): List of system packages to install in the dev container

## Usage

1. Open the [calories-tracker](https://calories-tracker.streamlit.app) at your browser.
2. Log in using your username/password or Google account.
3. Track your daily calorie and macronutrient intake by logging meals.
4. Visualize your progress with custom progress bars.
