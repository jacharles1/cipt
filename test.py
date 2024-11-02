class Question:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

questions = [
    Question(
        "Which of the following may pose a “client side” privacy risk?",
        ["A. An employee loading personal data on a company laptop.",
         "B. Failure of a firewall that is protecting the company’s network.",
         "C. A distributed denial of service (DDoS) attack on the organization.",
         "D. A remote employee placing communication software on a company server."],
        "A"
    ),
    Question(
        "You are browsing the web and shopping for new patio furniture. You then open your favorite social media app and begin to scroll through the posts. While doing so, you start noticing ads for patio furniture. This is an example of what?",
        ["A. Direct marketing.",
         "B. Individual advertising.",
         "C. Behavioral advertising.",
         "D. Indirect marketing."],
        "C"
    ),
    Question(
        "Which of the following privacy practices would be most useful to users who are not knowledgeable about protecting their personal information?",
        ["A. Choice.",
         "B. Control.",
         "C. Notice.",
         "D. Consent."],
        "C"
    ),
    Question(
        "Which of the following privacy-related principles would be the main concern during the data usage stage of the data life cycle?",
        ["A. Transparency.",
         "B. Data minimization.",
         "C. Storage limitation.",
         "D. Purpose limitation."],
        "D"
    ),
    Question(
        "Under the EU’s General Data Protection Regulation (GDPR), which of the following types of information would NOT require notification to a supervisory authority in the event of a personal data breach?",
        ["A. Pseudonymized data.",
         "B. Anonymized data.",
         "C. Reidentified data.",
         "D. Deidentified data."],
        "B"
    ),
    Question(
        "Authentication can be accomplished by a variety of mechanisms. Which are the four main categories?",
        ["A. What you know, when you know, where you are, what you are.",
         "B. What you know, what you have, when you know, where you are.",
         "C. What you know, what you have, where you are, what you are.",
         "D. What you know, what you have, where you are, when you know."],
        "C"
    ),
    Question(
        "The acronym PGP stands for:",
        ["A. Protect Good People.",
         "B. Planned Group Protocol.",
         "C. Pretty Good Privacy.",
         "D. Parsed Group Protocol."],
        "C"
    ),
    Question(
        "Julie needs to securely transfer a file containing personal data to Katlyn. They decide to use asymmetric encryption. Select the correct steps that Julie and Katlyn should use.",
        ["A. Julie encrypts the file using her own private key and Katlyn decrypts the file using her own public key.",
         "B. Julie encrypts the file using Katlyn’s public key and Katlyn decrypts the file using her own private key.",
         "C. Julie encrypts the file using her own public key and Katlyn decrypts the file using Julie’s public key.",
         "D. Julie encrypts the file using Katlyn’s private key and Katlyn decrypts the file using Julie’s public key."],
        "B"
    ),
    Question(
        "When purchasing a product from TripeType’s website, a customer must enter basic information into a purchase form. A link to TripeType’s privacy statement is provided on the purchase form. However, it does not disclose that it will use personal information for other purposes. The statement provides that TripeType will store the customer information in its database. A month later, TripeType’s sales team wants to generate new leads and decides to use the information collected from customers. This is an example of what?",
        ["A. Secondary use.",
         "B. Involuntary use.",
         "C. Disapproved use.",
         "D. Selective use."],
        "A"
    ),
    Question(
        "Which of the following explains why it is difficult to regulate what individually identifiable data is?",
        ["A. Many people mistakenly expose personal information online.",
         "B. Personal information means different things to different people.",
         "C. Most legislative bodies are hesitant to enact laws about identifiable data.",
         "D. Data that is not overtly identifiable can be combined to identify individuals."],
        "D"
    ),
    Question(
        "Ubiquitous computing can raise significant concerns about the sheer volume of data that can be collected by a system. Each of the following are necessary considerations when utilizing a data collection process that falls into this category EXCEPT which?",
        ["A. The system should provide end-users with both feedback and control.",
         "B. The system should have obvious value.",
         "C. The retention of data by the system should be limited.",
         "D. The data collected by system should be aggregated and made available to all users."],
        "D"
    ),
    Question(
        "In creating a registration form for a mobile app directed at grade school children, what privacy engineering objective is addressed by asking for grade level instead of date of birth?",
        ["A. Disassociability.",
         "B. Manageability.",
         "C. Security.",
         "D. Predictability"],
        "A"
    ),
    Question(
        "Which of the following is NOT an example of automated decision-making?",
        ["A. Receiving an answer to a support question utilizing a chatbot.",
         "B. Obtaining approval for insurance through an online application.",
         "C. Requesting an emailed catalog from an online retailer.",
         "D. Setting airfare based on browser history and date of purchase."],
        "C"
    ),
    Question(
        "Which of the following circumstances would best be addressed by utilizing radio frequency identification (RFID) technology?",
        ["A. An organization has a high error rate for entering credit card data into its POS system.",
         "B. An organization requires two-way communication between its discoverable devices.",
         "C. An organization needs to develop an encryption-supported network.",
         "D. An organization’s inventory process is taking too long."],
        "D"
    ),
    Question(
        "What type of interference occurs when false or inaccurate information on a credit application results in denial of credit?",
        ["A. Decisional.",
         "B. Intrusion.",
         "C. Disclosure.",
         "D. Appropriation."],
        "A"
    ),
    Question(
        "Which of the following is an objective for privacy engineering?",
        ["A. Encryption.",
         "B. Anonymization.",
         "C. Manageability.",
         "D. Audit."],
        "C"
    ),
    Question(
        "Which of the following technologies allows individuals to participate in a salary survey without revealing the specific salary or personal information of any of the participants?",
        ["A. Secure multiparty computation.",
         "B. Digital rights management.",
         "C. Ciphertext.",
         "D. Homomorphic encryption."],
        "A"
    ),
    Question(
        "An organization wants to enter into a contract with a third-party cloud provider for storage of client personal information. The business head is entering into this agreement to eliminate risk associated with a data breach by transferring the information to the third-party processor. She asks you if this is a good way to eliminate breach risk. Please choose the best response from the choices below.",
        ["A. Third party processors have sole liability for the data they process, because the data is in their possession. We can rely on the security program of the third party since they did not report a data breach in the previous 12 months.",
         "B. Under most privacy and data protection laws, following a data breach, an organization retains liability for personal data that it has collected and transferred to third party processors. Third party processors may share liability for the breach as well. We should routinely validate data protection controls of third parties we are doing business with to make sure our client data is protected properly.",
         "C. Organizations can transfer data to a third party to avert all liability for damages resulting from a data breach. We can use contract language to eliminate the need for third party due diligence.",
         "D. Organizations can only be liable for data breaches if an individual brings a lawsuit. A government agency is able to investigate the organization but can only issue orders to the organization to correct deficiencies in the information security program. Money penalties are only available to individual plaintiffs, or as a result of a class action."],
        "B"
    ),
    Question(
        "When creating a data inventory, it is important to include a range of detailed information on the company's data assets. This information should include how the data is accessed and by whom, how the data is managed, who owns it, where the data is stored, and the ____________ that defines the individual data records and what they contain.",
        ["A. Structured data.",
         "B. Schema.",
         "C. Metadata.",
         "D. Dictionary."],
        "B"
    ),
    Question(
        "Testing during software development generally consists of which two sets of activities?",
        ["A. Implementation and deployment.",
         "B. Alpha and beta testing.",
         "C. Validation and verification.",
         "D. Runtime monitoring and auditing."],
        "C"
    ),
    Question(
        "A marketing lead has collected a large data set of personal information and stored it in a shared folder. The marketing lead controls who has access to the shared folder. The type of access control being used is:",
        ["A. Discretionary.",
         "B. Mandatory.",
         "C. Attribute-Based.",
         "D. Rule-Based."],
        "A"
    ),
    Question(
        "Vulnerability is determined by what two factors?",
        ["A. Probability and confidentiality.",
         "B. Capability and portability.",
         "C. Confidentiality and integrity.",
         "D. Capability and probability."],
        "D"
    ),
    Question(
        "Low-level design concerns the details of the overall design of the system and focuses on improving the quality of programming practices through each of the following mechanisms EXCEPT:",
        ["A. Information hiding.",
         "B. Threat modeling.",
         "C. Reusing existing standard API libraries.",
         "D. Loose coupling."],
        "B"
    ),
    Question(
        "You have been tasked with developing an incident response process for your employer, BrandEnt Company, a media entertainment company. As the senior manager of information privacy, you have been creating privacy-related procedures for the company. There has been an uptick in the number of privacy-related questions being sent to customer service through the website’s generic portal, and the customer service reps are unsure of what to do with the questions. This has led to the director of privacy asking that you work with the IT department to identify, track and resolve privacy-related incidents, as well as with the Information Security team to leverage their existing incident-management process. As you review the questions, you notice that many customers are asking what personal information BrandEnt has collected about them. You grow concerned as you notice that customer service representatives are not always responding to these inquiries. The website doesn’t have a portal dedicated to asking privacy-related questions, and instead a general customer service portal form is being used. This form only requests the customer’s name and their email address. The site does not require authentication to get to this portal. For responses that have been processed, the customer service representatives sent compressed files containing all data collected regarding the individual and sent it to the email provided. You reach out to the Information Security team to request access to their incident ticketing system to determine if the existing process can be leveraged. As you review the incident tickets, you notice several security incidents related to data breaches. After speaking with the Information Security team lead, you learn that the tickets were closed after the vulnerabilities were patched and the system owners were notified. Which common privacy principle is missing at BrandEnt?",
        ["A. Use limitation.",
         "B. Collection limitation.",
         "C. Security safeguard.",
         "D. Data quality."],
        "C"
    ),
    Question(
        "You have been tasked with developing an incident response process for your employer, BrandEnt Company, a media entertainment company. As the senior manager of information privacy, you have been creating privacy-related procedures for the company. There has been an uptick in the number of privacy-related questions being sent to customer service through the website’s generic portal, and the customer service reps are unsure of what to do with the questions. This has led to the director of privacy asking that you work with the IT department to identify, track and resolve privacy-related incidents, as well as with the Information Security team to leverage their existing incident-management process. As you review the questions, you notice that many customers are asking what personal information BrandEnt has collected about them. You grow concerned as you notice that customer service representatives are not always responding to these inquiries. The website doesn’t have a portal dedicated to asking privacy-related questions, and instead a general customer service portal form is being used. This form only requests the customer’s name and their email address. The site does not require authentication to get to this portal. For responses that have been processed, the customer service representatives sent compressed files containing all data collected regarding the individual and sent it to the email provided. You reach out to the Information Security team to request access to their incident ticketing system to determine if the existing process can be leveraged. As you review the incident tickets, you notice several security incidents related to data breaches. After speaking with the Information Security team lead, you learn that the tickets were closed after the vulnerabilities were patched and the system owners were notified.What follow up should be done regarding the data breaches that have already occurred?",
        ["A. Review the fixes applied for the vulnerability and verify that it was applied on all affected systems.",
         "B. Review the information that was breached and determine what levels of notification are required.",
         "C. Send a notification to all customers notifying them of the breach.",
         "D. Nothing is required as the security team reviewed and closed the incident."],
        "B"
    )
]

import random

class FlashcardGame:
    def __init__(self, questions):
        self.questions = questions.copy()  # Make a copy to preserve original list
        random.shuffle(self.questions)     # Randomize the questions order
        self.current_index = 0
        self.score = 0

    def display_question(self):
        if self.current_index >= len(self.questions):
            return None
        return self.questions[self.current_index]

    def check_answer(self, user_answer):
        current_question = self.questions[self.current_index]
        is_correct = user_answer.upper() == current_question.correct_answer
        if is_correct:
            self.score += 1
        self.current_index += 1
        return is_correct

def play_game():
    game = FlashcardGame(questions)
    
    while True:
        question = game.display_question()
        if question is None:
            break
            
        print("\n" + "="*50)
        print("\nQuestion:", question.question)
        print("\nChoices:")
        for choice in question.choices:
            print(choice)
            
        answer = input("\nEnter your answer (A/B/C/D) or 'q' to quit: ").upper()
        if answer == 'Q':
            break
            
        if answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input! Please enter A, B, C, or D")
            continue
            
        is_correct = game.check_answer(answer)
        print("\n✓ Correct!" if is_correct else "\n✗ Incorrect! The correct answer was " + question.correct_answer)
        print(f"Current score: {game.score}/{game.current_index}")
    
    # Show final score
    total_questions = game.current_index
    if total_questions > 0:
        print(f"\nGame Over! Final score: {game.score}/{total_questions}")
        print(f"Percentage: {(game.score/total_questions)*100:.1f}%")

if __name__ == "__main__":
    play_game()
