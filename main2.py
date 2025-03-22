import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import random

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

# Load articles from file
def load_articles_from_file(filename="articles.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            articles = content.split('---')
            return [article.strip() for article in articles if article.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create the file with articles.")
        return []

# Process the dataset
if __name__ == "__main__":
    article_dataset = load_articles_from_file()
    if not article_dataset:
        print("No articles to process. Exiting.")
    else:
        print("Summarizing articles from the dataset...\n")
        
        # Option 2a: Summarize all articles
        for i, article in enumerate(article_dataset, 1):
            print(f"Article {i}:")
            print(article)
            print("\nSummary:")
            summary = summarize_article(article)
            print(summary)
            print("-" * 50)

        # Option 2b: Summarize a random article (uncomment to use instead)
        # chosen_article = random.choice(article_dataset)
        # print("Randomly Chosen Article:")
        # print(chosen_article)
        # print("\nSummary:")
        # summary = summarize_article(chosen_article)
        # print(summary)