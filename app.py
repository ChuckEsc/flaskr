from flask import Flask, request, make_response, render_template, jsonify

import flaskr

app = flaskr.create_app()

# 使用会话之前你必须设置一个密钥
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/hello')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/search')
def search():
    searchword = request.args.get('key', '')
    return f"searchword: {searchword}"


# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp


if __name__ == '__main__':
    app.run(port=9000, debug=True)
