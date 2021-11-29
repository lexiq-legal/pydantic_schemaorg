from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase


class Thing(SchemaOrgBase):
    """The most generic type of item.

    See https://schema.org/Thing.

    """

    mainEntityOfPage: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="Indicates a page (or other CreativeWork) for which this thing is the main entity being"
     "described. See [background notes](/docs/datamodel.html#mainEntityBackground)"
     "for details.",
    )
    additionalType: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="An additional type for the item, typically used for adding more specific types from external"
     "vocabularies in microdata syntax. This is a relationship between something and a class"
     "that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof'"
     "attribute - for multiple types. Schema.org tools may have only weaker understanding"
     "of extra types, in particular those defined externally.",
    )
    url: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="URL of the item.",
    )
    alternateName: Optional[Union[List[str], str]] = Field(
        None,
        description="An alias for the item.",
    )
    sameAs: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the"
     "URL of the item's Wikipedia page, Wikidata entry, or official website.",
    )
    name: Optional[Union[List[str], str]] = Field(
        None,
        description="The name of the item.",
    )
    identifier: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="The identifier property represents any kind of identifier for any kind of [[Thing]],"
     "such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for"
     "representing many of these, either as textual strings or as URL (URI) links. See [background"
     "notes](/docs/datamodel.html#identifierBg) for more details.",
    )
    potentialAction: Any = Field(
        None,
        description="Indicates a potential Action, which describes an idealized action in which this thing"
     "would play an 'object' role.",
    )
    subjectOf: Any = Field(
        None,
        description="A CreativeWork or Event about this Thing.",
    )
    description: Optional[Union[List[str], str]] = Field(
        None,
        description="A description of the item.",
    )
    disambiguatingDescription: Optional[Union[List[str], str]] = Field(
        None,
        description="A sub property of description. A short description of the item used to disambiguate from"
     "other, similar items. Information from other properties (in particular, name) may"
     "be necessary for the description to be useful for disambiguation.",
    )
    image: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].",
    )
    locals().update({"@type": Field("Thing", const=True)})


Thing.update_forward_refs()
