from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('csti.html')

@app.route('/ssti')
def ssti():
    # Vulnerable SSTI via user-controlled template
    template = "<h1>Hello {{ name }}</h1>"
    return render_template_string(template, name=request.args.get('name', 'Guest'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)