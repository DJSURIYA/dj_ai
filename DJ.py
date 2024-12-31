import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyChU5QfdHAhXb9ZkDmZ-YQ18Kpr3d81ZXI")

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Function to handle input and generate response
def generate_response():
    user_input = st.session_state.user_input  # Get the input
    if user_input:
        try:
            # Initialize the Generative Model
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)

            # Append the query and response to the history
            st.session_state.history.append({"query": user_input, "response": response.text})

            # Clear the input box
            st.session_state.user_input = ""  # Reset input field
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Custom CSS to fix the input box and make the chat scrollable
st.markdown("""
    <style>
        /* Make the chat container scrollable */
        .chat-container {
            max-height: 500px;  /* Set max height for chat */
            overflow-y: scroll; /* Enable vertical scrolling */
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        /* Make the input box fixed at the bottom */
        .input-container {
            position: fixed;
            bottom: 20px;
            width: calc(100% - 40px);
            left: 20px;
            background-color: white;
            padding: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            border-radius: 8px;
        }

        /* Scrollbar styling */
        .chat-container::-webkit-scrollbar {
            width: 6px;
        }
        
        .chat-container::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 6px;
        }
        .chat-container::-webkit-scrollbar-thumb:hover {
            background: #555;
        }

        /* Title styling */
        .ai-name {
            font-size: 24px;
            font-weight: bold;
            color: #4B9CD3;  /* Customize with your preferred color */
            margin-bottom: 10px;
            padding-top: 20px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Main content container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# AI Name at the top
st.markdown('<div class="ai-name">Djsuriya</div>', unsafe_allow_html=True)

# Chat container (scrollable messages)
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for item in st.session_state.history:
    st.write(f"**You:** {item['query']}")
    st.write(f"**AI:** {item['response']}")
st.markdown('</div>', unsafe_allow_html=True)

# Input box fixed at the bottom
st.markdown('<div class="input-container">', unsafe_allow_html=True)
st.text_input(
    "Your Query:",
    placeholder="Type your question and press Enter...",
    key="user_input",
    on_change=generate_response,  # Triggered when the user presses Enter
    label_visibility="collapsed",  # Hides the label for a clean interface
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
