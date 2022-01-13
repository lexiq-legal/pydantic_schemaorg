from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreativeWork import CreativeWork


class Code(CreativeWork):
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet"
     "samples, scripts, templates.

    See: https://schema.org/Code
    Model depth: 3
    """

    type_: str = Field("Code", const=True, alias="@type")


if TYPE_CHECKING:

    Code.update_forward_refs()
