from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.BioChemEntity import BioChemEntity


class ChemicalSubstance(BioChemEntity):
    """A chemical substance is 'a portion of matter of constant composition, composed of molecular"
     "entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).

    See: https://schema.org/ChemicalSubstance
    Model depth: 3
    """

    type_: str = Field("ChemicalSubstance", const=True, alias="@type")
    chemicalComposition: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The chemical composition describes the identity and relative ratio of the chemical"
        "elements that make up the substance.",
    )
    chemicalRole: "Optional[Union[List[Union[DefinedTerm, str]], Union[DefinedTerm, str]]]" = Field(
        None,
        description="A role played by the BioChemEntity within a chemical context.",
    )
    potentialUse: "Optional[Union[List[Union[DefinedTerm, str]], Union[DefinedTerm, str]]]" = Field(
        None,
        description="Intended use of the BioChemEntity by humans.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.DefinedTerm import DefinedTerm

    ChemicalSubstance.update_forward_refs()
