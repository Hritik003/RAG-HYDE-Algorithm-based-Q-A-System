from HyDE_Implementation import create_chat_completion
from HyDE_Implementation import final_prompt

def Final_Answer_generator(history, final_prompt):
    # Predefined system message
    system_message = (
        "Consider the prompts and data provided as a comprehensive resource to craft an accurate response. Feel free to extract relevant details or modify the prompts for clarity." 
    )

    history.append({"role": "system", "content": system_message})
    history.append({"role": "user", "content": final_prompt})

    completion = create_chat_completion(history)
    new_message = {"role": "assistant", "content": ""}

    for chunk in completion:
        if 'content' in chunk.choices[0].delta:
            new_message["content"] += chunk.choices[0].delta.content

    if new_message["content"]:
        history.append(new_message)

    return new_message["content"]

# Example usage:
history = []  # Initialize history as an empty list
Final_Output = Final_Answer_generator(history, final_prompt)
print(Final_Output)