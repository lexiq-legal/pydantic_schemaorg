from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class EndorseAction(ReactAction):
    """An agent approves/certifies/likes/supports/sanction an object.

    See: https://schema.org/EndorseAction
    Model depth: 5
    """
    type_: str = Field("EndorseAction", alias='@type')
    endorsee: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="A sub property of participant. The person/organization being supported.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
