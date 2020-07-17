SELECT
  "time" AS "time",
  frec_resp
FROM api_medic_hypertable
WHERE
  $__timeFilter("time") AND
  kit_id = '$kit_id'
ORDER BY 1