def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if len(zip_code) > 4 and zip_code.isdigit():
        return True
    else:
        return False

# Press the green button in the gutter to run the script.
help(str)
zip_code = input('enter zip code')

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    results = []
    for item in doc_list:
        print(item)
        if (keyword+"." or keyword+" " )in item.lower():
            results.append(doc_list.index(item))
    return results
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    results = {keyword:doc_list.index(item) for keyword in keywords for item in doc_list if keyword in item and (keyword + '.' in item or keyword +' ' in item or ' ' + keyword in item)}
    return results

doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['they','casino' ]
print(multi_word_search(doc_list, keywords))
if __name__ == '__main__':
    is_valid_zip(zip_code)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
