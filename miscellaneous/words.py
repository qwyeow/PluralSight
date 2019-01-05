#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>

"""

import sys
from urllib.request import urlopen  


def fetch_word(urls): 
    """Fetch a list of words from a URL.
    
    Args: 
        urls: the URL of the UTF-8 text document.

    Returns:
        A list of strings containing words from the document.    
    """
    with urlopen(urls) as story:
        story_text = []
        for text in story:
            line = text.decode('utf-8').split()
            for i in line:
                story_text.append(i)
    return story_text            

# def joined_text(text):
#     j_text = ' '.join(text)
#     print(j_text)

def print_items(items):
    """Print items one per line.
    
    Args:
        items: an iterable collection of items
            
    """
    for item in items:
        print(item)


def main(urls):    
    """Print words contained in a text document from a URL
    
    ARGS:
        urls: the URL containing the text document.
    """
    word = fetch_word(urls)
    #joined_text(word)
    print_items(word)
    


if __name__ == "__main__":
    main(sys.argv[1]) # sys.argv[0] is the module file name

