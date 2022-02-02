from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DDxElement(MedicalIntangible):
    """An alternative, closely-related condition typically considered later in the differential"
     "diagnosis process along with the signs that are used to distinguish it.

    See: https://schema.org/DDxElement
    Model depth: 4
    """
    type_: str = Field("DDxElement", alias='@type')
    diagnosis: Optional[Union[List[Union['MedicalCondition', str]], 'MedicalCondition', str]] = Field(
        None,
        description="One or more alternative conditions considered in the differential diagnosis process"
     "as output of a diagnosis process.",
    )
    distinguishingSign: Optional[Union[List[Union['MedicalSignOrSymptom', str]], 'MedicalSignOrSymptom', str]] = Field(
        None,
        description="One of a set of signs and symptoms that can be used to distinguish this diagnosis from others"
     "in the differential diagnosis.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom
