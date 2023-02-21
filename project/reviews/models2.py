import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class ReviewInference(Model):
    __keyspace__ = "review_inferences"
    uuid = columns.UUID(partition_key=True , default=uuid.uuid1)
    query = columns.Text()
    label = columns.Text()
    confidence = columns.Float()
    model_version = columns.Text(default='v1')
