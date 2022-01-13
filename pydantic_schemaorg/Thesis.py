from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.CreativeWork import CreativeWork


class Thesis(CreativeWork):
    """A thesis or dissertation document submitted in support of candidature for an academic"
     "degree or professional qualification.

    See: https://schema.org/Thesis
    Model depth: 3
    """

    type_: str = Field("Thesis", const=True, alias="@type")
    inSupportOf: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Qualification, candidature, degree, application that Thesis supports.",
    )


if TYPE_CHECKING:

    Thesis.update_forward_refs()
