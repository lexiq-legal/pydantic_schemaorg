from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Musculoskeletal(MedicalSpecialty):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders"
     "of muscles, ligaments and skeletal system.

    See: https://schema.org/Musculoskeletal
    Model depth: 6
    """
    type_: str = Field("Musculoskeletal", alias='@type')
    

