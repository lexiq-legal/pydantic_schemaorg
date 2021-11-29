from pydantic import Field, AnyUrl
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from typing import Any, Union, List, Optional
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Thing import Thing


class Taxon(Thing):
    """A set of organisms asserted to represent a natural cohesive biological unit.

    See https://schema.org/Taxon.

    """

    hasDefinedTerm: Optional[Union[List[DefinedTerm], DefinedTerm]] = Field(
        None,
        description="A Defined Term contained in this term set.",
    )
    childTaxon: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="Closest child taxa of the taxon in question.",
    )
    parentTaxon: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="Closest parent taxon of the taxon in question.",
    )
    taxonRank: Optional[Union[List[Union[AnyUrl, str, PropertyValue]], Union[AnyUrl, str, PropertyValue]]] = Field(
        None,
        description="The taxonomic rank of this taxon given preferably as a URI from a controlled vocabulary"
     "– (typically the ranks from TDWG TaxonRank ontology or equivalent Wikidata URIs).",
    )
    locals().update({"@type": Field("Taxon", const=True)})


Taxon.update_forward_refs()
