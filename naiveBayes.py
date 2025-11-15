from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample data (similar to your lab materials on spam/ham)
messages = ['Free credit card now!', 'Meeting tomorrow at 10 AM.', 
            'Win $1000 prize!', 'Call me back.', 'URGENT: Claim your free gift.']
labels = ['spam', 'ham', 'spam', 'ham', 'spam']

# Create a simple pipeline: Vectorizer -> Naive Bayes
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(messages, labels)

# Test a new message
new_message = ["Congratulations! You've won a FREE trip."]
prediction = model.predict(new_message)

print("\n--- Naïve Bayes Concept (Spam Filter) ---")
print(f"Test Message: '{new_message[0]}'")
print(f"Prediction: {prediction[0]}")

# Scenario Solution: Calculate Precision
TN = 180 # True Negatives (Correctly predicted Ham)
FP = 20  # False Positives (Actual Ham, Predicted Spam)
FN = 10  # False Negatives (Actual Spam, Predicted Ham)
TP = 90  # True Positives (Correctly predicted Spam)

# Precision is the accuracy of positive predictions (Spam in this case).
# Formula: Precision = TP / (TP + FP)

precision_spam = TP / (TP + FP)

print("\n--- Scenario Solution: Precision Calculation ---")
print(f"True Positives (TP): {TP}")
print(f"False Positives (FP): {FP}")
print(f"Spam Precision: {precision_spam:.4f} (or {precision_spam*100:.2f}%)")