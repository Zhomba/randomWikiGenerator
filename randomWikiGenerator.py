import requests

def fetch_random_article():
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'random',
        'rnnamespace': 0,  # Namespace for articles
        'rnlimit': 1  # Number of random articles to retrieve
    }

    response = requests.get(api_url, params=params)
    data = response.json()
    
    # Extract the title of the random article
    random_title = data['query']['random'][0]['title']
    
    return random_title

def fetch_article_content(title):
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'titles': title,
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True
    }

    response = requests.get(api_url, params=params)
    data = response.json()
    
    # Extract the text of the article
    page = next(iter(data['query']['pages'].values()))
    article_text = page['extract'] if 'extract' in page else "No content available."

    return article_text

def main():
    print("Welcome to Wiki Random Article Generator!")

    while True:
        print("\nFetching random article...")
        random_title = fetch_random_article()
        print(f"\nTitle: {random_title}")

        user_input = input("Do you want to read this article? (yes/no): ").lower()

        if user_input == 'yes':
            article_text = fetch_article_content(random_title)
            print("\n", article_text[:999])
        elif user_input == 'no':
            print("Fetching another article...")
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()