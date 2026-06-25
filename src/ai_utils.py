from datetime import datetime


def ai_assistant():
    print("\n=== AI Utilities ===")

    question = input("Ask something: ")

    responses = {
        "hello": "Hello. Automation Hub is operational.",
        "time": f"Current time: {datetime.now()}",
        "version": "Automation Hub Version 8.0"
    }

    answer = responses.get(
        question.lower(),
        "No built-in answer available."
    )

    print(answer)
