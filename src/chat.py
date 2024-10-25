import streamlit as st
import uuid
from streamlit_option_menu import option_menu


def initialize_session_state():
    if "conversations" not in st.session_state:
        st.session_state.conversations = {}
    if "current_conversation" not in st.session_state:
        st.session_state.current_conversation = None


def create_new_conversation():
    conversation_id = str(uuid.uuid4())
    st.session_state.conversations[conversation_id] = []
    st.session_state.current_conversation = conversation_id


def display_chat():
    st.header("Chat")


def display_resources():
    st.header("Upload Resources")
    uploaded_file = st.file_uploader(
        "Choose a file to upload", type=["csv", "txt", "pdf"]
    )
    if uploaded_file is not None:
        st.success(f"File {uploaded_file.name} uploaded successfully!")
        # Here you can add code to process the uploaded file


def display_tasks():
    st.header("Predefined Tasks")
    st.write("Coming soon...")
    task_options = ["Task 1", "Task 2", "Task 3"]
    selected_task = st.selectbox("Choose a task", task_options)
    if st.button("Execute Task"):
        st.info(f"Executing {selected_task}")
        # Here you can add code to execute the selected task


def display_thread():
    st.header("DataNova")

    if st.session_state.current_conversation is None:
        create_new_conversation()
    if st.session_state.get("switch_button", False):
        st.session_state["menu_option"] = (
            st.session_state.get("menu_option", 0) + 1
        ) % 3
        manual_select = st.session_state["menu_option"]
    else:
        manual_select = None

    selected4 = option_menu(
        None,
        ["Chat", "Resources", "Tasks"],
        icons=["chat", "cloud-upload", "list-task"],
        orientation="horizontal",
        manual_select=manual_select,
        key="menu_4",
    )

    if selected4 == "Chat":
        display_chat()
    elif selected4 == "Resources":
        display_resources()
    elif selected4 == "Tasks":
        display_tasks()


def display_store():
    st.header("Store")


def display_conversation_history():
    st.sidebar.title("DataNova")

    # New conversation button
    if st.sidebar.button("New Thread", key="new_thread"):
        create_new_conversation()
        st.rerun()

    st.sidebar.markdown("---")  # Add a separator

    # Display existing conversations
    for conv_id, messages in st.session_state.conversations.items():
        if messages:
            button_label = f"{messages[0]['content'][:20]}..."
        else:
            button_label = "New Thread"

        if st.sidebar.button(button_label, key=conv_id):
            st.session_state.current_conversation = conv_id
            st.rerun()


def main():
    st.set_page_config(page_title="DataNova", layout="wide")
    initialize_session_state()

    # Sidebar
    display_conversation_history()

    # Main content
    display_thread()


if __name__ == "__main__":
    main()
