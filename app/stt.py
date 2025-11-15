import azure.cognitiveservices.speech as speechsdk

class AzureSTT:
    def __init__(self):
        self.speech_key = "43b88b0188fa42e9a546792c531cea41"
        self.region = "westeurope"
        self.config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.region)
        self.config.speech_recognition_language = "it-IT"

    def recognize(self, audio_file):
        audio_input = speechsdk.audio.AudioConfig(filename=audio_file)
        recognizer = speechsdk.SpeechRecognizer(speech_config=self.config, audio_config=audio_input)
        result = recognizer.recognize_once()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        return ""
