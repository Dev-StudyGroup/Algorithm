SELECT id,
       name,
       host_id
FROM   places HOST_ID
WHERE  host_id IN (SELECT host_id
                   FROM   places
                   GROUP  BY host_id
                   HAVING Count(*) >= 2) 