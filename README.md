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


## Usage

1. **Data Preparation**: Download the AG News dataset and place it in the `data` directory. If you're using a different dataset, make sure it follows the same format or preprocess accordingly.

2. **Preprocessing**: Preprocess the dataset by running the preprocessing script:

    ```
    python preprocess.py
    ```

    This script will tokenize the text, remove stopwords, and convert the labels into numerical format.

3. **Model Training (Optional)**: If you want to train your own models, you can follow these steps. Otherwise, skip to step 4.

    - Train the models using the provided scripts or your custom implementations.

4. **Prediction App**: Use the provided prediction app to classify news articles. Here's how to run the app:

    - Ensure that you have the necessary dependencies installed.
    
    - Run the prediction app using the following command:
    
        ```
        python predict_app.py
        ```
        
    - The app will prompt you to input the text of a news article. Enter the text and press enter.
    
    - The app will then predict the category of the news article based on the trained model.
    

## Models

This repository includes implementations of the following models:

- Multinomial Naive Bayes
- SGD (Stochastic Gradient Descent)
- Convolutional Neural Network (CNN

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.

