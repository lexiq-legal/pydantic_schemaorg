from pydantic import AnyUrl, Field
from pydantic_schemaorg.CreativeWork import CreativeWork
from typing import List, Optional, Union
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase


class Thing(SchemaOrgBase):
    """The most generic type of item.

    See https://schema.org/Thing.

    """
    type_: str = Field("Thing", const=True, alias='@type')
    mainEntityOfPage: Optional[Union[List[Union[AnyUrl, CreativeWork, str]], Union[AnyUrl, CreativeWork, str]]] = Field(
        None,
        description="Indicates a page (or other CreativeWork) for which this thing is the main entity being"
     "described. See [background notes](/docs/datamodel.html#mainEntityBackground)"
     "for details.",
    )
    additionalType: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="An additional type for the item, typically used for adding more specific types from external"
     "vocabularies in microdata syntax. This is a relationship between something and a class"
     "that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof'"
     "attribute - for multiple types. Schema.org tools may have only weaker understanding"
     "of extra types, in particular those defined externally.",
    )
    url: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="URL of the item.",
    )
    alternateName: Optional[Union[List[str], str]] = Field(
        None,
        description="An alias for the item.",
    )
    sameAs: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the"
     "URL of the item's Wikipedia page, Wikidata entry, or official website.",
    )
    name: Optional[Union[List[str], str]] = Field(
        None,
        description="The name of the item.",
    )
    identifier: Optional[Union[List[Union[AnyUrl, str, PropertyValue]], Union[AnyUrl, str, PropertyValue]]] = Field(
        None,
        description="The identifier property represents any kind of identifier for any kind of [[Thing]],"
     "such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for"
     "representing many of these, either as textual strings or as URL (URI) links. See [background"
     "notes](/docs/datamodel.html#identifierBg) for more details.",
    )
    potentialAction: Optional[Union[List[Union[Action, str]], Union[Action, str]]] = Field(
        None,
        description="Indicates a potential Action, which describes an idealized action in which this thing"
     "would play an 'object' role.",
    )
    subjectOf: Optional[Union[List[Union[CreativeWork, Event, str]], Union[CreativeWork, Event, str]]] = Field(
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
    image: Optional[Union[List[Union[AnyUrl, ImageObject, str]], Union[AnyUrl, ImageObject, str]]] = Field(
        None,
        description="An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].",
    )
    

Thing.update_forward_refs()
