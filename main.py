import langchain
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage

import streamlit as st
from dotenv import load_dotenv
from tools import GenerateProfileTool

langchain.debug = True

load_dotenv()


def get_agent(memory=None):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", streaming=True)

    agent_kwargs = {
        "system_message": SystemMessage(
            content="You are a talkative assistant. \
                Help the user fill in the content of the profile. \
                If there are items with unclear content, ask the user. \
                Once the profile content is filled in, generate the profile using `generate_profile` function."
        ),
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    }

    agent = initialize_agent(
        tools=[GenerateProfileTool()],
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs=agent_kwargs,
        memory=memory,
        verbose=True,
    )
    return agent


def get_memory():
    # get memory from session state if it exists
    memory = st.session_state.get("memory", None)

    # initialize memory if it doesn't exist
    if memory is None:
        memory = ConversationBufferMemory(memory_key="memory", return_messages=True)

    return memory


if __name__ == "__main__":
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "こんにちは！あなたのプロフィールの作成をお手伝いします．あなたのことを教えてください！"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        memory = get_memory()
        agent = get_agent(memory=memory)

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.empty())
            response = agent.run(prompt, callbacks=[st_cb])

            # save agent memory to session state
            st.session_state["memory"] = agent.memory

            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
