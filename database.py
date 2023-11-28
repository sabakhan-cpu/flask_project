
from sqlalchemy import create_engine, text

db_connection_string ="mysql+pymysql://8mcerihi6gr6o9fnw8a4:pscale_pw_JQRLiQ5Ip7SlV01gNqRQrLZzP5qsFK13XRmpz1n5dsn@aws.connect.psdb.cloud/avengers_database?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl": {
                               "ssl_ca": "/etc/ssl/cert.pem"

                           }
                       }
                       )
def load_data_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('select * from JOBS'))
        job = result.all()
        return job


def Convert(db_data, di):
    for a, b in db_data:
        di.setdefault(a, []).append(b)
    print(di)


# Driver Code

dictionary = {}
Convert(load_data_from_db(), dictionary)

