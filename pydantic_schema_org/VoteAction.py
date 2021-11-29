from pydantic import Field
from pydantic_schema_org.Person import Person
from typing import Any, Optional, Union, List
from pydantic_schema_org.ChooseAction import ChooseAction


class VoteAction(ChooseAction):
    """The act of expressing a preference from a fixed/finite/structured set of choices/options.

    See https://schema.org/VoteAction.

    """

    candidate: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A sub property of object. The candidate subject of this action.",
    )
    locals().update({"@type": Field("VoteAction", const=True)})


VoteAction.update_forward_refs()
