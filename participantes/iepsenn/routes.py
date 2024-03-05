from fastapi import HTTPException
from models import Transaction
from utils import format_date_to_utc
from datetime import datetime
from database import read_sql_file, create_database_connection
from fastapi import APIRouter

router = APIRouter()
con = create_database_connection()


@router.post("/clientes/{id}/transacoes")
def post_transaction(id: int, transaction: Transaction):
    if len(transaction.description) > 10:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid parameter DESCRICAO! {transaction.description}",
        )

    if transaction.type not in ["c", "d"]:
        raise HTTPException(
            status_code=422, detail=f"Invalid parameter TIPO! {transaction.type}"
        )

    cur = con.cursor()

    sql = read_sql_file(filename="get_client_infos.sql", params={"id": id})
    res = cur.execute(sql)
    client_info = res.fetchone()

    if client_info is None:
        raise HTTPException(status_code=404, detail="Client not found")

    transaction_op = 1 if transaction.type == "d" else -1
    new_balance = client_info[2] + (transaction_op * transaction.value)

    if new_balance < (client_info[1] * -1):
        raise HTTPException(status_code=422, detail=f"Invalid transaction.")

    sql = read_sql_file(
        filename="get_client_transactions.sql",
        params={
            "id": id,
            "value": transaction.value,
            "type": transaction.type,
            "description ": transaction.description,
        },
    )
    cur.execute(sql)
    con.commit()
    cur.close()

    return {"limite": client_info[1], "saldo": new_balance}


@router.get("/clientes/{id}/extrato")
def get_statement(id: int):
    cur = con.cursor()

    sql = read_sql_file(filename="get_client_infos.sql", params={"id": id})
    res = cur.execute(sql)
    client_info = res.fetchone()

    if client_info is None:
        raise HTTPException(status_code=404, detail="Client not found")

    sql = read_sql_file(filename="get_client_transactions.sql", params={"id": id})
    res = cur.execute(sql)
    transactions = []
    for transaction in res.fetchall()[-10:]:
        transactions.append(
            {
                "valor": transaction[0],
                "tipo": transaction[1],
                "descricao": transaction[2],
                "realizada_em": format_date_to_utc(
                    datetime.strptime(str(transaction[3]), "%Y-%m-%d %H:%M:%S")
                ),
            }
        )

    request_time = format_date_to_utc(datetime.now())
    cur.close()
    return {
        "saldo": {
            "total": client_info[2],
            "data_extrato": request_time,
            "limite": client_info[1],
        },
        "ultimas_transacoes": transactions,
    }
