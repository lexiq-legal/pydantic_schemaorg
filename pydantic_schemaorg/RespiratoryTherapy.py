from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class RespiratoryTherapy(MedicalSpecialty, MedicalTherapy):
    """The therapy that is concerned with the maintenance or improvement of respiratory function"
     "(as in patients with pulmonary disease).

    See https://schema.org/RespiratoryTherapy.

    """
    type_: str = Field("RespiratoryTherapy", const=True, alias='@type')
    

RespiratoryTherapy.update_forward_refs()
