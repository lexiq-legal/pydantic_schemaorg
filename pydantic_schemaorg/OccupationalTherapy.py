from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class OccupationalTherapy(MedicalTherapy):
    """A treatment of people with physical, emotional, or social problems, using purposeful"
     "activity to help them overcome or learn to deal with their problems.

    See https://schema.org/OccupationalTherapy.

    """

    locals().update({"@type": Field("OccupationalTherapy", const=True)})


OccupationalTherapy.update_forward_refs()
