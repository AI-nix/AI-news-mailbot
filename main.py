from news_fetcher import fetch_ai_news
from summarizer import summarize_news
from mailer import send_email

def main():
    articles = fetch_ai_news()
    summary = summarize_news(articles)
    send_email(summary)

if __name__ == "__main__":
    main()
