import json


def json_data_counter(file):
    data = json.load(open(file))
    intents = set()
    entities = set()
    # intents = ['break','directTranslation',]
    for s in data["sentences"]:
        intents.add(s['intent'])
        if s['entities']:
            entities.add(s['entities'][0]['entity'])

    intent_results = {}
    entities_results = {}
    for intent in intents:
        intent_results[intent] = dict(training=0, test=0)
    for entity in entities:
        entities_results[entity] = dict(training=0, test=0)

    for s in data["sentences"]:
        for intent in intents:
            if s['intent'] == intent:
                if s['training']:
                    intent_results[intent]['training'] = intent_results[intent]['training']+1
                else:
                    intent_results[intent]['test'] = intent_results[intent]['test']+1
        for entity in entities:
            if s['entities']:
                if s['entities'][0]['entity'] == entity:
                    if s['training']:
                        entities_results[entity]['training'] = entities_results[entity]['training']+1
                    else:
                        entities_results[entity]['test'] = entities_results[entity]['test']+1

    print(intent_results)
    print(entities_results)
