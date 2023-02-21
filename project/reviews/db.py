from nbs.configurations import config
from cassandra.cluster import Cluster 
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine import connection
import pathlib

settings = config.get_settings()

ASTRADB_CLIENT_ID = settings.ASTRA_DB_CLIENT_ID
ASTRADB_CLIENT_SECRET = settings.ASTRA_DB_CLIENT_SECRET
BASE_DIR = pathlib.Path(__file__).resolve().parent
CLUSTER_BUNDLE = str(BASE_DIR/'ignored'/'astradb_connect.zip') 

def get_cluster():
    cloud_config={
        'secure_connect_bundle': CLUSTER_BUNDLE
    }
    auth_provider = PlainTextAuthProvider(ASTRADB_CLIENT_ID, ASTRADB_CLIENT_SECRET)   
    return Cluster(cloud=cloud_config, auth_provider=auth_provider)  


def get_session():
    cluster = get_cluster()
    session = cluster.connect()
    connection.register_connection(str(session), session=session)
    connection.set_default_connection(str(session))
    return session