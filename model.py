from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel

def get_weather(city: str) -> str:  
    """Get weather for a given city."""  
    return f"It's always sunny in {city}!"

class WeatherResponse(BaseModel):
    conditions: str

model = init_chat_model(
    "gpt-4o-mini",
    temperature=0,
    model_provider="openai"
)

agent = create_react_agent(
    model=model,
    tools=[get_weather],
    prompt="You are a helpful assistant",
    response_format=WeatherResponse
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

# Print structured result
print(response["structured_response"].conditions)
