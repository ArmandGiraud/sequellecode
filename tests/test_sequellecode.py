#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `sequellecode` package."""


import unittest

from sequellecode import sequellecode

class TestSequellecode(unittest.TestCase):
    """Tests for `sequellecode` package."""

    def __init__(self, *args, **kwargs):
        super(TestSequellecode, self).__init__(*args, **kwargs)
        self.st = self.test_instance()
        
        
    def test_instance(self, mapping = None):
        if mapping is None:
            st = sequellecode.SequellText()
        else:
            st = sequellecode.SequellText(mapping)
        return st

    # integration tests
    def test_put_links(self):
        test_text = """Une pause de 20 minutes est obligatoire au bout de six heures de travail échues. Cette obligation est énoncée aux l’article L3121-33 et L. 3121-31 du Code du travail: mais toutefois cela contredit l'article  L3187-1 du code de la sécurité sociale"""
        res = self.st.put_links(test_text)
        expected_res = """Une pause de 20 minutes est obligatoire au bout de six heures de travail échues. Cette obligation est énoncée aux l’article <a href="https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000035653042&cidTexte=LEGITEXT000006072050&dateTexte=20191231">L3121-33</a> et <a href="https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000033020364&cidTexte=LEGITEXT000006072050&dateTexte=20191231">L3121-31</a> du Code du travail: mais toutefois cela contredit l'article  L3187-1 du code de la sécurité sociale"""
        self.assertEqual(res, expected_res)
    
    def test_put_links_single(self):
        test_text = "L. 3121-31"
        expected_res = """<a href="https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000033020364&cidTexte=LEGITEXT000006072050&dateTexte=20191231">L3121-31</a>"""
        res = self.st.put_links(test_text)
        self.assertEqual(res, expected_res)
    
    def test_find_links(self):
        test_text = """Une pause de 20 minutes est obligatoire au bout de six heures de travail échues. Cette obligation est énoncée aux l’article L3121-33 et L. 3121-31 du Code du travail: mais toutefois cela contredit l'article  L3187-1 du code de la sécurité sociale"""
        links = self.st.find_links(test_text)
        expected_links = [('L3121-33', 'https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000035653042&cidTexte=LEGITEXT000006072050&dateTexte=20191231'),
                          ('L3121-31', 'https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000033020364&cidTexte=LEGITEXT000006072050&dateTexte=20191231'),
                          ('L3187-1', None)]
        
        self.assertIsInstance(links, list)
        self.assertIsInstance(links[0], tuple)
        self.assertIsInstance(links[0][0], str)
        self.assertTrue(links[0][1].startswith("http"), "should be a http link")
        self.assertTrue(links[2][1] is None, "should be None if no code de la sécu spécified")
        self.assertEqual(links, expected_links)





    
