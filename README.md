# plagiarism-check
Retrieving the top K least redundant blogs.

### Problem Statement:

Blogs are the richest source of information. However, much of the text information is redundant. Tech Mahindra takes up the job of designing a blog retrieval and summarization system where the goal is to retrieve the K least redundant blogs while returning the top-K search results. You are a software developer at Tech Mahindra. Your Team is assigned the task of designing the blog search tool. To find the top K results, the team leader decides to use the plagiarism score as a metric for evaluation.  You are being asked to design a prototype for this tool using basic text processing techniques like edit distance and n-gram model considering the processing speed. Write a program for designing the plagiarism check tool. 


### Solution:

#### Pre-Requisite Understandings:

As the problem statement asks to retrieve the K least redundant blogs, the following program will retrieve the 5 least redundant blogs, where K = 5.
The following statements are taken as a parameter and will further have their plagiarism scores calculated. These statements represent the “blogs” the problem statement is discussing. 

	paragraphs = ['The girl with a green umbrella.',
			  'Who are you and how are you doing?',
			  'This is a sample paragraph with some text.',
			  'This is another sample paragraph with some more text.',
			  'The girl using a pink umbrella.',
			  'She is walking the dog on the right lane.',
			  'The lazy lady is annoying me.',
			  'The girl is walking with a yellow umbrella.',
			  'This is yet another paragraph for testing the program',
			  'This is the final paragraph of the input']
	
Therefore, each paragraph within the “paragraphs” array is a blog.

#### Procedure:

Step 1: We start the program by importing the necessary tools in order for further execution of the code to be successful. Here, we import 3 modules: itertools, re, and Counter (from collections). 

	Itertools - retrieves all possible combinations of paragraphs from the blogs we input.
	Re - allows for easier data analysis by cleaning the data in terms of removing punctuation, whitespaces, and any other unnecessary characters.
	Counter - counts the frequency of n-grams in all paragraphs.

Step 2: Then, we define a function called a tokenizer, which takes “words” as its input parameter. This function utilizes the re module to remove whitespaces, capitalization, and punctuation of the text. 

Step 3: The program further defines a function called edit_dist, taking the input parameter of 2 strings - str1 and str2. This function implements the edit-distance algorithm which calculates the minimum number of operations required in order to change one string into another. We construct a 2-dimensional array here where rows = first string characters and columns = second string characters. Using the dynamic programming approach, we fill the rest of the cells in the matrix - each cell refers to the minimum number of operations needed to change the prefix/beginning of the first string into the prefix/beginning of the second string. 

As we iterate from the first cell, if 2 characters at the current cell are equal, the value of the cell is the same as the value of the cell to the left-most cell in the same row. However, if they are not equal, the value of the cell is the minimum of the values of the left, above, and upper-left cells + 1. 

The final edit distance is given by the value in the bottom right corner of the entire matrix. 

Step 4: We define a function called n_grams, which takes the input parameters as tokens and n. This function returns a list of n-grams. Working hand-in-hand with step 2, after the initial function removes all punctuation, whitespaces, and unnecessary characters, the n_grams function tokenizes the text and generates the total number of n-grams. It then joins all ngrams into a single string. 

Step 5: To calculate the plagiarism score, the program defines a function called plagiarism_score, taking a total of 4 input parameters - txt1, txt2, n, and k. In the function, we call the n_grams function initially in order to generate a list of n-grams for each text. We then use the Counter function to count the number of times each n-gram appears in that list. The intersection of the two sets is calculated.

For each ngram in that intersection, we find the minimum between both sets and add it our initial score of 0. We calculate the final plagiarism score by taking the score and dividing by the maximum length of the two n-gram lists. We then call the edit_dist function to calculate the edit distance between txt1 and txt2. 

Step 6: Using the main function, we pass in the paragraphs array that we will analyze the plagiarism scores of. Initially, we print the total comparisons of each blog to every other blog in the array and generate their scores along with their edit distances.

Step 7: The top K least redundant (least plagiarism scores) are returned. 









