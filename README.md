# EthioMart Amharic NER System for Telegram E-Commerce Integration

## Project Overview
This project focuses on consolidating Ethiopian e-commerce activities conducted via Telegram by developing an Amharic Named Entity Recognition (NER) system. By leveraging fine-tuned Large Language Models (LLMs), the system extracts key business entities—product names, prices, and locations—from unstructured text, images, and documents shared in multiple Telegram channels. 

The extracted entities are organized into a centralized database, enabling EthioMart to provide a unified platform for customers and vendors. This project is part of an effort to revolutionize Ethiopian e-commerce by improving accessibility, convenience, and efficiency for all stakeholders.

---

## Objectives
1. **Entity Extraction**:
   - Extract key entities (e.g., product names, prices, and locations) from Telegram messages in the Amharic language.
   
2. **Model Fine-tuning**:
   - Fine-tune multilingual LLMs such as XLM-Roberta and BERT-tiny-Amharic for Amharic NER tasks.
   
3. **Model Evaluation**:
   - Compare the performance of multiple models and select the best-performing one.
   
4. **Interpretability**:
   - Use tools like SHAP and LIME to provide transparency into model predictions.
   
5. **Integration**:
   - Develop a pipeline for real-time data extraction and storage in a centralized database.

---

## Dataset Overview
- **Source**: Messages from Ethiopian e-commerce Telegram channels.
- **Types**:
  - **Text**: Amharic language messages.
  - **Images**: Product images and marketing materials.
  - **Metadata**: Sender details, timestamps.
- **Labeling**: CoNLL format for Named Entity Recognition (NER), identifying entities such as product names, prices, and locations.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - NLP: Hugging Face Transformers, NLTK
  - Data Manipulation: pandas, numpy
  - Data Visualization: matplotlib, seaborn
  - Model Evaluation: scikit-learn
- **Database**: MySQL for structured entity storage
- **Model Interpretability**: SHAP, LIME
- **Development Tools**: Jupyter Notebook, Google Colab, Git, GitHub
- **Deployment**: Flask or Streamlit for user-facing applications

---

## Repository Structure
```plaintext
├── .github/
│   └── workflows/
│       └── ci_cd.yml        # CI/CD pipeline for automated testing and deployment
├── .gitignore
├── README.md                # Project documentation
├── requirements.txt         # Required libraries and dependencies
├── src/
│   ├── __init__.py
│   ├── data_ingestion.py    # Script to fetch data from Telegram channels
│   ├── preprocessing.py     # Text preprocessing and tokenization
│   ├── ner_fine_tuning.py   # Fine-tuning LLMs for Amharic NER
│   ├── evaluate_model.py    # Model evaluation and comparison
│   ├── interpretability.py  # SHAP and LIME implementation
│   └── database_integration.py # Storing extracted entities into MySQL
├── data/
│   ├── raw/                 # Raw data collected from Telegram channels
│   ├── processed/           # Preprocessed and labeled data
│   └── examples/            # Example CoNLL format files
├── notebooks/
│   ├── eda.ipynb            # Exploratory Data Analysis
│   ├── preprocessing.ipynb  # Text preprocessing and labeling workflow
│   ├── model_training.ipynb # Fine-tuning and evaluation
│   └── interpretability.ipynb # Model interpretability exploration
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py     # Unit tests for various project components
├── results/
│   ├── metrics/             # Evaluation metrics for different models
│   └── interpretability/    # Outputs from SHAP and LIME
```
## Author
Yonatan Abrham
- Email: [email2yonatan@gmail.com](mailto:email2yonatan@gmail.com)
- LinkedIn: [Yonatan Abrham](https://www.linkedin.com/in/yonatan-abrham1/)
- GitHub: [YonInsights](https://github.com/YonInsights)
