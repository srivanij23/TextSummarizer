import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK data (run once)
try:
    nltk.download('punkt')
    nltk.download('stopwords')
except:
    print("Error downloading NLTK data. Please check your internet connection.")

def summarize_article(article, num_sentences=2):
    """
    Summarizes a given article using extractive summarization.
    """
    sentences = sent_tokenize(article)
    if len(sentences) < num_sentences:
        return "Article is too short to summarize with the requested number of sentences."

    stop_words = set(stopwords.words('english'))
    words = [word_tokenize(sentence.lower()) for sentence in sentences]
    words = [[word for word in sentence if word not in stop_words and word.isalnum()] 
             for sentence in words]

    word_freq = {}
    for sentence_words in words:
        for word in sentence_words:
            word_freq[word] = word_freq.get(word, 0) + 1

    sentence_scores = {}
    for i, sentence_words in enumerate(words):
        if sentence_words:
            score = sum(word_freq[word] for word in sentence_words)
            sentence_scores[i] = score

    if not sentence_scores:
        return "Unable to summarize: No meaningful content found."
    
    top_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    top_indices.sort()
    summary = " ".join(sentences[i] for i in top_indices)

    return summary

# Process manually entered paragraph
if __name__ == "__main__":
    print("Please enter your paragraph (press Enter twice when finished):")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    paragraph = " ".join(lines)

    if not paragraph.strip():
        print("No text entered. Exiting.")
    else:
        print("\nYour entered paragraph:")
        print(paragraph)
        print("\nSummary:")
        summary = summarize_article(paragraph)
        print(summary)