from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class School(EducationalOrganization):
    """A school.

    See: https://schema.org/School
    Model depth: 4
    """

    type_: str = Field("School", const=True, alias="@type")


if TYPE_CHECKING:

    School.update_forward_refs()
