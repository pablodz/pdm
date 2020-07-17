SELECT
  "time" AS "time",
  temp_corp
FROM api_medic_hypertable
WHERE
  $__timeFilter("time") AND
  kit_id = '$kit_id'
ORDER BY 1