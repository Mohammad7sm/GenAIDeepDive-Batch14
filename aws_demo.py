from langchain_aws import ChatBedrockConverse

from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatBedrockConverse(
    model="amazon.nova-micro-v1:0",
)

response = llm.invoke('What is Generative AI ? explain to 10 years old kid' )

print(response.content)