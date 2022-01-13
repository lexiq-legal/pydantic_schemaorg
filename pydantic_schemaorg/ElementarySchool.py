from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class ElementarySchool(EducationalOrganization):
    """An elementary school.

    See: https://schema.org/ElementarySchool
    Model depth: 4
    """

    type_: str = Field("ElementarySchool", const=True, alias="@type")


if TYPE_CHECKING:

    ElementarySchool.update_forward_refs()
