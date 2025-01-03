# Load necessary libraries
library(rgl)
library(dplyr)

# Hardcoded sample dataset with 5 rows
data_clean <- data.frame(
  Name = c("Asteroid1", "Asteroid2", "Asteroid3", "Asteroid4", "Asteroid5"),
  min_distance = c(0.05, 0.1, 0.02, 0.07, 0.03),    # Example minimum distances (in AU)
  velocity_km_s = c(25.3, 18.7, 22.1, 30.5, 27.4)    # Example velocities (in km/s)
)

# Check the structure of the hardcoded data
head(data_clean)

# Create a 3D scatter plot using 'min_distance' and 'velocity_km_s'
# We'll use 'min_distance' for x-axis, 'velocity_km_s' for y-axis, and use an index (row number) for z-axis
plot3d(data_clean$min_distance, data_clean$velocity_km_s, seq_along(data_clean$min_distance),
       col = "blue", size = 5, type = "s", 
       xlab = "Minimum Distance (AU)", ylab = "Velocity (km/s)", zlab
       = "Index")

