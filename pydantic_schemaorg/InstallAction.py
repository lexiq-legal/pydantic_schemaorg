from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ConsumeAction import ConsumeAction


class InstallAction(ConsumeAction):
    """The act of installing an application.

    See: https://schema.org/InstallAction
    Model depth: 4
    """

    type_: str = Field("InstallAction", const=True, alias="@type")


if TYPE_CHECKING:

    InstallAction.update_forward_refs()
