
def addAccount():
    return dict()


def save():
    submitted_account_name = request.vars.account_name
    submitted_account_number = request.vars.account_number
    submitted_bank = request.vars.bank
    submitted_branch = request.vars.branch

    results = db.users.insert(
            db_account_name = submitted_account_name,
            db_account_number = submitted_account_number,
            db_bank = submitted_bank,
            db_branch = submitted_branch
    )

    if results:
        return "User saved successfully"
    else:
        return "An Error Occured. Please check and try again."


def viewAccounts():
    accounts = db().select(db.users.ALL)
    return dict(users=accounts)        
