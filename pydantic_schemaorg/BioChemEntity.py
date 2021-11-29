from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Thing import Thing


class BioChemEntity(Thing):
    """Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical;"
     "a synthetic chemical.

    See https://schema.org/BioChemEntity.

    """

    bioChemSimilarity: Any = Field(
        None,
        description="A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms.",
    )
    isPartOfBioChemEntity: Any = Field(
        None,
        description="Indicates a BioChemEntity that is (in some sense) a part of this BioChemEntity.",
    )
    hasMolecularFunction: Optional[Union[List[Union[AnyUrl, DefinedTerm, PropertyValue]], Union[AnyUrl, DefinedTerm, PropertyValue]]] = Field(
        None,
        description="Molecular function performed by this BioChemEntity; please use PropertyValue if you"
     "want to include any evidence.",
    )
    hasRepresentation: Optional[Union[List[Union[AnyUrl, str, PropertyValue]], Union[AnyUrl, str, PropertyValue]]] = Field(
        None,
        description="A common representation such as a protein sequence or chemical structure for this entity."
     "For images use schema.org/image.",
    )
    hasBioChemEntityPart: Any = Field(
        None,
        description="Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part.",
    )
    associatedDisease: Union[List[Union[AnyUrl, PropertyValue, Any]], Union[AnyUrl, PropertyValue, Any]] = Field(
        None,
        description="Disease associated to this BioChemEntity. Such disease can be a MedicalCondition or"
     "a URL. If you want to add an evidence supporting the association, please use PropertyValue.",
    )
    taxonomicRange: Union[List[Union[AnyUrl, str, DefinedTerm, Any]], Union[AnyUrl, str, DefinedTerm, Any]] = Field(
        None,
        description="The taxonomic grouping of the organism that expresses, encodes, or in someway related"
     "to the BioChemEntity.",
    )
    isInvolvedInBiologicalProcess: Optional[Union[List[Union[AnyUrl, DefinedTerm, PropertyValue]], Union[AnyUrl, DefinedTerm, PropertyValue]]] = Field(
        None,
        description="Biological process this BioChemEntity is involved in; please use PropertyValue if"
     "you want to include any evidence.",
    )
    biologicalRole: Optional[Union[List[DefinedTerm], DefinedTerm]] = Field(
        None,
        description="A role played by the BioChemEntity within a biological context.",
    )
    bioChemInteraction: Any = Field(
        None,
        description="A BioChemEntity that is known to interact with this item.",
    )
    isEncodedByBioChemEntity: Any = Field(
        None,
        description="Another BioChemEntity encoding by this one.",
    )
    isLocatedInSubcellularLocation: Optional[Union[List[Union[AnyUrl, DefinedTerm, PropertyValue]], Union[AnyUrl, DefinedTerm, PropertyValue]]] = Field(
        None,
        description="Subcellular location where this BioChemEntity is located; please use PropertyValue"
     "if you want to include any evidence.",
    )
    locals().update({"@type": Field("BioChemEntity", const=True)})


BioChemEntity.update_forward_refs()
