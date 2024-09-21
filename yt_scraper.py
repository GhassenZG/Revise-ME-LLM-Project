from youtube_transcript_api import YouTubeTranscriptApi
import re

def scrape_youtube_transcript(url):
    try:
        video_id = extract_video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        content = " ".join([entry['text'] for entry in transcript])
        title = f"YouTube Video: {video_id}"

        return {
            'title': title,
            'content': content
        }
    except Exception as e:
        return {
            'title': 'Error',
            'content': f"Error scraping the YouTube video: {str(e)}"
        }

def extract_video_id(url):
    # Support various YouTube URL formats
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([0-9A-Za-z_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([0-9A-Za-z_-]{11})'
    ]
    for pattern in patterns:
        match = re.match(pattern, url)
        if match:
            return match.group(1)
    raise ValueError("Invalid YouTube URL")
