from flask import Flask, request, render_template_string, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('csti.html')

@app.route('/ssti', methods=['GET', 'POST'])
def ssti():
    if request.method == 'POST':
        email = request.form['email']
        try:
            template_value = render_template_string(email)
            return render_template('thankyou.html', email=template_value)

        except Exception as e:
            return f"Erreur : {e}"

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)