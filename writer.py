from config import OUTPUT_PATH


def write_page(filename, content):
    with open(f'{OUTPUT_PATH}/{filename}.html', 'w') as f:
        f.write(content)
        return f

