# Project: Sports Car Price Analysis and Visualization

This project explores the relationship between price, performance, and certain specifications in sports cars. Through a series of insightful visualizations, it aims to uncover patterns across brands that drive vehicle cost and prestige.

## Data

The dataset includes the following key columns:

- **Car Make**: The car manufacturer (e.g., Ferrari, Lamborghini).  
- **Car Model**: The specific model name of the car.  
- **Year**: The model year of the car.  
- **Engine Size (L)**: The engine displacement in liters.  
- **Horsepower**: Engine horsepower.  
- **Torque (lb-ft)**: The torque output of the engine measured in pound-feet.  
- **0-60 MPH Time (seconds)**: The time it takes for the car to accelerate from 0 to 60 miles per hour.  
- **Price (in USD)**: The price of the car in US dollars.

**Source:** The data for this project was taken from [Kaggle](https://www.kaggle.com/datasets/rkiattisak/sports-car-prices-dataset).

## Visualizations

The project includes four main visualizations to analyze various aspects of sports car data:

1. **Price Trends of Top 3 Sports Car Brands**
   
   This plot shows the price evolution over recent years (from 2019 onwards) for Ferrari, Lamborghini, and McLaren.  
   Using logarithmic scale and regression lines, it highlights the pricing trends for these luxury brands, making it easier to compare their market dynamics.
   
   ![Описание](images/demo_plot_1.png)



3. **Price Distribution Across Car Brands**
   
   A boxplot visualization displaying the distribution of car prices for all brands on a logarithmic scale.  
   Outliers are hidden to focus on the core price range, providing insight into the typical price ranges and variability within each brand, and allowing comparison across multiple manufacturers.
   
   ![Описание](images/demo_plot_2.png)


   
5. **Fastest Cars with Price Coloring**

   Bar chart displays car models capable of accelerating from 0 to 60 mph in under 3 seconds.  
   Cars are sorted by their acceleration time in descending order. Each bar is color-coded based on the car's price, helping to quickly compare performance against cost. The color gradient represents the price range, with a capped upper limit to ensure visual clarity between extremely high-priced models and the rest.
   
   This chart allows for an intuitive comparison between speed and cost across elite supercars.
   
   ![Описание](images/demo_plot_3.png)



7. **Relationship Between Engine Size and Price**
   
   A quadratic regression plot that demonstrates how engine size (in liters) affects the car price, plotted on a logarithmic scale.  
   This visualization helps to understand the correlation between engine capacity and market value, categorizing prices into low, medium, and high tiers based on engine displacement.
   
   ![Описание](images/demo_plot_4.png)



## Final Output

The final output of this project includes:

- A Python script that loads, cleans, and analyzes the sports car data.

- Four insightful visualizations illustrating price trends, distribution, and the impact of speed and engine size on car price.

- Use of logarithmic scales and regression models to communicate market patterns.

- A visual analysis tool to support decision-making and further research into sports car pricing and performance.

## How to Run

```bash
pip install -r requirements.txt
python app.py

