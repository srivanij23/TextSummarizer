import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import random

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Dataset of articles (hardcoded)
article_dataset = [
    """
    The rapid advancement of technology has transformed industries worldwide. 
    From artificial intelligence to renewable energy, innovations are driving economic growth. 
    However, these changes also bring challenges, such as job displacement and ethical concerns. 
    Governments and companies must adapt to balance progress with social stability. 
    In 2024, AI adoption reached new heights, with applications in healthcare, education, and transportation. 
    Despite its benefits, experts warn of privacy issues and the need for regulation.
    """,
    """
    Climate change is one of the biggest threats facing humanity today. 
    Rising global temperatures are causing extreme weather events, such as hurricanes and droughts. 
    Scientists urge immediate action to reduce carbon emissions and transition to sustainable energy. 
    In 2023, international agreements aimed to limit warming to 1.5°C, but progress has been slow. 
    Communities worldwide are already adapting to rising sea levels and shifting ecosystems.
    """,
    """
    Space exploration has entered a new era with private companies leading the charge. 
    Firms like SpaceX and Blue Origin are developing reusable rockets to lower costs. 
    In 2025, NASA plans to return humans to the moon as a stepping stone to Mars. 
    These missions could unlock new scientific discoveries and inspire future generations. 
    However, critics argue that funds should focus on Earth’s immediate problems instead.
    """
]

def summarize_article(article, num_sentences=2):
    """
    Summarizes a given article using extractive summarization.
    """
    try:
        sentences = sent_tokenize(article)
    except Exception as e:
        return f"Error in tokenizing sentences: {e}"

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

# Process the dataset
if __name__ == "__main__":
    print("Summarizing articles from the dataset...\n")
    
    for i, article in enumerate(article_dataset, 1):
        print(f"Article {i}:")
        print(article.strip())
        print("\nSummary:")
        summary = summarize_article(article)
        print(summary)
        print("-" * 50)
