from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnByMail(ReturnMethodEnumeration):
    """Specifies that product returns must to be done by mail.

    See: https://schema.org/ReturnByMail
    Model depth: 5
    """

    type_: str = Field("ReturnByMail", const=True, alias="@type")


if TYPE_CHECKING:

    ReturnByMail.update_forward_refs()
