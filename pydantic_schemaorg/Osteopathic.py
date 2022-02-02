from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicineSystem import MedicineSystem


class Osteopathic(MedicineSystem):
    """A system of medicine focused on promoting the body's innate ability to heal itself.

    See: https://schema.org/Osteopathic
    Model depth: 6
    """
    type_: str = Field("Osteopathic", alias='@type')
    

