import metapy

def tokens_lowercase(doc):
    #Write a token stream that tokenizes with ICUTokenizer (use the argument "suppress_tags=True"), 
    #lowercases, removes words with less than 2 and more than 5  characters. 
    #performs stemming and creates trigrams (name the final call to ana.analyze as "trigrams")
    #Write a token stream that tokenizes with ICUTokenizer (use the argument "suppress_tags=True"),
    tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
    #lowercases, removes words with less than 2 and more than 5  characters
    lowercase_filter = metapy.analyzers.LowercaseFilter(tok)
    length_filter = metapy.analyzers.LengthFilter(lowercase_filter, min=2, max=5)
    #performs stemming and creates trigrams (name the final call to ana.analyze as "trigrams")
    stemmer = metapy.analyzers.Porter2Filter(length_filter)
    trigram = metapy.analyzers.NGramWordAnalyzer(3, stemmer)
    trigrams = trigram.analyze(doc)
    
    #leave the rest of the code as is
    tok.set_content(doc.content())
    tokens, counts = [], []
    for token, count in trigrams.items():
        counts.append(count)
        tokens.append(token)
    return tokens
    
if __name__ == '__main__':
    doc = metapy.index.Document()
    doc.content("I said that I can't believe that it only costs $19.95! I could only find it for more than $30 before.")
    print(doc.content()) #you can access the document string with .content()
    tokens = tokens_lowercase(doc)
    print(tokens)
