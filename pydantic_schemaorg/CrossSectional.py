from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalObservationalStudyDesign import (
    MedicalObservationalStudyDesign,
)


class CrossSectional(MedicalObservationalStudyDesign):
    """Studies carried out on pre-existing data (usually from 'snapshot' surveys), such as"
     "that collected by the Census Bureau. Sometimes called Prevalence Studies.

    See: https://schema.org/CrossSectional
    Model depth: 6
    """

    type_: str = Field("CrossSectional", const=True, alias="@type")


if TYPE_CHECKING:

    CrossSectional.update_forward_refs()
