# coding: utf-8
""" Some test for the UI """
from django.test import TestCase

TEXTS = [
    """Covering approximately 9.6 million square kilometres, China is the world's second-largest country by land area,[17] but only the third or fourth-largest by total area, dependent on whether the surface areas of various inland bodies of water such as the Great Lakes are included in the total area of a country.[g] China's landscape is vast and diverse, ranging from forest steppes and the Gobi and Taklamakan deserts in the arid north to subtropical forests in the wetter south. The Himalaya, Karakoram, Pamir and Tian Shan mountain ranges separate China from South and Central Asia. The Yangtze and Yellow Rivers, the third- and sixth-longest in the world, run from the Tibetan Plateau to the densely populated eastern seaboard. China's coastline along the Pacific Ocean is 14,500 kilometres (9,000 mi) long, and is bounded by the Bohai, Yellow, East and South China Seas.""",
    """Władzę w ChRL sprawuje od 1949 roku Komunistyczna Partia Chin. Do końca lat 70. Chiny były państwem totalitarnym na wzór stalinowski, a w latach 60. nasiliły się w kraju tendencje izolacjonistyczne. Po śmierci Mao Zedonga i fiasku maoizmu, w latach 80. partia rozpoczęła jednak reformy ekonomiczne, tj. odejście od gospodarki planowej i otwarcie na świat, a ustrój zaczął przesuwać się w stronę autorytaryzmu. W latach 80. i 90. nastąpiła liberalizacja życia społecznego i kulturalnego, poprzez m.in. wprowadzenie wolności podróżowania. Wraz z reformami ekonomicznymi zapoczątkowało to dokonującą się obecnie największą migrację w historii świata – ze wsi do miast przeniosło się już 140 mln Chińczyków."""
]

class SimpleTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_nltk_en(self):
        response = self.client.post('/', {"text": TEXTS[0], "method": "nltk" })
        self.assertEqual(response.status_code, 200)

    def test_post_nltk_pl(self):
        response = self.client.post('/', {"text": TEXTS[1], "method": "nltk" })
        self.assertEqual(response.status_code, 200)

    def test_post_pure_en(self):
        response = self.client.post('/', {"text": TEXTS[0], "method": "pure" })
        self.assertEqual(response.status_code, 200)

    def test_post_pure_pl(self):
        response = self.client.post('/', {"text": TEXTS[1], "method": "pure" })
        self.assertEqual(response.status_code, 200)