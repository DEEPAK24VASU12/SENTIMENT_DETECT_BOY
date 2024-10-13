import openai
import streamlit as st

# Set your API key
openai.api_key = st.secrets["KEY"]
def analyze_sentiment(review, category):
    prompt = f"Analyze the sentiment of the following {category} review and classify it as Positive, Negative, or Neutral:\n\nReview: {review}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a sentiment analysis assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    # Extract the sentiment analysis from GPT's response
    sentiment = response['choices'][0]['message']['content']
    return sentiment.strip()

def main():
    st.title("Sentiment Analysis Tool")

    # Get input from user using Streamlit input fields
    category = st.text_input("Enter the category of the review (e.g., Food, Product, Place, Other):")
    review = st.text_area(f"Enter your {category} review:")

    if st.button("Analyze Sentiment"):
        if review:
            sentiment = analyze_sentiment(review, category)
            st.write(f"**Sentiment Analysis Result:** {sentiment}")
        else:
            st.error("Please enter a valid review.")

if __name__ == "__main__":
    main()
