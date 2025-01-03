
library(shiny)
library(ggplot2)
library(randomForest)  
library(caret)         


data <- read.csv("C:/Users/Ayushman Singh/Downloads/NEO Earth Close Approaches.csv")


data_subset <- head(data, 5)
data_numeric <- data_subset[, sapply(data_subset, is.numeric)]


set.seed(123)
trainData <- data_numeric  
rf_model <- randomForest(CA.DistanceNominal..au. ~ ., data = trainData, ntree = 100)


predictions <- predict(rf_model, newdata = data_numeric)


ui <- fluidPage(
  titlePanel("Closest Approach of Objects - Analysis and Prediction"),
  sidebarLayout(
    sidebarPanel(
      selectInput("xvar", "Select X-axis Variable:", choices = names(data_subset), selected = "Object")
    ),
    mainPanel(
      tabsetPanel(
        tabPanel("Data Visualization",
                 plotOutput("barPlot")),
        tabPanel("ML Predictions",
                 plotOutput("predictionPlot")),
        tabPanel("Actual vs ML Comparison",
                 plotOutput("comparisonPlot"))
      )
    )
  )
)


server <- function(input, output) {
  output$barPlot <- renderPlot({
    ggplot(data_subset, aes_string(x = input$xvar, y = "CA.DistanceNominal..au.")) +
      geom_bar(stat = "identity", fill = "skyblue") +
      labs(title = paste("Nominal Closest Approach Distance vs.", input$xvar),
           x = input$xvar,
           y = "Nominal Closest Approach Distance (AU)") +
      theme_minimal() +
      theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 12),
            plot.title = element_text(size = 16, face = "bold"))
  })
  
  output$predictionPlot <- renderPlot({
    # Get the selected x-axis variable
    xvar <- input$xvar
    
    # Ensure the x-axis variable is numeric or treat it as a factor if needed
    if (!is.numeric(data_subset[[xvar]])) {
      data_subset[[xvar]] <- as.factor(data_subset[[xvar]])
    }
    
    # Combine actual and predicted values in a data frame
    results <- data.frame(
      x = data_subset[[xvar]],  # Dynamic x-axis based on dropdown selection
      Actual = data_numeric$CA.DistanceNominal..au.,
      Predicted = predictions
    )
    
    # Plot the actual vs predicted line graph
    ggplot(results, aes(x = x)) +
      geom_line(aes(y = Actual, color = "Actual"), size = 1) +
      geom_line(aes(y = Predicted, color = "Predicted"), size = 1, linetype = "dashed") +
      labs(title = "Random Forest Prediction of Nominal Closest Approach Distance",
           x = xvar,
           y = "Nominal Closest Approach Distance (AU)") +
      scale_color_manual(name = "Legend", values = c("Actual" = "blue", "Predicted" = "red")) +
      theme_minimal() +
      theme(plot.title = element_text(size = 16, face = "bold"))
  })
  
  
  output$comparisonPlot <- renderPlot({
    results <- data.frame(
      Actual = data_numeric$CA.DistanceNominal..au.,
      Predicted = predictions
    )
    
    ggplot(results, aes(x = Actual, y = Predicted)) +
      geom_point(color = "blue", size = 3) +
      geom_abline(slope = 1, intercept = 0, linetype = "dashed", color = "red") +  # Line y = x (perfect prediction)
      labs(title = "Actual vs ML Predicted Nominal Closest Approach Distance",
           x = "Actual Closest Approach Distance (AU)",
           y = "Predicted Closest Approach Distance (AU)") +
      theme_minimal() +
      theme(plot.title = element_text(size = 16, face = "bold"))
  })
}

# Run the application 
shinyApp(ui = ui, server = server, options=list(port = 9090))
