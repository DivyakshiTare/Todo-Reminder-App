from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template
# app= Flask (__name__)

# @app.route('/')
# def hello_world():
#     return render_template('index.html')
#     # return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)