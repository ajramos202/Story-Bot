import os
import openai
#import backoff
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


#@backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.ServiceUnavailableError))

def bot(user_prompt) -> str:
    system_prompt = "You are an alien named Bill. You are very sarcastic and you have a tendency to be patronizing."
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
    print(bot("How do you feel about squirrels?"))
