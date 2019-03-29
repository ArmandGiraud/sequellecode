"""utility functions for the main module sequellecode"""

import re

def find_context(text, article):
    """check for a given article the surrounding text and try to find some reference to codes"""
    before = r"(?P<before>.{1,80})?"
    after = r"(?P<after>.{1,80})?"
    regex_article = before + article + after
    regex_article = re.compile(regex_article)
    context_list = re.findall(regex_article, text)
    if context_list:
        context = " ".join(context_list[0]).lower()
        return context
    else:
        print("article menntion not found")

def find_articles_position(text):
    """find articles mentions in raw string"""
    regex_article = re.compile(r"((?:R|L|D|l|r|d)(?:\s|\.|\.\s)?\d{3,4}(?:-\d{1,2})?(?:-\d{1,2})?)")
    articles = list(re.finditer(regex_article, text))

    if not articles:
        return None, None

    articles = [(art.group(), art.span()) for art in articles]

    articles, positions = list(zip(*articles))
    return articles, positions


def detect_code(context, code_strings):
    """detect in the given surrounding context a code reference"""
    return set(code for code in code_strings if code in context)

def find_articles_code(text, code_strings = ["code du travail"]):
    """detect articles and reference to a code in the surrounding 80 characters"""
    articles, positions = find_articles_position(text)
    if not articles:
        return None, (None, None)
    contextes = [find_context(text, art) for art in articles]
    assert len(articles) == len(contextes), "problem in function find_context"
    codes = [detect_code(context, code_strings) for context in contextes]
    articles_normalized = [normalize_digit(art) for art in articles]
    
    return list(zip(articles_normalized, codes)), (articles, positions)



#------------ normalize different code format

def replace_space(text):
    "remove any kind of space"
    return re.sub(r"\xa0|\n|\s","", text)

def replace_lower(text):
    return text.upper()

def replace_point(text):
    "remove point in article mention"
    return re.sub("\.", "", text)

def normalize_digit(text):
    """take ill-defined article reference and turn it into Legifrance ready
    ex: l. 783-2 --> L783-2"""
    text = replace_space(text)
    text = replace_lower(text)
    text = replace_point(text)
    return text

# -------------------------- build url
def build_url(legiart):
    """turn LEGIARTI ID into url"""
    url = "https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=" + legiart + "&cidTexte=LEGITEXT000006072050&dateTexte=20191231"
    return url

def add_single_markup(text, markup, offset):
    """insert the markup inside the text (it is required to offset
     the text of the markup length minus the href text length)"""
    markup_text, art_len, position = markup
    start, end = position
    start, end = start + offset, end + offset
    new_text = text[:start] + markup_text + text[end:]
    return new_text, len(markup_text) - len(art_len)  + offset

def make_href_mark(url, text):
    """simply transform url into hrml markup"""
    return '<a href="' + url + '">' + text + '</a>'