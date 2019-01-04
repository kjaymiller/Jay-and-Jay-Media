from _header_links import navLink
SITE_TITLE = "Jay and Jay Media"
SITE_SUBTITLE = "Focus on your Product!"
OWNER = {
        "name": "Productivity in Tech", 
        "url": "https://productivityintech.com",
        }

SITE_URL = "https://jayandjay.media"
AUTHOR = 'KJAYMILLER'
REGION = 'US/Pacific'
BASE_PATH = 'content'
OUTPUT_PATH = 'output'

# Header Links
links = (
        ('services', 'pages/services'),
        ('blog', 'blog'),
        ('Contact', 'pages/contact'),
        )

LINKS = (navLink(link) for link in links)
