import string
import re
import nltk
from collections import defaultdict
from nltk.tokenize import RegexpTokenizer
import pathlib
# Make a list from stopwords_en.txt
file_p = open("./stopwords_en.txt",'r')
ls = []
with file_p:
    for line in file_p:
        ls.append(line.strip('\n'))
# Normalize the file by reading it and removing the spl character and frming a dictionary
def normalize(addr, k):
    file_pointer = open(addr, 'r')
    content = defaultdict(int)
    p = ""
    st = ""
    with file_pointer:
        for line in file_pointer:
            line = line.strip('\n').lower()
            line = re.sub(r"(^|\W)\d+", "", line)
            tokenizer = RegexpTokenizer(r'\w+')
            s = tokenizer.tokenize(line)
            for item in s:
                if item not in ls and item not in [i for i in 'qwertyuoplkjhgfdsazxcvbnm']:
                    
                    p =item.strip()
                    st += p + ' '
                    content[p] +=1
    # Write the file with most frequent words
    pathlib.Path(k).write_text(st)
    return content
# Main function to control the flow of the code
if __name__ == '__main__':
    file1 = "./con_ marijuana_raw.txt"
    file2 = "./pro_ marijuana_raw.txt"
    f1=normalize(file1,"file1.txt")
    f2=normalize(file2, "file2.txt")
    for _ in range(5):
        print(f" con--->{max(f1, key=f1.get)}")
        print(f" pros--->{max(f2, key=f2.get)}")
        del f1[max(f1, key=f1.get)]
        del f2[max(f2, key=f2.get)]
    str1 =  " ".join([i for i in f1.keys()])
    str2 = " ".join([i for i in f2.keys()])
    pathlib.Path("cons.txt").write_text(str1)
    pathlib.Path("pros.txt").write_text(str2)
    ls1 = list(nltk.bigrams([i for i in str1.split()]))
    ls2 = list(nltk.bigrams([i for i in str2.split()]))
    s1=""
    s2=""
    for i in ls1:
        s1 += str(i)+'\n' 
    for i in ls1:
        s2 += str(i)+'\n' 
    print(f"Bigram for Pros: {s1}")
    print(f"Bigram for Cons: {s2}")
    pathlib.Path("consbigram.txt").write_text(s1)
    pathlib.Path("prosbigram.txt").write_text(s2)

            