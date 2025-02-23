from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')


# Redirect the default route to '/profile'
@app.route('/')
def home():
    # Render the profile page at '/profile' and return it as a static HTML
    return redirect(url_for('profile'))


# Serve the profile page with dynamic parameters and save it as a static HTML
@app.route('/profile')
def profile():
    # Passing dynamic data (e.g., name, bio, etc.)
    user_name = "Dmitry Razumenko"
    user_bio = "Hello! I am Dmitry Razumenko, a first-year master degree student at ITMO University in St. Petersburg. I enjoy sports and application security."

    # Render the HTML content dynamically
    html_content = render_template('index.html', name=user_name, bio=user_bio)

    # Write the rendered HTML to a file
    with open('index.html', 'w') as file:
        file.write(html_content)

    print("Static HTML file has been saved!")

    # Return the dynamically rendered HTML content for the profile page
    return html_content


if __name__ == '__main__':
    app.run(debug=True)
