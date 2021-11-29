from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class CrossSectional(MedicalObservationalStudyDesign):
    """Studies carried out on pre-existing data (usually from 'snapshot' surveys), such as"
     "that collected by the Census Bureau. Sometimes called Prevalence Studies.

    See https://schema.org/CrossSectional.

    """

    locals().update({"@type": Field("CrossSectional", const=True)})


CrossSectional.update_forward_refs()
