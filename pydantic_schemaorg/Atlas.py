from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreativeWork import CreativeWork


class Atlas(CreativeWork):
    """A collection or bound volume of maps, charts, plates or tables, physical or in media form"
     "illustrating any subject.

    See: https://schema.org/Atlas
    Model depth: 3
    """

    type_: str = Field("Atlas", const=True, alias="@type")


if TYPE_CHECKING:

    Atlas.update_forward_refs()
