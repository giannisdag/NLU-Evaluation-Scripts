from nlu_converters.dialogflow_converter import DialogflowConverter
from nlu_converters.watson_converter import WatsonConverter
from nlu_analysers.dialogflow_analyser import DialogflowAnalyser

##dialogflow
dialogflow_converter = DialogflowConverter()
dialogflow_converter.import_corpus("json_data/english_teaching.json")
dialogflow_converter.export("exports/english_teaching_dialog_flow.zip")

##watson
watson_converter = WatsonConverter()
watson_converter.import_corpus("json_data/english_teaching.json")
watson_converter.export("exports/english_teaching_watson.json")

##dialogflow
dialogflow_analyser = DialogflowAnalyser("testenglishteacher")
dialogflow_analyser.get_annotations("json_data/english_teaching.json", "WebApplicationsAnnotations_Dialogflow.json")
dialogflow_analyser.analyse_annotations("WebApplicationsAnnotations_Dialogflow.json", "WebApplicationsCorpus.json", "WebApplicationsAnalysis_Dialogflow.json")

