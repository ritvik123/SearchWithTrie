By: Justin Serowik
CS 600 project Web Search Project
Requirements:
Implement the simplified Search Engine described in Section 23.5.4 for the pages of a small Web site. Use all the words in the pages of the site as index terms, excluding stop words such as articles, prepositions, and pronouns.
Submit the following four files:
1. A read me file that contains details of your approach to the problem.
2. Your coded, well-commented code file in your favorite language, such as Python, Java, C++,... 
3. The input file that contains the few pages you have used as input, including some links to your other pages..
4. Output file that has samples of your run. Make sure you have tested the boundary conditions.

I created my project in Python because it is a great language for creating dynamic objects and easy to code. I have included test inputs (labeled test#.txt) that query a few words in the 8 extracted documents and output how many times they appear in each, before returning the highest ranking search. I then output the occurrence list and the trie for each, so you can examine the inputs and methodology.

I used beautifulsoup to extract webpages from an RSS feed from CNBC. I then stripped all html and css properties and stored the text in TXT files under the Data folder labeled from 0 to 7, to make opening and using them easier. I then open the TXT files where the data is stored and process the text. I remove all stop words and punctuation and split the words into an array. 

From here I count the number of times a word occurs in the list and create an occurrence list. I then take every word from this occurrence list and pass it into a function I made to create a standard trie which has the index of its location in the occurrence list, as outlined by Section 23.5.4. I also created a function that searches through the tries to find a word and returns the index of that search word in the occurrence list if it exists.

I also created a function to create 8 tries from each sampled webpage at once and stores their occurrence list in a list, and also stores its trie in a list so that they can be quickly accessed. Once this function opens the TXT files and forms the inverted index for each webpage, I can search through each webpage for whatever terms I wish. When searching, I split the search into each individual word and use a very simple ranking technique. I query the inverted index for the search word, and if it exists I get its occurrences and sums those up. The webpage with the highest sum, or the most occurrences of the search words, is ranked highest. I then output everything to a TXT file so it can be inspected.
