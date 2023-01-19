import wikipedia

def scrape(name, length=1):
    """
        documentation of the function
    """
    result = wikipedia.summary(name, sentences=length)

    return result