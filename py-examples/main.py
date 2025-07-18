from dotenv import load_dotenv
load_dotenv()  # pulls keys into os.environ

from e2b_code_interpreter import Sandbox
from groq import Groq
import os

e2b_api_key = os.environ.get("E2B_API_KEY")
groq_api_key = os.environ.get("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

LLM_MODEL = "llama-3.3-70b-versatile"
SYSTEM_PROMPT = """You are a Python data scientist. Generate simple code that:
1. Uses numpy to generate 5 random numbers
2. Prints only the mean and standard deviation in a clean format
Example output format:
Mean: 5.2
Std Dev: 1.8"""
USER_PROMPT = "Generate 20 random whole numbers between 1 and 100, print those numbers, and show their mean and standard deviation"


def main():
    # Create sandbox instance (by default, sandbox instances stay alive for 5 mins)
    sbx = Sandbox()

    # Get code from Groq
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT},
        ],
    )

    # Extract and run the code
    code = response.choices[0].message.content
    if "```python" in code:
        code = code.split("```python")[1].split("```")[0]

    print("System Prompt:")
    print(SYSTEM_PROMPT)
    print("\nUser Prompt:")
    print(USER_PROMPT)

    print(f"\nThe following is the Python code is generated by the model: [{LLM_MODEL}]\n")
    print(f"```python\n{code}\n```")

    print("\nExecuting code in sandbox...")
    execution = sbx.run_code(code)
    print(execution.logs.stdout[0])


if __name__ == "__main__":
    main()
