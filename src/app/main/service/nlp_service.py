from app.main import nlp
from app.main.model.user_feature import UserF

from spacy.symbols import dobj, xcomp, VERB, ADJ

first_person_pronouns = ['i', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours']

intent_keywords = ['i want', 'i wish', 'i would like', 'i will buy',
                   'it would be nice if', 'i\'d really appreciate it if you could',
                   'I\'d be delighted to']

attitude_keywords = ['i think', 'in my opinion', 'i believe', 'if you ask me', 'in my estimation',
                     'i regard', 'speaking for myself', 'as for me', 'it seems to me', 'according to me',
                     'i have noticed', 'meseems', 'methinks', 'from my point of view', 'the way i see it',
                     'i maintain that', 'i am of the opinion that', 'in my mind']

attribute_keywords = ['i have', 'i bought', 'i own', 'i carry']


def extract_features(text, user_id):
    doc = nlp(text)

    features = []
    for sent in doc.sents:
        feature = extract_feature(sent.string.strip())
        feature.user_id = user_id

        if feature is not None:
            features.append(feature.serialize)

    return {'features': features}


def extract_feature(sentence) -> UserF:
    if check_phrases(sentence, intent_keywords):
        return handle_intent(sentence)

    elif check_phrases(sentence, attitude_keywords):
        return handle_attitude(sentence)

    elif check_phrases(sentence, attribute_keywords):
        return handle_attribute(sentence)

    return None


def check_phrases(sentence, phrases):
    for phrase in phrases:
        if phrase.lower() in sentence.lower():
            return True

    return False


def handle_intent(sentence) -> UserF:
    data = nlp(sentence)

    root = next((t for t in data if t.dep_ == 'ROOT'), None)
    verb = next((t for t in root.children if t.dep == xcomp and t.pos == VERB), None)
    if verb is None:
        verb = root

    context = create_context(verb)

    properties = {}
    type = 'intent'
    subtype = 'object'
    obj = next((t for t in verb.children if t.dep == dobj), None)

    if obj is not None:
        adjectives = list(map(lambda t: t.text, filter(lambda t: t.pos == ADJ, obj.children)))
        properties['object'] = obj.text
        properties['adjectives'] = adjectives
    else:
        subtype = 'action'
        properties['verb'] = verb.text

    feature = UserF(type, subtype, properties, context)

    return feature


def handle_attitude(sentence) -> UserF:
    feature = UserF()

    return feature


def handle_attribute(sentence) -> UserF:
    data = nlp(sentence)

    root = next((t for t in data if t.dep_ == 'ROOT'), None)
    verb = next((t for t in root.children if t.dep == xcomp and t.pos == VERB), None)
    if verb is None:
        verb = root

    context = create_context(verb)

    properties = {}
    type = 'attribute'
    subtype = 'property'
    obj = next((t for t in verb.children if t.dep == dobj), None)

    adjectives = list(map(lambda t: t.text, filter(lambda t: t.pos == ADJ, obj.children)))
    properties['object'] = obj.text
    properties['adjectives'] = adjectives

    feature = UserF(type, subtype, properties, context)

    return feature


def create_context(main_token):
    subtree = main_token.subtree

    dit = {x.i: x for x in subtree}
    dit[main_token.i] = main_token

    context = ' '.join([dit[i].text for i in sorted(dit.keys())])

    return context
