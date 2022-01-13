from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class Preschool(EducationalOrganization):
    """A preschool.

    See: https://schema.org/Preschool
    Model depth: 4
    """

    type_: str = Field("Preschool", const=True, alias="@type")


if TYPE_CHECKING:

    Preschool.update_forward_refs()
