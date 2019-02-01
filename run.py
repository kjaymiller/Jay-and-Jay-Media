import config
from generators import gen_static 
import shutil
from pathlib import Path
from pages.paginate import write_paginated_pages
from pages import (
        Page,
        Collection,
        )

from generators import gen_static
from writer import write_page, writer



shutil.rmtree(Path(config.OUTPUT_PATH))
gen_static()

page = Collection(name='pages', content_type=Page, content_path='pages')
page.output_path.mkdir(parents=True, exist_ok=True)

@writer(route='index.html')
def index():
    return Page(template='index.html').html

index()
