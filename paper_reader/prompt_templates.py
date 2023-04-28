"""Prompt Templates for GPT on paper reading tasks"""
from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
)
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)


# recognize section titles from texts in pdf
section_titles_identification = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "You are a helpful research assistant."
    ),
    HumanMessagePromptTemplate(prompt=PromptTemplate(
        input_variables=["list_of_texts"],
        template="You will be given several texts and your task is to "
        "identify which of them are section titles of a research paper. "
        "If a title includes a number, it must be retained. "
        "Your output should be in JSON format and include a list of the identified section titles. "
        "Your output format:\n\n"
        """{\n"titles": ["section title text", "section title text", ...]\n}\n\n"""
        "Here are the texts: {{ list_of_texts }}",
        template_format='jinja2'
    )),
])
# section_titles_identification.format_messages()
# section_titles_identification.format_prompt().to_messages()

section_summarization = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "You are a helpful research assistant. "
        "You help the user with paper reading, summarizing, and review."
    ),
    HumanMessagePromptTemplate(prompt=PromptTemplate(
        input_variables=['key_points', 'section_title', 'section_texts'],
        template="I will provide you with a reseach paper on a specific topic "
        "and you will create a summary of the whole paper part by part. "
        "Your summary should be concise and accurately reflect the content of "
        "the original paper. For each section, the summary should be no longer "
        "than 5 sentences. Your summary should focus on the following key "
        "points if the paper has mentioned relevant information about them:\n"
        "{{ key_points }}\n"
        "The contents of section {{ section_title }} are as follows.\n"
        "{{ section_texts }}",
        template_format='jinja2'
    )),
])
