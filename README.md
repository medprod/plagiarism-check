# plagiarism-check
Retrieving the top K least redundant blogs.

Problem Statement:

Blogs are the richest source of information. However, much of the text information is redundant. Tech Mahindra takes up the job of designing a blog retrieval and summarization system where the goal is to retrieve the K least redundant blogs while returning the top-K search results. You are a software developer at Tech Mahindra. Your Team is assigned the task of designing the blog search tool. To find the top K results, the team leader decides to use the plagiarism score as a metric for evaluation.  You are being asked to design a prototype for this tool using basic text processing techniques like edit distance and n-gram model considering the processing speed. Write a program for designing the plagiarism check tool. 


Solution:

Pre-Requisite Understandings:

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




