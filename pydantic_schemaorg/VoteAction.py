from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.ChooseAction import ChooseAction


class VoteAction(ChooseAction):
    """The act of expressing a preference from a fixed/finite/structured set of choices/options.

    See: https://schema.org/VoteAction
    Model depth: 5
    """
    type_: str = Field("VoteAction", alias='@type')
    candidate: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A sub property of object. The candidate subject of this action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
