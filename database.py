from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy import text
load_dotenv()
db_string=os.environ["DB_CONNECTION_STRING"]

engine = create_engine(
    db_string,
    connect_args={
        "ssl": {
            "ssl_ca": "C:\\Users\\Precision15-XeonEdit\\Desktop\\samplecodes\\new-jovian\\DigiCertGlobalRootG2.crt.pem",
        }
    },

)

def load_jobs():
    with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      result_dicts = []
      for row in result.all():
          #The ._mapping attribute in SQLAlchemy Row objects provides dictionary-like access to the data in a database row.
          result_dicts.append(dict(row._mapping))
      
    return result_dicts

def load_job_id(id):
   with engine.connect() as conn:
      result = conn.execute(text("select * from jobs where id = :val"), {"val": id})
      rows = result.all()
      if len(rows) == 0:
          return None
      else:
          return dict(rows[0]._mapping)
   

