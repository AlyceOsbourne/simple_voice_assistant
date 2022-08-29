import io
import gtts
from pydub import AudioSegment
from pydub.playback import play


def say(text):
    tts = gtts.gTTS(text=text, lang='en')
    bio = io.BytesIO()
    tts.write_to_fp(bio)
    bio.seek(0)
    play(AudioSegment.from_file(bio, format='mp3'))
