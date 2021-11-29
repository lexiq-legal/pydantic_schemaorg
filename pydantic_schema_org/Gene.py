from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.BioChemEntity import BioChemEntity
from pydantic_schema_org.DefinedTerm import DefinedTerm
from pydantic_schema_org.AnatomicalSystem import AnatomicalSystem
from pydantic_schema_org.AnatomicalStructure import AnatomicalStructure


class Gene(BioChemEntity):
    """A discrete unit of inheritance which affects one or more biological traits (Source:"
     "[https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene))."
     "Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific"
     "RNA 21), A- (agouti genotype).

    See https://schema.org/Gene.

    """

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
    expressedIn: Optional[Union[List[Union[DefinedTerm, BioChemEntity, AnatomicalSystem, AnatomicalStructure]], Union[DefinedTerm, BioChemEntity, AnatomicalSystem, AnatomicalStructure]]] = Field(
        None,
        description="Tissue, organ, biological sample, etc in which activity of this gene has been observed"
     "experimentally. For example brain, digestive system.",
    )
    locals().update({"@type": Field("Gene", const=True)})


Gene.update_forward_refs()
