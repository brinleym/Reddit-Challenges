from sys import argv
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

class Senitments:

	def __init__(self):
		self.happy = ['love','loved','like','liked','awesome','amazing','good','great','excellent']
		self.sad = ['hate','hated','dislike','disliked','awful','terrible','bad','painful','worst']

class Video:

	def __init__(self):
		self.base = "https://plus.googleapis.com/u/0/_/widget/render/comments?first_party_property=YOUTUBE&href="
		self.user_input = ""
		self.url = ""
		self.comments = []
		self.sample_size = 20 # init sample size
		self.happy_total = 0
		self.sad_total = 0
		self.isHappy = False

	def get_user_input(self):

		script, url, sample_size = argv
		self.user_input = url
		self.url = self.base + url # concat base and user-input url
		self.sample_size = sample_size

	def analyze(self):

		for comment in self.comments:
			if comment.isHappy == True:
				self.happy_total += 1
			else:
				self.sad_total += 1

	def report_results(self):

		print "Analysis complete."
		print ""
		print "Sentiment analysis results for: " + self.user_input
		print ""

		print "Total happy comments: " + str(self.happy_total)
		print "Total sad comments: " + str(self.sad_total)

		if self.happy_total > self.sad_total:
			print "The general feelings toward this video were happy."
		elif self.happy_total == self.sad_total:
			print "The general feelings toward this video were mixed."
		else:
			print "The general feelings toward this video were sad."

class Comment:

	def __init__(self, comment):
		self.text = comment
		self.word_list = []
		self.happy_count = 0
		self.sad_count = 0
		self.isHappy = False

	def analyze(self):

		print "analyzing comment.."

		mySentiments = Senitments() # instantiate Sentiments

		# convert string of text to array of words
		self.word_list = self.text.split()

		happy_overlap = set(self.word_list) & set(mySentiments.happy)
		self.happy_count = len(happy_overlap)

		sad_overlap = set(self.word_list) & set(mySentiments.sad)
		self.sad_count = len(sad_overlap)

		if self.happy_count > self.sad_count:
			self.isHappy = True


class Request:

	def __init__(self, target_url):
		self.url = target_url
		self.plain_text = self.makeRequest()
		self.soup = self.parseHtml()
		
	def makeRequest(self):
		try:
			response = requests.get(self.url) # make GET request
		except ConnectionError as error:
			print "Page not found."
			print error
			return None

		return response.text # return plain text 

	def parseHtml(self):

		# corner case: request failed, no response text to parse
		if self.plain_text is None: 
			return None

		html_soup = BeautifulSoup(self.plain_text, "html.parser")
		return html_soup


class Scraper:

	def __init__(self, response):
		self.soup = response

	def scrape(self, video):

		print "Analyzing webpage.."
		print "This will take a couple seconds. Please be patient."
		# scrape commments
		for comment in self.soup.find_all("div", class_="Ct"):
			newComment = Comment(comment.get_text())

			# analyze comment
			newComment.analyze()

			# append comment to video's list of comments
			video.comments.append(newComment)


myVideo = Video()
myVideo.get_user_input()

myRequest = Request(myVideo.url)
myScraper = Scraper(myRequest.soup)
myScraper.scrape(myVideo)

myVideo.analyze()
myVideo.report_results()




