
def addAccount():
    return dict()


def save():
    submitted_account_name = request.vars.account_name
    submitted_account_number = request.vars.account_number
    submitted_bank = request.vars.bank
    submitted_branch = request.vars.branch

    results = db.accounts.insert(
            db_account_name = submitted_account_name,
            db_account_number = submitted_account_number,
            db_bank = submitted_bank,
            db_branch = submitted_branch
    )

    if results:
        return "Account added successfully"
    else:
        return "An Error Occured. Please check and try again."


def viewAccounts():
    accounts = db().select(db.accounts.ALL)
    return dict(accounts=accounts)

def editAccount():
    parameters = request.args
    submitted_id = parameters[0]
    return dict(id=submitted_id)

def update():
    submitted_account_name = request.vars.account_name
    submitted_account_number = request.vars.account_number
    submitted_bank = request.vars.bank
    submitted_branch = request.vars.branch
    submitted_id = request.vars.id

    if db(db.accounts.id == submitted_id).select():

        db(db.accounts.id == submitted_id).update(
        db_account_name = submitted_account_name,
        db_account_number = submitted_account_number,
        db_bank = submitted_bank,
        db_branch = submitted_branch
        )
        return 'Account Updated successfully'

    else:
        return 'No Account With the ID found. Please Try Another ID.'

def delete():
    parameters = request.args
    submitted_id = parameters[0]

    if db(db.accounts.id == submitted_id).select():

        db(db.accounts.id == submitted_id).delete()
        return 'Account Deleted Successfully'

    else:
        return 'No Account With ID found'
