from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class RespiratoryTherapy(MedicalTherapy, MedicalSpecialty):
    """The therapy that is concerned with the maintenance or improvement of respiratory function"
     "(as in patients with pulmonary disease).

    See https://schema.org/RespiratoryTherapy.

    """

    locals().update({"@type": Field("RespiratoryTherapy", const=True)})


RespiratoryTherapy.update_forward_refs()
