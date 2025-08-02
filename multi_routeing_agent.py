import os
from pathlib import Path
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
from agno.team import Team


env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)


API_KEY = os.getenv('OPENAI_API_KEY')
openai_client = OpenAIChat(api_key=API_KEY)


# --------------------------Tool 2: Tech Support Tool------------------------

class TechSupport:
    __name__ = 'TechSupport'

    def __call__(self, query: str) -> str: #type: ignore
        responses = {
            "app crash": "Please try reinstalling the app and update your OS.",
            "login issue": "Try resetting your password using the 'Forgot Password' link.",
            "freezing": "Clear the app cache and restart your device."
        }

        for item, response in responses.items():
            if item in query.lower():
                return response
        return 'thank you for reaching oout., pls be specific'
        


# --------------------------Tool 2: Sales Support Tool------------------------


class SalesSupport:
    __name__ = 'SalesSupport'

    def __call__(self, query: str) -> str:  # type: ignore
        responses = {
            "cost": "Our premium plan costs $49.99/month with 24/7 support.",
            "discount": "Yes! We are offering 20% off for new users this week.",
            "pricing": "We have Basic, Pro, and Premium plans starting at $9.99/month."
        }

        for keyword, response in responses.items():
            if keyword in query.lower():
                return response
        return 'thank you for reaching out, pls specify the type of prmotion/sale you are looking for?'


# --------------------------Tool 2: Sales Support Tool------------------------

class FaqEnquiry:
    __name__ = 'FaqEnquiry'

    def __call__(self, query: str) -> str:  # type: ignore
        responses = {
            "hours": "We are open from 9 AM to 6 PM, Monday to Friday.",
            "location": "Our headquarters are located in San Francisco, CA.",
            "contact": "You can contact us at support@example.com or call 1800-123-456."
        }

        for keyword, response in responses.items():
            if keyword in query.lower():
                return response

        return 'thank you for reaching out, pls specify your question if its other than time and location!'

# --------------------------Tool 2: Sales Support Tool------------------------


tech_support_agent = Agent(
    name='tech_support',
    model=openai_client,
    role='Address technical query from the enquirer!',
    tools=[TechSupport().__call__],
    instructions=[
        'Use the technical support tool to answer user queries. '
        'Keep responses helpful and simple. '
        'Provide them direct answer using the tool, do not ask further questions. '
        'Provide short answer in less than two lines.'
    ],
    show_tool_calls=True,
    markdown=True
)

sales_support_agent = Agent(
    name='sales_support',
    model=openai_client,
    role='Address sales query from the enquirer!',
    tools=[SalesSupport().__call__],
    instructions=[
        'Use the sales tool to answer pricing and discount-related questions. '
        'Provide them direct answer using the tool, do not ask further questions. '
        'Provide short answer in less than two lines.'
    ],
    show_tool_calls=True,
    markdown=True
)

faq_support_agent = Agent(
    name='faq_support',
    model=openai_client,
    role='Address general query from the enquirer!',
    tools=[FaqEnquiry().__call__],
    instructions=[
        'Use the general info tool to help with common inquiries.'
        'Provide them direct answer using the tool, do not ask further questions.'
        'Provide short answer in less than two lines.'
    ],
    show_tool_calls=True,
    markdown=True
)

ticket_operator = Team(
    name='customer_support_operator',
    members=[tech_support_agent, sales_support_agent, faq_support_agent],
    mode='route',
    model=openai_client,
    instructions=[
        'Route the query to the correct agent based on whether it’s technical, sales, or general.'],
    show_members_responses=True,
    show_tool_calls=True,
    markdown=True
)
ticket_operator.print_response('I am unable to login', stream=True)
