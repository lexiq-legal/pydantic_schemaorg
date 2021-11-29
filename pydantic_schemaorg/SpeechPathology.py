from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class SpeechPathology(MedicalSpecialty):
    """The scientific study and treatment of defects, disorders, and malfunctions of speech"
     "and voice, as stuttering, lisping, or lalling, and of language disturbances, as aphasia"
     "or delayed language acquisition.

    See https://schema.org/SpeechPathology.

    """

    locals().update({"@type": Field("SpeechPathology", const=True)})


SpeechPathology.update_forward_refs()
