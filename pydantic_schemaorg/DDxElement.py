from pydantic import Field
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from typing import List, Optional, Union
from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DDxElement(MedicalIntangible):
    """An alternative, closely-related condition typically considered later in the differential"
     "diagnosis process along with the signs that are used to distinguish it.

    See https://schema.org/DDxElement.

    """
    type_: str = Field("DDxElement", const=True, alias='@type')
    diagnosis: Optional[Union[List[Union[MedicalCondition, str]], Union[MedicalCondition, str]]] = Field(
        None,
        description="One or more alternative conditions considered in the differential diagnosis process"
     "as output of a diagnosis process.",
    )
    distinguishingSign: Optional[Union[List[Union[MedicalSignOrSymptom, str]], Union[MedicalSignOrSymptom, str]]] = Field(
        None,
        description="One of a set of signs and symptoms that can be used to distinguish this diagnosis from others"
     "in the differential diagnosis.",
    )
    

DDxElement.update_forward_refs()
