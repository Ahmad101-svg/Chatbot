import openai

# Set the API key
openai.api_key = "your-api-key"

# List of keywords to filter mental health topics
MENTAL_HEALTH_KEYWORDS = [
    "anxiety", "depression", "stress", "therapy", "mental health",
    "well-being", "mindfulness", "burnout", "self-care", "panic attacks",
    "coping", "psychology", "mental illness", "emotional support"
]

def is_mental_health_topic(user_input):
    # Check if any mental health keyword is in the user's input
    return any(keyword in user_input.lower() for keyword in MENTAL_HEALTH_KEYWORDS)

def chat_gpt(prompt):
    try:
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        if is_mental_health_topic(user_input):
            response = chat_gpt(user_input)
            print("MentalHealthBot: ", response)
        else:
            print("MentalHealthBot: I can only discuss mental health-related topics. Please ask a relevant question.")