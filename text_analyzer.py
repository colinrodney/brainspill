# Text Analyzer


"""
Write a program that determines how many times a word
appears within a text:

06/20/2019: Create class Analyze_Text:
> create 2 objects: 'word' and 'word_count'

"""
def Text():
    """Simple text analysis program"""
    def __init__(self, filename, *args):
        self. word = word
        self. word_count = word_count
        
        
    def count_words(filename, word):
    """ Reads text and returns number of times the word is found in the text"""
    
    with open(filename) as f_object: # open file in read-only mode
        file_contents = f_object.read() # read entire text file

    for word in args:
        substring = word
        if substring in file_contents:
            word_count = file_contents.count(substring)
            return( "The word {} appears in this text {} times.".format(substring,word_count))
        #elif word not in contents:

filename = 'chapter10.txt'
#result = analyze_text(filename, 'error', 'Python', 'the', 'and')
        






        
    
