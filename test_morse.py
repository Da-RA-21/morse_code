import unittest
from morse import translate


class TestTranslate(unittest.TestCase):
    def test_translate(self):
        self.assertEqual(translate('Hello'), '.... . .-.. .-.. ---')
        self.assertEqual(translate('123456789'), '.---- ..--- ...-- ....- ..... -.... --... ---.. ----.')
        self.assertEqual(translate(',.?/-()'), '--..-- .-.-.- ..--.. -..-. -....- -.--. -.--.-')
        self.assertEqual(translate(' '), '/')
        self.assertEqual(translate('@#$'), 'error error error')
        self.assertEqual(translate('He12. @'), '.... . .---- ..--- .-.-.- / error')
