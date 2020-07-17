SELECT
  "time" AS "time",
  pres_card,
  kit_id
FROM api_medic_hypertable
WHERE
  $__timeFilter("time")
ORDER BY 1
LIMIT 512