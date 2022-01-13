from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GovernmentOffice import GovernmentOffice


class PostOffice(GovernmentOffice):
    """A post office.

    See: https://schema.org/PostOffice
    Model depth: 5
    """

    type_: str = Field("PostOffice", const=True, alias="@type")


if TYPE_CHECKING:

    PostOffice.update_forward_refs()
