# Fyyur
# Background
[Project Details](Original_README.md)
## Introduction
Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.
## Main Files: Project Structure
  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes your SQLAlchemy models.
                    "python app.py" to run after installing dependencies
  ├── config.py *** Database URLs, CSRF generation, etc
  ├── error.log
  ├── forms.py *** Your forms
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├── static
  │   ├── css 
  │   ├── font
  │   ├── ico
  │   ├── img
  │   └── js
  └── templates
      ├── errors
      ├── forms
      ├── layouts
      └── pages
  ```

## Development Setup
* Create and activate a vertial environment
* Install the dependencies:pip install -r requirements.txt
* Run the development server:FLASK_APP=app.py FLASK_DEBUG=true flask run
* Navigate to http://127.0.0.1:5000/

## Features
* Facebook link is validated to make sure it is a Facebook link
* Website is validated to make sure it is a valid web site address
* The phone number needs to be in either all numeric or 999-999-9999 format
* The phone number also needs to be a valid US phone number.