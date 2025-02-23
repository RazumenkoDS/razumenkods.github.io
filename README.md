# Homework 1 Profile page
## Description

The profile page displays user information such as name, bio, and other details. It creates a dynamic profile page using Flask for the backend and HTML/CSS for the frontend.The Flask app renders the profile page dynamically, and the default route (/) is redirected to /profile, where the profile information is displayed. Flask to dynamically generate the content of index.html and save it to a file, which can then be uploaded to your GitHub Pages repository. It allows to work with Flask's **dynamic** features **while** still hosting a **static** site on GitHub Pages.

## Features

### Flask Backend:
- Renders the profile page using render_template.
- Passes dynamic content (name, bio, etc.) to the template.
- Redirects the default route (/) to /profile.

### Frontend:
- HTML template for the profile page.
- Styling applied using a CSS file to make the profile page visually appealing.
- Static resources (images, CSS) served correctly by Flask.

### Deployment:
- A static version of the profile page is generated and pushed to GitHub Pages.
