select
    value,
    type,
    description,
    timestamp 
from transactions
where id_client = {{ id }}