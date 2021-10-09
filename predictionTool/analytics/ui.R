dashboardPage(
  dashboardHeader(title = "Delivery Forecast"),
  dashboardSidebar(
    useShinyjs(), 
    sidebarMenu(
      menuItem("Forecast", tabName = "forecast", icon = icon("dashboard"))
      
    )
  ),
  dashboardBody(
    tabItems(
      # Customers section
      tabItem(tabName = "forecast",
              fluidRow(column(2,uiOutput("ui.supplier")), column(1,br(),actionButton("run.sup","Run")), column(2,br(),h5("select supplier"))), 
              tabBox(width = 1200,
                     
                     tabPanel("Forecast",
                              fluidRow(column(6,"Forecasts for selected supplier")),
                              fluidRow(column(width=8,div(DTOutput('tbl1'),style = "font-size:80%"))), br(),
                            )
              
               ))

    )
    
  )
)