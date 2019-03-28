=============
sequelle code
=============


.. image:: https://img.shields.io/pypi/v/sequellecode.svg
        :target: https://pypi.python.org/pypi/sequellecode

.. image:: https://img.shields.io/travis/armandgiraud/sequellecode.svg
        :target: https://travis-ci.org/armandgiraud/sequellecode

.. image:: https://readthedocs.org/projects/sequellecode/badge/?version=latest
        :target: https://sequellecode.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




find legifrance link in natural language


* Free software: GNU General Public License v3
* Documentation: https://sequellecode.readthedocs.io.


Install
-------
``pip install git+https://github.com/ArmandGiraud/autosuggest.git``

Usage
-----

.. code-block:: python

    mapping_path = "../data/mapping-articles-cdtn.json"
    st = SequellText(mapping_path)
    test_text = """Une pause de 20 minutes est obligatoire au bout de six heures de travail échues.
    Cette obligation est énoncée aux l’article L3121-33 et L. L3121-31 du Code du travail:
    mais toutefois cela contredit l'article  L3187-1 du code de la sécurité sociale"""

    st.put_links(text=test_text, code_strings=["code du travail"])

    >>> 'Une pause de 20 minutes est obligatoire au bout de six heures de travail échues.
    Cette obligation est énoncée aux l’article <a href="https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000035653042&cidTexte=LEGITEXT000006072050&dateTexte=20191231">L3121-33</a>
    et L. <a href="https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000033020364&cidTexte=LEGITEXT000006072050&dateTexte=20191231">L3121-31</a> du Code du travail:
    mais toutefois cela contredit l'article  L3187-1 du code de la sécurité sociale'

.. raw:: html

     <embed>
    Une pause de 20 minutes est obligatoire au bout de six heures de travail échues.
    Cette obligation est énoncée aux l’article <a href="https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000035653042&cidTexte=LEGITEXT000006072050&dateTexte=20191231">L3121-33</a>
     et L. <a href="https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000033020364&cidTexte=LEGITEXT000006072050&dateTexte=20191231">L3121-31</a> du Code du travail:
     mais toutefois cela contredit l'article  L3187-1 du code de la sécurité sociale
     </embed>



* TODO

1. tests
2. find all codes mapping and fix line 15 of sequellecode.py

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
