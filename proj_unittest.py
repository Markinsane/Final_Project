from model import *
import unittest


class api_query(unittest.TestCase): 

    def test_api_query(self):
        self.assertEqual(get_data_for_web('Los Angeles')[0][0], "Paper Tiger Bar")
        self.assertEqual(get_data_for_web('Los Angeles')[0][5], 97)
        self.assertEqual(get_data_for_web('Los Angeles')[0][1], 4.5)
        self.assertEqual(get_data_for_web('Ann Arbor')[0][0], 'The Last Word')
        self.assertEqual(get_data_for_web('Ann Arbor')[0][5], 198)
        self.assertEqual(get_data_for_web('Ann Arbor')[0][1], 4.0)

class store_class (unittest.TestCase):

    def test_store(self):
        store=Store("Paper Tiger Bar", 4.5, 97)
        self.assertEqual(store.name, "Paper Tiger Bar")
        self.assertEqual(store.review, 97)
        self.assertEqual(store.rating, 4.5)
        self.assertEqual(store.__str__(), 'Paper Tiger Bar, Rating:4.5, Review:97 ')


class data_base (unittest.TestCase):
    def test_data_base(self):
        info_1=get_from_db("Detroit")[0][:30]
        info_2=get_from_db("Ann Arbor")[0][:30]
        info_3=get_from_db("Los Angeles")[0][:30]
        info_4=get_from_db("Troy")[0][:30]
        info_5=get_from_db("San Diego")[0][:30]

        self.assertEqual(info_1, 'Detroit,  city, seat of Wayne ')
        self.assertEqual(info_2, 'Ann Arbor,  city, seat (1826) ')
        self.assertEqual(info_3, "Los Angeles ,  city, seat of L")
        self.assertEqual(info_4, "Troy,  city, seat (1793) of Re")
        self.assertEqual(info_5, "San Diego,  port and city, sea")


     
     
     
        # self.assertEqual(len(self.az_site_list), 24)














if __name__ == "__main__":
	unittest.main(verbosity=2)