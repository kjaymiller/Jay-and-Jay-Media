from dataclasses import dataclass

@dataclass
class Link:
    title: str
    url: str


SITE_TITLE = "Jay and Jay Media"
SITE_SUBTITLE = "Focus on Creating while we focus on your creativity!"
SITE_URL = "https://jayandjay.media"
OWNER = {
        'name': 'Jay Miller',
        'email': 'jay@jayandjay.media',
        }

AUTHOR = 'KJAYMILLER'
REGION = 'US/Pacific'
BASE_PATH = 'content'
OUTPUT_PATH = 'output'

# Header Links
CONTENT_PATH = 'content'
OUTPUT_PATH = 'output'
STATIC_PATH = 'static'

# Header Links
LINKS = (
    Link('Podcasting', '/pages/podcast_services'),
    Link('Contact','/pages/contact.html'),
    )
