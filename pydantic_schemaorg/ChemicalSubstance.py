from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.BioChemEntity import BioChemEntity


class ChemicalSubstance(BioChemEntity):
    """A chemical substance is 'a portion of matter of constant composition, composed of molecular"
     "entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).

    See: https://schema.org/ChemicalSubstance
    Model depth: 3
    """
    type_: str = Field("ChemicalSubstance", alias='@type')
    chemicalComposition: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The chemical composition describes the identity and relative ratio of the chemical"
     "elements that make up the substance.",
    )
    chemicalRole: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        None,
        description="A role played by the BioChemEntity within a chemical context.",
    )
    potentialUse: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        None,
        description="Intended use of the BioChemEntity by humans.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
