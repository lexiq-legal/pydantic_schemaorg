from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union
from pydantic_schemaorg.CreativeWork import CreativeWork


class Quotation(CreativeWork):
    """A quotation. Often but not necessarily from some written work, attributable to a real"
     "world author and - if associated with a fictional character - to any fictional Person."
     "Use [[isBasedOn]] to link to source/origin. The [[recordedIn]] property can be used"
     "to reference a Quotation from an [[Event]].

    See https://schema.org/Quotation.

    """
    type_: str = Field("Quotation", const=True, alias='@type')
    spokenByCharacter: Optional[Union[List[Union[Organization, Person, str]], Union[Organization, Person, str]]] = Field(
        None,
        description="The (e.g. fictional) character, Person or Organization to whom the quotation is attributed"
     "within the containing CreativeWork.",
    )
    

Quotation.update_forward_refs()
