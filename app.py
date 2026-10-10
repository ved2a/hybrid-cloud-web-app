
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hybrid Cloud Practical</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background: #eef2f7;
                padding: 60px 20px;
            }
            .card {
                background: white;
                padding: 35px;
                border-radius: 12px;
                max-width: 600px;
                margin: auto;
            }
            h1 { color: #2457a7; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hybrid Cloud Web Application</h1>
            <h2>Practical No. 3</h2>
            <p>My web application is deployed on the cloud.</p>
            <p>Technology: Python Flask</p>
            <p>Platform: Render</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
