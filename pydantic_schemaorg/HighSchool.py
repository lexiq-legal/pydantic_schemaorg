from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class HighSchool(EducationalOrganization):
    """A high school.

    See: https://schema.org/HighSchool
    Model depth: 4
    """

    type_: str = Field("HighSchool", const=True, alias="@type")


if TYPE_CHECKING:

    HighSchool.update_forward_refs()
