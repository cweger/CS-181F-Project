from django.db import models

class cardTable(models.Model):
    # cardID:   A unique identifier number for each card
	cardID = models.PositiveIntegerField()

    # set:      The unique setID for the set that the card belongs to
    #setID = models.ManyToManyField(userSetTable)
	setID = models.PositiveIntegerField()

    # front:    A string for the data on the front of the card
	front = models.CharField(max_length=140)

    # back:     A string for the data on the back of the card
	back = models.CharField(max_length=140) 

    # get_absolute_url
    # Purpose:  Return a url unique to each card (based on its cardID) that
    #           will point to the card's edit page.
    # Input:    self - the cardTable object
    # Returns:  A url unique to each card
	def get_absolute_url(self):
		return u"/set/card/%s/" % (self.cardID)
	def __unicode__(self):
		return u"fc(%s,%s)" % (self.front, self.back) #modified from u"Note(%


'''    def get_absolute_url(self):
         return u"/set/%s/card/%s/" % (self.setID,self.cardID)'''


