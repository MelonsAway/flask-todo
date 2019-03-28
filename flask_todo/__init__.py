from flask import Flask, request, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    @app.route('/')
    def default():
        return render_template('index.html')
    @app.route('/hello')
    def hello():
        name = request.args.get('name', 'world')
#        return f"Hello {name}!"
        return render_template('hello.html', name=name)
    return app
