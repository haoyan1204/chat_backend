from zhipuai import ZhipuAI

# just use your ai key
client = ZhipuAI(api_key="")

class info:
    def __init__(self):
        self.content = content
        self.role = role
        self.tool_calls = tool_calls

def chat(question):
    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {"role": "user", "content": question},
        ],
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

if __name__ == '__main__':
    chat("what's you")