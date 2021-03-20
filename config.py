class Config(object):
    DEBUG = False
    TESTING = False
    app.config['SECRET_KEY'] = 'super secret key'
  #  params=urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};Server=tcp:dbserver-2.database.windows.net,1433;Database=db-create-1;Uid=nehaadmin;Pwd=Welcome@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
   # app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///mydb.db'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    app.config['SECRET_KEY'] = 'super secret key'
    #params=urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};Server=tcp:dbserver-2.database.windows.net,1433;Database=db-create-1;Uid=nehaadmin;Pwd=Welcome@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    #app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///mydb.db'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    

class TestingConfig(Config):
    TESTING = True
    app.config['SECRET_KEY'] = 'super secret key'
    params=urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};Server=tcp:dbserver-2.database.windows.net,1433;Database=development-db;Uid=nehaadmin;Pwd=Welcome@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    