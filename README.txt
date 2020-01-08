CS 600 SEARCH ENGINE PROJECT by Ritvik Tiwari 
USE python 3.7 
import all the necessary modules 

QUESTION:

Implement the simplified Search Engine described in Section 23.5.4 for the pages of a small Web site. Use all the words in the pages of the site as index terms, excluding stop words such as articles, prepositions, and pronouns.
Submit the following four files:
1. A read me file that contains details of your approach to the problem.
2. Your coded, well-commented code file in your favorite language, such as Python, Java, C++,... 
3. The input file that contains the few pages you have used as input, including some links to your other pages..
4. Output file that has samples of your run. Make sure you have tested the boundary conditions.

The project uses python 2.7 and modules like beautifulsoup and goose are used to implement extraction. The searching is done using inverted index and trie data structure. Upon running, the code asks for a search term to be searched in the extracted pages from the internet. The web pages used are in the file usedReuter.txt and the results are stored in the file Output.txt. All the scraped web pages without the HTML and formatting are stored in the DATA folder in saperate txt files.

The Output file has the ranking of each webpage asper the search term and tells the highest ranking web page for the given search term/terms. It then displays all the inverted index and the tries for each webpage for manual verification.

I used beautifulsoup to extract webpages from an RSS feed from CNBC. I then open the TXT files under the DATA folder where the data is stored and process the text. I remove all stop words and punctuation and split the words into an array. 

From here I count the number of times a word occurs in the list and create an occurrence list. I then take every word from this occurrence list and pass it into a function I made to create a standard trie which has the index of its location in the occurrence list, as outlined by Section 23.5.4. I also created a function that searches through the tries to find a word and returns the index of that search word in the occurrence list if it exists.
