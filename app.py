from flask import Flask, render_template_string

app = Flask(__name__)

# data you want to display
NAME = "Saket Sarvaiya"
APP_ID = "2408838"

@app.route("/")
def index():
    # render directly from a string for simplicity
    return render_template_string(
        """
        <h1>Application Info</h1>
        <p><strong>Name:</strong> {{ name }}</p>
        <p><strong>AppID:</strong> {{ appid }}</p>
        """,
        name=NAME,
        appid=APP_ID,
    )

if __name__ == "__main__":
    # start the development server
    app.run(debug=True)