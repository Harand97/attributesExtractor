from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import request
from flask import abort
from flask import make_response
from flask import jsonify

from app.main import create_app, db
from app.main.model import user_feature
from app.main.service.feature_service import save_new_feature, get_user_features
from app.main.service.nlp_service import extract_features

app = create_app()
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@app.route('/api/v1/users/messages', methods=['POST'])
def post_user_message():
    if not request.json:
        abort(400)

    data = request.json

    response_object, code = save_new_feature(data)

    return make_response(jsonify(response_object), code)


@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    if not request.json:
        abort(400)

    data = request.json

    answer = extract_features(data['text'], data['user-id'])
    return make_response(jsonify(answer), 200)


@app.route('/api/v1/users/<string:user_id>', methods=['GET'])
def get_feature(user_id):
    return_data = get_user_features(user_id)
    return jsonify(json_list=return_data)


if __name__ == '__main__':
    manager.run()
