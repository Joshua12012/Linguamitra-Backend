from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Language, Lesson, Flashcard, Question
from datetime import datetime

# Setup database connection (SQLite in this example)
DATABASE_URL = "sqlite:///linguamitra.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Ensure English language exists (assuming lessons are in English)
language = session.query(Language).filter_by(language_name="English").first()
if not language:
    language = Language(language_name="English")
    session.add(language)
    session.commit()

# Define lessons data (Lessons 1 to 10) based on your document
lessons_data = [
    {
        "title": "Lesson 1: Introduction to Basic Words",
        "content": """Description:
This lesson builds the foundation by introducing everyday English words along with their Marathi translations.

Flashcards (20):
1. House - "I live in a big house." - Pronunciation: haus (/haʊs/) - Marathi: घर
2. Car - "My car is blue." - Pronunciation: kahr (/kɑːr/) - Marathi: गाडी
3. Tree - "The tree is very tall." - Pronunciation: tree (/triː/) - Marathi: झाड
4. Book - "I read a book every night." - Pronunciation: buhk (/bʊk/) - Marathi: पुस्तक
5. Pen - "I write with a pen." - Pronunciation: pen (/pɛn/) - Marathi: लेखणी
6. Chair - "Please sit on the chair." - Pronunciation: chair (/tʃɛər/) - Marathi: खुर्ची
7. Table - "The table is made of wood." - Pronunciation: tey-buhl (/ˈteɪbəl/) - Marathi: टेबल
8. Window - "Open the window for fresh air." - Pronunciation: win-doh (/ˈwɪndoʊ/) - Marathi: खिडकी
9. Door - "Close the door behind you." - Pronunciation: dor (/dɔːr/) - Marathi: दरवाजा
10. Bed - "I sleep on a comfortable bed." - Pronunciation: bed (/bɛd/) - Marathi: पलंग
11. Cup - "Pour water into the cup." - Pronunciation: kuhp (/kʌp/) - Marathi: कप
12. Phone - "My phone is ringing." - Pronunciation: fohn (/foʊn/) - Marathi: फोन
13. Computer - "I use a computer for work." - Pronunciation: kuhm-pyoo-ter (/kəmˈpjuːtər/) - Marathi: संगणक
14. Bag - "She carries a leather bag." - Pronunciation: bag (/bæg/) - Marathi: बॅग
15. Shoe - "These shoes are very comfortable." - Pronunciation: shoo (/ʃuː/) - Marathi: बूट
16. Watch - "He wears a gold watch." - Pronunciation: wach (/wɒtʃ/) - Marathi: घड्याळ
17. Clock - "The clock shows 3 o’clock." - Pronunciation: klok (/klɒk/) - Marathi: घड्याळ (दुसरे स्वरूप)
18. Lamp - "Turn on the lamp, please." - Pronunciation: lamp (/læmp/) - Marathi: दिवा
19. Road - "The road is long and winding." - Pronunciation: rohd (/roʊd/) - Marathi: रस्ता
20. Garden - "The garden is full of flowers." - Pronunciation: gahr-den (/ˈɡɑːrdən/) - Marathi: बाग

Quiz Questions (5):
1. MCQ: What is the Marathi word for "House"? Options: [गाडी, घर, झाड, टेबल] - Answer: घर
2. MCQ: Which item is "संगणक" in Marathi? Options: [Phone, Computer, Bag, Clock] - Answer: Computer
3. Fill-in-the-Blank: "I write with a ______." (Answer: लेखणी) - Answer: Pen
4. MCQ: How do you say "Window" in Marathi? Options: [दरवाजा, खुर्ची, खिडकी, कप] - Answer: खिडकी
5. True/False: "Door" translates as "दरवाजा" in Marathi. - Answer: True

Matching Sets:
Matching Set 1:
- House → _____, Car → _____, Tree → _____, Book → _____ (Answer Key: घर, गाडी, झाड, पुस्तक)
Matching Set 2:
- Pen → _____, Chair → _____, Table → _____, Window → _____ (Answer Key: लेखणी, खुर्ची, टेबल, खिडकी)
""",
        "flashcards": [  # We'll seed flashcards separately using a simplified version from the description
            {"term": "House", "sentence": "I live in a big house.", "pronunciation": "haus (/haʊs/)", "meaning": "घर", "display_order": 1},
            {"term": "Car", "sentence": "My car is blue.", "pronunciation": "kahr (/kɑːr/)", "meaning": "गाडी", "display_order": 2},
            {"term": "Tree", "sentence": "The tree is very tall.", "pronunciation": "tree (/triː/)", "meaning": "झाड", "display_order": 3},
            {"term": "Book", "sentence": "I read a book every night.", "pronunciation": "buhk (/bʊk/)", "meaning": "पुस्तक", "display_order": 4},
            {"term": "Pen", "sentence": "I write with a pen.", "pronunciation": "pen (/pɛn/)", "meaning": "लेखणी", "display_order": 5},
            {"term": "Chair", "sentence": "Please sit on the chair.", "pronunciation": "chair (/tʃɛər/)", "meaning": "खुर्ची", "display_order": 6},
            {"term": "Table", "sentence": "The table is made of wood.", "pronunciation": "tey-buhl (/ˈteɪbəl/)", "meaning": "टेबल", "display_order": 7},
            {"term": "Window", "sentence": "Open the window for fresh air.", "pronunciation": "win-doh (/ˈwɪndoʊ/)", "meaning": "खिडकी", "display_order": 8},
            {"term": "Door", "sentence": "Close the door behind you.", "pronunciation": "dor (/dɔːr/)", "meaning": "दरवाजा", "display_order": 9},
            {"term": "Bed", "sentence": "I sleep on a comfortable bed.", "pronunciation": "bed (/bɛd/)", "meaning": "पलंग", "display_order": 10},
            {"term": "Cup", "sentence": "Pour water into the cup.", "pronunciation": "kuhp (/kʌp/)", "meaning": "कप", "display_order": 11},
            {"term": "Phone", "sentence": "My phone is ringing.", "pronunciation": "fohn (/foʊn/)", "meaning": "फोन", "display_order": 12},
            {"term": "Computer", "sentence": "I use a computer for work.", "pronunciation": "kuhm-pyoo-ter (/kəmˈpjuːtər/)", "meaning": "संगणक", "display_order": 13},
            {"term": "Bag", "sentence": "She carries a leather bag.", "pronunciation": "bag (/bæg/)", "meaning": "बॅग", "display_order": 14},
            {"term": "Shoe", "sentence": "These shoes are very comfortable.", "pronunciation": "shoo (/ʃuː/)", "meaning": "बूट", "display_order": 15},
            {"term": "Watch", "sentence": "He wears a gold watch.", "pronunciation": "wach (/wɒtʃ/)", "meaning": "घड्याळ", "display_order": 16},
            {"term": "Clock", "sentence": "The clock shows 3 o’clock.", "pronunciation": "klok (/klɒk/)", "meaning": "घड्याळ (दुसरे स्वरूप)", "display_order": 17},
            {"term": "Lamp", "sentence": "Turn on the lamp, please.", "pronunciation": "lamp (/læmp/)", "meaning": "दिवा", "display_order": 18},
            {"term": "Road", "sentence": "The road is long and winding.", "pronunciation": "rohd (/roʊd/)", "meaning": "रस्ता", "display_order": 19},
            {"term": "Garden", "sentence": "The garden is full of flowers.", "pronunciation": "gahr-den (/ˈɡɑːrdən/)", "meaning": "बाग", "display_order": 20},
        ],
        "quiz_questions": [
            {"question_text": "What is the Marathi word for \"House\"?", "correct_answer": "घर", "options": ["गाडी", "घर", "झाड", "टेबल"]},
            {"question_text": "Which item is \"संगणक\" in Marathi?", "correct_answer": "Computer", "options": ["Phone", "Computer", "Bag", "Clock"]},
            {"question_text": "I write with a ______.", "correct_answer": "लेखणी", "options": ["Pen", "Chair", "Table", "Lamp"]},
            {"question_text": "How do you say \"Window\" in Marathi?", "correct_answer": "खिडकी", "options": ["दरवाजा", "खुर्ची", "खिडकी", "कप"]},
            {"question_text": "True/False: \"Door\" translates as \"दरवाजा\" in Marathi.", "correct_answer": "True", "options": ["True", "False"]}
        ]
    },
    {
        "title": "Lesson 2: Greetings and Salutations",
        "content": """Description:
This lesson focuses on common greetings and expressions to start conversations in English with Marathi support.

Flashcards (20):
1. Hello - "Hello, how are you?" - Pronunciation: heh-loh (/həˈloʊ/) - Marathi: नमस्कार
2. Good Morning - "Good morning, everyone!" - Pronunciation: good mawr-ning (/ɡʊd ˈmɔːrnɪŋ/) - Marathi: शुभ सकाळ
3. Good Afternoon - "Good afternoon, hope you're well." - Pronunciation: good af-ter-noon (/ɡʊd ˌæftərˈnuːn/) - Marathi: शुभ दुपारी
4. Good Evening - "Good evening, it's nice to see you." - Pronunciation: good ee-ven-ing (/ɡʊd ˈiːvnɪŋ/) - Marathi: शुभ संध्याकाळ
5. Good Night - "Good night and sweet dreams." - Pronunciation: good nyt (/ɡʊd naɪt/) - Marathi: शुभ रात्री
6. How are you? - "How are you today?" - Pronunciation: how ar yoo (/haʊ ɑːr juː/) - Marathi: तुम्ही कसे आहात?
7. I'm Fine - "I'm fine, thank you." - Pronunciation: aim fayn (/aɪm faɪn/) - Marathi: मी ठीक आहे
8. Welcome - "Welcome to our home." - Pronunciation: wel-kuhm (/ˈwɛlkəm/) - Marathi: स्वागत आहे
9. See You Later - "See you later, alligator." - Pronunciation: see yoo ley-ter (/siː juː ˈleɪtər/) - Marathi: नंतर भेटू
10. Goodbye - "Goodbye, have a nice day." - Pronunciation: gud-bye (/ɡʊdˈbaɪ/) - Marathi: अलविदा
11. Nice to Meet You - "Nice to meet you in person." - Pronunciation: nys to meet yoo (/naɪs tuː miːt juː/) - Marathi: तुम्हाला भेटून आनंद झाला
12. Please - "Please pass the salt." - Pronunciation: pleez (/pliːz/) - Marathi: कृपया
13. Thank You - "Thank you for your help." - Pronunciation: thank yoo (/θæŋk juː/) - Marathi: धन्यवाद
14. Sorry - "I'm sorry for being late." - Pronunciation: sor-ee (/ˈsɒri/) - Marathi: माफ करा
15. Excuse Me - "Excuse me, can I get by?" - Pronunciation: ex-kyoos mee (/ɪkˈskjuːz miː/) - Marathi: माफ करा
16. Congratulations - "Congratulations on your success!" - Pronunciation: kuhn-grach-uh-lay-shuns (/kənˌɡrætʃəˈleɪʃənz/) - Marathi: अभिनंदन
17. Good Luck - "Good luck on your exam." - Pronunciation: gud luhk (/ɡʊd lʌk/) - Marathi: शुभेच्छा
18. Take Care - "Take care and stay safe." - Pronunciation: tey-k kayr (/teɪk keər/) - Marathi: काळजी घ्या
19. What's Up? - "What's up, buddy?" - Pronunciation: hwuts up (/wʌts ʌp/) - Marathi: काय चाललं आहे?
20. Have a Nice Day - "Have a nice day ahead." - Pronunciation: hav a nys dey (/hæv ə naɪs deɪ/) - Marathi: छान दिवस जावो

Quiz Questions (5):
1. MCQ: What is the Marathi translation of "Good Morning"? Options: [नमस्कार, शुभ सकाळ, अलविदा, शुभ रात्री] - Answer: शुभ सकाळ
2. MCQ: How do you say "How are you?" in Marathi? Options: [मी ठीक आहे, तुम्ही कसे आहात?, धन्यवाद, नमस्कार] - Answer: तुम्ही कसे आहात?
3. Fill-in-the-Blank: "______ means 'धन्यवाद'." - Answer: Thank You
4. MCQ: Which expression means "नंतर भेटू"? Options: [See You Later, Goodbye, Welcome, Nice to Meet You] - Answer: See You Later
5. True/False: "Excuse me" translates as "माफ करा" in Marathi. - Answer: True

Matching Sets:
Matching Set 1:
Match the following greetings:
- Hello, Good Morning, Good Evening, Goodbye
Answer Key: नमस्कार, शुभ सकाळ, शुभ संध्याकाळ, अलविदा

Matching Set 2:
Match the following polite expressions:
- Please, Thank You, Sorry, Excuse Me
Answer Key: कृपया, धन्यवाद, माफ करा, माफ करा
""",
        "flashcards": [
            {"term": "Hello", "sentence": "Hello, how are you?", "pronunciation": "heh-loh (/həˈloʊ/)", "meaning": "नमस्कार", "display_order": 1},
            {"term": "Good Morning", "sentence": "Good morning, everyone!", "pronunciation": "good mawr-ning (/ɡʊd ˈmɔːrnɪŋ/)", "meaning": "शुभ सकाळ", "display_order": 2},
            {"term": "Good Afternoon", "sentence": "Good afternoon, hope you're well.", "pronunciation": "good af-ter-noon (/ɡʊd ˌæftərˈnuːn/)", "meaning": "शुभ दुपारी", "display_order": 3},
            {"term": "Good Evening", "sentence": "Good evening, it's nice to see you.", "pronunciation": "good ee-ven-ing (/ɡʊd ˈiːvnɪŋ/)", "meaning": "शुभ संध्याकाळ", "display_order": 4},
            {"term": "Good Night", "sentence": "Good night and sweet dreams.", "pronunciation": "good nyt (/ɡʊd naɪt/)", "meaning": "शुभ रात्री", "display_order": 5},
            {"term": "How are you?", "sentence": "How are you today?", "pronunciation": "how ar yoo (/haʊ ɑːr juː/)", "meaning": "तुम्ही कसे आहात?", "display_order": 6},
            {"term": "I'm Fine", "sentence": "I'm fine, thank you.", "pronunciation": "aim fayn (/aɪm faɪn/)", "meaning": "मी ठीक आहे", "display_order": 7},
            {"term": "Welcome", "sentence": "Welcome to our home.", "pronunciation": "wel-kuhm (/ˈwɛlkəm/)", "meaning": "स्वागत आहे", "display_order": 8},
            {"term": "See You Later", "sentence": "See you later, alligator.", "pronunciation": "see yoo ley-ter (/siː juː ˈleɪtər/)", "meaning": "नंतर भेटू", "display_order": 9},
            {"term": "Goodbye", "sentence": "Goodbye, have a nice day.", "pronunciation": "gud-bye (/ɡʊdˈbaɪ/)", "meaning": "अलविदा", "display_order": 10},
            {"term": "Nice to Meet You", "sentence": "Nice to meet you in person.", "pronunciation": "nys to meet yoo (/naɪs tuː miːt juː/)", "meaning": "तुम्हाला भेटून आनंद झाला", "display_order": 11},
            {"term": "Please", "sentence": "Please pass the salt.", "pronunciation": "pleez (/pliːz/)", "meaning": "कृपया", "display_order": 12},
            {"term": "Thank You", "sentence": "Thank you for your help.", "pronunciation": "thank yoo (/θæŋk juː/)", "meaning": "धन्यवाद", "display_order": 13},
            {"term": "Sorry", "sentence": "I'm sorry for being late.", "pronunciation": "sor-ee (/ˈsɒri/)", "meaning": "माफ करा", "display_order": 14},
            {"term": "Excuse Me", "sentence": "Excuse me, can I get by?", "pronunciation": "ex-kyoos mee (/ɪkˈskjuːz miː/)", "meaning": "माफ करा", "display_order": 15},
            {"term": "Congratulations", "sentence": "Congratulations on your success!", "pronunciation": "kuhn-grach-uh-lay-shuns (/kənˌɡrætʃəˈleɪʃənz/)", "meaning": "अभिनंदन", "display_order": 16},
            {"term": "Good Luck", "sentence": "Good luck on your exam.", "pronunciation": "gud luhk (/ɡʊd lʌk/)", "meaning": "शुभेच्छा", "display_order": 17},
            {"term": "Take Care", "sentence": "Take care and stay safe.", "pronunciation": "tey-k kayr (/teɪk keər/)", "meaning": "काळजी घ्या", "display_order": 18},
            {"term": "What's Up?", "sentence": "What's up, buddy?", "pronunciation": "hwuts up (/wʌts ʌp/)", "meaning": "काय चाललं आहे?", "display_order": 19},
            {"term": "Have a Nice Day", "sentence": "Have a nice day ahead.", "pronunciation": "hav a nys dey (/hæv ə naɪs deɪ/)", "meaning": "छान दिवस जावो", "display_order": 20}
        ],
        "quiz_questions": [
            {"question_text": "What is the Marathi translation of \"Good Morning\"?", "correct_answer": "शुभ सकाळ", "options": ["नमस्कार", "शुभ सकाळ", "अलविदा", "शुभ रात्री"]},
            {"question_text": "How do you say \"How are you?\" in Marathi?", "correct_answer": "तुम्ही कसे आहात?", "options": ["मी ठीक आहे", "तुम्ही कसे आहात?", "धन्यवाद", "नमस्कार"]},
            {"question_text": "Fill-in-the-Blank: \"______ means 'धन्यवाद'.\"", "correct_answer": "Thank You", "options": ["Thank You", "Sorry", "Please", "Welcome"]},
            {"question_text": "Which expression means \"नंतर भेटू\"?", "correct_answer": "See You Later", "options": ["See You Later", "Goodbye", "Welcome", "Nice to Meet You"]},
            {"question_text": "True/False: \"Excuse me\" translates as \"माफ करा\" in Marathi.", "correct_answer": "True", "options": ["True", "False"]}
        ]
    },
    {
        "title": "Lesson 3: Numbers and Counting",
        "content": """Description:
Learn English numbers (1–20) with their Marathi translations to build counting skills.

Flashcards (20):
1. One - "I have one apple." - Pronunciation: wuhn (/wʌn/) - Marathi: एक
2. Two - "There are two cats." - Pronunciation: too (/tuː/) - Marathi: दोन
3. Three - "I see three birds." - Pronunciation: three (/θriː/) - Marathi: तीन
4. Four - "She has four pencils." - Pronunciation: fohr (/fɔːr/) - Marathi: चार
5. Five - "There are five chairs." - Pronunciation: faiv (/faɪv/) - Marathi: पाच
6. Six - "Six cars are parked." - Pronunciation: siks (/sɪks/) - Marathi: सहा
7. Seven - "Seven days in a week." - Pronunciation: sev-uhn (/ˈsɛvən/) - Marathi: सात
8. Eight - "I ate eight cookies." - Pronunciation: eyt (/eɪt/) - Marathi: आठ
9. Nine - "Nine birds are singing." - Pronunciation: nain (/naɪn/) - Marathi: नऊ
10. Ten - "Ten fingers on your hands." - Pronunciation: ten (/tɛn/) - Marathi: दहा
11. Eleven - "Eleven is one more than ten." - Pronunciation: ih-lev-uhn (/ɪˈlɛvən/) - Marathi: अकरा
12. Twelve - "There are twelve months." - Pronunciation: twelv (/twɛlv/) - Marathi: बारा
13. Thirteen - "Thirteen is considered unlucky by some." - Pronunciation: thur-teen (/ˌθɜːrˈtiːn/) - Marathi: तेरा
14. Fourteen - "Her birthday is on the fourteenth." - Pronunciation: fohr-teen (/ˌfɔːrˈtiːn/) - Marathi: चौदा
15. Fifteen - "I have fifteen marbles." - Pronunciation: fif-teen (/ˌfɪfˈtiːn/) - Marathi: पंधरा
16. Sixteen - "The bus leaves at sixteen hundred hours." - Pronunciation: siks-teen (/ˌsɪksˈtiːn/) - Marathi: सोळा
17. Seventeen - "Seventeen players are on the team." - Pronunciation: sev-uhn-teen (/ˌsɛvənˈtiːn/) - Marathi: सतरा
18. Eighteen - "She is eighteen years old." - Pronunciation: eyt-teen (/ˌeɪˈtiːn/) - Marathi: अठरा
19. Nineteen - "Nineteen can be written as 19." - Pronunciation: nain-teen (/ˌnaɪnˈtiːn/) - Marathi: एकोणिस
20. Twenty - "Twenty students are in the class." - Pronunciation: twen-tee (/ˈtwɛnti/) - Marathi: वीस

Quiz Questions (5):
1. MCQ: What is the Marathi word for \"Five\"? Options: [पाच, सहा, चार, दोन] - Answer: पाच
2. MCQ: How do you say \"Eight\" in Marathi? Options: [आठ, नऊ, दहा, एक] - Answer: आठ
3. Fill-in-the-Blank: \"______ means 'तीन' in Marathi.\" - Answer: Three
4. MCQ: Which number is written as \"दहा\" in Marathi? Options: [Eight, Ten, Twelve, Six] - Answer: Ten
5. True/False: \"Seventeen\" translates as \"सतरा\" in Marathi. - Answer: True

Matching Sets:
Matching Set 1:
Match the numbers:
- One, Two, Three, Four
Answer Key: एक, दोन, तीन, चार

Matching Set 2:
Match the numbers:
- Five, Six, Seven, Eight
Answer Key: पाच, सहा, सात, आठ
""",
        "flashcards": [
            {"term": "One", "sentence": "I have one apple.", "pronunciation": "wuhn (/wʌn/)", "meaning": "एक", "display_order": 1},
            {"term": "Two", "sentence": "There are two cats.", "pronunciation": "too (/tuː/)", "meaning": "दोन", "display_order": 2},
            {"term": "Three", "sentence": "I see three birds.", "pronunciation": "three (/θriː/)", "meaning": "तीन", "display_order": 3},
            {"term": "Four", "sentence": "She has four pencils.", "pronunciation": "fohr (/fɔːr/)", "meaning": "चार", "display_order": 4},
            {"term": "Five", "sentence": "There are five chairs.", "pronunciation": "faiv (/faɪv/)", "meaning": "पाच", "display_order": 5},
            {"term": "Six", "sentence": "Six cars are parked.", "pronunciation": "siks (/sɪks/)", "meaning": "सहा", "display_order": 6},
            {"term": "Seven", "sentence": "Seven days in a week.", "pronunciation": "sev-uhn (/ˈsɛvən/)", "meaning": "सात", "display_order": 7},
            {"term": "Eight", "sentence": "I ate eight cookies.", "pronunciation": "eyt (/eɪt/)", "meaning": "आठ", "display_order": 8},
            {"term": "Nine", "sentence": "Nine birds are singing.", "pronunciation": "nain (/naɪn/)", "meaning": "नऊ", "display_order": 9},
            {"term": "Ten", "sentence": "Ten fingers on your hands.", "pronunciation": "ten (/tɛn/)", "meaning": "दहा", "display_order": 10},
            {"term": "Eleven", "sentence": "Eleven is one more than ten.", "pronunciation": "ih-lev-uhn (/ɪˈlɛvən/)", "meaning": "अकरा", "display_order": 11},
            {"term": "Twelve", "sentence": "There are twelve months.", "pronunciation": "twelv (/twɛlv/)", "meaning": "बारा", "display_order": 12},
            {"term": "Thirteen", "sentence": "Thirteen is considered unlucky by some.", "pronunciation": "thur-teen (/ˌθɜːrˈtiːn/)", "meaning": "तेरा", "display_order": 13},
            {"term": "Fourteen", "sentence": "Her birthday is on the fourteenth.", "pronunciation": "fohr-teen (/ˌfɔːrˈtiːn/)", "meaning": "चौदा", "display_order": 14},
            {"term": "Fifteen", "sentence": "I have fifteen marbles.", "pronunciation": "fif-teen (/ˌfɪfˈtiːn/)", "meaning": "पंधरा", "display_order": 15},
            {"term": "Sixteen", "sentence": "The bus leaves at sixteen hundred hours.", "pronunciation": "siks-teen (/ˌsɪksˈtiːn/)", "meaning": "सोळा", "display_order": 16},
            {"term": "Seventeen", "sentence": "Seventeen players are on the team.", "pronunciation": "sev-uhn-teen (/ˌsɛvənˈtiːn/)", "meaning": "सतरा", "display_order": 17},
            {"term": "Eighteen", "sentence": "She is eighteen years old.", "pronunciation": "eyt-teen (/ˌeɪˈtiːn/)", "meaning": "अठरा", "display_order": 18},
            {"term": "Nineteen", "sentence": "Nineteen can be written as 19.", "pronunciation": "nain-teen (/ˌnaɪnˈtiːn/)", "meaning": "एकोणिस", "display_order": 19},
            {"term": "Twenty", "sentence": "Twenty students are in the class.", "pronunciation": "twen-tee (/ˈtwɛnti/)", "meaning": "वीस", "display_order": 20}
        ],
        "quiz_questions": [
            {"question_text": "What is the Marathi word for \"Five\"?", "correct_answer": "पाच", "options": ["पाच", "सहा", "चार", "दोन"]},
            {"question_text": "How do you say \"Eight\" in Marathi?", "correct_answer": "आठ", "options": ["आठ", "नऊ", "दहा", "एक"]},
            {"question_text": "Fill-in-the-Blank: \"______ means 'तीन' in Marathi.\"", "correct_answer": "Three", "options": ["Three", "Four", "Two", "One"]},
            {"question_text": "Which number is written as \"दहा\" in Marathi?", "correct_answer": "Ten", "options": ["Eight", "Ten", "Twelve", "Six"]},
            {"question_text": "True/False: \"Seventeen\" translates as \"सतरा\" in Marathi.", "correct_answer": "True", "options": ["True", "False"]}
        ]
    },
    {
        "title": "Lesson 4: Colors and Shapes",
        "content": """Description:
This lesson introduces common colors and basic shapes in English, along with their Marathi names.

Flashcards (20):
-- Colors (10)
1. Red - "The apple is red." - Pronunciation: red (/rɛd/) - Marathi: लाल
2. Blue - "The sky is blue." - Pronunciation: bloo (/bluː/) - Marathi: निळा
3. Green - "The grass is green." - Pronunciation: green (/ɡriːn/) - Marathi: हिरवा
4. Yellow - "The lemon is yellow." - Pronunciation: yel-oh (/ˈjɛloʊ/) - Marathi: पिवळा
5. Orange - "The fruit is orange." - Pronunciation: or-inj (/ˈɒrɪndʒ/) - Marathi: नारंगी
6. Purple - "The flower is purple." - Pronunciation: pur-puhl (/ˈpɜːrpəl/) - Marathi: जांभळा
7. Pink - "She wore a pink dress." - Pronunciation: pink (/pɪŋk/) - Marathi: गुलाबी
8. Black - "The cat is black." - Pronunciation: blak (/blæk/) - Marathi: काळा
9. White - "Snow is white." - Pronunciation: hwayt (/hwaɪt/) - Marathi: पांढरा
10. Brown - "The table is brown." - Pronunciation: brown (/braʊn/) - Marathi: तपकिरी
-- Shapes (10)
11. Circle - "Draw a circle." - Pronunciation: sur-kuhl (/ˈsɜːrkəl/) - Marathi: वर्तुळ
12. Square - "The picture is in a square frame." - Pronunciation: skwair (/skwɛər/) - Marathi: चौरस
13. Triangle - "The sign is a triangle." - Pronunciation: trai-ang-guhl (/ˈtraɪæŋɡəl/) - Marathi: त्रिकोण
14. Rectangle - "Cut a rectangle out of paper." - Pronunciation: rek-tang-guhl (/ˈrɛktæŋɡəl/) - Marathi: आयत
15. Oval - "Draw an oval shape." - Pronunciation: oh-vuhl (/ˈoʊvəl/) - Marathi: अंडाकृती
16. Star - "The star shines brightly." - Pronunciation: stahr (/stɑːr/) - Marathi: तारा
17. Heart - "The heart is a symbol of love." - Pronunciation: hart (/hɑːrt/) - Marathi: हृदय
18. Diamond - "The shape is a diamond." - Pronunciation: dai-muhnd (/ˈdaɪəmənd/) - Marathi: हिरा (आकार)
19. Pentagon - "The building has a pentagon shape." - Pronunciation: pen-tuh-gon (/ˈpɛntəɡɒn/) - Marathi: पंचकोण
20. Hexagon - "A honeycomb has a hexagon pattern." - Pronunciation: hek-suh-gon (/ˈhɛksəɡɒn/) - Marathi: षटकोण

Quiz Questions (5):
1. MCQ: What is the Marathi word for \"Blue\"? Options: [हिरवा, निळा, लाल, पिवळा] - Answer: निळा
2. MCQ: Which shape is \"वर्तुळ\" in Marathi? Options: [Square, Circle, Triangle, Rectangle] - Answer: Circle
3. Fill-in-the-Blank: \"Red\" means \"______\" in Marathi. - Answer: लाल
4. MCQ: How do you say \"Triangle\" in Marathi? Options: [त्रिकोण, आयत, वर्तुळ, चौरस] - Answer: त्रिकोण
5. True/False: \"Oval\" translates as \"अंडाकृती\" in Marathi. - Answer: True

Matching Sets:
Matching Set 1:
Match the following colors:
- Red, Blue, Green, Yellow
Answer Key: लाल, निळा, हिरवा, पिवळा

Matching Set 2:
Match the following shapes:
- Circle, Square, Triangle, Rectangle
Answer Key: वर्तुळ, चौरस, त्रिकोण, आयत
""",
        "flashcards": [
            {"term": "Red", "sentence": "The apple is red.", "pronunciation": "red (/rɛd/)", "meaning": "लाल", "display_order": 1},
            {"term": "Blue", "sentence": "The sky is blue.", "pronunciation": "bloo (/bluː/)", "meaning": "निळा", "display_order": 2},
            {"term": "Green", "sentence": "The grass is green.", "pronunciation": "green (/ɡriːn/)", "meaning": "हिरवा", "display_order": 3},
            {"term": "Yellow", "sentence": "The lemon is yellow.", "pronunciation": "yel-oh (/ˈjɛloʊ/)", "meaning": "पिवळा", "display_order": 4},
            {"term": "Orange", "sentence": "The fruit is orange.", "pronunciation": "or-inj (/ˈɒrɪndʒ/)", "meaning": "नारंगी", "display_order": 5},
            {"term": "Purple", "sentence": "The flower is purple.", "pronunciation": "pur-puhl (/ˈpɜːrpəl/)", "meaning": "जांभळा", "display_order": 6},
            {"term": "Pink", "sentence": "She wore a pink dress.", "pronunciation": "pink (/pɪŋk/)", "meaning": "गुलाबी", "display_order": 7},
            {"term": "Black", "sentence": "The cat is black.", "pronunciation": "blak (/blæk/)", "meaning": "काळा", "display_order": 8},
            {"term": "White", "sentence": "Snow is white.", "pronunciation": "hwayt (/hwaɪt/)", "meaning": "पांढरा", "display_order": 9},
            {"term": "Brown", "sentence": "The table is brown.", "pronunciation": "brown (/braʊn/)", "meaning": "तपकिरी", "display_order": 10},
            {"term": "Circle", "sentence": "Draw a circle.", "pronunciation": "sur-kuhl (/ˈsɜːrkəl/)", "meaning": "वर्तुळ", "display_order": 11},
            {"term": "Square", "sentence": "The picture is in a square frame.", "pronunciation": "skwair (/skwɛər/)", "meaning": "चौरस", "display_order": 12},
            {"term": "Triangle", "sentence": "The sign is a triangle.", "pronunciation": "trai-ang-guhl (/ˈtraɪæŋɡəl/)", "meaning": "त्रिकोण", "display_order": 13},
            {"term": "Rectangle", "sentence": "Cut a rectangle out of paper.", "pronunciation": "rek-tang-guhl (/ˈrɛktæŋɡəl/)", "meaning": "आयत", "display_order": 14},
            {"term": "Oval", "sentence": "Draw an oval shape.", "pronunciation": "oh-vuhl (/ˈoʊvəl/)", "meaning": "अंडाकृती", "display_order": 15},
            {"term": "Star", "sentence": "The star shines brightly.", "pronunciation": "stahr (/stɑːr/)", "meaning": "तारा", "display_order": 16},
            {"term": "Heart", "sentence": "The heart is a symbol of love.", "pronunciation": "hart (/hɑːrt/)", "meaning": "हृदय", "display_order": 17},
            {"term": "Diamond", "sentence": "The shape is a diamond.", "pronunciation": "dai-muhnd (/ˈdaɪəmənd/)", "meaning": "हिरा (आकार)", "display_order": 18},
            {"term": "Pentagon", "sentence": "The building has a pentagon shape.", "pronunciation": "pen-tuh-gon (/ˈpɛntəɡɒn/)", "meaning": "पंचकोण", "display_order": 19},
            {"term": "Hexagon", "sentence": "A honeycomb has a hexagon pattern.", "pronunciation": "hek-suh-gon (/ˈhɛksəɡɒn/)", "meaning": "षटकोण", "display_order": 20}
        ],
        "quiz_questions": [
            {"question_text": "What is the Marathi word for \"Blue\"?", "correct_answer": "निळा", "options": ["हिरवा", "निळा", "लाल", "पिवळा"]},
            {"question_text": "Which shape is \"वर्तुळ\" in Marathi?", "correct_answer": "Circle", "options": ["Square", "Circle", "Triangle", "Rectangle"]},
            {"question_text": "Fill-in-the-Blank: \"Red\" means \"______\" in Marathi.", "correct_answer": "लाल", "options": ["लाल", "निळा", "हिरवा", "पिवळा"]},
            {"question_text": "How do you say \"Triangle\" in Marathi?", "correct_answer": "त्रिकोण", "options": ["त्रिकोण", "आयत", "वर्तुळ", "चौरस"]},
            {"question_text": "True/False: \"Oval\" translates as \"अंडाकृती\" in Marathi.", "correct_answer": "True", "options": ["True", "False"]}
        ]
    },
    {
        "title": "Lesson 5: Family and Relationships",
        "content": """Description:
This lesson teaches vocabulary related to family members and interpersonal relationships in English with Marathi equivalents.

Flashcards (20):
1. Mother - "My mother is kind." - Pronunciation: muh-thur (/ˈmʌðər/) - Marathi: आई
2. Father - "My father works hard." - Pronunciation: fah-thur (/ˈfɑːðər/) - Marathi: वडील
3. Brother - "I have one brother." - Pronunciation: bruh-thur (/ˈbrʌðər/) - Marathi: भाऊ
4. Sister - "My sister loves to sing." - Pronunciation: sis-ter (/ˈsɪstər/) - Marathi: बहिणी
5. Grandmother - "My grandmother tells stories." - Pronunciation: gran-muh-thur (/ˈɡrænˌmʌðər/) - Marathi: आजी
6. Grandfather - "My grandfather is wise." - Pronunciation: gran-fah-thur (/ˈɡrænˌfɑːðər/) - Marathi: आजोबा
7. Uncle - "My uncle visits every summer." - Pronunciation: uhn-kuhl (/ˈʌŋkəl/) - Marathi: काका / मामा
8. Aunt - "My aunt makes delicious food." - Pronunciation: ant (/ænt/) - Marathi: काकू / मावशी
9. Cousin - "My cousin is my best friend." - Pronunciation: kuh-zuhn (/ˈkʌzən/) - Marathi: चुलत भाऊ / बहिणी
10. Son - "Their son is in school." - Pronunciation: suhn (/sʌn/) - Marathi: मुलगा
11. Daughter - "Her daughter loves art." - Pronunciation: daw-ter (/ˈdɔːtər/) - Marathi: मुलगी
12. Nephew - "My nephew is very playful." - Pronunciation: nep-yoo (/ˈnɛpjuː/) - Marathi: भाऊपुत्र
13. Niece - "My niece is learning to read." - Pronunciation: nees (/niːs/) - Marathi: भाऊमुलगी
14. Wife - "His wife is a doctor." - Pronunciation: whyf (/waɪf/) - Marathi: पत्नी
15. Husband - "Her husband is an engineer." - Pronunciation: huhz-buhnd (/ˈhʌzbənd/) - Marathi: नवरा
16. Friend - "A friend is always there for you." - Pronunciation: frend (/frɛnd/) - Marathi: मित्र
17. Neighbor - "My neighbor is very kind." - Pronunciation: nay-bor (/ˈneɪbər/) - Marathi: शेजारी
18. Teacher - "The teacher explains lessons clearly." - Pronunciation: tee-cher (/ˈtiːtʃər/) - Marathi: शिक्षक / शिक्षिका
19. Child - "Every child deserves love." - Pronunciation: chahyld (/tʃaɪld/) - Marathi: मुलगा / मुलगी
20. Parent - "Every parent cares deeply." - Pronunciation: peh-ruhnt (/ˈpɛrənt/) - Marathi: पालक

Quiz Questions (5):
1. MCQ: What is the Marathi translation of \"Mother\"? Options: [वडील, आई, बहिणी, मित्र] - Answer: आई
2. MCQ: How do you say \"Father\" in Marathi? Options: [आई, वडील, भाऊ, पालक] - Answer: वडील
3. Fill-in-the-Blank: \"My ______ is my best friend.\" (Answer: Cousin) - Answer: Cousin
4. MCQ: Which word means \"पत्नी\" in Marathi? Options: [Wife, Husband, Daughter, Friend] - Answer: Wife
5. True/False: \"Neighbor\" translates as \"शेजारी\" in Marathi. - Answer: True

Matching Sets:
Matching Set 1:
Match the family member with its translation:
- Mother, Father, Brother, Sister
Answer Key: आई, वडील, भाऊ, बहिणी

Matching Set 2:
Match these family roles:
- Uncle, Aunt, Son, Daughter
Answer Key: काका/मामा, काकू/मावशी, मुलगा, मुलगी
""",
        "flashcards": [
            {"term": "Mother", "sentence": "My mother is kind.", "pronunciation": "muh-thur (/ˈmʌðər/)", "meaning": "आई", "display_order": 1},
            {"term": "Father", "sentence": "My father works hard.", "pronunciation": "fah-thur (/ˈfɑːðər/)", "meaning": "वडील", "display_order": 2},
            {"term": "Brother", "sentence": "I have one brother.", "pronunciation": "bruh-thur (/ˈbrʌðər/)", "meaning": "भाऊ", "display_order": 3},
            {"term": "Sister", "sentence": "My sister loves to sing.", "pronunciation": "sis-ter (/ˈsɪstər/)", "meaning": "बहिणी", "display_order": 4},
            {"term": "Grandmother", "sentence": "My grandmother tells stories.", "pronunciation": "gran-muh-thur (/ˈɡrænˌmʌðər/)", "meaning": "आजी", "display_order": 5},
            {"term": "Grandfather", "sentence": "My grandfather is wise.", "pronunciation": "gran-fah-thur (/ˈɡrænˌfɑːðər/)", "meaning": "आजोबा", "display_order": 6},
            {"term": "Uncle", "sentence": "My uncle visits every summer.", "pronunciation": "uhn-kuhl (/ˈʌŋkəl/)", "meaning": "काका / मामा", "display_order": 7},
            {"term": "Aunt", "sentence": "My aunt makes delicious food.", "pronunciation": "ant (/ænt/)", "meaning": "काकू / मावशी", "display_order": 8},
            {"term": "Cousin", "sentence": "My cousin is my best friend.", "pronunciation": "kuh-zuhn (/ˈkʌzən/)", "meaning": "चुलत भाऊ / बहिणी", "display_order": 9},
            {"term": "Son", "sentence": "Their son is in school.", "pronunciation": "suhn (/sʌn/)", "meaning": "मुलगा", "display_order": 10},
            {"term": "Daughter", "sentence": "Her daughter loves art.", "pronunciation": "daw-ter (/ˈdɔːtər/)", "meaning": "मुलगी", "display_order": 11},
            {"term": "Nephew", "sentence": "My nephew is very playful.", "pronunciation": "nep-yoo (/ˈnɛpjuː/)", "meaning": "भाऊपुत्र", "display_order": 12},
            {"term": "Niece", "sentence": "My niece is learning to read.", "pronunciation": "nees (/niːs/)", "meaning": "भाऊमुलगी", "display_order": 13},
            {"term": "Wife", "sentence": "His wife is a doctor.", "pronunciation": "whyf (/waɪf/)", "meaning": "पत्नी", "display_order": 14},
            {"term": "Husband", "sentence": "Her husband is an engineer.", "pronunciation": "huhz-buhnd (/ˈhʌzbənd/)", "meaning": "नवरा", "display_order": 15},
            {"term": "Friend", "sentence": "A friend is always there for you.", "pronunciation": "frend (/frɛnd/)", "meaning": "मित्र", "display_order": 16},
            {"term": "Neighbor", "sentence": "My neighbor is very kind.", "pronunciation": "nay-bor (/ˈneɪbər/)", "meaning": "शेजारी", "display_order": 17},
            {"term": "Teacher", "sentence": "The teacher explains lessons clearly.", "pronunciation": "tee-cher (/ˈtiːtʃər/)", "meaning": "शिक्षक / शिक्षिका", "display_order": 18},
            {"term": "Child", "sentence": "Every child deserves love.", "pronunciation": "chahyld (/tʃaɪld/)", "meaning": "मुलगा / मुलगी", "display_order": 19},
            {"term": "Parent", "sentence": "Every parent cares deeply.", "pronunciation": "peh-ruhnt (/ˈpɛrənt/)", "meaning": "पालक", "display_order": 20}
        ],
        "quiz_questions": [
            {"question_text": "What is the Marathi translation of \"Mother\"?", "correct_answer": "आई", "options": ["वडील", "आई", "बहिणी", "मित्र"]},
            {"question_text": "How do you say \"Father\" in Marathi?", "correct_answer": "वडील", "options": ["आई", "वडील", "भाऊ", "पालक"]},
            {"question_text": "Fill-in-the-Blank: \"My ______ is my best friend.\"", "correct_answer": "Cousin", "options": ["Cousin", "Uncle", "Aunt", "Sibling"]},
            {"question_text": "Which word means \"पत्नी\" in Marathi?", "correct_answer": "Wife", "options": ["Wife", "Husband", "Daughter", "Friend"]},
            {"question_text": "True/False: \"Neighbor\" translates as \"शेजारी\" in Marathi.", "correct_answer": "True", "options": ["True", "False"]}
        ]
    },
    {
        "title": "Lesson 6: Common Verbs and Actions",
        "content": """Description:
This lesson introduces frequently used English verbs that describe daily actions, with their Marathi meanings.

Flashcards (20):
1. Run - "I run every morning." - Pronunciation: ruhn (/rʌn/) - Marathi: धावणे
2. Walk - "We walk to school." - Pronunciation: wawk (/wɔːk/) - Marathi: चालणे
3. Eat - "I eat breakfast at 8 AM." - Pronunciation: eet (/iːt/) - Marathi: खाणे
4. Drink - "They drink water after exercise." - Pronunciation: dringk (/drɪŋk/) - Marathi: पिणे
5. Sleep - "He sleeps for eight hours." - Pronunciation: sleep (/sliːp/) - Marathi: झोपणे
6. Read - "She reads a book daily." - Pronunciation: reed (/riːd/) - Marathi: वाचणे
7. Write - "I write letters to my friend." - Pronunciation: ryt (/raɪt/) - Marathi: लेखन करणे
8. Speak - "They speak English in class." - Pronunciation: speek (/spiːk/) - Marathi: बोलणे
9. Listen - "Please listen carefully." - Pronunciation: lis-uhn (/ˈlɪsən/) - Marathi: ऐकणे
10. Jump - "The child can jump high." - Pronunciation: jʌmp (/dʒʌmp/) - Marathi: उडी मारणे
11. Dance - "We dance at the festival." - Pronunciation: dans (/dæns/) - Marathi: नृत्य करणे
12. Sing - "They sing beautiful songs." - Pronunciation: sing (/sɪŋ/) - Marathi: गाणे
13. Cook - "She cooks delicious meals." - Pronunciation: kuk (/kʊk/) - Marathi: स्वयंपाक करणे
14. Drive - "I drive to work every day." - Pronunciation: draiv (/draɪv/) - Marathi: चालवणे
15. Swim - "He likes to swim in the pool." - Pronunciation: swim (/swɪm/) - Marathi: पोहत जाणे
16. Play - "The children play in the park." - Pronunciation: pley (/pleɪ/) - Marathi: खेळणे
17. Work - "My father works in an office." - Pronunciation: wurk (/wɜːrk/) - Marathi: काम करणे
18. Laugh - "They laugh at the funny joke." - Pronunciation: laf (/læf/) - Marathi: हसणे
19. Cry - "Sometimes, babies cry." - Pronunciation: krahy (/kraɪ/) - Marathi: रडणे
20. Think - "I think before I speak." - Pronunciation: thingk (/θɪŋk/) - Marathi: विचार करणे

Quiz Questions (5):
1. MCQ: What is the Marathi translation of \"Run\"? Options: [चालणे, धावणे, उडी मारणे, बोलणे] - Answer: धावणे
2. MCQ: How do you say \"Eat\" in Marathi? Options: [खाणे, पिणे, झोपणे, वाचणे] - Answer: खाणे
3. Fill-in-the-Blank: \"To ______ means 'बोलणे' in Marathi.\" - Answer: Speak
4. MCQ: Which verb means \"रडणे\" in Marathi? Options: [Laugh, Cry, Think, Play] - Answer: Cry
5. True/False: \"Swim\" translates as \"पोहत जाणे\" in Marathi. - Answer: True

Matching Sets:
Matching Set 1:
Match the verbs:
- Run, Walk, Eat, Drink
Answer Key: धावणे, चालणे, खाणे, पिणे

Matching Set 2:
Match the verbs:
- Read, Write, Speak, Listen
Answer Key: वाचणे, लेखन करणे, बोलणे, ऐकणे
""",
        "flashcards": [
            {"term": "Run", "sentence": "I run every morning.", "pronunciation": "ruhn (/rʌn/)", "meaning": "धावणे", "display_order": 1},
            {"term": "Walk", "sentence": "We walk to school.", "pronunciation": "wawk (/wɔːk/)", "meaning": "चालणे", "display_order": 2},
            {"term": "Eat", "sentence": "I eat breakfast at 8 AM.", "pronunciation": "eet (/iːt/)", "meaning": "खाणे", "display_order": 3},
            {"term": "Drink", "sentence": "They drink water after exercise.", "pronunciation": "dringk (/drɪŋk/)", "meaning": "पिणे", "display_order": 4},
            {"term": "Sleep", "sentence": "He sleeps for eight hours.", "pronunciation": "sleep (/sliːp/)", "meaning": "झोपणे", "display_order": 5},
            {"term": "Read", "sentence": "She reads a book daily.", "pronunciation": "reed (/riːd/)", "meaning": "वाचणे", "display_order": 6},
            {"term": "Write", "sentence": "I write letters to my friend.", "pronunciation": "ryt (/raɪt/)", "meaning": "लेखन करणे", "display_order": 7},
            {"term": "Speak", "sentence": "They speak English in class.", "pronunciation": "speek (/spiːk/)", "meaning": "बोलणे", "display_order": 8},
            {"term": "Listen", "sentence": "Please listen carefully.", "pronunciation": "lis-uhn (/ˈlɪsən/)", "meaning": "ऐकणे", "display_order": 9},
            {"term": "Jump", "sentence": "The child can jump high.", "pronunciation": "jʌmp (/dʒʌmp/)", "meaning": "उडी मारणे", "display_order": 10},
            {"term": "Dance", "sentence": "We dance at the festival.", "pronunciation": "dans (/dæns/)", "meaning": "नृत्य करणे", "display_order": 11},
            {"term": "Sing", "sentence": "They sing beautiful songs.", "pronunciation": "sing (/sɪŋ/)", "meaning": "गाणे", "display_order": 12},
            {"term": "Cook", "sentence": "She cooks delicious meals.", "pronunciation": "kuk (/kʊk/)", "meaning": "स्वयंपाक करणे", "display_order": 13},
            {"term": "Drive", "sentence": "I drive to work every day.", "pronunciation": "draiv (/draɪv/)", "meaning": "चालवणे", "display_order": 14},
            {"term": "Swim", "sentence": "He likes to swim in the pool.", "pronunciation": "swim (/swɪm/)", "meaning": "पोहत जाणे", "display_order": 15},
            {"term": "Play", "sentence": "The children play in the park.", "pronunciation": "pley (/pleɪ/)", "meaning": "खेळणे", "display_order": 16},
            {"term": "Work", "sentence": "My father works in an office.", "pronunciation": "wurk (/wɜːrk/)", "meaning": "काम करणे", "display_order": 17},
            {"term": "Laugh", "sentence": "They laugh at the funny joke.", "pronunciation": "laf (/læf/)", "meaning": "हसणे", "display_order": 18},
            {"term": "Cry", "sentence": "Sometimes, babies cry.", "pronunciation": "krahy (/kraɪ/)", "meaning": "रडणे", "display_order": 19},
            {"term": "Think", "sentence": "I think before I speak.", "pronunciation": "thingk (/θɪŋk/)", "meaning": "विचार करणे", "display_order": 20}
        ],
        "quiz_questions": [
            {"question_text": "What is the Marathi translation of \"Run\"?", "correct_answer": "धावणे", "options": ["चालणे", "धावणे", "उडी मारणे", "बोलणे"]},
            {"question_text": "How do you say \"Eat\" in Marathi?", "correct_answer": "खाणे", "options": ["खाणे", "पिणे", "झोपणे", "वाचणे"]},
            {"question_text": "Fill-in-the-Blank: \"To ______ means 'बोलणे' in Marathi.\"", "correct_answer": "Speak", "options": ["Speak", "Read", "Write", "Listen"]},
            {"question_text": "Which verb means \"रडणे\" in Marathi?", "correct_answer": "Cry", "options": ["Laugh", "Cry", "Think", "Play"]},
            {"question_text": "True/False: \"Swim\" translates as \"पोहत जाणे\" in Marathi.", "correct_answer": "True", "options": ["True", "False"]}
        ]
    },
    {
        "title": "Lesson 7: Everyday Expressions",
        "content": """Description:
This lesson covers common phrases and expressions used in daily English conversation with their Marathi translations.

Flashcards (20):
1. Thank You - "Thank you for your help." - Pronunciation: thank yoo (/θæŋk juː/) - Marathi: धन्यवाद
2. Please - "Please pass the salt." - Pronunciation: pleez (/pliːz/) - Marathi: कृपया
3. Sorry - "I'm sorry for the mistake." - Pronunciation: sor-ee (/ˈsɒri/) - Marathi: माफ करा
4. Excuse Me - "Excuse me, can I get by?" - Pronunciation: ex-kyoos mee (/ɪkˈskjuːz miː/) - Marathi: माफ करा
5. You're Welcome - "You're welcome, anytime." - Pronunciation: yoor wel-kuhm (/jʊr ˈwɛlkəm/) - Marathi: स्वागत आहे
6. Good Morning - "Good morning, have a nice day." - Pronunciation: good mawr-ning (/ɡʊd ˈmɔːrnɪŋ/) - Marathi: शुभ सकाळ
7. Good Night - "Good night, sleep tight." - Pronunciation: good nyt (/ɡʊd naɪt/) - Marathi: शुभ रात्री
8. How are You? - "How are you doing today?" - Pronunciation: how ar yoo (/haʊ ɑːr juː/) - Marathi: तुम्ही कसे आहात?
9. I'm Fine - "I'm fine, thank you." - Pronunciation: aim fayn (/aɪm faɪn/) - Marathi: मी ठीक आहे
10. What's Up? - "What's up, buddy?" - Pronunciation: hwuts up (/wʌts ʌp/) - Marathi: काय चाललं आहे?
11. Nice to Meet You - "Nice to meet you." - Pronunciation: nys to meet yoo (/naɪs tuː miːt juː/) - Marathi: तुम्हाला भेटून आनंद झाला
12. See You - "See you soon." - Pronunciation: see yoo (/siː juː/) - Marathi: पुन्हा भेटू
13. Take Care - "Take care of yourself." - Pronunciation: tey-k kayr (/teɪk keər/) - Marathi: काळजी घ्या
14. Congratulations - "Congratulations on your success!" - Pronunciation: kuhn-grach-uh-lay-shuns (/kənˌɡrætʃəˈleɪʃənz/) - Marathi: अभिनंदन
15. Good Luck - "Good luck with your project." - Pronunciation: gud luhk (/ɡʊd lʌk/) - Marathi: शुभेच्छा
16. All the Best - "All the best for your exam." - Pronunciation: awl the best (/ɔːl ðə bɛst/) - Marathi: सर्व शुभेच्छा
17. Bless You - "Bless you (after a sneeze)." - Pronunciation: bles yoo (/blɛs juː/) - Marathi: आशीर्वाद
18. Cheers - "Cheers to our success." - Pronunciation: cheerz (/tʃɪərz/) - Marathi: चियर्स
19. Welcome Back - "Welcome back, we missed you." - Pronunciation: wel-kuhm bak (/ˈwɛlkəm bæk/) - Marathi: पुन्हा स्वागत आहे
20. Good Job - "Good job on your presentation." - Pronunciation: gud jahb (/ɡʊd dʒɒb/) - Marathi: छान काम

Quiz Questions (5):
1. MCQ: What is the Marathi translation of \"Thank You\"? Options: [कृपया, माफ करा, धन्यवाद, स्वागत आहे] - Answer: धन्यवाद
2. MCQ: How do you say \"I'm Fine\" in Marathi? Options: [मी ठीक आहे, मी रुग्ण आहे, धन्यवाद, नमस्कार] - Answer: मी ठीक आहे
3. Fill-in-the-Blank: \"______ means 'काळजी घ्या'.\" - Answer: Take Care
4. MCQ: Which phrase translates as \"पुन्हा भेटू\"? Options: [See You, Welcome Back, Take Care, Excuse Me] - Answer: See You
5. True/False: \"Good Luck\" means \"शुभेच्छा\" in Marathi. - Answer: True

Matching Sets:
Matching Set 1:
Match the expressions:
- Thank You, Please, Sorry, Excuse Me
Answer Key: धन्यवाद, कृपया, माफ करा, माफ करा

Matching Set 2:
Match the greetings:
- Good Morning, Good Night, How are You?, I'm Fine
Answer Key: शुभ सकाळ, शुभ रात्री, तुम्ही कसे आहात?, मी ठीक आहे
""",
        "flashcards": [
            {"term": "Thank You", "sentence": "Thank you for your help.", "pronunciation": "thank yoo (/θæŋk juː/)", "meaning": "धन्यवाद", "display_order": 1},
            {"term": "Please", "sentence": "Please pass the salt.", "pronunciation": "pleez (/pliːz/)", "meaning": "कृपया", "display_order": 2},
            {"term": "Sorry", "sentence": "I'm sorry for the mistake.", "pronunciation": "sor-ee (/ˈsɒri/)", "meaning": "माफ करा", "display_order": 3},
            {"term": "Excuse Me", "sentence": "Excuse me, can I get by?", "pronunciation": "ex-kyoos mee (/ɪkˈskjuːz miː/)", "meaning": "माफ करा", "display_order": 4},
            {"term": "You're Welcome", "sentence": "You're welcome, anytime.", "pronunciation": "yoor wel-kuhm (/jʊr ˈwɛlkəm/)", "meaning": "स्वागत आहे", "display_order": 5},
            {"term": "Good Morning", "sentence": "Good morning, have a nice day.", "pronunciation": "good mawr-ning (/ɡʊd ˈmɔːrnɪŋ/)", "meaning": "शुभ सकाळ", "display_order": 6},
            {"term": "Good Night", "sentence": "Good night, sleep tight.", "pronunciation": "good nyt (/ɡʊd naɪt/)", "meaning": "शुभ रात्री", "display_order": 7},
            {"term": "How are You?", "sentence": "How are you doing today?", "pronunciation": "how ar yoo (/haʊ ɑːr juː/)", "meaning": "तुम्ही कसे आहात?", "display_order": 8},
            {"term": "I'm Fine", "sentence": "I'm fine, thank you.", "pronunciation": "aim fayn (/aɪm faɪn/)", "meaning": "मी ठीक आहे", "display_order": 9},
            {"term": "What's Up?", "sentence": "What's up, buddy?", "pronunciation": "hwuts up (/wʌts ʌp/)", "meaning": "काय चाललं आहे?", "display_order": 10},
            {"term": "Nice to Meet You", "sentence": "Nice to meet you.", "pronunciation": "nys to meet yoo (/naɪs tuː miːt juː/)", "meaning": "तुम्हाला भेटून आनंद झाला", "display_order": 11},
            {"term": "See You", "sentence": "See you soon.", "pronunciation": "see yoo (/siː juː/)", "meaning": "पुन्हा भेटू", "display_order": 12},
            {"term": "Take Care", "sentence": "Take care of yourself.", "pronunciation": "tey-k kayr (/teɪk keər/)", "meaning": "काळजी घ्या", "display_order": 13},
            {"term": "Congratulations", "sentence": "Congratulations on your success!", "pronunciation": "kuhn-grach-uh-lay-shuns (/kənˌɡrætʃəˈleɪʃənz/)", "meaning": "अभिनंदन", "display_order": 14},
            {"term": "Good Luck", "sentence": "Good luck with your project.", "pronunciation": "gud luhk (/ɡʊd lʌk/)", "meaning": "शुभेच्छा", "display_order": 15},
            {"term": "All the Best", "sentence": "All the best for your exam.", "pronunciation": "awl the best (/ɔːl ðə bɛst/)", "meaning": "सर्व शुभेच्छा", "display_order": 16},
            {"term": "Bless You", "sentence": "Bless you (after a sneeze).", "pronunciation": "bles yoo (/blɛs juː/)", "meaning": "आशीर्वाद", "display_order": 17},
            {"term": "Cheers", "sentence": "Cheers to our success.", "pronunciation": "cheerz (/tʃɪərz/)", "meaning": "चियर्स", "display_order": 18},
            {"term": "Welcome Back", "sentence": "Welcome back, we missed you.", "pronunciation": "wel-kuhm bak (/ˈwɛlkəm bæk/)", "meaning": "पुन्हा स्वागत आहे", "display_order": 19},
            {"term": "Good Job", "sentence": "Good job on your presentation.", "pronunciation": "gud jahb (/ɡʊd dʒɒb/)", "meaning": "छान काम", "display_order": 20}
        ],
        "quiz_questions": [
            {"question_text": "What is the Marathi translation of \"Thank You\"?", "correct_answer": "धन्यवाद", "options": ["कृपया", "माफ करा", "धन्यवाद", "स्वागत आहे"]},
            {"question_text": "How do you say \"I'm Fine\" in Marathi?", "correct_answer": "मी ठीक आहे", "options": ["मी ठीक आहे", "मी रुग्ण आहे", "धन्यवाद", "नमस्कार"]},
            {"question_text": "Fill-in-the-Blank: \"______ means 'काळजी घ्या'.\"", "correct_answer": "Take Care", "options": ["Take Care", "Thank You", "Sorry", "Welcome"]},
            {"question_text": "Which phrase translates as \"पुन्हा भेटू\"?", "correct_answer": "See You", "options": ["See You", "Welcome Back", "Take Care", "Excuse Me"]},
            {"question_text": "True/False: \"Good Luck\" means \"शुभेच्छा\" in Marathi.", "correct_answer": "True", "options": ["True", "False"]}
        ]
    },
    {
        "title": "Lesson 8: Time and Date",
        "content": """Description:
This lesson teaches vocabulary related to time, dates, and days of the week in English with their Marathi translations.

Flashcards (20):
1. Morning - "I wake up in the morning." - Pronunciation: mawr-ning (/ˈmɔːrnɪŋ/) - Marathi: सकाळ
2. Afternoon - "Lunch is served in the afternoon." - Pronunciation: af-ter-noon (/ˌæftərˈnuːn/) - Marathi: दुपारी
3. Evening - "The evening is calm." - Pronunciation: ee-ven-ing (/ˈiːvnɪŋ/) - Marathi: संध्याकाळ
4. Night - "Stars shine at night." - Pronunciation: nyt (/naɪt/) - Marathi: रात्री
5. Today - "Today is a special day." - Pronunciation: tuh-dey (/təˈdeɪ/) - Marathi: आज
6. Tomorrow - "We will meet tomorrow." - Pronunciation: tuh-mawr-oh (/təˈmɒroʊ/) - Marathi: उद्या
7. Yesterday - "Yesterday was fun." - Pronunciation: yes-ter-dey (/ˈjɛstərdeɪ/) - Marathi: काल
8. Week - "There are seven days in a week." - Pronunciation: week (/wiːk/) - Marathi: आठवडा
9. Month - "A month has around 30 days." - Pronunciation: munth (/mʌnθ/) - Marathi: महिना
10. Year - "A year has 12 months." - Pronunciation: yeer (/jɪər/) - Marathi: वर्ष
11. Monday - "Monday is the first day of the week." - Pronunciation: muhn-dey (/ˈmʌndeɪ/) - Marathi: सोमवार
12. Tuesday - "Tuesday comes after Monday." - Pronunciation: tyooz-dey (/ˈtuːzdeɪ/) - Marathi: मंगळवार
13. Wednesday - "Wednesday is mid-week." - Pronunciation: wenz-dey (/ˈwɛnzdeɪ/) - Marathi: बुधवार
14. Thursday - "Thursday is approaching." - Pronunciation: thurz-dey (/ˈθɜːrzdeɪ/) - Marathi: गुरुवार
15. Friday - "Friday is the start of the weekend." - Pronunciation: frahy-dey (/ˈfraɪdeɪ/) - Marathi: शुक्रवार
16. Saturday - "Saturday is for leisure." - Pronunciation: sat-er-dey (/ˈsætərdeɪ/) - Marathi: शनिवार
17. Sunday - "Sunday is a day of rest." - Pronunciation: suhn-dey (/ˈsʌndeɪ/) - Marathi: रविवार
18. Hour - "An hour has 60 minutes." - Pronunciation: auhr (/aʊər/) - Marathi: तास
19. Minute - "Wait for a minute." - Pronunciation: min-it (/ˈmɪnɪt/) - Marathi: मिनिट
20. Second - "There are 60 seconds in a minute." - Pronunciation: sek-uhnd (/ˈsɛkənd/) - Marathi: सेकंद

Quiz Questions (5):
1. MCQ: What is the Marathi word for \"Morning\"? Options: [दुपारी, रात्री, सकाळ, आज] - Answer: सकाळ
2. MCQ: How do you say \"Today\" in Marathi? Options: [उद्या, काल, आज, शनिवार] - Answer: आज
3. Fill-in-the-Blank: \"______ means 'उद्या' in Marathi.\" - Answer: Tomorrow
4. MCQ: Which day is \"बुधवार\" in English? Options: [Monday, Tuesday, Wednesday, Friday] - Answer: Wednesday
5. True/False: \"Minute\" translates as \"मिनिट\" in Marathi. - Answer: True

Matching Sets:
Matching Set 1:
Match the time-related words:
- Morning, Afternoon, Evening, Night
Answer Key: सकाळ, दुपारी, संध्याकाळ, रात्री

Matching Set 2:
Match the days of the week:
- Monday, Tuesday, Wednesday, Thursday
Answer Key: सोमवार, मंगळवार, बुधवार, गुरुवार
""",
        "flashcards": [
            {"term": "Morning", "sentence": "I wake up in the morning.", "pronunciation": "mawr-ning (/ˈmɔːrnɪŋ/)", "meaning": "सकाळ", "display_order": 1},
            {"term": "Afternoon", "sentence": "Lunch is served in the afternoon.", "pronunciation": "af-ter-noon (/ˌæftərˈnuːn/)", "meaning": "दुपारी", "display_order": 2},
            {"term": "Evening", "sentence": "The evening is calm.", "pronunciation": "ee-ven-ing (/ˈiːvnɪŋ/)", "meaning": "संध्याकाळ", "display_order": 3},
            {"term": "Night", "sentence": "Stars shine at night.", "pronunciation": "nyt (/naɪt/)", "meaning": "रात्री", "display_order": 4},
            {"term": "Today", "sentence": "Today is a special day.", "pronunciation": "tuh-dey (/təˈdeɪ/)", "meaning": "आज", "display_order": 5},
            {"term": "Tomorrow", "sentence": "We will meet tomorrow.", "pronunciation": "tuh-mawr-oh (/təˈmɒroʊ/)", "meaning": "उद्या", "display_order": 6},
            {"term": "Yesterday", "sentence": "Yesterday was fun.", "pronunciation": "yes-ter-dey (/ˈjɛstərdeɪ/)", "meaning": "काल", "display_order": 7},
            {"term": "Week", "sentence": "There are seven days in a week.", "pronunciation": "week (/wiːk/)", "meaning": "आठवडा", "display_order": 8},
            {"term": "Month", "sentence": "A month has around 30 days.", "pronunciation": "munth (/mʌnθ/)", "meaning": "महिना", "display_order": 9},
            {"term": "Year", "sentence": "A year has 12 months.", "pronunciation": "yeer (/jɪər/)", "meaning": "वर्ष", "display_order": 10},
            {"term": "Monday", "sentence": "Monday is the first day of the week.", "pronunciation": "muhn-dey (/ˈmʌndeɪ/)", "meaning": "सोमवार", "display_order": 11},
            {"term": "Tuesday", "sentence": "Tuesday comes after Monday.", "pronunciation": "tyooz-dey (/ˈtuːzdeɪ/)", "meaning": "मंगळवार", "display_order": 12},
            {"term": "Wednesday", "sentence": "Wednesday is mid-week.", "pronunciation": "wenz-dey (/ˈwɛnzdeɪ/)", "meaning": "बुधवार", "display_order": 13},
            {"term": "Thursday", "sentence": "Thursday is approaching.", "pronunciation": "thurz-dey (/ˈθɜːrzdeɪ/)", "meaning": "गुरुवार", "display_order": 14},
            {"term": "Friday", "sentence": "Friday is the start of the weekend.", "pronunciation": "frahy-dey (/ˈfraɪdeɪ/)", "meaning": "शुक्रवार", "display_order": 15},
            {"term": "Saturday", "sentence": "Saturday is for leisure.", "pronunciation": "sat-er-dey (/ˈsætərdeɪ/)", "meaning": "शनिवार", "display_order": 16},
            {"term": "Sunday", "sentence": "Sunday is a day of rest.", "pronunciation": "suhn-dey (/ˈsʌndeɪ/)", "meaning": "रविवार", "display_order": 17},
            {"term": "Hour", "sentence": "An hour has 60 minutes.", "pronunciation": "auhr (/aʊər/)", "meaning": "तास", "display_order": 18},
            {"term": "Minute", "sentence": "Wait for a minute.", "pronunciation": "min-it (/ˈmɪnɪt/)", "meaning": "मिनिट", "display_order": 19},
            {"term": "Second", "sentence": "There are 60 seconds in a minute.", "pronunciation": "sek-uhnd (/ˈsɛkənd/)", "meaning": "सेकंद", "display_order": 20}
        ],
        "quiz_questions": [
            {"question_text": "What is the Marathi word for \"Morning\"?", "correct_answer": "सकाळ", "options": ["दुपारी", "रात्री", "सकाळ", "आज"]},
            {"question_text": "How do you say \"Today\" in Marathi?", "correct_answer": "आज", "options": ["उद्या", "काल", "आज", "शनिवार"]},
            {"question_text": "Fill-in-the-Blank: \"______ means 'उद्या' in Marathi.\"", "correct_answer": "Tomorrow", "options": ["Tomorrow", "Yesterday", "Today", "Next"]},
            {"question_text": "Which day is \"बुधवार\" in English?", "correct_answer": "Wednesday", "options": ["Monday", "Tuesday", "Wednesday", "Friday"]},
            {"question_text": "True/False: \"Minute\" translates as \"मिनिट\" in Marathi.", "correct_answer": "True", "options": ["True", "False"]}
        ]
    },
    {
        "title": "Lesson 9: Food and Drinks",
        "content": """Description:
This lesson introduces names of common foods and beverages in English with their Marathi translations, useful for everyday situations.

Flashcards (20):
1. Water - "I drink water every day." - Pronunciation: waw-ter (/ˈwɔːtər/) - Marathi: पाणी
2. Bread - "I eat bread for breakfast." - Pronunciation: bred (/brɛd/) - Marathi: पाव
3. Milk - "Milk is nutritious." - Pronunciation: milk (/mɪlk/) - Marathi: दूध
4. Rice - "Rice is a staple food." - Pronunciation: rahys (/raɪs/) - Marathi: भात
5. Fruit - "I love eating fresh fruit." - Pronunciation: froot (/fruːt/) - Marathi: फळ
6. Vegetable - "Vegetables are healthy." - Pronunciation: vej-tuh-buhl (/ˈvɛdʒtəbl/) - Marathi: भाजीपाला
7. Meat - "He prefers chicken meat." - Pronunciation: meet (/miːt/) - Marathi: मांस
8. Soup - "A bowl of soup is warming." - Pronunciation: soop (/suːp/) - Marathi: सूप
9. Juice - "Orange juice is refreshing." - Pronunciation: joos (/dʒuːs/) - Marathi: रस
10. Coffee - "I need a cup of coffee." - Pronunciation: kaw-fee (/ˈkɒfi/) - Marathi: कॉफी
11. Tea - "Tea is popular here." - Pronunciation: tee (/tiː/) - Marathi: चहा
12. Egg - "Eggs are a good source of protein." - Pronunciation: eg (/ɛɡ/) - Marathi: अंडी
13. Cheese - "I like cheese on my sandwich." - Pronunciation: cheez (/tʃiːz/) - Marathi: चीज
14. Pasta - "Pasta is an Italian dish." - Pronunciation: pas-tuh (/ˈpæstə/) - Marathi: पास्ता
15. Salad - "Fresh salad is delicious." - Pronunciation: sal-uhd (/ˈsæləd/) - Marathi: सलाड
16. Sandwich - "I had a ham sandwich." - Pronunciation: sand-wich (/ˈsændwɪtʃ/) - Marathi: सँडविच
17. Pizza - "Pizza is my favorite food." - Pronunciation: pee-zuh (/ˈpiːtsə/) - Marathi: पिझ्झा
18. Burger - "A burger with fries is tasty." - Pronunciation: bur-ger (/ˈbɜːrɡər/) - Marathi: बर्गर
19. Cake - "Birthday cake is sweet." - Pronunciation: kayk (/keɪk/) - Marathi: केक
20. Ice Cream - "I love vanilla ice cream." - Pronunciation: ays kreem (/aɪs kriːm/) - Marathi: आइसक्रीम

Quiz Questions (5):
1. MCQ: What is the Marathi translation of \"Milk\"? Options: [पाणी, पाव, दूध, भात] - Answer: दूध
2. MCQ: Which word means \"भात\" in Marathi? Options: [Rice, Bread, Meat, Juice] - Answer: Rice
3. Fill-in-the-Blank: \"______ means 'चहा' in Marathi.\" - Answer: Tea
4. MCQ: How do you say \"Juice\" in Marathi? Options: [रस, सूप, कॉफी, पिझ्झा] - Answer: रस
5. True/False: \"Egg\" translates as \"अंडी\" in Marathi. - Answer: True

Matching Sets:
Matching Set 1:
Match the food items:
- Water, Bread, Milk, Rice
Answer Key: पाणी, पाव, दूध, भात

Matching Set 2:
Match the food items:
- Fruit, Vegetable, Soup, Juice
Answer Key: फळ, भाजीपाला, सूप, रस
""",
        "flashcards": [
            {"term": "Water", "sentence": "I drink water every day.", "pronunciation": "waw-ter (/ˈwɔːtər/)", "meaning": "पाणी", "display_order": 1},
            {"term": "Bread", "sentence": "I eat bread for breakfast.", "pronunciation": "bred (/brɛd/)", "meaning": "पाव", "display_order": 2},
            {"term": "Milk", "sentence": "Milk is nutritious.", "pronunciation": "milk (/mɪlk/)", "meaning": "दूध", "display_order": 3},
            {"term": "Rice", "sentence": "Rice is a staple food.", "pronunciation": "rahys (/raɪs/)", "meaning": "भात", "display_order": 4},
            {"term": "Fruit", "sentence": "I love eating fresh fruit.", "pronunciation": "froot (/fruːt/)", "meaning": "फळ", "display_order": 5},
            {"term": "Vegetable", "sentence": "Vegetables are healthy.", "pronunciation": "vej-tuh-buhl (/ˈvɛdʒtəbl/)", "meaning": "भाजीपाला", "display_order": 6},
            {"term": "Meat", "sentence": "He prefers chicken meat.", "pronunciation": "meet (/miːt/)", "meaning": "मांस", "display_order": 7},
            {"term": "Soup", "sentence": "A bowl of soup is warming.", "pronunciation": "soop (/suːp/)", "meaning": "सूप", "display_order": 8},
            {"term": "Juice", "sentence": "Orange juice is refreshing.", "pronunciation": "joos (/dʒuːs/)", "meaning": "रस", "display_order": 9},
            {"term": "Coffee", "sentence": "I need a cup of coffee.", "pronunciation": "kaw-fee (/ˈkɒfi/)", "meaning": "कॉफी", "display_order": 10},
            {"term": "Tea", "sentence": "Tea is popular here.", "pronunciation": "tee (/tiː/)", "meaning": "चहा", "display_order": 11},
            {"term": "Egg", "sentence": "Eggs are a good source of protein.", "pronunciation": "eg (/ɛɡ/)", "meaning": "अंडी", "display_order": 12},
            {"term": "Cheese", "sentence": "I like cheese on my sandwich.", "pronunciation": "cheez (/tʃiːz/)", "meaning": "चीज", "display_order": 13},
            {"term": "Pasta", "sentence": "Pasta is an Italian dish.", "pronunciation": "pas-tuh (/ˈpæstə/)", "meaning": "पास्ता", "display_order": 14},
            {"term": "Salad", "sentence": "Fresh salad is delicious.", "pronunciation": "sal-uhd (/ˈsæləd/)", "meaning": "सलाड", "display_order": 15},
            {"term": "Sandwich", "sentence": "I had a ham sandwich.", "pronunciation": "sand-wich (/ˈsændwɪtʃ/)", "meaning": "सँडविच", "display_order": 16},
            {"term": "Pizza", "sentence": "Pizza is my favorite food.", "pronunciation": "pee-zuh (/ˈpiːtsə/)", "meaning": "पिझ्झा", "display_order": 17},
            {"term": "Burger", "sentence": "A burger with fries is tasty.", "pronunciation": "bur-ger (/ˈbɜːrɡər/)", "meaning": "बर्गर", "display_order": 18},
            {"term": "Cake", "sentence": "Birthday cake is sweet.", "pronunciation": "kayk (/keɪk/)", "meaning": "केक", "display_order": 19},
            {"term": "Ice Cream", "sentence": "I love vanilla ice cream.", "pronunciation": "ays kreem (/aɪs kriːm/)", "meaning": "आइसक्रीम", "display_order": 20}
        ],
        "quiz_questions": [
            {"question_text": "What is the Marathi translation of \"Milk\"?", "correct_answer": "दूध", "options": ["पाणी", "पाव", "दूध", "भात"]},
            {"question_text": "Which word means \"भात\" in Marathi?", "correct_answer": "Rice", "options": ["Rice", "Bread", "Meat", "Juice"]},
            {"question_text": "Fill-in-the-Blank: \"______ means 'चहा' in Marathi.\"", "correct_answer": "Tea", "options": ["Tea", "Coffee", "Bread", "Cake"]},
            {"question_text": "How do you say \"Juice\" in Marathi?", "correct_answer": "रस", "options": ["रस", "सूप", "कॉफी", "पिझ्झा"]},
            {"question_text": "True/False: \"Egg\" translates as \"अंडी\" in Marathi.", "correct_answer": "True", "options": ["True", "False"]}
        ]
    },
    {
        "title": "Lesson 10: Directions and Places",
        "content": """Description:
This lesson teaches vocabulary for giving directions and naming common places in English with Marathi translations.

Flashcards (20):
1. Left - "Turn left at the corner." - Pronunciation: left (/lɛft/) - Marathi: डावीकडे
2. Right - "The shop is on the right." - Pronunciation: rahyt (/raɪt/) - Marathi: उजवीकडे
3. Straight - "Go straight ahead." - Pronunciation: streyt (/streɪt/) - Marathi: सरळ
4. Back - "Walk back to the start." - Pronunciation: bak (/bæk/) - Marathi: मागे
5. North - "The north wind is cold." - Pronunciation: nawth (/nɔːrθ/) - Marathi: उत्तरेकडे
6. South - "They live in the south." - Pronunciation: sawth (/saʊθ/) - Marathi: दक्षिणेकडे
7. East - "The sun rises in the east." - Pronunciation: eest (/iːst/) - Marathi: पूर्वेकडे
8. West - "The mountains lie to the west." - Pronunciation: west (/wɛst/) - Marathi: पश्चिमेकडे
9. Street - "I live on a quiet street." - Pronunciation: street (/striːt/) - Marathi: रस्ता
10. Avenue - "They moved to a new avenue." - Pronunciation: av-uh-nyoo (/ˈævəˌnjuː/) - Marathi: मार्ग
11. Road - "This road is busy." - Pronunciation: rohd (/roʊd/) - Marathi: रस्ता
12. Intersection - "The intersection is crowded." - Pronunciation: in-ter-sek-shun (/ˌɪntərˈsɛkʃən/) - Marathi: चौक
13. School - "The school is near my home." - Pronunciation: skool (/skuːl/) - Marathi: शाळा
14. Hospital - "He was taken to the hospital." - Pronunciation: hos-pi-tl (/ˈhɒspɪtl/) - Marathi: रुग्णालय
15. Market - "I went to the market for vegetables." - Pronunciation: mahr-kit (/ˈmɑːrkɪt/) - Marathi: बाजार
16. Park - "The park is full of trees." - Pronunciation: pahrk (/pɑːrk/) - Marathi: उद्यान
17. Bank - "I deposited money in the bank." - Pronunciation: bank (/bæŋk/) - Marathi: बँक
18. Post Office - "The post office is open today." - Pronunciation: pohst aw-fis (/poʊst ˈɒfɪs/) - Marathi: पोस्ट ऑफिस
19. Library - "I study in the library." - Pronunciation: lahy-brer-ee (/ˈlaɪbrɛri/) - Marathi: ग्रंथालय
20. Station - "The train station is busy." - Pronunciation: stay-shuhn (/ˈsteɪʃən/) - Marathi: स्टेशन

Quiz Questions (5):
1. MCQ: What is the Marathi word for \"Left\"? Options: [उजवीकडे, डावीकडे, सरळ, मागे] - Answer: डावीकडे
2. MCQ: How do you say \"School\" in Marathi? Options: [रस्ता, शाळा, बँक, पोस्ट ऑफिस] - Answer: शाळा
3. Fill-in-the-Blank: \"______ means 'बाजार' in Marathi.\" - Answer: Market
4. MCQ: Which direction is \"पूर्वेकडे\" in English? Options: [West, South, East, North] - Answer: East
5. True/False: \"Post Office\" translates as \"पोस्ट ऑफिस\" in Marathi. - Answer: True

Matching Sets:
Matching Set 1:
Match the directional words:
- Left, Right, North, South
Answer Key: डावीकडे, उजवीकडे, उत्तरेकडे, दक्षिणेकडे

Matching Set 2:
Match the places:
- School, Hospital, Market, Library
Answer Key: शाळा, रुग्णालय, बाजार, ग्रंथालय
""",
        "flashcards": [
            {"term": "Left", "sentence": "Turn left at the corner.", "pronunciation": "left (/lɛft/)", "meaning": "डावीकडे", "display_order": 1},
            {"term": "Right", "sentence": "The shop is on the right.", "pronunciation": "rahyt (/raɪt/)", "meaning": "उजवीकडे", "display_order": 2},
            {"term": "Straight", "sentence": "Go straight ahead.", "pronunciation": "streyt (/streɪt/)", "meaning": "सरळ", "display_order": 3},
            {"term": "Back", "sentence": "Walk back to the start.", "pronunciation": "bak (/bæk/)", "meaning": "मागे", "display_order": 4},
            {"term": "North", "sentence": "The north wind is cold.", "pronunciation": "nawth (/nɔːrθ/)", "meaning": "उत्तरेकडे", "display_order": 5},
            {"term": "South", "sentence": "They live in the south.", "pronunciation": "sawth (/saʊθ/)", "meaning": "दक्षिणेकडे", "display_order": 6},
            {"term": "East", "sentence": "The sun rises in the east.", "pronunciation": "eest (/iːst/)", "meaning": "पूर्वेकडे", "display_order": 7},
            {"term": "West", "sentence": "The mountains lie to the west.", "pronunciation": "west (/wɛst/)", "meaning": "पश्चिमेकडे", "display_order": 8},
            {"term": "Street", "sentence": "I live on a quiet street.", "pronunciation": "street (/striːt/)", "meaning": "रस्ता", "display_order": 9},
            {"term": "Avenue", "sentence": "They moved to a new avenue.", "pronunciation": "av-uh-nyoo (/ˈævəˌnjuː/)", "meaning": "मार्ग", "display_order": 10},
            {"term": "Road", "sentence": "This road is busy.", "pronunciation": "rohd (/roʊd/)", "meaning": "रस्ता", "display_order": 11},
            {"term": "Intersection", "sentence": "The intersection is crowded.", "pronunciation": "in-ter-sek-shun (/ˌɪntərˈsɛkʃən/)", "meaning": "चौक", "display_order": 12},
            {"term": "School", "sentence": "The school is near my home.", "pronunciation": "skool (/skuːl/)", "meaning": "शाळा", "display_order": 13},
            {"term": "Hospital", "sentence": "He was taken to the hospital.", "pronunciation": "hos-pi-tl (/ˈhɒspɪtl/)", "meaning": "रुग्णालय", "display_order": 14},
            {"term": "Market", "sentence": "I went to the market for vegetables.", "pronunciation": "mahr-kit (/ˈmɑːrkɪt/)", "meaning": "बाजार", "display_order": 15},
            {"term": "Park", "sentence": "The park is full of trees.", "pronunciation": "pahrk (/pɑːrk/)", "meaning": "उद्यान", "display_order": 16},
            {"term": "Bank", "sentence": "I deposited money in the bank.", "pronunciation": "bank (/bæŋk/)", "meaning": "बँक", "display_order": 17},
            {"term": "Post Office", "sentence": "The post office is open today.", "pronunciation": "pohst aw-fis (/poʊst ˈɒfɪs/)", "meaning": "पोस्ट ऑफिस", "display_order": 18},
            {"term": "Library", "sentence": "I study in the library.", "pronunciation": "lahy-brer-ee (/ˈlaɪbrɛri/)", "meaning": "ग्रंथालय", "display_order": 19},
            {"term": "Station", "sentence": "The train station is busy.", "pronunciation": "stay-shuhn (/ˈsteɪʃən/)", "meaning": "स्टेशन", "display_order": 20}
        ],
        "quiz_questions": [
            {"question_text": "What is the Marathi word for \"Left\"?", "correct_answer": "डावीकडे", "options": ["उजवीकडे", "डावीकडे", "सरळ", "मागे"]},
            {"question_text": "How do you say \"School\" in Marathi?", "correct_answer": "शाळा", "options": ["रस्ता", "शाळा", "बँक", "पोस्ट ऑफिस"]},
            {"question_text": "Fill-in-the-Blank: \"______ means 'बाजार' in Marathi.\"", "correct_answer": "Market", "options": ["Market", "Street", "Avenue", "Bank"]},
            {"question_text": "Which direction is \"पूर्वेकडे\" in English?", "correct_answer": "East", "options": ["West", "South", "East", "North"]},
            {"question_text": "True/False: \"Post Office\" translates as \"पोस्ट ऑफिस\" in Marathi.", "correct_answer": "True", "options": ["True", "False"]}
        ]
    }
]

# Seed lessons, flashcards, and quiz questions
for idx, lesson_data in enumerate(lessons_data, start=1):
    # Create lesson
    lesson = Lesson(
        title=lesson_data["title"],
        content=lesson_data["content"],
        language_id=language.language_id,
        level="beginner",  # Assuming all are beginner for this example; modify if needed
        lesson_order=idx
    )
    session.add(lesson)
    session.commit()  # Commit to get lesson_id

    # Insert flashcards
    for fc in lesson_data["flashcards"]:
        flashcard = Flashcard(
            lesson_id=lesson.lesson_id,
            term=fc["term"],
            sentence=fc["sentence"],
            pronunciation=fc["pronunciation"],
            meaning=fc["meaning"],
            display_order=fc["display_order"]
        )
        session.add(flashcard)
    session.commit()

    # Insert quiz questions
    for qq in lesson_data["quiz_questions"]:
        question = Question(
            lesson_id=lesson.lesson_id,
            question_text=qq["question_text"],
            correct_answer=qq["correct_answer"],
            options=qq["options"]
        )
        session.add(question)
    session.commit()

print("✅ All lessons, flashcards, and quiz questions have been added successfully!")
