from environs import Env
from data_presenter import DataPresenter
from nlu_converters.dialogflow_converter import DialogflowConverter
from nlu_converters.watson_converter import WatsonConverter
from environs import Env
from nlu_analysers.watson_analyser import WatsonAnalyser
from nlu_analysers.dialogflow_analyser import DialogflowAnalyser
from data_presenter import DataPresenter
import helper

env = Env()
# Read .env into os.environ
env.read_env()
# helper.implicit()
helper.json_data_counter("json_data/english_teaching.json")
#dialogflow
# dialogflow_converter = DialogflowConverter()
# dialogflow_converter.import_corpus("json_data/english_teaching.json")
# dialogflow_converter.export("exports/english_teaching_dialog_flow.zip")
##watson
# watson_converter = WatsonConverter()
# watson_converter.import_corpus("json_data/english_teaching.json")
# watson_converter.export("exports/english_teaching_watson.json")


#dialogflow
# dialogflow_analyser = DialogflowAnalyser("testenglishteacher")
# dialogflow_analyser.get_annotations("json_data/english_teaching.json", "exports/annotated/english_teaching_Dialogflow.json")
# dialogflow_analyser.analyse_annotations(
#     "exports/annotated/english_teaching_Dialogflow.json",
#     "json_data/english_teaching.json",
#     "exports/analysis/english_teaching_Analysis_Dialogflow.json")
#
#
# #watson
# watson_analyser = WatsonAnalyser(env.str("IAM_API_KEY"), env.str("WATSON_URL"), env.str("ASSISTANT_ID"))
# watson_analyser.get_annotations("json_data/english_teaching.json", "exports/annotated/english_teaching_Watson.json")
# watson_analyser.analyse_annotations(
#     "exports/annotated/english_teaching_Watson.json",
#     "json_data/english_teaching.json",
#     "exports/analysis/english_teaching_Analysis_Watson.json"
# )
# data_presenter = DataPresenter()
# data_presenter.bar_presenter(
#     "exports/analysis/english_teaching_Analysis_Watson.json",
#     "exports/analysis/english_teaching_Analysis_Dialogflow.json",
# )
