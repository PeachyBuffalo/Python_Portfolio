from bs4 import BeautifulSoup
import requests
import logging
from concurrent.futures import ThreadPoolExecutor
import category_config as config

# Configure logging
logging.basicConfig(level=logging.INFO)

def parse_html(html_content, parse_function):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Utilize the custom parse function from the configuration
    return parse_function(soup)

def fetch_data(url, parse_function):
    try:
        response = requests.get(url)
        if response.headers['Content-Type'] == 'application/json':
            return response.json()  # If JSON, return JSON
        else:
            return parse_html(response.text, parse_function)  # If HTML, parse HTML
    except requests.RequestException as e:
        logging.error(f"Error fetching data from {url}: {e}")
        return None

def process_and_display(data):
    # Process and display the data
    print(data)

def select_categories():
    print("Available categories:")
    for category in config.categories:
        print(f"- {category}")
    selected = input("Enter the categories you want to process (comma-separated): ")
    return [cat.strip() for cat in selected.split(',')]

def main():
    selected_categories = select_categories()

    for category in selected_categories:
        if category in config.categories:
            details = config.categories[category]
            urls = details["urls"]
            parse_function_name = details.get("parse_function")

            if parse_function_name and hasattr(config, parse_function_name):
                parse_function = getattr(config, parse_function_name)
            else:
                parse_function = lambda soup: "Default parsing logic"

            try:
                with ThreadPoolExecutor(max_workers=5) as executor:
                    # Pass the parse function along with the URL
                    results = executor.map(lambda url: fetch_data(url, parse_function), urls)
                for result in results:
                    if result:
                        process_and_display(result)
            except Exception as e:
                logging.error(f"Error processing category {category}: {e}")
        else:
            logging.warning(f"Selected category '{category}' is not available.")

if __name__ == "__main__":
    main()