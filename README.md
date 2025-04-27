# SSTI & CSTI Study  
*(Suggested project name: **Template Injection Playground**)*

A hands-on study of Server-Side Template Injection (SSTI) and Client-Side Template Injection (CSTI), prepared for the **PriviaSecurity Intern Exam Blog**.

---

## 📂 Project Structure

```
/
├── app.py                # Flask SSTI example
├── static/
│   ├── csti.html         # AngularJS CSTI example
│   └── style.css
├── templates/
│   ├── contact.html      # SSTI input form
│   └── thankyou.html     # SSTI output template
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 🚀 Features

- **SSTI (Server-Side Template Injection)**  
  - Demonstrates a minimal Flask app (`app.py`) handling user input through Jinja2.  
  - Uses a sandboxed environment to prevent arbitrary code execution.
- **CSTI (Client-Side Template Injection)**  
  - A simple AngularJS example (`csti.html`) showing how unescaped interpolation can be abused.  
  - Easily swap out the AngularJS version in the `<script>` tag to experiment with sandbox bypasses.

---

## 🔄 AngularJS Versioning (CSTI)

In `static/csti.html`, you’ll find:

```html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.3/angular.js"></script>
```

→ **Tip:** Change `1.8.3` to any other version (e.g. `1.6.9`, `1.7.9`) to explore known sandbox-bypass vectors.

---

## 🔗 References

- **PayloadsAllTheThings – AngularJS payloads**  
  https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Client-side%20Template%20Injection/AngularJS

---

## 🔒 Secure SSTI Handling

> **Never** call `render_template_string()` directly on untrusted input.  
> Instead, use Jinja2’s `SandboxedEnvironment` and explicitly compile the template:

```python
from flask import Flask, request, render_template
from jinja2.sandbox import SandboxedEnvironment

app = Flask(__name__)
env = SandboxedEnvironment(autoescape=True)

@app.route('/ssti', methods=['GET', 'POST'])
def ssti():
    if request.method == 'POST':
        user_tpl = request.form.get('email', '')
        try:
            # Compile & render within a sandbox
            tpl = env.from_string(user_tpl)
            safe_email = tpl.render()
            return render_template('thankyou.html', email=safe_email)
        except Exception as e:
            return f"Error: {e}"
    return render_template('contact.html')
```

---

## 🏁 Quick Start

1. **Clone the repo**  
   ```bash
git clone https://github.com/yanard18/SSTI-CSTI-Study.git
cd SSTI-CSTI-Study
```  
2. **Create & activate a virtual environment**  
   ```bash
python3 -m venv venv
source venv/bin/activate
```  
3. **Install dependencies**  
```bash
pip install -r requirements.txt
```  
4. **Run the server**  
```bash
python app.py
```  
5. **Browse the demos**  
   - CSTI: `http://localhost:5000/`  
   - SSTI: `http://localhost:5000/ssti`

---

## ✨ License

This project is licensed under the **MIT License**. See the LICENSE file for more details.

Feel free to adapt, modify, and use it—but **always** follow secure coding practices when handling user-supplied templates!

