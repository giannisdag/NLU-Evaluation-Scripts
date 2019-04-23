import json


def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    # storage_client = storage.Client()
    storage_client = storage.Client.from_service_account_json(
        'keys/testenglishteacher-4ab6c044ae12.json')
    project_id = 'testenglishteacher'
    url = "https://dialogflow.googleapis.com/v2/projects/" + project_id + "/agent/sessions/1:detectIntent"
    encoded_text = 'patates'
    data = {'queryInput': {'text': {'text': encoded_text, 'languageCode': 'en'}}}
    res = storage_client._http.post(url=url, data=data)
    print(res.content)
    # Make an authenticated API request
    print(storage_client.get_service_account_email('testenglishteacher'))
    print(storage_client.project)
    buckets = list(storage_client.list_buckets())
    print(buckets)


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
