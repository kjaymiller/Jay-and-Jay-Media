import config
from pathlib import Path
from render_engine.content import Page, BlogPost, MicroBlogPost, PodcastEpisode
from _path import ContentPath
import generators


pages = ContentPath(
        name = 'pages',
        content_type = Page,
        content_path = 'pages'
        )

PATHS = ([pages])

generators.generate(PATHS)

index =  Page(template='index.html').html
generators.write_page('index', index)

