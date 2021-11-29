from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Intangible import Intangible


class Audience(Intangible):
    """Intended audience for an item, i.e. the group for whom the item was created.

    See https://schema.org/Audience.

    """

    audienceType: Optional[Union[List[str], str]] = Field(
        None,
        description="The target group associated with a given audience (e.g. veterans, car owners, musicians,"
     "etc.).",
    )
    geographicArea: Any = Field(
        None,
        description="The geographic area associated with the audience.",
    )
    locals().update({"@type": Field("Audience", const=True)})


Audience.update_forward_refs()
