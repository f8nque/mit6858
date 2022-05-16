from zoodb import *
from debug import *
from auth import *
import time

def transfer(sender, recipient, zoobars,token):
    persondb = person_setup()
    senderp = persondb.query(Person).get(sender)
    recipientp = persondb.query(Person).get(recipient)

    sender_balance = senderp.zoobars - zoobars
    recipient_balance = recipientp.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()
    if(check_token(sender,token)):
        senderp.zoobars = sender_balance
        recipientp.zoobars = recipient_balance
        persondb.commit()

        transfer = Transfer()
        transfer.sender = sender
        transfer.recipient = recipient
        transfer.amount = zoobars
        transfer.time = time.asctime()

        transferdb = transfer_setup()
        transferdb.add(transfer)
        transferdb.commit()

def balance(username):
    db = person_setup()
    person = db.query(Person).get(username)
    return person.zoobars

def get_log(username):
    db = transfer_setup()
    l = db.query(Transfer).filter(or_(Transfer.sender==username,
                                      Transfer.recipient==username))
    r = []
    for t in l:
       r.append({'time': t.time,
                 'sender': t.sender ,
                 'recipient': t.recipient,
                 'amount': t.amount })
    return r 


