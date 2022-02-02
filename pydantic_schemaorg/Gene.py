from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.BioChemEntity import BioChemEntity


class Gene(BioChemEntity):
    """A discrete unit of inheritance which affects one or more biological traits (Source:"
     "[https://en.wikipedia.org/wiki/Gene](https://en.wikipedia.org/wiki/Gene))."
     "Examples include FOXP2 (Forkhead box protein P2), SCARNA21 (small Cajal body-specific"
     "RNA 21), A- (agouti genotype).

    See: https://schema.org/Gene
    Model depth: 3
    """
    type_: str = Field("Gene", alias='@type')
    hasBioPolymerSequence: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A symbolic representation of a BioChemEnity. For example, a nucleotide sequence of"
     "a Gene or an amino acid sequence of a Protein.",
    )
    encodesBioChemEntity: Optional[Union[List[Union['BioChemEntity', str]], 'BioChemEntity', str]] = Field(
        None,
        description="Another BioChemEntity encoded by this one.",
    )
    alternativeOf: Optional[Union[List[Union['Gene', str]], 'Gene', str]] = Field(
        None,
        description="Another gene which is a variation of this one.",
    )
    expressedIn: Optional[Union[List[Union['AnatomicalStructure', 'AnatomicalSystem', 'BioChemEntity', 'DefinedTerm', str]], 'AnatomicalStructure', 'AnatomicalSystem', 'BioChemEntity', 'DefinedTerm', str]] = Field(
        None,
        description="Tissue, organ, biological sample, etc in which activity of this gene has been observed"
     "experimentally. For example brain, digestive system.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BioChemEntity import BioChemEntity
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
