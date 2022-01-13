from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class MeasurementTypeEnumeration(Enumeration):
    """Enumeration of common measurement types (or dimensions), for example \"chest\" for"
     "a person, \"inseam\" for pants, \"gauge\" for screws, or \"wheel\" for bicycles.

    See: https://schema.org/MeasurementTypeEnumeration
    Model depth: 4
    """

    type_: str = Field("MeasurementTypeEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    MeasurementTypeEnumeration.update_forward_refs()
