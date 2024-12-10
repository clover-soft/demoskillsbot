

from openai import OpenAI
client = OpenAI(api_key="")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Ты помошник, пишешь только по русски. Помоги пользователю."},
        {
            "role": "user",
            "content": "Как пользоваться chat GPT через telegram?"
        }
    ]
)

print(completion.choices[0].message)
