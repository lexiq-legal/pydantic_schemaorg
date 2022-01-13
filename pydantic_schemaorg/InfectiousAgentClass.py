from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class InfectiousAgentClass(MedicalEnumeration):
    """Classes of agents or pathogens that transmit infectious diseases. Enumerated type.

    See: https://schema.org/InfectiousAgentClass
    Model depth: 5
    """

    type_: str = Field("InfectiousAgentClass", const=True, alias="@type")


if TYPE_CHECKING:

    InfectiousAgentClass.update_forward_refs()
