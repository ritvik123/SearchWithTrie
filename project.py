import datetime
import requests
from nltk.corpus import stopwords
from collections import Counter
from boilerpipe.extract import Extractor
from bs4 import BeautifulSoup
import html5lib
# Function to create a trie using a list of words
end = 'last'
def create_trie(words):
	root = {}
	index_trie = 0
	for word in words:
		current_dict = root
		for letter in word:
			current_dict = current_dict.setdefault(letter, {})
		current_dict[end] = index_trie
		index_trie = index_trie + 1
	return root

# Function to find and return the index value from a trie
def find_in_trie(trie, word):
	current_dict = trie
	for letter in word:
		if letter in current_dict:
			current_dict = current_dict[letter]
		else:
			return 0
	else:
		if end in current_dict:
			return current_dict[end]
		else:
			return 0

# Function that gets tries 
trie = []
indexTerms = []
def Trie_ALL(number_of_links):
	for i in range(0,number_of_links):
		# Opens Text file with text from a scraped webpage
		file = "Data/"+(str(i)) + ".txt"
		lfile = open(file)
		dt = lfile.read()
		lfile.close()
		# returns text count
		iterms = occurences(dt)
		indexTerms.append(occurences(dt))
		# creates list of words from the dictionary to make a trie out of
		wordList=[]
		for w in iterms:
			wordList.append(w[0])
		trie.append(create_trie(wordList))

def search(term,number_of_links):
	# create temp list to split search term into
	rank = []
	temp = []
	temp = term.split()
	f.write("Search terms:")
	f.write("%s\n"%temp)

	# iterate through every trie
	for i in range(0,number_of_links):
		sum = 0
		#iterate through every search term
		for t in temp:
			# If search finds the term, it adds the occurrences to the rank
			if find_in_trie(trie[i], t) > 0:
				n=find_in_trie(trie[i], t)
				# Uses index at the bottom of trie to find number of occurrences in the index terms
				sum = sum + int(list(indexTerms[i])[n][1])
		rank.append(sum)
	return rank

# Scraping RSS feed for DATA 

def scrape(file, split1, split2, urlName):
	links_from_RSS_feed = []
	Requests_from_RSS = requests.get('http://feeds.reuters.com/reuters/businessNews')
	Rss_soup = BeautifulSoup(Requests_from_RSS.text, "html5lib")

	lFile = open(file,"r")
	usedLinks = [line.strip() for line in lFile]
	lFile.close()

	for link in Rss_soup.find_all('guid'):
		links_from_RSS_feed.append(str(link.getText().replace('?feedType=RSS&feedName=businessNews', '')))

	l_file = open(file,"w")
	for item in links_from_RSS_feed:
		l_file.write(str(item)+"\n")
	l_file.close()

	no_of_links= len(links_from_RSS_feed)

	for i in range(0, no_of_links):
		fileName = links_from_RSS_feed[i].rsplit('/', split1)[split2]
		extractedText = Extractor(extractor='ArticleExtractor', url=urlName+fileName)
		print(fileName)
		write_file = open("Data/"+str(i)+".txt","w")
		write_file.write(str(datetime.date.today()) + "\n")
		write_file.write(str(extractedText.getText().encode("utf-8")))
		write_file.close()
	return no_of_links

# Function that outputs occurrence lists

def occurences(text):
	# Create list of characters to delete
	characters_to_delete = [".",",","/","?","<",">",":",";","[","]","{","}","-",
	"_","+","=","|",'"',"!","@","#","$","%","^","&","*","(",")"]
	for char in characters_to_delete:
		text = text.replace(char,"")
	numbers_to_delete = list(range(10))
	for num in numbers_to_delete:
		text = text.replace(str(num),"")
	# Splits data into a list
	datAr = text.split()
	# Creates a list of stopwords to delete using the NLTK library
	stopwords_to_delete = list(str(stopwords.words('english')))
	# Adding extra words not covered above
	excludes = ["the", "The", "to","and", "of", "for", "is"]
	for w in excludes:
		stopwords_to_delete.append(w)
	for word in datAr:
		if word in stopwords_to_delete:
			datAr.remove(word)
	# Uses Counter to make an occurrence list which is stored in a dictionary
	counts = Counter(datAr)
	index_terms = counts.items()
	return index_terms

menu = True
while menu:
	print ("""
	1. Extract News / Search 
	2. Exit/Quit
	""")
	menu = input("Enter input: ") 
	if menu == "1": 
		count_of_links=scrape("usedReuter.txt",1,-1,"http://www.reuters.com/article/") # Scrape the webpages
		Trie_ALL(count_of_links) 													   # Create Trie fpr all the webpages
		f = open('Output.txt', 'w')													   # Open the output file to write 
		input_string= input("\n Enter the search term/terms : \n") 					   # Input search terms from user
		rank_of_pages = search(input_string,count_of_links)							   # Get rank of all the pages
		print("The rank of pages are :{0}".format(rank_of_pages))					   # Display rank on the console 
		best_ranked_page = [None, 0]												   # Calculate the best ranked webpage 
		for it in range(0,count_of_links):
			f.write("Webpage " + str(it) + " rank:")								   # Write the ranks in output file 
			f.write("%s\n"%rank_of_pages[it])
			if best_ranked_page[1] < rank_of_pages[it]:
				best_ranked_page[0] = it
				best_ranked_page[1] = rank_of_pages[it]
		if best_ranked_page[0] == None:
			f.write("Search result not found in any of the webpages.")
		else:
			f.write("Highest ranking search from Webpage " + str(best_ranked_page[0]))
		f.write("\n \n \n \n")
		f.write("\n Index Terms Output \n ")											# Write the occurence list in the output file 
		for j in range(0, count_of_links):
			f.write("\n Webpage " + str(j) + "\n")
			f.write("%s\n"%indexTerms[j])
		f.write("\n")
		f.close()
		print("\nResult in Output.txt\n")
		print("\n Press 2 \n")
	elif menu == "2":
		print("Goodbye")
		menu = False 
	elif menu != "":
		print("\n Not Valid Choice Try again") 