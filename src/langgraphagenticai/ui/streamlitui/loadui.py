import streamlit as st
import os
from datetime import date


from langchain_core.messages import AIMessage, HumeanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamLitUI:
    def __init__(self):
        self.config = Config()  # config
        self.user_controls = {}
