from pydantic import Field
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty
from pydantic_schema_org.MedicalTherapy import MedicalTherapy


class RespiratoryTherapy(MedicalSpecialty, MedicalTherapy):
    """The therapy that is concerned with the maintenance or improvement of respiratory function"
     "(as in patients with pulmonary disease).

    See https://schema.org/RespiratoryTherapy.

    """

    locals().update({"@type": Field("RespiratoryTherapy", const=True)})


RespiratoryTherapy.update_forward_refs()
