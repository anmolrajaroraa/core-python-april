def1 = 'Machine learning is an application of artificial intelligence AI that provides systems the ability to automatically learn and improve from experience without being explicitly programmed Machine learning focuses on the development of computer programs that can access data and use it learn for themselves The ability to learn Machine learning is actively being used today perhaps in many more places than one would expect'
def2 = 'Machine Learning is the field of study that gives computers the capability to learn without being explicitly programmed ML is one of the most exciting technologies that one would have ever come across As it is evident from the name it gives the computer that which makes it more similar to humans The ability to learn Machine learning is actively being used today perhaps in many more places than one would expect'
# Jaccard's distance = ( intersection / union )  *  100
words1 = set(def1.split())
words2 = set(def2.split())
stopwords = {'is', 'an', 'of', 'that', 'the', 'to', 'and', 'from', 'on', 'the', 'of', 'that', 'can', 'and', 'it', 'for', 'is', 'the', 'of', 'that', 'the',
             'to', 'is', 'of', 'the', 'that', 'would', 'have', 'As', 'it', 'is', 'from', 'the', 'it', 'the', 'that', 'which', 'it', 'to', 'The', 'to', 'is', 'in', 'than'}
words1.difference_update(stopwords)
words2.difference_update(stopwords)
intersection = words1.intersection(words2)
union = words1.union(words2)
distance = (len(intersection) / len(union)) * 100
print(f"Similarity between thwo definitions is {distance}%")
