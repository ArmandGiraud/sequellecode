# -*- coding: utf-8 -*-

"""Main module."""

import json
from .utils import find_articles_code, build_url, add_single_markup, make_href_mark

class SequellText:
    def __init__(self, mapping_path):
        self._load_mappings(mapping_path)

    def put_links(self, text, code_strings = ["code du travail"]):
        articles_normalized, (articles, positions) = find_articles_code(text, code_strings)
        
        articles_normalized = [art[0] for art in articles_normalized] # change this line to add new codes// filter code
        links = [self._find_article_id(art) for art in articles_normalized]
        markups = [(make_href_mark(link, art_norm), art, pos) for link, art_norm, art, pos in zip(links, articles_normalized, articles, positions) if link]
        offset = 0
        for markup in markups:
            text , offset = add_single_markup(text, markup, offset)
            
        return text
    
    def _find_article_id(self, article):
        """return article legi id, if not found: either article is obsolete or not in the detected code"""
        article_id = self.code_json.get(article)
        if not article_id: 
            return None
        return build_url(article_id)
    
    def _load_mappings(self, mapping_path):
        with open(mapping_path, "r") as f:
            self.code_json = json.load(f)

if __name__ == "__main__":
    mapping_path = "../data/mapping-articles-cdtn.json"
    st = SequellText(mapping_path)
    test_text = """Une pause de 20 minutes est obligatoire au bout de six heures de travail échues.
        Cette obligation est énoncée aux l’article L3121-33 et L. L3121-31 du Code du travail:
    mais toutefois cela contredit l'article  L3187-1 du code de la sécurité sociale"""
    print(st.put_links(text=test_text, code_strings=["code du travail"]))
