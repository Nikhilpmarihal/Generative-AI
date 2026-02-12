from dotenv import load_dotenv
from datetime import date

from langchain_mistralai.chat_models import ChatMistralAI
from langchain.tools import tool
from langchain.messages import HumanMessage, AIMessage
# Load environment variables
load_dotenv()

# Define tool
@tool
def get_current_date():
    """Get the current date"""
    return str(date.today())

# Initialize model and bind tool
model = ChatMistralAI(
    model="mistral-small-latest"
).bind_tools([get_current_date])

# Invoke model
response = model.invoke(
    [HumanMessage(content="What is today's date?")]
)

# Handle tool call (if triggered)
if response.tool_calls:
    tool_call = response.tool_calls[0]
    tool_output = get_current_date.invoke(tool_call["args"])
    print(tool_output)
else:
    print(response.content)
