import unittest
import os
from speech_to_text import pull_audio_input_stream_compressed_opus


class TestSpeechToText(unittest.TestCase):
    def test_speech_to_text(self):
        pull_audio_input_stream_compressed_opus("./samples/one-voice-some-static.opus", {
            "subscription": os.environ.get("AZURE_SPEECH_TO_TEXT_KEY"),
            "region": os.environ.get("AZURE_SPEECH_TO_TEXT_REGION")
        })
