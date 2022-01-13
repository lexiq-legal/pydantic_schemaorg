from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreateAction import CreateAction


class FilmAction(CreateAction):
    """The act of capturing sound and moving images on film, video, or digitally.

    See: https://schema.org/FilmAction
    Model depth: 4
    """

    type_: str = Field("FilmAction", const=True, alias="@type")


if TYPE_CHECKING:

    FilmAction.update_forward_refs()
