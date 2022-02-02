from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalDevice(MedicalEntity):
    """Any object used in a medical capacity, such as to diagnose or treat a patient.

    See: https://schema.org/MedicalDevice
    Model depth: 3
    """
    type_: str = Field("MedicalDevice", alias='@type')
    postOp: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A description of the postoperative procedures, care, and/or followups for this device.",
    )
    preOp: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A description of the workup, testing, and other preparations required before implanting"
     "this device.",
    )
    seriousAdverseOutcome: Optional[Union[List[Union['MedicalEntity', str]], 'MedicalEntity', str]] = Field(
        None,
        description="A possible serious complication and/or serious side effect of this therapy. Serious"
     "adverse outcomes include those that are life-threatening; result in death, disability,"
     "or permanent damage; require hospitalization or prolong existing hospitalization;"
     "cause congenital anomalies or birth defects; or jeopardize the patient and may require"
     "medical or surgical intervention to prevent one of the outcomes in this definition.",
    )
    procedure: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A description of the procedure involved in setting up, using, and/or installing the"
     "device.",
    )
    adverseOutcome: Optional[Union[List[Union['MedicalEntity', str]], 'MedicalEntity', str]] = Field(
        None,
        description="A possible complication and/or side effect of this therapy. If it is known that an adverse"
     "outcome is serious (resulting in death, disability, or permanent damage; requiring"
     "hospitalization; or is otherwise life-threatening or requires immediate medical"
     "attention), tag it as a seriouseAdverseOutcome instead.",
    )
    contraindication: Optional[Union[List[Union[str, 'Text', 'MedicalContraindication']], str, 'Text', 'MedicalContraindication']] = Field(
        None,
        description="A contraindication for this therapy.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
    from pydantic_schemaorg.MedicalContraindication import MedicalContraindication
