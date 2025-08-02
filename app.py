from flask import Flask, render_template, request
from scraper import fetch_case_details
app = Flask(__name__)

# Home Route -> Show Form
@app.route('/')
def home():
    return render_template('index.html')

# Search Route -> Handle Form Submission
@app.route('/search', methods=['POST'])
def search():
    case_type = request.form['case_type']
    case_no = request.form['case_no']
    year = request.form['year']
    data = fetch_case_details(case_type, case_no, year)


    # Check if data fetching was successful
    if data['status'] == "success":
        return render_template('result.html', details=data)
    else:
   
         return f"<h3>{data['message']}</h3>"

    

    # Render result page
    return render_template('result.html', details=details)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

