from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Taxon(Thing):
    """A set of organisms asserted to represent a natural cohesive biological unit.

    See: https://schema.org/Taxon
    Model depth: 2
    """
    type_: str = Field("Taxon", alias='@type')
    hasDefinedTerm: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        None,
        description="A Defined Term contained in this term set.",
    )
    childTaxon: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Taxon']], AnyUrl, 'URL', str, 'Text', 'Taxon']] = Field(
        None,
        description="Closest child taxa of the taxon in question.",
    )
    parentTaxon: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Taxon']], AnyUrl, 'URL', str, 'Text', 'Taxon']] = Field(
        None,
        description="Closest parent taxon of the taxon in question.",
    )
    taxonRank: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'PropertyValue']], AnyUrl, 'URL', str, 'Text', 'PropertyValue']] = Field(
        None,
        description="The taxonomic rank of this taxon given preferably as a URI from a controlled vocabulary"
     "– (typically the ranks from TDWG TaxonRank ontology or equivalent Wikidata URIs).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
