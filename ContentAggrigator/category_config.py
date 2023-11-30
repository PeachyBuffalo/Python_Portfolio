# Define custom parsing functions for different categories
# def parse_news(soup):
#     # Implement logic for parsing news content
#     # Example: Extracting the title and text of a news article
#     title = soup.find('h1', class_='news-title').get_text(strip=True)
#     content = soup.find('div', class_='article-content').get_text(strip=True)
#     # for script in soup(["script", "style"]):
#     #     script.extract()
#     return {"title": title, "content": content}
def parse_news(soup):
    title_tag = soup.find('title', class_='news-title')
    title = title_tag.get_text(strip=True) if title_tag else "Title not found"

    content_div = soup.find('div', class_='article-content')
    if content_div:
        paragraphs = content_div.find_all('p')
        content = ' '.join(p.get_text(strip=True) for p in paragraphs)
        return {"title": title, "content": content}
    else:
        return {"title": title, "content": "Content not found"}

def parse_social_media(soup):
    # Implement logic for parsing social media content
    # Example: Extracting a post's author and content
    author = soup.find('span', class_='post-author').get_text(strip=True)
    post_content = soup.find('div', class_='post-content').get_text(strip=True)
    return {"author": author, "content": post_content}

def parse_videos(soup):
    # Implement logic for parsing video content
    # Example: Extracting the video title and description
    title = soup.find('h1', class_='video-title').get_text(strip=True)
    description = soup.find('div', class_='video-description').get_text(strip=True)
    return {"title": title, "description": description}

# Define categories with URLs and corresponding parsing functions
categories = {
    "news": {
        "urls": [
            "https://www.inc.com/jennifer-conrad/fidelity-national-financial-is-latest-ransomware-victim.html",
            "https://techcrunch.com/2023/11/27/ransomware-catastrophe-at-fidelity-national-financial-causes-panic-with-homeowners-and-buyers/",
            # Add more news URLs
        ],
        "parse_function": "parse_news"
    },
    "social_media": {
        "urls": [
            "https://www.reddit.com/r/business/comments/1859t8r/ransomware_catastrophe_at_fidelity_national/",
            "https://www.reddit.com/r/cybersecurity/comments/180vvx2/fidelity_national_financial/",
            # Add more social media URLs
        ],
        "parse_function": "parse_social_media"
    },
    "videos": {
        "urls": [
            "http://example-videos.com/video1",
            "http://example-videos.com/video2",
            # Add more video URLs
        ],
        "parse_function": "parse_videos"
    }
    # Add other categories as needed
}