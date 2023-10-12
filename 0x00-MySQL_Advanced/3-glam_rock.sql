-- Rank country origins of bands based on fans
SELECT country, COUNT(*) AS num_bands
FROM bands
GROUP BY country
ORDER BY num_bands DESC;
