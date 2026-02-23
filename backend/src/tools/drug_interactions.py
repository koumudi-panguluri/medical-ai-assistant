"""Tools for drug lookup and interaction checking."""

from langchain_core.tools import tool

from src.data.drug_database import check_interactions, lookup_drug


@tool
def lookup_drug_info(drug_name: str) -> str:
    """Look up detailed information about a specific drug.

    Returns drug class, indications, side effects, and warnings.

    Args:
        drug_name: The name of the drug (e.g. "metformin", "lisinopril").
    """
    info = lookup_drug(drug_name)
    if info is None:
        return f"Drug '{drug_name}' not found in the database."

    return (
        f"Drug: {drug_name.title()}\n"
        f"Class: {info['class']}\n"
        f"Indications: {', '.join(info['indications'])}\n"
        f"Common Side Effects: {', '.join(info['common_side_effects'])}\n"
        f"Serious Warnings: {', '.join(info['serious_warnings'])}\n"
    )


@tool
def check_drug_interactions(drug_names: list[str]) -> str:
    """Check for known drug-drug interactions among a list of medications.

    Args:
        drug_names: List of drug names to check for interactions
                    (e.g. ["warfarin", "aspirin"]).
    """
    interactions = check_interactions(drug_names)
    if not interactions:
        return f"No known interactions found among: {', '.join(drug_names)}."

    output_parts = []
    for ix in interactions:
        output_parts.append(
            f"⚠ {ix['severity']} Interaction: {ix['drug_a'].title()} + {ix['drug_b'].title()}\n"
            f"  {ix['description']}\n"
        )
    return "\n".join(output_parts)
