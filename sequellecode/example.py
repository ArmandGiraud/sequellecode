from sequellecode import SequellText
mapping_path = "../data/mapping-articles-cdtn.json"
st = SequellText(mapping_path)
test_text = """Une pause de 20 minutes est obligatoire au bout de six heures de travail échues.
    Cette obligation est énoncée aux l’article L3121-33 et L. L3121-31 du Code du travail:
mais toutefois cela contredit l'article  L3187-1 du code de la sécurité sociale"""
test_text = ""
print(st.put_links(text=test_text, code_strings=["code du travail"]))