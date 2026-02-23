"""Tool for searching simulated medical literature."""

from langchain_core.tools import tool

from src.data.medical_articles import search_articles


@tool
def search_medical_literature(query: str) -> str:
    """Search medical literature for articles matching the query.

    Use this to find clinical guidelines, treatment evidence, and medical
    research relevant to a patient's condition. Provide keywords like
    disease names, symptoms, or drug names.

    Args:
        query: Search terms (e.g. "diabetes metformin", "pneumonia treatment").
    """
    results = search_articles(query)
    if not results:
        return "No articles found matching the query."

    output_parts = []
    for article in results:
        output_parts.append(
            f"[{article['id']}] {article['title']} ({article['year']})\n"
            f"  {article['abstract']}\n"
        )
    return "\n".join(output_parts)
