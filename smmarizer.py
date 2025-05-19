import re
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")

def summarize_section(text, model="llama-3.3-70b-versatile"):
    prompt = f"""You are a helpful and expert text summarizing assistant. given a markdown file's content summarize the content in it while retaining names headings and other crucial details. Since it is a markdown file the headings and subheadings are all indicated by a sequence of hash signs (#). 
    Whatever happens DO NOT TOUCH THE SOURCES AND REFERENCES.\n\ntext: {text}"""
    llm=ChatGroq(model="llama-3.3-70b-versatile")
    response = llm.invoke(prompt)
    return response.content

def split_markdown_by_heading(content):
    pattern = re.compile(r'(?=^#{1,6} )', re.MULTILINE)
    return pattern.split(content)

def summarize_markdown_file(file_path, chunk_model="gpt-3.5-turbo"):
    with open(file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    sections = split_markdown_by_heading(md_text)
    summarized_sections = []

    for idx, section in enumerate(sections):
        if section.strip():
            print(f"\n📍 Summarizing section {idx+1}/{len(sections)}...")
            summary = summarize_section(section.strip(), model=chunk_model)
            summarized_sections.append(f"### Summary of Section {idx+1}\n{summary}")

    full_summary = "\n\n".join(summarized_sections)

    with open("summary_output.md", "w", encoding="utf-8") as f:
        f.write(full_summary)

    print("\n✅ Summarization complete. Output saved to `summary_output.md`.")

summarize_markdown_file("output1.md")
