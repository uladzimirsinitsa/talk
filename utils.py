
def simple_slug_generator(name):
    """Title ==> slug"""
    slug = str(name).lower()
    dict_symbol = ('@', '#', '(', ')', '%', '№', ',', '.', ':', ';', '"', "'", '!')
    for symbol in dict_symbol:
        slug = slug.replace(symbol, '')
    slug = slug.replace('--', '-')
    slug = slug.strip()
    slug = slug.replace(' ', '-')
    return slug
