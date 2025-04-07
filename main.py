# main.py
from summarizer import summarize_news
from mailer import send_email

if __name__ == '__main__':
    news_list = summarize_news()

    # Markdown 스타일 텍스트 요약 생성
    summary = ""
    for news in news_list[:10]:
        summary += f"**{news['title']}**\n"
        summary += f"{news['summary']}\n"
        if news.get('link'):
            summary += f"🔗 {news['link']}\n"
        summary += "\n"

    # HTML 버전 요약 생성
    summary_html = "<h2>🧠 오늘의 AI 뉴스 요약</h2><ol>"
    for news in news_list[:10]:
        summary_html += f"<li><strong>{news['title']}</strong><br>"
        summary_html += f"<p>{news['summary']}</p>"
        if news.get('link'):
            summary_html += f"<a href='{news['link']}'>[원문 보기]</a>"
        summary_html += "</li>"
    summary_html += "</ol>"

    send_email("[오늘의 AI 뉴스 요약]", summary, summary_html)