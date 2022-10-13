"""
Dev Matching: 헤비 유저가 소유한 장소
"""
SELECT * FROM places WHERE host_id 
IN (SELECT host_id FROM places GROUP BY host_id HAVING count(host_id) > 1) 
ORDER BY id ASC
