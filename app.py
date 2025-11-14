"""
Simple OpenAI Chat Agent
Running:
    python app.py
    or ensure that you are using pipenv env: 
    pipenv run python app.py
"""
import os
from openai import OpenAI
from dotenv import load_dotenv


def main():
    # Load  API key from .env file
    load_dotenv()
    
    # Initialize OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Validate API key exists
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it using: export OPENAI_API_KEY='your-api-key'")
        return
    
    # Create an instance of the OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Print instructions
    print("OpenAI Agent - Ask me anything! (Type 'quit' or 'exit' to stop)\n")
    
    # Main loop - runs until user exits
    while True:
        # Get user input
        question = input("You: ").strip()
    
        # If user types any of these, exit the loop
        if question.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        # Skip if user entered an empty string
        if not question:
            continue
        
        #  API call wrapped to handle errors
        try:
            # Call OpenAI API 
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    # "System" sets the behavior of the agent
                    {"role": "system", "content": "You are a helpful assistant that answers questions clearly and concisely."},
                    # "User" contains the user question
                    {"role": "user", "content": question}
                ],
                
                # Controls randomness/creativity of responses
                temperature=0.7,
                max_tokens=200
            )
            
            # Extract the agent's response 
            answer = response.choices[0].message.content
            # Display to the user
            print(f"\nAgent: {answer}\n")
            
        except Exception as e:
            print(f"Error: {e}\n")

# Run the main function
if __name__ == "__main__":
    main()