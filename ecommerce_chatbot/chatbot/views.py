from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from .models import Product,Category
from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category 
from .models import Product
from .serializers import CategorySerializer, ProductSerializer
from django.shortcuts import render
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


import time

start_time = time.process_time()

# Code to be measured

end_time = time.process_time()
execution_time = end_time - start_time
print("CPU time:", execution_time)

import time

start_time = time.perf_counter()

# Code to be measured

end_time = time.perf_counter()
execution_time = end_time - start_time
print("Wall-clock time:", execution_time)



## worked code
from django.shortcuts import render
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import strip_accents_ascii



from django.shortcuts import render
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    # Remove HTML tags (if any)
    text = remove_html_tags(text)
    
    # Lowercase the text
    text = text.lower()

    # Remove punctuation and non-alphabetical characters
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    
    # Tokenize the text
    words = text.split()

    # Lemmatize words and remove stopwords
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]

    # Join the processed words back into a single string
    processed_text = " ".join(words)

    return processed_text


def nlp_recommend(user_query, num):
    preprocessed_query = preprocess_text(user_query)
    user_query_vector = tf.transform([preprocessed_query])
    cosine_similarities_nlp = linear_kernel(user_query_vector, tfidf_matrix)
    similar_indices_nlp = cosine_similarities_nlp[0].argsort()[:-num-1:-1]
    recommended_products = [
        (item(ds.iloc[i]['id']), ds.iloc[i]['description'].split('\n', 2)[:2]) 
        for i in similar_indices_nlp
    ]
    return recommended_products


# Load and preprocess the dataset
ds = pd.read_csv("C:/Users/sample-data.csv")
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
ds['description'] = ds['description'].apply(remove_html_tags)

#tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=1, stop_words='english')
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 4), min_df=2, stop_words='english')
tfidf_matrix = tf.fit_transform(ds['description'])
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

results = {}
for idx, row in ds.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]
    results[row['id']] = similar_items[1:]

# Define functions for recommendation
def item(id):
    return ds.loc[ds['id'] == id]['description'].tolist()[0].split(' - ')[0]

def recommend(item_id, num):
    recs = results[item_id][:num]
    recommended_products = [
        (item(rec[1]), ds[ds['id'] == rec[1]]['description'].iloc[0].split('\n', 2)[:2]) 
        for rec in recs
    ]
    return recommended_products

# Define a function to perform NLP-based recommendations
# def nlp_recommend(user_query, num):
#     user_query_vector = tf.transform([user_query])
#     cosine_similarities_nlp = linear_kernel(user_query_vector, tfidf_matrix)
#     similar_indices_nlp = cosine_similarities_nlp[0].argsort()[:-num-1:-1]
#     recommended_products = [
#         (item(ds.iloc[i]['id']), ds.iloc[i]['description'].split('\n', 2)[:2]) 
#         for i in similar_indices_nlp
#     ]
#     return recommended_products

def nlp_recommend(user_query, num):
    preprocessed_query = preprocess_text(user_query)  # Preprocess the user query
    user_query_vector = tf.transform([preprocessed_query])
    cosine_similarities_nlp = linear_kernel(user_query_vector, tfidf_matrix)
    similar_indices_nlp = cosine_similarities_nlp[0].argsort()[:-num-1:-1]
    recommended_products = [
        (item(ds.iloc[i]['id']), ds.iloc[i]['description'].split('\n', 2)[:2]) 
        for i in similar_indices_nlp
    ]
    return recommended_products


# Define the recommendation view
def recommendation_view(request):
    recommended_products = []

    if request.method == 'POST':
        user_query = request.POST.get('user_query')
        if user_query:
            user_query = user_query.lower()
            recommended_products = nlp_recommend(user_query, num=3)
    
    return render(request, 'chatbot/recommendation.html', {'recommended_products': recommended_products})



# ... (Import statements and code for loading dataset and preprocessing)

# Define the customer service view for providing information and guidance
# ... (Import statements and code for loading dataset and preprocessing)

# Define the customer service view for providing information and guidance
from django.shortcuts import render

# ... (Import statements and code for loading dataset and preprocessing)

# Define the customer service view for providing information and guidance

# Initialize the chatbot
chatbot = ChatBot('EcommerceBot')
trainer = ListTrainer(chatbot)

# Training data
training_data = [
    'Hi',
    'Hello! How can I assist you with women\'s fashion?',
    'What products do you offer for women?',
    'We offer a wide range of women\'s clothing, accessories, and shoes.',
    'Do you have any new arrivals for women?',
    'Yes, we have recently added new collections for women. Check them out on our website.',
    'Can you help me find a specific product for women?',
    'Of course! Please provide me with some details or keywords about the product you are looking for.',
    'Thank you!',
    'You\'re welcome! If you have any more questions, feel free to ask.',
    'Bye',
    'Bye',
    'Tell me more about <product_name>',
    'Sure! <product_description>',
    'How much does <product_name> cost?',
    'The price of <product_name> is $<product_price>.',

    'What are the latest fashion trends?',
    'The latest fashion trends include oversized blazers, animal prints, and neon colors.',
    'Where can I find stylish dresses?',
    'You can find stylish dresses at our online store. We offer a wide range of options for every occasion.',
    'How can I style a little black dress?',
    'A little black dress can be styled with statement accessories and high heels for a chic look.',
    'What is the price range for your handbags?',
    'Our handbags range from $50 to $200, depending on the brand and style.',
    'Can you recommend a good pair of jeans?',
    'Sure! Our best-selling jeans are from the XYZ brand. They offer a perfect fit and come in various styles.',
    'How can I return a product?',
    'To return a product, please contact our customer support team and provide your order details.',
]

# Train the chatbot
trainer.train(training_data)

from django.shortcuts import get_object_or_404




from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

# Your other imports and code...

# views.py

import requests





from django.shortcuts import render,redirect
from chatterbot import ChatBot



# views.py
from django.shortcuts import render
from chatterbot import ChatBot
from .models import Product

# chatbot/views.py

from django.shortcuts import render,redirect
from chatterbot import ChatBot
from .models import Product

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'chatbot/login.html'
    success_url = reverse_lazy('chatbot:chat')  # Redirect to chat page on successful login
# views.py

from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    template_name= 'chatbot/logout.html'
    next_page = reverse_lazy('chatbot:login')  # Redirect to login page on logout

# Initialize the chatbot
chatbot = ChatBot('EcommerceBot')
trainer = ListTrainer(chatbot)

def product_search(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        products = Product.objects.filter(name__icontains=query, category__name__icontains="tshirts")
        return render(request, 'chatbot/product_search.html', {'products': products})
    else:
        return render(request, 'chatbot/product_search.html')

def new_arrivals(request):
    products = Product.objects.filter(category__name__icontains="women")
    return render(request, 'chatbot/new_arrivals.html', {'products': products})

def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'chatbot/product_details.html', {'product': product})




def get_product_details(product_name):
    try:
        product = Product.objects.get(name__icontains=product_name)
        return product
    except Product.DoesNotExist:
        return None
# def get_product_details(self, product_name):
#         product = Product.objects.filter(name__icontains=product_name).first()
#         return product


def get_product_recommendation(user_preference):
    # Implement your product recommendation logic here based on user_preference
    # For example, you can filter products based on category or any other criteria
    recommended_products = Product.objects.filter(category__name__icontains=user_preference)
    return recommended_products


@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product

# ...

@api_view(['GET'])
def product_details_api(request, product_name):
    product = get_object_or_404(Product, name__icontains=product_name)
    serializer = ProductSerializer(product)
    return Response(serializer.data)



def product_search(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        products = Product.objects.filter(name__icontains=query, category__name__icontains="tshirts")
        return render(request, 'chatbot/product_search.html', {'products': products})
    else:
        return render(request, 'chatbot/product_search.html')

def new_arrivals(request):
    products = Product.objects.filter(category__name__icontains="women")
    return render(request, 'chatbot/new_arrivals.html', {'products': products})

def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'chatbot/product_details.html', {'product': product})



def customer_service_view(request):
    response_message = None
    matching_products = []

    if request.method == 'POST':
        user_action = request.POST.get('user_action')
        
        if user_action == 'product_details':
            response_message = "Sure! Please provide the product name or keyword you're looking for."
            user_query = request.POST.get('user_query')

            if user_query:
                user_query = user_query.lower()
                matching_products = nlp_recommend(user_query, num=3)

        elif user_action == 'order_product':
            response_message = 'To order a product, please follow these steps:\n' \
                               '1. Browse our products and select the desired item.\n' \
                               '2. Add the product to your cart and proceed to checkout.\n' \
                               '3. Provide shipping information and choose a payment method.\n' \
                               '4. Review your order and confirm the purchase.'

        elif user_action == 'return_refund':
            response_message = "For returns or exchanges, please follow these steps:\n" \
                               "1. Contact our customer support within 30 days of receiving the product.\n" \
                               "2. Provide your order details and reason for the return/exchange.\n" \
                               "3. Follow the return instructions provided by our team.\n" \
                               "Refunds will be processed within 7-10 business days after the return is received."
            
        elif user_action == 'select_options':
            response_message = "To select product options, please follow these steps:\n" \
                               "1. Visit the product page for the item you're interested in.\n" \
                               "2. Check for available options such as size, color, and quantity.\n" \
                               "3. Choose the desired options before adding the product to your cart."
        
        elif user_action == 'search_products':
            search_query = request.POST.get('search_query')
            if search_query:
                search_results = nlp_recommend(search_query, num=3)
            
    return render(request, 'chatbot/customer_service.html', {
        'response_message': response_message,
        'matching_products': matching_products
    })

faq_database = {
    "What products do you offer for kids?": "We offer a wide range of kid's clothing, accessories, and shoes.",
    "How can I return a product?": "To return a product, please contact our customer support team and provide your order details or type 2",
    "What is your return policy?": "Our return policy allows you to return items within 30 days of purchase...",
    "How can I return a product": "To return a product, please contact our customer support team and provide your order details or type 2",
    "What is your return policy": "Our return policy allows you to return items within 30 days of purchase... type 2 for customer service",
    "How can I contact customer support?": "You can contact our customer support team by emailing support@ecommerce.com...",
    "Can you recommend a good pair of jeans?": "Sure! Our best-selling jeans are from the XYZ brand. They offer a perfect fit and come in various styles.",
    "Can you recommend a good pair of jeans": "Sure! Our best-selling jeans are from the XYZ brand. They offer a perfect fit and come in various styles.",
    "Do you have any new arrivals for kids?":"Yes, we have recently added new collections for women. Check them out on our website.",
    "Do you have any new arrivals for kids":"Yes, we have recently added new collections for women. Check them out on our website.",
    "What is your return policy?": "Our return policy allows you to return items within 30 days of purchase or  type 2 for customer service...",
    "How can I contact customer support?": "You can contact our customer support team by emailing support@example.com...",
    "What is your return policy": "Our return policy allows you to return items within 30 days of purchase or type 2 for customer service...",
    "How can I contact customer support": "You can contact our customer support team by emailing support@example.com...",
}   

from django.shortcuts import render
from chatterbot import ChatBot
from .models import Product


# Initialize the chatbot
chatbot = ChatBot('EcommerceBot')
trainer = ListTrainer(chatbot)
chat_history = []


def chat(request):
    global chat_history
    matching_products = []  # Define matching_products here
    response = None
    
    
    
    if request.method == 'POST':
        message = request.POST.get('message', '')
        message = message.lower()
        chat_history.append({'sender': 'user', 'message': message})

        if message in ['hello', 'hey', 'hi', 'there','howdy']:
            response = "Hello! How can I assist you today?\n1. Get product recommendations\n2. Customer service\n3. Find the right size for kids' clothing and fit"
            chat_history.append({'sender': 'bot', 'message': response})

        elif any(phrase in message.lower() for phrase in ['tell me more about', 'tell me about']):
            product_name = message.lower().replace('tell me more about', '').replace('tell me about', '').strip('?').strip()
            product = get_product_details(product_name)
            if product:
                response = f"Sure! Here are the details for {product.name}: {product.description} and the price of it is {product.price}."
            else:
                response = "I couldn't find any information about that product."

            #chat_history.append({'sender': 'user', 'message': message})
            chat_history.append({'sender': 'bot', 'message': response})
        
        elif 'how much does' in message.lower() and 'cost' in message.lower():
            product_name = message.lower().replace('how much does', '').replace('cost', '').strip('?').strip()
            product = get_product_details(product_name)
            if product:
                response = f"The price of {product.name} is ${product.price}."
            else:
                response = "I couldn't find any information about that product."

            #chat_history.append({'sender': 'user', 'message': message})
            chat_history.append({'sender': 'bot', 'message': response})
        
        elif message == '1':
        # Redirect to the recommendations view
            return redirect('chatbot:recommendation_view')

        elif message == '2':
        # Redirect to the customer service view
            return redirect('chatbot:customer_service_view')
        
        elif message == '3':
            # Redirect to the kids size recommendation view
            return redirect('chatbot:kids_size_recommendation')
        
        elif message in faq_database:
            response = faq_database[message]

        elif message in ['bye','byee','see you']:
            response = "Bye, have a good day!";
           # return redirect('chatbot:login')

    

    # Append user's and bot's messages to chat history
            #chat_history.append({'sender': 'user', 'message': message})
            chat_history.append({'sender': 'bot', 'message': response})

        return render(request, 'chatbot/chat.html', {'response': response, 'message': message, 'chat_history': chat_history})
    
    return render(request, 'chatbot/chat.html', {'chat_history': chat_history})



def kids_size_recommendation(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        preferred_fit = request.POST.get('preferred_fit')
        
        size_recommendations = get_kids_size_recommendations(age, gender, preferred_fit)
        
        return render(request, 'chatbot/kids_size_recommendation_result.html', {'size_recommendations': size_recommendations})
    
    return render(request, 'chatbot/kids_size_recommendation.html')

def get_kids_size_recommendations(age, gender, preferred_fit):
    # Size recommendations based on age, gender, and fit preference
    recommendations = {
        'Tops': '',
        'Bottoms': '',
        'Shoes': '',
    }

    if age >= 1 and age <= 2:
        recommendations['Tops'] = '2T'
        recommendations['Bottoms'] = '2T'
        recommendations['Shoes'] = 'Infant size 4-5'
    elif age >= 3 and age <= 4:
        recommendations['Tops'] = '3T'
        recommendations['Bottoms'] = '3T'
        recommendations['Shoes'] = 'Toddler size 6-7'
    elif age >= 5 and age <= 6:
        recommendations['Tops'] = '4T'
        recommendations['Bottoms'] = '4T'
        recommendations['Shoes'] = 'Toddler size 8-9'
    elif age >= 7 and age <= 8:
        recommendations['Tops'] = 'Small'
        recommendations['Bottoms'] = 'Small'
        recommendations['Shoes'] = 'Youth size 1-2'
    # Add more age ranges and size recommendations based on your sizing chart

    if preferred_fit == 'loose':
        recommendations['Tops'] += ' (Loose Fit)'
        recommendations['Bottoms'] += ' (Loose Fit)'
    elif preferred_fit == 'slim':
        recommendations['Tops'] += ' (Slim Fit)'
        recommendations['Bottoms'] += ' (Slim Fit)'

    return recommendations

def faqs(request):
    faqs_data = {
        "What is your return policy?": "Our return policy allows you to return items within 30 days of purchase...",
        "How can I contact customer support?": "You can contact our customer support team by emailing support@example.com...",
        # Add more FAQs and answers here
    }

    return render(request, "faqs.html", {"faqs_data": faqs_data})

from django.shortcuts import render

def display_recommendations(request):
    
    return render(request, 'chatbot/display_recommendations.html')



