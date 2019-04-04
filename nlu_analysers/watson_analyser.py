import json
import urllib

from environs import Env
from watson_developer_cloud import AssistantV2

from nlu_analysers.analyser import Analyser

env = Env()
# Read .env into os.environ
env.read_env()


class WatsonAnalyser(Analyser):

    # def __init__(self, workspace_id, user, password):
    # 	super(WatsonAnalyser, self).__init__()
    # 	self.workspace_id = workspace_id
    # 	self.user = user
    # 	self.password = password
    # 	self.url = "https://gateway.watsonplatform.net/assistant/api/v1/workspaces/" + self.workspace_id + "/message?version=2018-02-16"

    def __init__(self, api_key, url, assistant_id):
        super(WatsonAnalyser, self).__init__()
        # self.workspace_id = workspace_id
        # self.apiKey = env.str("IAM_API_KEY")
        self.assistant_id = assistant_id
        self.assistant = AssistantV2(
            version='2019-02-28',
            iam_apikey=api_key,
            url=url
        )

        # self.url = "https://gateway-lon.watsonplatform.net/assistant/api"

    def get_annotations(self, corpus, output):
        data = json.load(open(corpus))
        annotations = {'results': []}
        self.assistant.set_detailed_response(True)
        response = self.assistant.create_session(
            assistant_id=self.assistant_id
        ).get_result()
        session_id = response['session_id']

        for s in data["sentences"]:
            if not s["training"]:  # only use test data
                res = self.assistant.message(
                    assistant_id=self.assistant_id,
                    session_id=session_id,
                    input={
                        'message_type': 'text',
                        'text': s['text']
                    }
                ).get_result()

                # print(json.dumps(res, indent=2))
                # encoded_text = s['text']  # urllib.parse.quote(s['text'])
                # headers = {'content-type': 'application/json'}
                # data = {"input": {"text": encoded_text}}
                # r = requests.post(self.url, data=json.dumps(data), headers=headers, auth=(self.user, self.password))
                res['output']['generic'] = {'text': s['text']}
                annotations['results'].append(res['output'])

        file = open(output, "wb")
        file.write(
            json.dumps(annotations, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False).encode(
                'utf-8'))
        file.close()

    def analyse_annotations(self, annotations_file, corpus_file, output_file):
        analysis = {"intents": {}, "entities": {}}

        corpus = json.load(open(corpus_file))
        gold_standard = []
        for s in corpus["sentences"]:
            if not s["training"]:  # only use test data
                gold_standard.append(s)

        # print urllib.unquote(open(annotations_file).read()).decode('utf8')
        annotations = json.load(open(annotations_file))

        i = 0
        for a in annotations["results"]:
            if not urllib.parse.unquote(a['generic']['text']) == gold_standard[i]["text"]:
                print("WARNING! Texts not equal")

            # intent
            if (len(a["intents"]) > 0):
                aIntent = a["intents"][0]["intent"]
            else:
                aIntent = None
            oIntent = gold_standard[i]["intent"].replace(" ", "_")

            Analyser.check_key(analysis["intents"], aIntent)
            Analyser.check_key(analysis["intents"], oIntent)

            if aIntent == oIntent:
                # correct
                analysis["intents"][aIntent]["truePos"] += 1
            else:
                # incorrect
                analysis["intents"][aIntent]["falsePos"] += 1
                analysis["intents"][oIntent]["falseNeg"] += 1

            # entities
            aEntities = a["entities"]
            oEntities = gold_standard[i]["entities"]

            for x in aEntities:
                Analyser.check_key(analysis["entities"], x["entity"])

                if len(oEntities) < 1:  # false pos
                    analysis["entities"][x["entity"]]["falsePos"] += 1
                else:
                    truePos = False

                    for y in oEntities:
                        if x["value"] == y["text"].lower():
                            if x["entity"] == y["entity"]:  # truePos
                                truePos = True
                                oEntities.remove(y)
                                break
                            else:  # falsePos + falseNeg
                                analysis["entities"][x["entity"]]["falsePos"] += 1
                                analysis["entities"][y["entity"]]["falseNeg"] += 1
                                oEntities.remove(y)
                                break
                    if truePos:
                        analysis["entities"][x["entity"]]["truePos"] += 1
                    else:
                        analysis["entities"][x["entity"]]["falsePos"] += 1

            for y in oEntities:
                Analyser.check_key(analysis["entities"], y["entity"])
                analysis["entities"][y["entity"]]["falseNeg"] += 1

            i += 1

        self.write_json(output_file, json.dumps(analysis, sort_keys=False, indent=4, separators=(',', ': '),
                                                ensure_ascii=False).encode('utf-8'))
