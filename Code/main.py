import wikipediaapi
import os
import logging
import shutil  

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_wikipedia_summary(word):
    try:
        user_agent = "MyPythonApp/1.0 (hetpateldgpatel@gmail.com)"
        wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
        logging.info(f"Searching Wikipedia for word: {word}")
        page = wiki.page(word)
        if page.exists():
            logging.info(f"Wikipedia page found for word: {word}")
            return page.summary
        else:  
            logging.warning(f"Wikipedia page not found for word: {word}")
            print(f"[Warning] Oops! Wikipedia page not found for your search: '{word}'.\nTry again later...")
            return None
    except Exception as e:  
        logging.error(f"Error loading Wikipedia summary: {str(e)}")
        print("[Error] An error occurred while loading the Wikipedia page.")
        return None

def save_to_txt(folder_path, filename, content):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logging.info(f"Created directory: {folder_path}")
        full_path = os.path.join(folder_path, filename)
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(content)
            logging.info(f"File stored at: {full_path}")
    except Exception as e:  
        logging.error(f"Error saving file: {str(e)}")

def center_text(text):
    terminal_width = shutil.get_terminal_size().columns
    return text.center(terminal_width)

def main():
    print("=" * 160)
    print(center_text("Wikipedia Search Tool"))
    print("=" * 160)
    print()

    while True:  
        word = input("Enter the word you want to search on Wikipedia: ").strip()
        print("-" * 160)
        
        if not word:  
            print("Please enter a valid word!")
            print()
            continue
        
        summary = fetch_wikipedia_summary(word)

        if summary:  
            folder_path = "Python-Task1-HetPatel"
            filename = f"{word}_wikipedia_summary.txt"
            save_to_txt(folder_path, filename, summary)
            print("-" * 160)
            print(f"Wikipedia summary stored in: {os.path.join(folder_path, filename)}")
        print("=" * 160)

        other_search = input("Do you want to search for another word? (yes/no): ").strip().lower()
        print("-" * 160)
        
        if other_search != 'yes':
            print()
            print(center_text("Thank you for using the Wikipedia search engine! See you next time."))
            print()
            print("=" * 160)
            print()
            break

if __name__ == "__main__":
    main()
