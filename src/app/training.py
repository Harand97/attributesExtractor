import spacy
from spacy.symbols import nsubj, dobj, root, amod, xcomp, VERB, ADJ

nlp = spacy.load('en_core_web_lg')

text = "I think that smoking is awful"

doc = nlp(text)

"""rt = next((t for t in doc if t.dep_ == 'ROOT'), None)
vb = next((t for t in rt.children if t.dep == xcomp and t.pos == VERB), None)
if vb is None:
    vb = rt

subtree = vb.subtree

dit = {x.i: x for x in subtree}
dit[vb.i] = vb

context = ' '.join([dit[i].text for i in sorted(dit.keys())])
print(context)
obj = next((t for t in vb.children if t.dep == dobj), None)
adjs = []

if obj is not None:
    adjs = list(filter(lambda t: t.pos == ADJ, obj.children))

print(rt.text, vb.text, obj.text)
for adj in adjs:
    print(adj.text)"""

"""for token in doc:
    if token.dep_ == 'ROOT':
        data[root] = token

    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

rt = data[root]
print(rt.text)
for token in rt.children:
    if token.dep == xcomp and token.pos == VERB:
        rt = token
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
print(rt.left_edge.i, rt.right_edge.i)
for token in rt.conjuncts:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
print(rt.text)
for token in rt.children:
    if token.dep == dobj:
        rt = token
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

print(rt.text)
for token in rt.children:
    if token.pos == ADJ:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)"""
