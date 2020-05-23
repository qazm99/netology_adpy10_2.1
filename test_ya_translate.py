import unittest
import ya_translate


class TestYatranslate(unittest.TestCase):
    def setUp(self):
        self.API = 'trnsl.1.1.20200125T113951Z.d376771cc4d168af.1614e80afaec48ec7f1de03eac47de3c5d9f880e'
        self.API_false = '!trnsl.1.1.20200125T113951Z.d376771cc4d168af.1614e80afaec48ec7f1de03eac47de3c5d9f880e'

    def test_ya_translate(self):
        word_translate = ya_translate.translate_it('Hello', 'en', 'ru', self.API)
        self.assertEqual(word_translate[1], 'Привет')
        self.assertEqual(word_translate[0], 200)
        word_translate = ya_translate.translate_it('Hello', 'ru', 'en', self.API)
        self.assertEqual(word_translate[1], 'Hello')
        self.assertEqual(word_translate[0], 200)
        word_translate = ya_translate.translate_it('Hello', 'en', 'ru', self.API_false)
        self.assertGreater(word_translate[0], 399)


if __name__ == '__main__':
    unittest.main()
