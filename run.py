import json
import config
from generators import gen_static 
import shutil
from pathlib import Path
from pages.paginate import write_paginated_pages
from links import Link
from pages import (
        Page,
        BlogPost,
        Collection,
        )

from pages.generators import gen_static
from pages.writer import write_page, writer



shutil.rmtree(Path(config.OUTPUT_PATH))
gen_static()

page = Collection(name='pages', content_type=Page, content_path='pages')
blog = Collection(name='blog', content_type=BlogPost, output_path='blog')

page_collections = page, blog 
for collection in page_collections:
    collection.output_path.mkdir(parents=True, exist_ok=True)
    for page in collection.pages:
        write_page(f'{collection.output_path}/{page.id}.html', page.html)

def pagination():
    write_paginated_pages(blog.name, blog.paginate, path=blog.output_path, template='blog_list.html')


@writer(route='index.html')
def index():
    links = (Link(
                name="Productivity In Tech",
                url="productivityintech.transistor.fm",
                image="https://s3-us-west-2.amazonaws.com/kjaymiller/images/pit-podcast.png",
                ), 
            Link(
                name=".Net Core Show",
                url="https://dotnetcore.show",
                image="https://dotnetcore.show/content/images/2018/08/jamie-taylor-logo-podcast.svg"
                ),
            Link(
                name="Ask A Brit",
                url="askabrit.transistor.fm",
                image="https://kjaymiller.s3-us-west-2.amazonaws.com/images/AskABritv4.png"
                )
                )
    return Page(template='index.html', links=links).html

def feed_gen():
    with open(f'{blog.output_path}/{blog.name}.json', 'w') as fp:
        json.dump(blog.json_feed, fp)

    with open(f'{blog.output_path}/{blog.name}.rss', 'w') as rss:
        rss.write(blog.rss_feed)

def categorization():
    category_filename = f'{blog.output_path}/categories'
    category_path = Path(category_filename)
    category_path.mkdir(parents=True, exist_ok=True)
    write_page(f'{category_path}/all.html', Page(template='categories.html',
        topic_list=[c for c in blog.categories]).html)

    for category in blog.categories:
        write_page(f'{category_path}/{category}.html',
                Page(template='blog_list.html',
                    post_list=blog.categories[category], output_path=blog.output_path).html)
    
    tag_path = Path(f'{blog.output_path}/tag')
    tag_path.mkdir(parents=True, exist_ok=True)
    write_page(f'{tag_path}/all.html', Page(template='categories.html',
        topic_list=[t for t in blog.tags]).html)
    for tag in blog.tags:
        write_page(f'{tag_path}/{tag}.html', Page(template='blog_list.html',
            post_list=blog.categories[category], output_path=blog.output_path).html)


categorization()
pagination()
feed_gen()
index()
