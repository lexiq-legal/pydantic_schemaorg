from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.BioChemEntity import BioChemEntity


class Protein(BioChemEntity):
    """Protein is here used in its widest possible definition, as classes of amino acid based"
     "molecules. Amyloid-beta Protein in human (UniProt P05067), eukaryota (e.g. an OrthoDB"
     "group) or even a single molecule that one can point to are all of type schema:Protein."
     "A protein can thus be a subclass of another protein, e.g. schema:Protein as a UniProt"
     "record can have multiple isoforms inside it which would also be schema:Protein. They"
     "can be imagined, synthetic, hypothetical or naturally occurring.

    See: https://schema.org/Protein
    Model depth: 3
    """
    type_: str = Field(default="Protein", alias='@type', const=True)
    hasBioPolymerSequence: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A symbolic representation of a BioChemEnity. For example, a nucleotide sequence of"
     "a Gene or an amino acid sequence of a Protein.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
