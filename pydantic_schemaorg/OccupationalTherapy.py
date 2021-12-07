from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class OccupationalTherapy(MedicalTherapy):
    """A treatment of people with physical, emotional, or social problems, using purposeful"
     "activity to help them overcome or learn to deal with their problems.

    See https://schema.org/OccupationalTherapy.

    """
    type_: str = Field("OccupationalTherapy", const=True, alias='@type')
    

OccupationalTherapy.update_forward_refs()
