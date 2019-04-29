from .. import db


class UserFeature(db.Model):
    __tablename__ = "userFeature"

    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    user_id = db.Column(db.String(100), nullable=False)
    intent_word = db.Column(db.String(255), nullable=False)
    context = db.Column(db.String(1000), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user-id': self.user_id,
            'intent-word': self.intent_word,
            'context': self.context
        }

    def __repr__(self):
        return "<User '{}' feature: intent '{}' in context '{}'>"\
            .format(self.user_id, self.intent_word, self.context)


class UserF:
    def __init__(self, type, subtype, properties, context, user_id='default'):
        self.user_id = user_id
        self.type = type
        self.subtype = subtype
        self.properties = properties
        self.context = context

    @property
    def serialize(self):
        return {
            'user-id': self.user_id,
            'type': self.type,
            'subtype': self.subtype,
            'properties': self.properties,
            'context': self.context
        }
