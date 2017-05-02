# Set parameters
output_file <- "index.html"
width <- 1200
height <- 1600
poster_width <- 36 # inches
res <- 300

# Render document
rmarkdown::render(
  input = "poster/flexdashboard-poster.Rmd",
  output_file = paste0("../output/", output_file)
)

# Render preview
webshot::webshot(
  url = paste0("output/", output_file),
  file = c("output/poster.jpeg", "output/poster.png"),
  vwidth = width,
#  vheight = floor(width * sqrt(2)),          # Use A series aspect ratio
  vheight = height,
  delay = 3,                                 # Wait to allow all element to load
  zoom = poster_width / (width / res)        # Adjust elements relative size
)

# End of script
