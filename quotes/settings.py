BOT_NAME = "quotes"

SPIDER_MODULES = ["quotes.spiders"]
NEWSPIDER_MODULE = "quotes.spiders"

# Crawl responsibly
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# Process items through your pipelines
ITEM_PIPELINES = {
    "quotes.pipelines.QuotesPipeline": 300,
}

# Export the scraped data
FEEDS = {
    "quotes.jsonl": {"format": "jsonlines"},
}
