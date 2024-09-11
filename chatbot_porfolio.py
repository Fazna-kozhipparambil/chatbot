{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNlirWpfOV3Ogab1mbvjJ66"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-gwJnXCl7qkW",
        "outputId": "f101edf7-7cfa-470b-e768-108a209630e9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Package punkt is already up-to-date!\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "You: hi\n",
            "Chatbot: Hi there! I'm here to help you learn more about my background. What would you like to know?\n"
          ]
        }
      ],
      "source": [
        "# Import necessary libraries\n",
        "import nltk\n",
        "from nltk.tokenize import word_tokenize\n",
        "\n",
        "# Download necessary NLTK data\n",
        "nltk.download('punkt')\n",
        "\n",
        "# Define chatbot response function\n",
        "def chatbot_response(user_input):\n",
        "    responses = {\n",
        "        \"hi\": \"Hi there! I'm here to help you learn more about my background. What would you like to know?\",\n",
        "        \"background\": \"I have a background in Civil Engineering and am currently pursuing a master's in Data Science. I've worked as Business Intelligence and Data Analysis.\",\n",
        "        \"projects\": \"I have experience working on various  machine learning,data visualization and analysis projects. Feel free to check my portfolio for details.\",\n",
        "        \"skills\": \"I have skills in Python, SQL, AWS, and advanced data analysis techniques. I'm also learning about NLP and machine learning.\",\n",
        "        \"contact details\": \"You can contact me via email at faznakp@gmail.com or visit my LinkedIn profile at linkedin.com/in/faznakp.\",\n",
        "        \"bye\": \"Goodbye! If you have more questions, feel free to ask.\"\n",
        "    }\n",
        "    return responses.get(user_input.lower(), \"Sorry, I don't understand that.\")\n",
        "\n",
        "# Test chatbot locally\n",
        "while True:\n",
        "    user_input = input(\"You: \")\n",
        "    if user_input.lower() == \"bye\":\n",
        "        print(\"Chatbot: Goodbye!\")\n",
        "        break\n",
        "    print(\"Chatbot:\", chatbot_response(user_input))\n"
      ]
    }
  ]
}