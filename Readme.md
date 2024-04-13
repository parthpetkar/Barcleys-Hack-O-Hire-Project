# Barcleys_Hack_O_Hire_Project
## Anomaly Detection

## 🎨 Table of Contents
- [Anomaly Detection](#anomaly-detection)
- [Contributors](#contributors)
- [Company Logo](#company-logo)
- [Description](#description)
- [Technology Stack](#technology-stack)
- [Badges](#badges)
- [Installation](#installation)
- [Inital Idea](#inital-idea)
- [Inital PPT](#inital-ppt)
- [Final PPT](#final-presentation)
- [How to Use the Project](#how-to-use-the-project)
- [How to Contribute to the Project](#how-to-contribute-to-the-project)
- [License](#license)
- [Security](#security)

## Contributors
- [Parth Petkar](https://github.com/parthpetkar)
- [Parth Petkar](https://github.com/contributor)
- [Leevan Herald](https://github.com/contributor)
- [Anshu Parihar](https://github.com/contributor)

## Company Logo
![Barclay's Logg](../barcleys_hack_o_hire_project/Assets/barclaycard_us_logo.jpg)

## Description
   This Project Was created for the Hackathon held by Barclay's called Hack-O-Hire. The Problem Statement was to develop an Anomaly Detection Framework that will help identify the potential issues and irregularities in the data when compared with the regular submissions. 

## Technology Stack
- ETL - Apache Spark
- Python
- Mongo DB
- Open-source Encryption/decryption algorithm
- ML -Isolation Forest
- Tableau
- Apache Airflow

## Initial Idea
### Abstract:

   In the realm of financial transactions, ensuring accuracy and reliability is paramount. However, trade data's vast volume and complexity pose significant challenges in detecting anomalies, which could result in erroneous calculations and payments. This project addresses this critical issue by proposing an Anomaly Detection Framework designed to identify irregularities and potential issues in trade data submissions. Leveraging advanced technologies such as Apache Spark, Airflow, and Tableau, combined with robust data engineering practices and machine learning algorithms, our solution aims to enhance accuracy, reduce manual effort, and foster self-learning across banking functions.

### Aim:

   This project aims to develop an Anomaly Detection Framework capable of efficiently identifying irregularities and potential issues within trade data submissions. By integrating cutting-edge technologies and best practices in data engineering and machine learning, our solution seeks to enhance the accuracy of payments, reduce manual effort, and promote self-learning across banking functions.

### Our Solution:

   Our solution revolves around a robust system architecture designed to handle the challenges associated with detecting anomalies in large and heterogeneous datasets. Data is retrieved from diverse sources, undergoes extraction, transformation, and loading (ETL) processes, and is stored in a suitable database system. Data Sources like Yahoo Finance, Upstox, Tradefeed, etc. A scheduling pipeline will help the workflow optimize the time taken for the process to occur. The pipeline will divide the data into multiple segments, each segment in the form queue will enter the pipeline where if the second segment in the queue is in etl process the other segment is in the loading process, and so on. Apache Spark forms the backbone of our system, enabling distributed processing of data in parallel to ensure scalability and performance. Pre-processing steps, including feature engineering, enhance the accuracy of anomaly detection. For anomaly detection, we utilize the Adtk library, which leverages historical trends in stock prices to identify abnormal patterns such as outlier data points, spike levels, and volatility shifts. The results of anomaly detection are visualized using Tableau, providing users with intuitive insights to investigate and address anomalies promptly. Airflow serves as a workflow management system, automating various stages of the data pipeline to ensure reliability and efficiency.

### Conclusion:

   In conclusion, our Anomaly Detection Framework offers a robust and scalable solution to the challenges of identifying irregularities in trade data submissions. By leveraging advanced technologies and best practices in data engineering and machine learning, we empower organizations to enhance accuracy, reduce manual effort, and foster self-learning across banking functions. Our solution aims to safeguard data integrity and promote operational excellence in the financial domain through continuous innovation and refinement.

## Inital PPT
- [PPT](c69e824automated_anomaly_detection_framework_for_identifying_data_irregularities.pdf)

## Final Presentation
- [PPT](https://he-s3.s3.amazonaws.com/media/sprint/hack-o-hire/team/1920102/9a09405final_barclays_presentation.pdf)


## Badges
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/parthpetkar/Barcleys_Hack_O_Hire_Project)](https://github.com/parthpetkar/Barcleys_Hack_O_Hire_Project/issues)
[![GitHub stars](https://img.shields.io/github/stars/parthpetkar/Barcleys_Hack_O_Hire_Project)](https://github.com/parthpetkar/Barcleys_Hack_O_Hire_Project/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/parthpetkar/Barcleys_Hack_O_Hire_Project)](https://github.com/parthpetkar/Barcleys_Hack_O_Hire_Project/network)

## Installation
To install and run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/parthpetkar/Barcleys_Hack_O_Hire_Project.git

2. Navigate to the project directory:
   ```bash
   cd Barcleys_Hack_O_Hire_Project

3. Install dependencies:
    Create a Virtual Environment 
    ```bash 
    python -m venv Barcleys_Hack_O_Hire_Project 

4. Create Mongo DB Collections
   - DB name - Hackathon
     - Collection_1 - Live-Stock-Data
     - Collection_2 - Stock-Data-Final
     - Collection_3 - Anomalies

5. Set up Docker Images:
    ```bash
    Docker build -t etlimage
    Docker build -t mlimage

6. Run Docker Compose:
    ```bash
    Docker-compose up -d 



## How to Use the Project
To use the project, follow these steps:

   1. Launch the application.
   2. Create a new invoice by filling in the required details.
   3. Save or print the generated invoice.

## 🛠️ Contribution guidelines for this project
We welcome contributions from the community! To contribute to this project, please follow these steps:

   1. Fork the repository.
   2. Create a new branch (`git checkout -b feature/contribution`).
   3. Make your changes and commit them (`git commit -am 'Add new feature'`).
   4. Push to the branch (`git push origin feature/contribution`).
   5. Create a new Pull Request.

## License
This project is licensed under the [MIT License](LICENSE).

## Security
🔒 If you discover any security-related issues, please email [parth.petkar221@vit.edu](parth.petkar221@vit.edu) instead of using the issue tracker.
