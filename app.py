from flask import Flask, render_template, request, send_file
from weasyprint import HTML
import io

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate_pdf():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    html = render_template('pdf_template.html', name=name, email=email, message=message)
    pdf_file = io.BytesIO()
    HTML(string=html).write_pdf(pdf_file)
    pdf_file.seek(0)

    return send_file(pdf_file, download_name="generated.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
