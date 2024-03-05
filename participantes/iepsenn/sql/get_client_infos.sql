select
    clients.id as id_client,
    min(clients.limit_value) as limit_value,
    coalesce(sum(
        case 
            when transactions.type = 'c' then transactions.value * -1 
            else transactions.value
        end
    ), 0) as balance
from clients
left join transactions on clients.id = transactions.id_client
where clients.id = {{ id }}
group by clients.id