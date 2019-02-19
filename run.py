import config
from generators import gen_static 
import shutil
from pathlib import Path
from pages.paginate import write_paginated_pages
from pages import (
        Page,
        BlogPost,
        Collection,
        )

from generators import gen_static
from writer import write_page, writer



shutil.rmtree(Path(config.OUTPUT_PATH))
gen_static()

page = Collection(name='pages', content_type=Page, content_path='pages')
blog = Collection(name='blog', content_type=BlogPost, output_path='blog')

page.output_path.mkdir(parents=True, exist_ok=True)
for page_content in page.pages:
    write_page(f'{page.output_path}/{page_content.id}.html', page_content.html)

blog.output_path.mkdir(parents=True, exist_ok=True)
for page_content in blog.pages:
    write_page(f'{page.output_path}/{page_content.id}.html', page_content.html)

def pagination():
    page_groups = blog, microblog
    for page in page_groups:
        write_paginated_pages(page.name, page.paginate, path=page.output_path, template='blog_list.html')


@writer(route='index.html')
def index():
    return Page(template='index.html').html

index()
