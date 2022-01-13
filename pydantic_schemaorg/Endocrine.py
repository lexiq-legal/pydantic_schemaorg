from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Endocrine(MedicalSpecialty):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders"
     "of endocrine glands and their secretions.

    See: https://schema.org/Endocrine
    Model depth: 6
    """

    type_: str = Field("Endocrine", const=True, alias="@type")


if TYPE_CHECKING:

    Endocrine.update_forward_refs()
