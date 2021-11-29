from pydantic import Field
from pydantic_schema_org.MedicalBusiness import MedicalBusiness
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty


class Oncologic(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that deals with benign and malignant tumors, including"
     "the study of their development, diagnosis, treatment and prevention.

    See https://schema.org/Oncologic.

    """

    locals().update({"@type": Field("Oncologic", const=True)})


Oncologic.update_forward_refs()
