from pydantic import Field
from pydantic_schema_org.MedicalCondition import MedicalCondition
from typing import Any, Optional, Union, List
from pydantic_schema_org.MedicalSignOrSymptom import MedicalSignOrSymptom
from pydantic_schema_org.MedicalIntangible import MedicalIntangible


class DDxElement(MedicalIntangible):
    """An alternative, closely-related condition typically considered later in the differential"
     "diagnosis process along with the signs that are used to distinguish it.

    See https://schema.org/DDxElement.

    """

    diagnosis: Optional[Union[List[MedicalCondition], MedicalCondition]] = Field(
        None,
        description="One or more alternative conditions considered in the differential diagnosis process"
     "as output of a diagnosis process.",
    )
    distinguishingSign: Optional[Union[List[MedicalSignOrSymptom], MedicalSignOrSymptom]] = Field(
        None,
        description="One of a set of signs and symptoms that can be used to distinguish this diagnosis from others"
     "in the differential diagnosis.",
    )
    locals().update({"@type": Field("DDxElement", const=True)})


DDxElement.update_forward_refs()
