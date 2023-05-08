import itertools
import re
from collections import Counter
from operator import itemgetter

def tokenizer(words):
    words = re.sub(r'[^\w\s]', '', words)
    words = words.lower()
    tokens = words.split()
    return tokens

def edit_dist(str1, str2):
    m = len(str1)+1
    n = len(str2)+1
    ed = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                ed[i][j] = j
            elif j == 0:
                ed[i][j] = i
            elif str1[i-1] == str2[j-1]:
                ed[i][j] = ed[i-1][j-1]
            else:
                ed[i][j] = min(ed[i][j-1], ed[i-1][j], ed[i-1][j-1]) + 1
    return ed[m][n]

def n_grams(tokens, n):
    total = []
    for i in range(len(tokens)-n+1):
        ngram = ' '.join(tokens[i:i+n])
        total.append(ngram)
        
    return total

def plagiarism_score(txt1, txt2, n, k):
    
    ng1 = n_grams(txt1, n)
    ng2 = n_grams(txt2, n)
   
    ngcount1 = Counter(ng1)
    ngcount2 = Counter(ng2)

    ngset1 = set(ngcount1.keys())
    ngset2 = set(ngcount2.keys())
    
    intersect = ngset2 & ngset2
    score = 0
    
    for ngram in intersect:
        mini= min(ngcount1[ngram], ngcount2[ngram])
        score += mini
        
    maxi = max(len(ng1), len(ng2))
    score = score/maxi
    
    edit_distance = edit_dist(txt1, txt2)
    return (score, edit_distance)

if __name__ == '__main__':
    paragraphs = ['The girl with a green umbrella.',
                  'Who are you and how are you doing?',
                  'Here is a sample blog with a little bit of text.',
                  'Here is another sample blog with some more text.',
                  'The girl using a pink umbrella.',
                  'She is walking the dog on the right lane.',
                  'The lady next door is annoying me.',
                  'The girl is walking with a yellow umbrella.',
                  'This is yet another blog for understanding the program.',
                  'This is the final blog of this input.']
    n = 3
    k = 5
    res = []
    
    for i, (para1, para2) in enumerate(itertools.combinations(paragraphs, 2)):
        score, edit_distance = plagiarism_score(para1, para2, n, k)
        res.append((i+1, score, edit_distance, para1, para2))
    
    res.sort(key=lambda x: x[1])
   
    for i, score, edit_distance, para1, para1 in res:
        print(f'{i}: plagiarism score={score:.5f}, \nedit distance={edit_distance},\ntext1="{para1}", \ntext2="{para2}"\n')

def each_score(p1, p2, ngram=3):
    
    t1 = [p1[i:i+ngram] for i in range(len(p1)-ngram+1)]
    t2 = [p2[i:i+ngram] for i in range(len(p2)-ngram+1)]
    
    intersect = set(t1) & set(t2)
    score = len(intersect) / (len(set(t1)) + len(set(t2)))
    return score

scores = []
for i, p1 in enumerate(paragraphs):
    total_score = 0
    for j, p2 in enumerate(paragraphs):
        if i != j:
            score = each_score(p1, p2)
            total_score += score
    scores.append((p1, total_score))
    
ascending = sorted(scores, key=itemgetter(1))

for paragraph in ascending:
    print(paragraph[0], paragraph[1])

print("\n")
for i in range(5):
    paragraph = ascending[i]
    print(paragraph[0])

