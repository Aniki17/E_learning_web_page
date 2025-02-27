from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Path to the folder where PDFs are stored
PDF_FOLDER = os.path.join(os.getcwd(), "static", "ebooks")
app.config["PDF_FOLDER"] = PDF_FOLDER

@app.route("/")
def home():
    return render_template("E_learning.html")

@app.route("/download/<subject>")
def download_ebook(subject):
    filename = f"{subject}.pdf"
    file_path = os.path.join(app.config["PDF_FOLDER"], filename)

    if os.path.exists(file_path):
        return send_from_directory(app.config["PDF_FOLDER"], filename, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True)
