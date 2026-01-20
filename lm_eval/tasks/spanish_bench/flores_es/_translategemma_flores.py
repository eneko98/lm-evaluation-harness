# /scratch/evalero/repos/lm-evaluation-harness/lm_eval/tasks/_translategemma_flores.py

def _msg(doc, src_field: str, src_code: str, tgt_code: str):
    # TranslateGemma expects: user.content = [ {type, source_lang_code, target_lang_code, text} ]
    return [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "source_lang_code": src_code,
                    "target_lang_code": tgt_code,
                    "text": doc[src_field],
                }
            ],
        }
    ]

# Basque (eus) <-> English (eng)
def flores_eu_en(doc): return _msg(doc, "sentence_eus_Latn", "eu", "en")
def flores_en_eu(doc): return _msg(doc, "sentence_eng_Latn", "en", "eu")

# Basque (eus) -> Spanish (spa)
def flores_eu_es(doc): return _msg(doc, "sentence_eus_Latn", "eu", "es")

# Spanish (spa) -> Basque (eus)
def flores_es_eu(doc): return _msg(doc, "sentence_spa_Latn", "es", "eu")

# Galician (glg) <-> Spanish (spa)
def flores_gl_es(doc): return _msg(doc, "sentence_glg_Latn", "gl", "es")
def flores_es_gl(doc): return _msg(doc, "sentence_spa_Latn", "es", "gl")

# Galician (glg) <-> English (eng)
def flores_gl_en(doc): return _msg(doc, "sentence_glg_Latn", "gl", "en")
def flores_en_gl(doc): return _msg(doc, "sentence_eng_Latn", "en", "gl")

# Catalan (cat) <-> Spanish (spa)
def flores_ca_es(doc): return _msg(doc, "sentence_cat_Latn", "ca", "es")
def flores_es_ca(doc): return _msg(doc, "sentence_spa_Latn", "es", "ca")

# Catalan (cat) <-> English (eng)
def flores_ca_en(doc): return _msg(doc, "sentence_cat_Latn", "ca", "en")
def flores_en_ca(doc): return _msg(doc, "sentence_eng_Latn", "en", "ca")

# Spanish (spa) <-> English (eng)
def flores_en_es(doc): return _msg(doc, "sentence_eng_Latn", "en", "es")
def flores_es_en(doc): return _msg(doc, "sentence_spa_Latn", "es", "en")
