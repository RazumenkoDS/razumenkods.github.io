from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    # Render the HTML content dynamically
    html_content = render_template('index.html')  # This will get your template content

    # Write the rendered HTML to a file
    with open('index.html', 'w') as file:
        file.write(html_content)

    print("Static HTML file has been saved!")
    return html_content  # Optional: return content to see in the browser

if __name__ == '__main__':
    app.run(debug=True)