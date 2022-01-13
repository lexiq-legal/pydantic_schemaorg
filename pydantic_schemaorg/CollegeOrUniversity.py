from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class CollegeOrUniversity(EducationalOrganization):
    """A college, university, or other third-level educational institution.

    See: https://schema.org/CollegeOrUniversity
    Model depth: 4
    """

    type_: str = Field("CollegeOrUniversity", const=True, alias="@type")


if TYPE_CHECKING:

    CollegeOrUniversity.update_forward_refs()
