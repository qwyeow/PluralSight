"""Retrieve and print words from a URL

Usage: 
    python3 words.py <URL>
"""


from urllib.request import urlopen
import sys


def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text documents

    Returns:
        A list of strings containing words.     
    """
    with urlopen(url) as f:
        text = []
        for lines in f:
            line = lines.decode("utf-8").split()
            for words in line:
                text.append(words)
    return text


def print_items(items):
    """Print items one per line
    
    Args:
        An iterable series of printable items
    """
    for item in items:
        print(item)


def main(url):
    """Fetch words and print them.

    Args:
        url: URL of text document
    """
    f = fetch_words(url)
    print_items(f)        


if __name__ == "__main__":
    main(sys.argv[1])
