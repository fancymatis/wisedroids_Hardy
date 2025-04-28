import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    st.title("Test Deployment Application")
    
    # Sidebar for API key input
    st.sidebar.title("Authentication")
    api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
    
    if st.sidebar.button("Set API Key"):
        if api_key:
            # Set the API key as an environment variable for the current session
            os.environ["OPENAI_API_KEY"] = api_key
            st.sidebar.success("API key set successfully!")
        else:
            st.sidebar.error("Please enter an API key.")
    
    # Check if API key is set
    if "OPENAI_API_KEY" in os.environ and os.environ["OPENAI_API_KEY"]:
        # Main application content
        st.write("Welcome to the application!")
        st.write("This is a test deployment.")
        
        # Display the original code functionality
        if st.button("Run Test"):
            try:
                st.success("Test deployment successful!")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        # Instructions for users who haven't set an API key
        st.info("""
        ## Welcome to the Test Deployment Application
        
        To use this application, please:
        1. Enter your OpenAI API key in the sidebar
        2. Click 'Set API Key'
        3. Your API key will only be used for the current session and won't be stored
        
        If you don't have an OpenAI API key, you can get one at: https://platform.openai.com/api-keys
        """)

if __name__ == "__main__":
    main()
