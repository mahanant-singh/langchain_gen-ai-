# step 1 indexing (document ingestion)
from youtube_transcript_api import YouTubeTranscriptApi
import faiss
import tiktoken
from dotenv import load_dotenv

load_dotenv()

video_id = "Gfr50f6ZBvo" # only the ID, not full URL
try:
    # If you don’t care which language, this returns the “best” one
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])

    # Flatten it to plain text
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")
# step 2b -indexing (text splitting)
splitter=R