from pydantic import Field
from typing import List, Optional, Union
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.BioChemEntity import BioChemEntity


class ChemicalSubstance(BioChemEntity):
    """A chemical substance is 'a portion of matter of constant composition, composed of molecular"
     "entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).

    See https://schema.org/ChemicalSubstance.

    """
    type_: str = Field("ChemicalSubstance", const=True, alias='@type')
    chemicalComposition: Optional[Union[List[str], str]] = Field(
        None,
        description="The chemical composition describes the identity and relative ratio of the chemical"
     "elements that make up the substance.",
    )
    chemicalRole: Optional[Union[List[Union[DefinedTerm, str]], Union[DefinedTerm, str]]] = Field(
        None,
        description="A role played by the BioChemEntity within a chemical context.",
    )
    potentialUse: Optional[Union[List[Union[DefinedTerm, str]], Union[DefinedTerm, str]]] = Field(
        None,
        description="Intended use of the BioChemEntity by humans.",
    )
    

ChemicalSubstance.update_forward_refs()
