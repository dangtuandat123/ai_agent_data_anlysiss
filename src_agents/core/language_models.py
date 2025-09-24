from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from logger import setup_logger

class LanguageModelManager:
    def __init__(self):
        """Initialize the language model manager"""
        self.logger = setup_logger()
        self.llm = None
        self.power_llm = None
        self.initialize_llms()

    def initialize_llms(self):
        """Initialize language models"""
        try:
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0.3,
                api_key=os.getenv("GOOGLE_API_KEY")
            )

            self.power_llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0.7,
                api_key=os.getenv("GOOGLE_API_KEY")
            )

            # JSON mode cho Gemini 1.5: ép phản hồi dạng JSON
           

            self.logger.info("Language models (Gemini) initialized successfully.")
        except Exception as e:
            self.logger.error(f"Error initializing Gemini models: {str(e)}")
            raise

    def get_models(self):
        """Return all initialized language models"""
        return {
            "llm": self.llm,
            "power_llm": self.power_llm,
        }
