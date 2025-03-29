from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
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

