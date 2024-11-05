# mahendar9
Report on Crop Price Forecasting Project
Introduction
In an effort to support farmers, traders, and policymakers in making informed decisions, a forecasting project has been developed to predict crop prices for the next five years (2024 to 2028). This project utilizes historical price data obtained from the Government of India’s open data portal, data.gov.in, covering the years 2018 to 2023. The forecasting model incorporates two machine learning techniques: Logistic Regression and Random Forest.

Objectives
To predict future Minimum Support Prices (MSP) for various crops.
To provide insights that can assist farmers in making better cultivation decisions and enable traders and policymakers to formulate effective agricultural policies.
Methodology
Data Collection
Data was sourced from data.gov.in, focusing on historical crop price information relevant to major commodities in India. The dataset was preprocessed to remove entries categorized as "Other Crops" to ensure a focused analysis.

Models Implemented
Two predictive models were developed to forecast crop prices:

Logistic Regression:

A statistical method for predicting binary outcomes, here adapted for continuous price prediction.
Average Metrics:
Average MAE: 87.6241
Average MSE: 25327.1874
Average R²: 0.9516
Random Forest:

An ensemble learning method that constructs multiple decision trees and outputs the mean prediction of individual trees.
Average Metrics:
Average MAE: 74.5590
Average MSE: 15741.1273
Average R²: 0.9605
Model Comparison
The results indicate that the Random Forest model outperforms the Logistic Regression model in terms of average accuracy metrics, demonstrating lower mean absolute error (MAE) and mean squared error (MSE), as well as a higher coefficient of determination (R²). This suggests that the Random Forest model is better suited for predicting crop prices in this context.

Application Development
The final predictions were integrated into a web application developed using Streamlit. This user-friendly platform allows users to interactively select crops and view projected prices, providing valuable insights for decision-making. The web application can be accessed at the following link: Crop Price Predictions Web App.

Results
The forecasting application provides real-time predictions of crop prices for selected commodities, enabling farmers to make informed choices about planting and selling their produce. The visual interface offers an engaging way to access complex data insights, significantly improving accessibility to crucial agricultural information.

Conclusion
This project successfully leverages historical data and machine learning techniques to forecast future crop prices, providing a vital tool for stakeholders in the agricultural sector. By making this information publicly accessible through a web application, it aims to empower farmers and enhance their decision-making capabilities, ultimately contributing to more effective agricultural practices and better economic outcomes.

Future Work
Future iterations of this project could involve:

Incorporating additional factors such as weather patterns, market demand, and production costs to improve prediction accuracy.
Implementing cross-validation techniques to further assess model robustness.
Expanding the application to include more crops and regions, allowing for broader usability.
