
# **OpenAI Adventure Bot**

This script uses OpenAI's GPT-3.5-Turbo model to generate creative storytelling responses based on user prompts. The bot adopts the persona of a world-traveling storyteller, sharing tales of adventure and wonder.  

---

## **Installation**

### **Step 1: Clone the Repository**  
Clone this project to your local machine:  
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```  

### **Step 2: Install Dependencies**  
Install the required Python packages:  
```bash
pip install openai python-dotenv
```  

### **Step 3: Set Up Your Environment**  
1. Create a `.env` file in the project directory.  
2. Add your OpenAI API key to the `.env` file:  
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```  

---

## **Usage**

To run the bot, execute the script and provide a prompt:  
```bash
python your_script_name.py
```  

### **Example**

**Prompt:**  
```
Tell me about the legend of Aria.
```  

**Output (example):**  
```
Aria was a land where the winds whispered secrets of the stars, and the rivers sang songs of ancient heroes...
```  

---

## **Requirements**

- **Python Version**: 3.7 or later  
- **Python Libraries**:  
  - `openai`  
  - `python-dotenv`  

---

## **How It Works**

1. The `bot` function initializes with a system prompt that sets the tone for responses.  
2. When a user enters a prompt, the script sends it to OpenAI's Chat API using the GPT-3.5-Turbo model.  
3. The API responds with a creative, storytelling-style message.  

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.  

---

## **Acknowledgments**

- OpenAI for providing the GPT-3.5-Turbo model.  
- Python community for the `dotenv` and `openai` libraries.  
