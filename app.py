from flask import Flask, render_template, request, flash, redirect, url_for
from threading import Thread
import subprocess

app = Flask(__name__, template_folder="template")
app.secret_key = 'asd149'  # Needed for flash messages


def run_selenium_script():
    subprocess.run(["python", "main.py"], check=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'userId' in request.form:
            user_id = request.form['userId']
            # Save the user_id to a file
            with open('user_id.txt', 'w') as f:
                f.write(user_id)

        if 'amount' in request.form:
            amount = request.form['amount']
            # Save the amount to a file
            with open('amount.txt', 'w') as f:
                f.write(amount)

            # Start the Selenium script in the background after receiving the amount
            Thread(target=run_selenium_script, daemon=True).start()

        return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
