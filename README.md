# Punch News Scraper

This Python project scrapes news articles from the Punch Nigeria website. It extracts articles from various categories, retrieves detailed information for each article, and saves the data in a CSV file.

## Project Overview

The project uses the following libraries:
- **`pandas`**: For storing and exporting data in a structured format (CSV).
- **`requests`**: For sending HTTP requests to retrieve HTML content from web pages.
- **`BeautifulSoup` (from `bs4`)**: For parsing HTML and extracting article data.

### Features:
1. Scrapes news articles from the Punch Nigeria website.
2. Extracts key information such as title, excerpt, date, author, and article content.
3. Downloads article images (if available).
4. Saves the results in a CSV file for further analysis.

### Categories Scraped:
- News
- Metro Plus
- Video
- Sports
- Politics

## Prerequisites

Before running the code, ensure you have the required libraries installed:

```bash
pip install pandas requests beautifulsoup4 lxml
```

## How It Works

1. **Extract Articles by Category and Page**: 
   - The script loops through a predefined list of categories and pages to retrieve the HTML content for each category page.
   - It identifies each article's container and scrapes the article titles, excerpts, dates, and links.

2. **Enrich Article Details**: 
   - After retrieving the basic details from the category page, the script sends a request to each article's page.
   - It extracts additional information such as the author's name, the article's full content, and the image (if available).

3. **Save to CSV**: 
   - All scraped data is stored in a list of dictionaries.
   - Once scraping is complete, the data is converted to a DataFrame using `pandas` and saved as a CSV file named `punch.csv`.

## Code Structure

- **`extract_articles(category, page)`**: Fetches all articles from a specific category and page.
- **`get_article_details(article, category)`**: Extracts the title, excerpt, date, and link from each article.
- **`enrich_article(article)`**: Sends a request to the article page and extracts the author, full content, and image.
- **Main Loop**: Iterates over each category and page to gather articles and stores them in the `articles` list.

### CSV File

The resulting CSV file includes the following columns:
- `category`: The category of the article (e.g., News, Sports).
- `title`: The title of the article.
- `excerpt`: A short summary of the article.
- `date`: The publication date of the article.
- `author`: The author of the article.
- `content`: The full content of the article.
- `image`: The URL of the article's image (if available).
- `link`: The article's URL.

## Running the Script

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/punch-news-scraper.git
   ```

