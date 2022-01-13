from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.MedicalCondition import MedicalCondition


class InfectiousDisease(MedicalCondition):
    """An infectious disease is a clinically evident human disease resulting from the presence"
     "of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi,"
     "protozoa, multicellular parasites, and prions. To be considered an infectious disease,"
     "such pathogens are known to be able to cause this disease.

    See: https://schema.org/InfectiousDisease
    Model depth: 4
    """

    type_: str = Field("InfectiousDisease", const=True, alias="@type")
    transmissionMethod: "Optional[Union[List[str], str]]" = Field(
        None,
        description="How the disease spreads, either as a route or vector, for example 'direct contact', 'Aedes"
        "aegypti', etc.",
    )
    infectiousAgent: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The actual infectious agent, such as a specific bacterium.",
    )
    infectiousAgentClass: "Optional[Union[List[Union[InfectiousAgentClass, str]], Union[InfectiousAgentClass, str]]]" = Field(
        None,
        description="The class of infectious agent (bacteria, prion, etc.) that causes the disease.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass

    InfectiousDisease.update_forward_refs()
