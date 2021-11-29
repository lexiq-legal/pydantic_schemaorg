from pydantic import Field
from pydantic_schema_org.MedicalTherapy import MedicalTherapy


class RadiationTherapy(MedicalTherapy):
    """A process of care using radiation aimed at improving a health condition.

    See https://schema.org/RadiationTherapy.

    """

    locals().update({"@type": Field("RadiationTherapy", const=True)})


RadiationTherapy.update_forward_refs()
