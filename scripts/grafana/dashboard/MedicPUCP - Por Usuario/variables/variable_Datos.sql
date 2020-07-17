-- Name:Datos
-- NO REVISADO POR QUERY DE TIMESCALEDB
SELECT CONCAT(auth_user.first_name,' ', auth_user.last_name,' DNI:',api_medic_kit_per_user.kit_id) AS variables
FROM auth_user
INNER JOIN api_medic_kit_per_user ON auth_user.id = api_medic_kit_per_user.user_id
INNER JOIN api_medic_hypertable ON api_medic_kit_per_user.kit_id=api_medic_hypertable.kit_id
GROUP BY api_medic_kit_per_user.user_id,auth_user.id,api_medic_kit_per_user.kit_id;