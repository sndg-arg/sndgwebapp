from Bio.SeqFeature import SeqFeature

from bioseq.models.Bioentry import Bioentry
from bioseq.models.BioentryQualifierValue import BioentryQualifierValue
from bioseq.models.SeqfeatureQualifierValue import SeqfeatureQualifierValue


class ProteinDoc:
    """
    id
    rid
    __text__  solo index / copy field
    extra    ni store ni index


    name = StringField(required=True)
    description = StringField(required=False)
    seq_aa = StringField(default="", required=True)   store no index
    seq_nt = StringField(default="", required=True)   store no index

    ncbi_tax_id
    ncbi_tax

    feature_*_identifier
    feature_*_start         store no index
    feature_*_end           store no index
    feature_*_strand        store no index
    feature_*_type
    feature_*_rid           store no index
    feature_*_description


    prop_*_rid           store no index
    prop_*_name
    prop_*_type         store no index
    prop_*_description  store no index
    prop_*_value
    prop_*_values
    prop_*_url          store no index

    organism = StringField()
    genes = ListField(StringField(), required=True)
    uniref100
    uniref90
    uniref50
    assembly_id = ReferenceField(SeqCollection)
    assembly_name = StringField(required=False)

    ontologies = ListField(StringField())

    size = EmbeddedDocumentField(Size)
    status = StringField(default="predicted")

    bxrefs = ListField(StringField())

    """

    def __init__(self, data: dict):
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return value

    @staticmethod
    def protein_rel(bioentry: Bioentry):

        data = {
            "rid": bioentry.bioentry_id,
            "name": bioentry.name,
            "accession": bioentry.accession,
            "description": bioentry.name,
            "seq_aa": bioentry.seq.seq,
            # seq_nt :
            "ncbi_tax_id": bioentry.taxon.ncbi_taxon_id,
            "ncbi_tax": bioentry.taxon.scientificName  #

        }

        for idx, f in enumerate(bioentry.features.all()):
            data.update(ProteinDoc._feature_rel(f, idx))

        for idx, q in enumerate(bioentry.qualifiers.all()):
            if q.term.identifier not in [SeqfeatureQualifierValue.TranslationValue, SeqfeatureQualifierValue.GeneValue,
                                         SeqfeatureQualifierValue.LocusTagValue, SeqfeatureQualifierValue.DBXREFValue,
                                         SeqfeatureQualifierValue.ProductValue,
                                         SeqfeatureQualifierValue.GeneSymbolValue,
                                         SeqfeatureQualifierValue.OldLocusTagValue,
                                         SeqfeatureQualifierValue.ProteinIDValue,
                                         SeqfeatureQualifierValue.AliasValue]:
                data.update(ProteinDoc._property_rel(q, idx))

        lt = bioentry.locus_tag()
        data["genes"] = [lt] + [x for x in bioentry.genes() if x != lt]
        # uniref100
        # uniref90
        # uniref50
        data["assembly_id"] = bioentry.biodatabase.biodatabase_id
        data["assembly_name"] = bioentry.biodatabase.name

        data["ontologies"] = ListField(StringField())

        data["size"] = EmbeddedDocumentField(Size)
        data["status"] = StringField(default="predicted")

        data["bxrefs"]

        pd = ProteinDoc(data)

        return pd

    @staticmethod
    def _property_rel(qualifier: BioentryQualifierValue, idx: int):
        """

        bioentry = models.ForeignKey(Bioentry, models.CASCADE, related_name="qualifiers")
        term = models.ForeignKey('Term', models.DO_NOTHING)
        value = models.TextField(blank=True, null=True)
        rank = models.IntegerField(default=1, null=True)

        prop_*_rid           store no index
        prop_*_name
        prop_*_type         store no index
        prop_*_description  store no index
        prop_*_value
        prop_*_values
        prop_*_url          store no index
        """
        feature = {
            f"prop_{idx}_rid": qualifier.bioentry_qualifiervalue_id,
            f"prop_{idx}_name": qualifier.term.name,
            f"prop_{idx}_type": qualifier.term.identifier,
            f"prop_{idx}_value": qualifier.value,
        }
        # TODO ver como resolver propiedad con multiples valores
        # if qualifier
        # feature[f"feature_{idx}_description"] = seqfeature.qualifiers.get(SeqfeatureQualifierValue.ProductValue, "")

        return feature

    @staticmethod
    def _feature_rel(seqfeature: SeqFeature, idx: int):
        """
        *_feature_*_identifier
        *_feature_*_start
        *_feature_*_end
        *_feature_*_strand
        *_feature_*_type
        *_feature_*_rid
        *_feature_*_description
        """
        feature = {
            f"feature_{idx}_rid": seqfeature.seqfeature_id,
            f"feature_{idx}_identifier": seqfeature.display_name,
            f"feature_{idx}_start": seqfeature.location.start,
            f"feature_{idx}_end": seqfeature.location.start,
            f"feature_{idx}_type": seqfeature.type,
        }
        if None != seqfeature.location.strand:
            feature[f"feature_{idx}_strand"] = seqfeature.location.strand
        feature[f"feature_{idx}_description"] = seqfeature.qualifiers.get(SeqfeatureQualifierValue.ProductValue, "")

        return feature
