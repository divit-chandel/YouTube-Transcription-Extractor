# libraries
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import extract

def main(url: str) -> str:
    try:
        # video ID from url
        video_id = extract.video_id(url)

        # instantiate API
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=['en'])
        transcript_text = " ".join(snippet.text for snippet in fetched)

        return transcript_text

    except Exception as err:
        print(f"Error: {err}")
        return ""

if __name__ == '__main__':
    video_url = input("Enter a YouTube video link: ")
    print("\nHere's the transcript:\n")
    print(main(video_url))

# uh huh! simply lovely, huh?
