from pydantic import AnyUrl, Field
from typing import List, Optional, Union
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from pydantic_schemaorg.Taxon import Taxon
from pydantic_schemaorg.Gene import Gene
from pydantic_schemaorg.Thing import Thing


class BioChemEntity(Thing):
    """Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical;"
     "a synthetic chemical.

    See https://schema.org/BioChemEntity.

    """
    type_: str = Field("BioChemEntity", const=True, alias='@type')
    bioChemSimilarity: Optional[Union[List[Union['BioChemEntity', str]], Union['BioChemEntity', str]]] = Field(
        None,
        description="A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms.",
    )
    isPartOfBioChemEntity: Optional[Union[List[Union['BioChemEntity', str]], Union['BioChemEntity', str]]] = Field(
        None,
        description="Indicates a BioChemEntity that is (in some sense) a part of this BioChemEntity.",
    )
    hasMolecularFunction: Optional[Union[List[Union[AnyUrl, DefinedTerm, PropertyValue, str]], Union[AnyUrl, DefinedTerm, PropertyValue, str]]] = Field(
        None,
        description="Molecular function performed by this BioChemEntity; please use PropertyValue if you"
     "want to include any evidence.",
    )
    hasRepresentation: Optional[Union[List[Union[AnyUrl, str, PropertyValue]], Union[AnyUrl, str, PropertyValue]]] = Field(
        None,
        description="A common representation such as a protein sequence or chemical structure for this entity."
     "For images use schema.org/image.",
    )
    hasBioChemEntityPart: Optional[Union[List[Union['BioChemEntity', str]], Union['BioChemEntity', str]]] = Field(
        None,
        description="Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part.",
    )
    associatedDisease: Optional[Union[List[Union[AnyUrl, PropertyValue, MedicalCondition, str]], Union[AnyUrl, PropertyValue, MedicalCondition, str]]] = Field(
        None,
        description="Disease associated to this BioChemEntity. Such disease can be a MedicalCondition or"
     "a URL. If you want to add an evidence supporting the association, please use PropertyValue.",
    )
    taxonomicRange: Optional[Union[List[Union[AnyUrl, str, DefinedTerm, Taxon]], Union[AnyUrl, str, DefinedTerm, Taxon]]] = Field(
        None,
        description="The taxonomic grouping of the organism that expresses, encodes, or in someway related"
     "to the BioChemEntity.",
    )
    isInvolvedInBiologicalProcess: Optional[Union[List[Union[AnyUrl, DefinedTerm, PropertyValue, str]], Union[AnyUrl, DefinedTerm, PropertyValue, str]]] = Field(
        None,
        description="Biological process this BioChemEntity is involved in; please use PropertyValue if"
     "you want to include any evidence.",
    )
    biologicalRole: Optional[Union[List[Union[DefinedTerm, str]], Union[DefinedTerm, str]]] = Field(
        None,
        description="A role played by the BioChemEntity within a biological context.",
    )
    bioChemInteraction: Optional[Union[List[Union['BioChemEntity', str]], Union['BioChemEntity', str]]] = Field(
        None,
        description="A BioChemEntity that is known to interact with this item.",
    )
    isEncodedByBioChemEntity: Optional[Union[List[Union[Gene, str]], Union[Gene, str]]] = Field(
        None,
        description="Another BioChemEntity encoding by this one.",
    )
    isLocatedInSubcellularLocation: Optional[Union[List[Union[AnyUrl, PropertyValue, DefinedTerm, str]], Union[AnyUrl, PropertyValue, DefinedTerm, str]]] = Field(
        None,
        description="Subcellular location where this BioChemEntity is located; please use PropertyValue"
     "if you want to include any evidence.",
    )
    

BioChemEntity.update_forward_refs()
