import autogen

config_list = [
    {
        'api_type': 'open_ai',
        'api_base': 'http://localhost:195/v1/models',
        'api_key': 'NULL'
    }
]

llm_config = {
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="you are a coder specializing in python."
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get(
        "content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
Make a snake game, every time it eat a apple it grows, if the snake hit itself or the wall it will end the game.
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)

task2 = """
make the visuals look good, make nice ui and score board.
"""

user_proxy.initiate_chat(
    assistant,
    message=task2
)
