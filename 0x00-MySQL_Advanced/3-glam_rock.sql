-- Get bands with Glam rock style
SELECT band_name, split - formed AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;