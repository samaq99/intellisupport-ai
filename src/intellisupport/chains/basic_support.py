"""
   Basic Support Chain for IntelliSupport AI.
   This is our first LangChain component that will:
   1. Take customer emails as input
   2. Generate professional responses
   3. Maintain TechSolutions GmbH brand voice
   Why we're building this:
   - Learn LangChain fundamentals
   - Create reusable component
   - Solve real business problem
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough                                                                                                                  
# Our configuration
from intellisupport.config import Config

class BasicSupportChain:
    """Basic customer support chain for initial email responses"""
    def __init__(self):
        """
            Initialize the chain.

            This is where we:
            1. Set up the LLM (OpenRouter)                                                                                                                                             2. Create the prompt template
            3. Build the chain structure
        """
        self.llm = ChatOpenAI(
            model=Config.OPENAI_MODEL,          # Which model to use
            temperature=Config.OPENAI_TEMPERATURE,  # Creativity level (0.1 = consistent)
            api_key=Config.OPENAI_API_KEY,      # Your OpenRouter key
            base_url=Config.OPENAI_API_BASE,    # OpenRouter endpoint
            max_tokens=Config.MAX_RESPONSE_TOKENS  # Limit response length
            )
        print(f"[INFO] LLM initialized with model: {Config.OPENAI_MODEL}")
        
        self.prompt = ChatPromptTemplate.from_messages ([
            ("system", """You are IntelliSupport AI, a customer support agent for TechSolutions GmbH.
             Company Context:
             - German SaaS company
             - Project management software
             - B2B customers in Europe.Your Guidelines:
             1. Be professional but friendly
             2. Respond in customer's language
             3. Ask for details when needed
             4. Don't make false promises
             5. Always end with: "Is there anything els I can help you with?"                                                                                                               """),
             ("human", "Customer Email:\n{email_body}")
             ])
        self.chain = (
            {"email_body": RunnablePassthrough()}  # Pass input through
            | self.prompt                          # Apply prompt template
            | self.llm                             # Send to LLM
            | StrOutputParser()                    # Get text output
            )
        print("[INFO] Chain built successfully")
        
    def respond(self, email_body:str)->str:
        """
        Generate a response for a customer email.
        Args:
        email_body: The customer's email content
        Returns:
            Generated response
            Example:
                >>> chain = BasicSupportChain()
                >>> response = chain.respond("I can't login")
                """
        try:
            response = self.chain.invoke(email_body)
            signature = "\n\n --- IntelliSupport AI\nTechSolutions GmbH \n"
            return response+signature
        except Exception as e:
            error_msg = "I appoligized, but I am having technical difficulties"
            print(f"[ERROR] Chain failed: {e}")
            return error_msg