SELECT api_medic_kit_per_user.estado_baterias , js.key, js.value
FROM api_medic_kit_per_user, json_each(api_medic_kit_per_user.estado_baterias) AS js
WHERE api_medic_kit_per_user.kit_id='$kit_id' AND js.key='bateria_mediband';