# 🌍 World Happiness Index Explorer

An interactive data exploration tool that analyzes the factors influencing happiness scores across countries based on the World Happiness Report data. This project provides visual insights through correlation heatmaps, country rankings, and comparisons over time.

---

## 🧪 Project Workflow

1. Load & clean UN happiness data  
2. Normalize selected features for correlation analysis  
3. Visualize correlations across economic and social indicators  
4. Display top countries by happiness score  
5. Allow interactive comparison of countries over years

---

## 📊 Visualizations

### 📌 Feature Correlation Heatmap

This heatmap visualizes how various factors (like GDP, freedom, corruption perception) are correlated with the overall happiness score across countries in a specific year.

> **Interpretation:** Helps identify which features are most strongly associated with national happiness.

📸 *Example Output:*  
![Figure_1](https://github.com/user-attachments/assets/08a39414-d289-4fd7-ad04-323ab6d27ea5)

---

### 📌 Top Happiest Countries

This horizontal bar plot displays the top N countries ranked by their happiness score (Ladder score) in the selected year.

> **Interpretation:** Provides a snapshot of which nations reported the highest well-being in a given year.

📸 *Example Output:*  
![Figure_2](https://github.com/user-attachments/assets/42234ca9-3b52-4123-89c2-e93fe61f1c3f)


---

### 📌 Country Comparison Over Years

This line chart compares the happiness score of two selected countries across multiple years, allowing users to analyze trends and improvements.

> **Interpretation:** Useful for seeing long-term shifts and comparing socio-economic progress between countries.

📸 *Example Output:*  
![Figure_1](https://github.com/user-attachments/assets/dee2637e-fe76-4ff6-a801-7c091ab81320)


---

## 🚀 How to Run

1. Download the dataset (e.g., `WHR25_Data_Figure_2.1.xlsx`) and update the file path in `world_happiness_explorer.py`
2. Run the script:
   ```bash
   python world_happiness_explorer.py
