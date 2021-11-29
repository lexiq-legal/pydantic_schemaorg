from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class LifestyleModification(MedicalEntity):
    """A process of care involving exercise, changes to diet, fitness routines, and other lifestyle"
     "changes aimed at improving a health condition.

    See https://schema.org/LifestyleModification.

    """

    locals().update({"@type": Field("LifestyleModification", const=True)})


LifestyleModification.update_forward_refs()
