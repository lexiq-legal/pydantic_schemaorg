from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class SchoolDistrict(AdministrativeArea):
    """A School District is an administrative area for the administration of schools.

    See: https://schema.org/SchoolDistrict
    Model depth: 4
    """

    type_: str = Field("SchoolDistrict", const=True, alias="@type")


if TYPE_CHECKING:

    SchoolDistrict.update_forward_refs()
