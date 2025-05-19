import requests
from bs4 import BeautifulSoup

def get_markdown(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {url}")
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find('div', {'id': 'mw-content-text'})

    markdown_lines = []

    main_heading = soup.find('h1', {'id': 'firstHeading'})
    if main_heading:
        markdown_lines.append(f"# {main_heading.get_text().strip()}\n")

    for element in content_div.find_all(recursive=False):
        for tag in element.descendants:
            if tag.name and tag.name.startswith('h') and tag.name[1:].isdigit():
                level = int(tag.name[1:]) + 1  # Add 1 to indent under main heading
                heading_text = tag.get_text().strip()
                markdown_lines.append(f"{'#' * level} {heading_text}\n")
            elif tag.name == 'p':
                text = tag.get_text().strip()
                if text:
                    markdown_lines.append(f"{text}\n")
            elif tag.name == 'ul':
                for li in tag.find_all('li'):
                    markdown_lines.append(f"- {li.get_text().strip()}")
                markdown_lines.append("")
            elif tag.name == 'ol':
                for i, li in enumerate(tag.find_all('li'), start=1):
                    markdown_lines.append(f"{i}. {li.get_text().strip()}")
                markdown_lines.append("")

    return '\n'.join(markdown_lines)

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Alexander_the_Great"  # Change to your desired Wikipedia page
    markdown = get_markdown(url)

    with open("output1.md", "w", encoding="utf-8") as f:
        f.write(markdown)

    print("Markdown content saved to output.mkd")
