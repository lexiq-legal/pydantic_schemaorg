from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.BioChemEntity import BioChemEntity


class MolecularEntity(BioChemEntity):
    """Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical,"
     "radical ion, complex, conformer etc., identifiable as a separately distinguishable"
     "entity.

    See https://schema.org/MolecularEntity.

    """

    iupacName: Optional[Union[List[str], str]] = Field(
        None,
        description="Systematic method of naming chemical compounds as recommended by the International"
     "Union of Pure and Applied Chemistry (IUPAC).",
    )
    smiles: Optional[Union[List[str], str]] = Field(
        None,
        description="A specification in form of a line notation for describing the structure of chemical species"
     "using short ASCII strings. Double bond stereochemistry \ indicators may need to be escaped"
     "in the string in formats where the backslash is an escape character.",
    )
    molecularWeight: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="This is the molecular weight of the entity being described, not of the parent. Units should"
     "be included in the form '&lt;Number&gt; &lt;unit&gt;', for example '12 amu' or as '&lt;QuantitativeValue&gt;.",
    )
    inChI: Optional[Union[List[str], str]] = Field(
        None,
        description="Non-proprietary identifier for molecular entity that can be used in printed and electronic"
     "data sources thus enabling easier linking of diverse data compilations.",
    )
    molecularFormula: Optional[Union[List[str], str]] = Field(
        None,
        description="The empirical formula is the simplest whole number ratio of all the atoms in a molecule.",
    )
    chemicalRole: Optional[Union[List[DefinedTerm], DefinedTerm]] = Field(
        None,
        description="A role played by the BioChemEntity within a chemical context.",
    )
    inChIKey: Optional[Union[List[str], str]] = Field(
        None,
        description="InChIKey is a hashed version of the full InChI (using the SHA-256 algorithm).",
    )
    monoisotopicMolecularWeight: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The monoisotopic mass is the sum of the masses of the atoms in a molecule using the unbound,"
     "ground-state, rest mass of the principal (most abundant) isotope for each element instead"
     "of the isotopic average mass. Please include the units the form '&lt;Number&gt; &lt;unit&gt;',"
     "for example '770.230488 g/mol' or as '&lt;QuantitativeValue&gt;.",
    )
    potentialUse: Optional[Union[List[DefinedTerm], DefinedTerm]] = Field(
        None,
        description="Intended use of the BioChemEntity by humans.",
    )
    locals().update({"@type": Field("MolecularEntity", const=True)})


MolecularEntity.update_forward_refs()
