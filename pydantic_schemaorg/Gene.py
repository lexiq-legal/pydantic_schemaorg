from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.BioChemEntity import BioChemEntity
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem


class Gene(BioChemEntity):
    """A discrete unit of inheritance which affects one or more biological traits (Source:"
     "[https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene))."
     "Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific"
     "RNA 21), A- (agouti genotype).

    See https://schema.org/Gene.

    """
    type_: str = Field("Gene", const=True, alias='@type')
    hasBioPolymerSequence: Optional[Union[List[str], str]] = Field(
        None,
        description="A symbolic representation of a BioChemEnity. For example, a nucleotide sequence of"
     "a Gene or an amino acid sequence of a Protein.",
    )
    encodesBioChemEntity: Optional[Union[List[BioChemEntity], BioChemEntity]] = Field(
        None,
        description="Another BioChemEntity encoded by this one.",
    )
    alternativeOf: Any = Field(
        None,
        description="Another gene which is a variation of this one.",
    )
    expressedIn: Optional[Union[List[Union[AnatomicalStructure, DefinedTerm, BioChemEntity, AnatomicalSystem]], Union[AnatomicalStructure, DefinedTerm, BioChemEntity, AnatomicalSystem]]] = Field(
        None,
        description="Tissue, organ, biological sample, etc in which activity of this gene has been observed"
     "experimentally. For example brain, digestive system.",
    )
    

Gene.update_forward_refs()
