from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalContraindication(MedicalEntity):
    """A condition or factor that serves as a reason to withhold a certain medical therapy. Contraindications"
     "can be absolute (there are no reasonable circumstances for undertaking a course of action)"
     "or relative (the patient is at higher risk of complications, but that these risks may"
     "be outweighed by other considerations or mitigated by other measures).

    See: https://schema.org/MedicalContraindication
    Model depth: 3
    """

    type_: str = Field("MedicalContraindication", const=True, alias="@type")


if TYPE_CHECKING:

    MedicalContraindication.update_forward_refs()
