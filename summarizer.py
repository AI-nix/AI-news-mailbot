def summarize_news(articles):
    # TODO: Integrate with OpenAI API or similar
    summaries = []
    for article in articles:
        summaries.append(f"- {article['title']}: {article['content'][:100]}...")
    return "\n".join(summaries)
