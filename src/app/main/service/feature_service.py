from app.main import db
from app.main.model.user_feature import UserFeature


def save_new_feature(data):
    new_feature = UserFeature(
        user_id=data['user-id'],
        intent_word=data['intent-word'],
        context=data['context']
    )

    save_changes(new_feature)

    response_object = {
        'status': 'success',
        'message': 'Feature registered'
    }

    return response_object, 201


def get_user_features(user_id):
    return serialize_features(UserFeature.query.filter_by(user_id=user_id))


def get_all_features(user_id):
    return UserFeature.query.all


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def serialize_features(data):
    return [i.serialize for i in data]
