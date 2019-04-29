from flask import request
from flask import abort
from flask import make_response

from manage import app


@app.route('/api/v1/users/messages', methods=['POST'])
def post_user_message():
    if not request.json:
        abort(400)

    return make_response("Successful", 201)


@app.route('/api/v1/user-features/<int:user_id>', methods=['GET'])
def get_user_features(user_id):
    return make_response("Good", 200)


@app.route('api/v1/user-features/<int:user_id>', methods=['DELETE'])
def delete_user_features(user_id):
    return make_response("Deleted", 200)