import pandas as pd
import requests as req
import lxml
from bs4 import BeautifulSoup as bs

# Define parameters
categories = ['news', 'metro-plus', 'video', 'sports', 'politics']
pages = 1
articles = []

# Function to extract article data from the category page


def extract_articles(category, page):
    url = f'https://punchng.com/topics/{category}/page/{page}/'
    response = req.get(url).text
    soup = bs(response, 'html.parser')

    article_container = soup.find('div', class_='latest-news-timeline-section')
    return article_container.find_all_next('article')

# Function to extract details from each article


def get_article_details(article, category):
    title = article.find('h1', 'post-title').text.strip().replace(' ', '')
    excerpt = article.find('p', 'post-excerpt').text.strip().replace(' ', '')
    date = article.find('span', 'post-date').text.strip()
    link = article.find('a')['href']

    return {
        'category': category,
        'title': title,
        'excerpt': excerpt,
        'date': date,
        'link': link
    }

# Function to extract author and content from the article page


def enrich_article(article):
    article_page = req.get(article['link']).text.strip()
    soup = bs(article_page, 'html.parser')

    article['author'] = soup.find(
        'span', class_='post-author').text.strip().replace('By ', '')
    article['content'] = soup.find(
        'div', class_='post-content').text.strip().replace(' ', '')
    image_wrapper = soup.find('div', class_='post-image-wrapper')

    article['image'] = image_wrapper.find_next(
        'img')['src'] if image_wrapper else ''
    return article


# Main loop over categories and pages
for category in categories:
    for page in range(1, pages + 1):
        articles_temp = extract_articles(category, page)

        for article in articles_temp:
            article_details = get_article_details(article, category)
            enriched_article = enrich_article(article_details)
            articles.append(enriched_article)
            print(f'Page {page} for {category} completed')
        print(f'Category {category} completed')

# Save the data to a CSV file
punch_df = pd.DataFrame(articles)
punch_df.to_csv('punch.csv', index=False)

print('Done')
