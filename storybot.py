import os
import openai
# import backoff
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


# @backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.ServiceUnavailableError))

def bot(user_prompt) -> str:
    system_prompt = "You are a traveler of worlds and you love telling stories of your adventures."
    output, *_ = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
    ).choices

    return output.message.content


if __name__ == '__main__':
    print(bot("Tell me about the legend of Aria."))
