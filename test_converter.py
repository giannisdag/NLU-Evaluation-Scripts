from environs import Env
from data_presenter import DataPresenter
from environs import Env

from data_presenter import DataPresenter

env = Env()
# Read .env into os.environ
env.read_env()

##dialogflow
# dialogflow_converter = DialogflowConverter()
# dialogflow_converter.import_corpus("json_data/english_teachingEleni.json")
# dialogflow_converter.export("exports/english_teaching_dialog_flowEleni.zip")

##dialogflow
# dialogflow_analyser = DialogflowAnalyser("testenglishteacher")
# dialogflow_analyser.get_annotations("json_data/english_teachingEleni.json", "exports/annotated/english_teaching_DialogflowEleni.json")
# dialogflow_analyser.analyse_annotations(
#     "exports/annotated/english_teaching_DialogflowEleni.json",
#     "json_data/english_teachingEleni.json",
#     "exports/analysis/english_teaching_Analysis_DialogflowEleni.json")

##watson
# watson_converter = WatsonConverter()
# watson_converter.import_corpus("json_data/english_teachingEleni.json")
# watson_converter.export("exports/english_teachingEleni_watson.json")

##watson
# watson_analyser = WatsonAnalyser(env.str("IAM_API_KEY"), env.str("WATSON_URL"), env.str("ASSISTANT_ID"))
# watson_analyser.get_annotations("json_data/english_teachingEleni.json", "exports/annotated/english_teaching_WatsonEleni.json")
# watson_analyser.analyse_annotations(
#     "exports/annotated/english_teaching_WatsonEleni.json",
#     "json_data/english_teachingEleni.json",
#     "exports/analysis/english_teaching_Analysis_WatsonEleni.json"
# )
data_presenter = DataPresenter()
data_presenter.bar_presenter(
    "exports/analysis/english_teaching_Analysis_WatsonEleni.json",
    "exports/analysis/english_teaching_Analysis_DialogflowEleni.json"
)
