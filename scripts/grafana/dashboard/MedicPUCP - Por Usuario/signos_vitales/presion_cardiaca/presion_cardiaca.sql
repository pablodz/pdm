SELECT
  "time" AS "time",
  pres_card
FROM api_medic_hypertable
WHERE
  $__timeFilter("time") AND
  kit_id = '$kit_id'
ORDER BY 1