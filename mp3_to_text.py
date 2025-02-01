# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai
import os
from dotenv import load_dotenv

load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLY_IA_TOKEN")

def mp3_to_text(mp3_filename: str) -> None:
    
    # FILE_URL = "61e6f487e234409b93ce978a30a2b69a.mp3"
    config = aai.TranscriptionConfig(speaker_labels=True,
                                speakers_expected=2,
                                language_code="pt")
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(mp3_filename, config=config)

    if transcript.status == aai.TranscriptStatus.error:
        return transcript.error
    else:
        for speaker_label in transcript.utterances:
            return f"{speaker_label.speaker}: {speaker_label.text}"
   