from googletrans import Translator


class FillText(object):

    def __init__(self, config):
        self.lang_map = config.lang_map
        self.input_map = config.input_map
        self.image_map = config.image_map
        self.config = config
        self.translator = Translator()

    def fill_text(self, text, iter):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            key = text[start + 1:end].lower()
            if key in self.config.static_keys:
                if iter == 1:
                    text = list(text)
                    text[start] = '('
                    text[end] = ')'
                    text = ''.join(text)
                    continue
            if isinstance(self.input_map.get(key), list):
                fill = ''
                i = 0
                for ele in self.input_map.get(key):
                    if len(self.input_map.get(key)) > 1 and i == len(self.input_map.get(key)) - 1:
                        fill = fill[:-1] + ' ' + self.lang_map.get('and') + ' ' + self.lang_map.get(ele)
                    else:
                        fill = fill + self.lang_map.get(ele) + ','
                    i = i + 1
                if fill[-1] == ',':
                    fill = fill[:-1]
                text = text[:start] + fill + text[end + 1:]
                continue
            else:
                k = self.input_map.get(key)
            if k in self.lang_map:
                fill = self.lang_map.get(k)
            else:
                fill = k
            text = text[:start] + fill + text[end + 1:]
        if iter == 1 and self.lang_map.get('lan') == 'en-IN':
            return text.replace('(', '{').replace(')', '}')
        if iter == 1:
            return self.translator.translate(text, dest=self.lang_map.get('lan')).text.replace('(', '{').replace(')',
                                                                                                                 '}')
        else:
            return text.capitalize()
