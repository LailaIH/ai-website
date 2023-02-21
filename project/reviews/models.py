from django.db import models
from django.contrib.auth.models import User
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Review(models.Model):
    review = models.TextField()
    owner=  models.ForeignKey(User, related_name="review_owner" , on_delete= models.CASCADE , default=1)


# class ReviewInference(Model):
#     __keyspace__ = "review_inferences"
#     uuid = columns.UUID(partition_key=True , default=uuid.uuid1)
#     query = columns.Text()
#     label = columns.Text()
#     confidence = columns.Float()
#     model_version = columns.Text(default='v1')


