from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class TripleBlindedTrial(MedicalTrialDesign):
    """A trial design in which neither the researcher, the person administering the therapy"
     "nor the patient knows the details of the treatment the patient was randomly assigned"
     "to.

    See: https://schema.org/TripleBlindedTrial
    Model depth: 6
    """
    type_: str = Field("TripleBlindedTrial", alias='@type')
    

