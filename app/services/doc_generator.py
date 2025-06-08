from app.core.openai_client import ask_openai
from app.models.schema import RepoDocResponse, RepoRequest


def generate_documentation(payload: RepoRequest) -> RepoDocResponse:
    summary_map = {}
    stack = set()

    for file in payload.structure:
        if file.type == "file" and len(file.content.strip()) < 5000:
            prompt = f"Explain this file:\n\n{file.content[:4000]}"
            summary = ask_openai(prompt)
            summary_map[file.path] = summary

            if "express" in file.content:
                stack.add("Express.js")
            if "react" in file.content:
                stack.add("React")
            if "mongoose" in file.content:
                stack.add("MongoDB")

    readme_prompt = f"Generate a README for a project called {payload.repo_name} with this structure: {list(summary_map.keys())}"
    readme = ask_openai(readme_prompt)

    return RepoDocResponse(readme=readme, stack=list(stack), summaries=summary_map)
