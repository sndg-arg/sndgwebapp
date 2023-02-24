
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

    *_feature_*_identifier
    *_feature_*_start
    *_feature_*_end
    *_feature_*_strand
    *_feature_*_type
    *_feature_*_rid
    *_feature_*_description

    {name}
    *_prop_*_type
    *_prop_*_description
    *_prop_*_value
    *_prop_*_values
    *_prop_*_url

    

    properties = ListField(EmbeddedDocumentField(BioProperty))
        _type = StringField(required=True)
        property = StringField()
        value = DynamicField()
        description = StringField()
        url = StringField()
        source = StringField()

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

    def __init__(self, data:dict):
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return value

