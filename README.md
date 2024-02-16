# AG News Text Classification

This repository contains code for text classification on the AG News dataset using various machine learning and deep learning techniques. The AG News dataset is a collection of news articles categorized into four classes: World, Sports, Business, and Science/Technology.

## Dataset

The AG News dataset consists of 120,000 training samples and 7,600 test samples, evenly distributed among the four classes. Each sample is a short news article accompanied by a title.

You can download the dataset from [here](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset).

## Dependencies

- Python
- NumPy
- Pandas
- Scikit-learn
- TensorFlow (for deep learning models)

## Models

This repository includes implementations of the following models:

- Multinomial Naive Bayes
- SGD (Stochastic Gradient Descent)
- Convolutional Neural Network (CNN)

## Usage

All the necessary steps for data preparation, preprocessing, and model training are contained within the Jupyter Notebook provided.

1. **Data Preparation**: Download the AG News dataset and place it in the `data` directory within the same directory as the notebook. If you're using a different dataset, make sure it follows the same format or preprocess accordingly.

2. **Preprocessing**: Execute the preprocessing cells in the notebook. These cells will tokenize the text, remove stopwords, and convert the labels into numerical format.

3. **Model Training (Optional)**: If you want to train your own models, execute the training cells in the notebook. You can use the provided scripts or your custom implementations to train the models.

    - Ensure that you have the necessary dependencies installed in your Jupyter environment.
    
4. **Prediction App**: Use the provided prediction app to classify news articles. Here's how to run the app:

    - Ensure that you have the necessary dependencies installed.
    
    - Run the prediction app using the following command:
    
        ```
        python app.py
        ```
        
    - The app will prompt you to input the text of a news article. Enter the text and press enter.
    
    - The app will then predict the category of the news article based on the trained model.

5. **Evaluation**: If you want to evaluate the performance of the trained models, execute the evaluation cells in the notebook. This will output accuracy and other evaluation metrics.
   
![Demo Screenshot](demo/screenshot.png)

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.

