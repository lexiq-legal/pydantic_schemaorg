from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalIntangible(MedicalEntity):
    """A utility class that serves as the umbrella for a number of 'intangible' things in the"
     "medical space.

    See https://schema.org/MedicalIntangible.

    """

    locals().update({"@type": Field("MedicalIntangible", const=True)})


MedicalIntangible.update_forward_refs()
