import requests
from bs4 import BeautifulSoup

def get_ai_news():
    url = "https://news.google.com/search?q=AI&hl=ko&gl=KR&ceid=KR:ko"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    news_items = []

    for item in soup.select("article")[:10]:
        title_tag = item.find("h3")
        if title_tag:
            title = title_tag.text
            link_tag = title_tag.find("a")
            link = "https://news.google.com" + link_tag["href"][1:] if link_tag else None
            news_items.append({
                "title": title,
                "summary": "요약 예정",  # 요약은 summarize_news에서 처리
                "link": link
            })

    return news_items
