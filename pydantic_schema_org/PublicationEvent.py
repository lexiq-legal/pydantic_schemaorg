from pydantic import StrictBool, Field
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.Event import Event


class PublicationEvent(Event):
    """A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork"
     "of any type e.g. a broadcast event, an on-demand event, a book/journal publication via"
     "a variety of delivery media.

    See https://schema.org/PublicationEvent.

    """

    publishedBy: Optional[Union[List[Union[Person, Organization]], Union[Person, Organization]]] = Field(
        None,
        description="An agent associated with the publication event.",
    )
    publishedOn: Any = Field(
        None,
        description="A broadcast service associated with the publication event.",
    )
    free: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    locals().update({"@type": Field("PublicationEvent", const=True)})


PublicationEvent.update_forward_refs()
