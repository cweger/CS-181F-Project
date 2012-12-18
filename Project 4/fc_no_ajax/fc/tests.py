"""
Authors: Chet and Michael

Description:
We use get() and post() functions to simulate get and post HttpRequest objects.
"""

"""
Chet's tests:
"""
from models import cardTable
from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
	
	"""
	black box testing: (Chet)
	"""
	#we test to make sure list page loads succesfully (test index 1.0):
	def test_create(self):
		c = Client()
		c.post('/create_set/', {'order': '1', 'setName': 'Test Set'})
		response = c.get('/set/1/')
		length = len(response.content)		
		self.assertEqual(length,926) #html returned is correct length

	#we add flashcard and then verify contents (1.1):
	#we also verify detail page loads succesfully (1.2):
	def test_show(self):
		c = Client()
		c.post('/create_set/', {'order': '1', 'setName': 'Test Set'})
		response1 = c.post('/create/1/', {'order': '47', 'front': 'der Hund', 'back': 'the dog'})
		response2 = c.get('/set/1/card/47/')
		length = len(response2.content)
		self.assertEqual(cardTable.objects.get(cardID = 47).back, 'the dog')
		self.assertEqual(length, 1133)

	#we test that we can delete a flashcard from a set (1.3):
	def test_delete(self):
		c = Client()
		c.post('/create/1776/', {'order': '47', 'front': 'der Hund', 'back': 'the dog'})
		response = c.post('/set/1776/card/47/delete_card/')
		self.assertEqual(len(cardTable.objects.all()), 0) #make sure the card was deleted!

	#we test that after a series of creates and deletes, we will have the number of cards expected (1.4):
	def test_backAndForth(self):
		c = Client()
		c.post('/create/1776/', {'order': '47', 'front': 'der Hund', 'back': 'the dog'})
		c.post('/create/1776/', {'order': '48', 'front': 'die Katze', 'back': 'the cat'})
		c.post('/create/1776/', {'order': '49', 'front': 'der Vogel', 'back': 'the bird'})
		count1 = len(cardTable.objects.all())
		response = c.post('/set/1776/card/47/delete_card/')
		response = c.post('/set/1776/card/48/delete_card/')
		c.post('/create/1776/', {'order': '1', 'front': 'der Mann', 'back': 'the man'})
		count2 = len(cardTable.objects.all())
		self.assertEqual(count1, 3)
		self.assertEqual(count2, 2)

	#we test that we can modify a flashcard (1.5): 
	def test_modify (self):
		c = Client()
		c.post('/create/1776/', {'order': '47', 'front': 'der Hund', 'back': 'the dog'})
		dog = cardTable.objects.get(cardID = 47).back
		c.post('/set/1776/card/47/update/', {'order': '47', 'front': 'die Katze', 'back': 'the cat'})
		cat = cardTable.objects.get(cardID =  47).back
		self.assertEqual(dog, 'the dog')
		self.assertEqual(cat, 'the cat')

	'''
	White box Testing (Chet)
	'''

	#we test that create_flashcard handles improper user input (2.0):
	def test_create_improper(self):
		c = Client()
		response = c.post('/create/1776/', {'order': 'string', 'front': 'der Mann', 'back': 'the man'}).content
		self.assertEqual(response, 'Please enter an integer value.')

	#we test that update_flashcard handles improper user input (2.1):
	def test_update_improper(self):
		c = Client()
		c.post('/create/1776/', {'order': '47', 'front': 'der Mann', 'back': 'the man'}).content
		response = c.post('/set/1776/card/47/update/', {'order': 'improper', 'front': 'die Katze', 'back': 'the cat'}).content
		self.assertEqual(response, 'Please enter an integer value.')


'''
Michael's tests:
'''

from django.test import TestCase
from django.test.client import Client
from models import userSetTable
from django.utils import unittest

class testCases(unittest.TestCase):

    #tests whether the list of materials is correct.
    def test_list_materials(self):
        c = Client()
        response = c.post('/create_set/', {'order': '1', 'setName': 'Test Set'})
        length = len(response.content)
        self.assertEqual(length, 0)

    #tests the create function
    def test_create(self):
        c = Client()
        response = c.post('/create_set/', {'order': '1', 'setName': 'Test Set'})
        self.assertEqual(userSetTable.objects.get(setID = 1).setName, 'Test Set')

    #tests the delete_set function
    def test_delete_set(self):
        c = Client()
        c.post('/create_set/', {'order': '1', 'setName': 'Test Set'})
        response = c.post('/user/set/1/delete_set/')
        self.assertEqual(len(userSetTable.objects.all()), 0)

