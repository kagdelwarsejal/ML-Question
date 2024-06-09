import spacy
from collections import defaultdict
import matplotlib.pyplot as plt

# Load NLP model
nlp = spacy.load('en_core_web_sm')

# Extract events
def extract_events(articles):
    events = defaultdict(list)
    for article in articles:
        doc = nlp(article)
        for ent in doc.ents:
            if ent.label_ == 'DATE':
                date = ent.text
                events[date].append(article)
    return events

events = extract_events(war_articles)

# Create timeline list
timeline = []
for date, articles in sorted(events.items()):
    summary = " ".join(articles[:1])  # Simple summarization for example
    timeline.append((date, summary))

# Print the timeline
for date, event in timeline:
    print(f"{date}: {event}")

# Optionally, create a visual plot
dates = [item[0] for item in timeline]
summaries = [item[1] for item in timeline]

plt.figure(figsize=(10, 5))
plt.plot(dates, range(len(dates)), marker='o')
plt.yticks(range(len(dates)), summaries)
plt.xlabel('Date')
plt.ylabel('Events')
plt.title('Timeline of Israel-Hamas War')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
