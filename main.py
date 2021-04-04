from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'INFORMATION_SECURITY'


@app.route('/carousel')
def carousel_func():
    params = {
        'title': 'ИНФОРМАЦИОННАЯ БЕЗОПАСНОСТЬ'
    }

    return render_template('info_sec.html', params=params)


def main():
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
