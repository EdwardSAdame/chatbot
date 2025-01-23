from transformers import AutoModelForCausalLM, AutoTokenizer

class SimpleChatbot:
    def __init__(self, model_name="microsoft/DialoGPT-medium"):
        """
        Initialize the chatbot with a pre-trained model and tokenizer.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def get_response(self, user_input):
        """
        Generate a response for the given user input.
        """
        inputs = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)
        response = self.tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        return response

