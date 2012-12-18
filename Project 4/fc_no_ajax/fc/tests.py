"""
Tests!
"""
from models import cardTable

from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
	def test_basic_addition(self):
		"""
		Tests that 1 + 1 always equals 2.
		"""
		print "hello"
		self.assertEqual(1 + 1, 2)
	
	"""
	black box testing:
	"""
	#we test to make sure list page loads succesfully (test index 1.0):
	def test_create(self):
		c = Client()
		response = c.get('/set/1776')
		length = len(response.content)		
		self.assertEqual(length,813) #html returned is correct length

	#we add flashcard and then verify contents (1.1):
	#we also verify detail page loads succesfully (1.2):
	def test_create(self):
		c = Client()
		response1 = c.post('/create/47/', {'order': '47', 'front': 'der Hund', 'back': 'the dog'})
		response2 = c.get('/set/2/card/47/')
		length = len(response2.content)
		self.assertEqual(cardTable.objects.get(cardID = 47).back, 'the dog')
		self.assertEqual(length, 1021)

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
		#print "\n\n**\n count1:", count1, "\n\n**\ncount2", count2, "\n**"
		self.assertEqual(count1, 3)
		self.assertEqual(count2, 2)

	#we test that we can modify a flashcard (1.5): 
	def test_modify (self):
		c = Client()
		c.post('/create/1776/', {'order': '47', 'front': 'der Hund', 'back': 'the dog'})
		dog = cardTable.objects.get(cardID = 47).back
		c.post('/set/1776/card/47/update/', {'order': '47', 'front': 'die Katze', 'back': 'the cat'})
		cat = cardTable.objects.get(cardID =  47).back
		print dog
		print cat
		self.assertEqual(dog, 'the dog')
		self.assertEqual(cat, 'the cat')

