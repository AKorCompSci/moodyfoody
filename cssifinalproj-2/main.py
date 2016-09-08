#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import json
import urllib
import urllib2
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('project2.html')
		self.response.write(template.render())
		
class JoyfulHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('joyful.html')
		self.response.write(template.render())
 		
class SadHandler(webapp2.RequestHandler):
     def get(self):
		template = jinja_environment.get_template('sad.html')
		self.response.write(template.render())
 		
class FeistyHandler(webapp2.RequestHandler):
     def get(self):
		template = jinja_environment.get_template('feisty.html')
		self.response.write(template.render())
 		
class LazyHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('lazy.html')
		self.response.write(template.render())
	def post(self):
		address = self.request.get('address')
		search = urllib.quote(address) 
		temp_url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyC6eXjzUIZLMuft3zUOhXA5pefPf3HlgpY' %search)
		geocoding_source = urllib2.urlopen(temp_url)
		geocoding_content = geocoding_source.read()
		parsed_geocoding_dictionary = json.loads(geocoding_content)
		geocodingLat = parsed_geocoding_dictionary['results'][0]['geometry']['location']['lat']
		geocodingLng = parsed_geocoding_dictionary['results'][0]['geometry']['location']['lng']
		values = {'loclat': geocodingLat, 'loclng': geocodingLng} 
		template = jinja_environment.get_template('map2.html') 
		self.response.write(template.render(values))
		
		#quote formats it so that any special characters are escaped
		#pass in 'address' as a readable code in json thus converting to lat lng
		#can also put direct url instead of variable
		#used %s to fill in white space as opposed to + and %20
		#read puts it into a parsed format so that we can store it inside a variable
		#parsed json makes it readable
		#gets it from the dictionary (use pretty print if not formatted)
		#dictionary result, first key, location in 2nd dictionary and references lat or lng
		#sets values for variables longitude and latitude in dictionary
		#references map2.html for geolocation
		
class MapHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('map.html')
		self.response.write(template.render())
		 		
class SickHandler(webapp2.RequestHandler):
     def get(self):
		template = jinja_environment.get_template('sick.html')
		self.response.write(template.render())
 		
class PeacefulHandler(webapp2.RequestHandler):
     def get(self):
		template = jinja_environment.get_template('peaceful.html')
		self.response.write(template.render())
 		
class EnthusiasticHandler(webapp2.RequestHandler):
 	def get(self):
		template = jinja_environment.get_template('enthusiastic.html')
		self.response.write(template.render())
 		
class FancyHandler(webapp2.RequestHandler):
     def get(self):
		template = jinja_environment.get_template('fancy.html')
		self.response.write(template.render())
 			
class FlirtyHandler(webapp2.RequestHandler):
     def get(self):
		template = jinja_environment.get_template('flirty.html')
		self.response.write(template.render())
 		
class AdventurousHandler(webapp2.RequestHandler):
     def get(self):
		template = jinja_environment.get_template('adventurous.html')
		self.response.write(template.render())
 		
class ZestyHandler(webapp2.RequestHandler):
     def get(self):
		template = jinja_environment.get_template('zesty.html')
		self.response.write(template.render())
		
class Rating(ndb.Model):
	theRating = ndb.StringProperty(required=True)
	
class RatingHandler(webapp2.RequestHandler) :
	def get(self):
		template = jinja_environment.get_template('rating.html')
		self.response.write(template.render())
	def post(self):
		rating = self.request.get('rating')
 		if rating == "One":
 			comment = 'Let us know how we can improve by emailing us at akor@csumb.edu'
 		elif rating == "Two":
 			comment = 'Thank you for your feedback!'
 		elif rating == "Three":
 			comment = 'Thank you for your feedback!'
 		elif rating == "Four":
 			comment = 'Thank you for your feedback!'
 		elif rating == "Five":
 			comment = 'Wow! Thank you for your feedback!'
 		values = {'rating':comment}
 		newRating = Rating(theRating = rating)
 		key = newRating.put()
  		template = jinja_environment.get_template('results.html')
		self.response.write(template.render(values))
		

app = webapp2.WSGIApplication([
    ('/', MainHandler),
     ('/joyful', JoyfulHandler),
     ('/sad', SadHandler),
     ('/feisty', FeistyHandler),
     ('/lazy', LazyHandler),
     ('/sick', SickHandler),
     ('/peaceful', PeacefulHandler),
     ('/enthusiastic', EnthusiasticHandler),
     ('/fancy', FancyHandler),
     ('/flirty', FlirtyHandler),
     ('/adventurous', AdventurousHandler),
     ('/zesty', ZestyHandler),
     ('/map', MapHandler),
     ('/rating', RatingHandler)
    
], debug=True)
