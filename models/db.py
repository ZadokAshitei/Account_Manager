from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL("sqlite://storage.sqlite")
db.define_table("users",
                Field('db_account_name'),
                Field('db_account_number'),
                Field('db_bank'),
                Field('db_branch'))
