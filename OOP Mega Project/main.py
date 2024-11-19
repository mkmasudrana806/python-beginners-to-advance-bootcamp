import google.generativeai as genai

# NLP model class
class NLPModel:
    def get_model(self):
        GOOGLE_API_KEY="AIzaSyD-TpraSOLFina4VVLvcLFcj4UcAKyWnh8"
        genai.configure(api_key=GOOGLE_API_KEY)

        model = genai.GenerativeModel('gemini-pro')
        return model


# NLPApp class
class NLPApp(NLPModel):
    def __init__(self):
        self.__database = {}
        self.app_home()
    
    # app homepage
    def app_home(self):
        user_input = input("""
            1. Not a member? Register
            2. Already a member? Login
            3. Don't want continuation? Exit!
            """)
        
        if user_input == "1":
            # Register
            self.__register()
        
        elif user_input == "2":
            # Login
            self.__login()
            
        elif user_input == "3":
            # Exit app
            exit()
            
    
        # app menu
   
   # app menu
    def app_menu(self):
        user_input = input("""
        Hi!, How would you like to proced?
        
            1. Sentiment Analysis
            2. Language Translation
            3. Language Detection
            """)
        
        if user_input == "1":
            # sentiment analysis
            self.__sentiment_analysis()
        
        elif user_input == "2":
            # language translation
            self.__language_translation()
            
            
        elif user_input == "3":
            # language detection
            self.__language_detection()
            
    

    # register
    def __register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        if email in self.__database:
            print("Email is already exist!")
            
        else:
            self.__database[email] = [name, password]
            print('Registration successfull! login with application')
            self.app_home()

    # login
    def __login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        if email in self.__database:
            if self.__database[email][1] == password:
                self.app_menu()
            else:
                print('Incorrect password!')
                self.__login()
        else:
            print('Email not found!, please register first!')
            self.app_home()
                

    # sentiment analysis
    def __sentiment_analysis(self):
        user_text = input('Enter your text: ')
        model = super().get_model()
        response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
        results = response.text
        print(results)
        self.app_menu()
        
    # language translation
    def __language_translation(self):
        user_text = input('Enter your text: ')
        model = super().get_model()
        response = model.generate_content(f"Give me hindi translation of this sentence: {user_text}")
        results = response.text
        print(results)
        self.app_menu()
        
    # language detection
    def __language_detection(self):
        user_text = input('Enter your text: ')
        model = super().get_model()
        response = model.generate_content(f"Detect the language of this sentence: {user_text}")
        results = response.text
        print(results)
        self.app_menu()
        
# run the NLP app
if __name__ == "__main__":
    app = NLPApp()
    