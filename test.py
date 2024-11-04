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
    ),
    Question(
        "A company that provides tutoring services to school children developed a service that was intended to allow tutors to provide services to children virtually through their home computers. However, the program unintentionally allowed anyone to register and interact with these children. This made it possible for strangers to contact the children without parental consent. Based on Solove’s taxonomy of privacy model, which privacy problem exists in this scenario?",
        ["A. Increased Exposure.",
         "B. Increased Disclosure.",
         "C. Increased Accessibility.",
         "D. Increased Appropriation."],
        "C"
    ),
    Question(
        "Jenny completed a purchase on a website and was presented with a pop-up box on the final page that read, 'Thank you for your purchase! We will email you in the future about related product and services. Please select an option below to opt-out.' The three buttons below the message read, 'Do Not Opt-Out,' 'Decline' and 'Skip This Step.' Jenny selected the option to 'Skip This Step,' believing it was the best choice to continue her browsing experience. This is an example of which of the following?",
        ["A. Dark pattern.",
         "B. Clickstream pattern.",
         "C. Guided marketing model.",
         "D. Ad choice design approach."],
        "A"
    ),
    Question(
        "A cloud service provider wants to advertise the benefits of its service by publishing information that shows how its users have interacted with the platform. It plans to publish only aggregated data to not identify its customers. What would be a best practice before publishing its aggregated data?",
        ["A. The company should review its legal basis for keeping the sales information and determine whether the customers have provided consent.",
         "B. The company should maintain a log of its employees that accessed the database to ensure the underlying data has not been modified prior to aggregation.",
         "C. The company should ensure its procedures for responding to information requests by customers allow it to correct any errors in the published data.",
         "D. The company should evaluate whether publicly available or other sources of information are sufficient to reconstruct the aggregated database and identify individuals."],
        "D"
    ),
    Question(
        "A utility company discovers that it is missing first names for some of its customers. It purchases householder data from a credit reference agency to obtain names and attempt to find a match in their customer database. The two companies will apply a logical rule that attributes the utility bills and assigns liability for such debts to the individual with the most active credit history at an address. What kind of privacy threat is most likely to occur based on this scenario?",
        ["A. The data could become distorted.",
         "B. An individual’s identity could be appropriated.",
         "C. The data could be used to identify an individual.",
         "D. An individual could be placed under illegal surveillance."],
        "A"
    ),
    Question(
        "An organization is using Scrum methodology to develop in-house solutions for customer support, which involves how personal data of its customers is processed. During each sprint, the team examines the implications the changes have on customer privacy and ensures the process remains compliant with their privacy program. When a change occurs in the system during development, there is a change management procedure that triggers an evaluation of whether the engineering, design, implementation or testing requirements needs to change within the development process. This example is a component of which of the below?",
        ["A. Code audit process.",
         "B. Code review process.",
         "C. Software evolution process.",
         "D. Runtime behavior monitoring."],
        "C"
    ),
    Question(
        "Beth’s client is keen on ensuring that her team considers privacy and data protection issues at every phase of each product’s lifecycle. Which of the following enables the team to test various phases of the lifecycle for potential risks?",
        ["A. Binding corporate rules (BCR).",
         "B. Transfer impact assessment (TIA).",
         "C. Record of processing activity (RoPA).",
         "D. Data protection impact assessment (DPIA)."],
        "D"
    ),
    Question(
        "A flaw in the requirements, design or implementation that occurs when one or more lines of computer source code do not correctly verify the authorization of an access attempt is known as a(n)?",
        ["A. Error.",
         "B. Fault.",
         "C. Defect.",
         "D. Failure."],
        "C"
    ),
    Question(
        "Which of the following statements about aggregated data sets is TRUE?",
        ["A. Combining multiple partial-identifiers can lead to individuals becoming identifiable.",
         "B. Removing names from the data set will prevent the individual from becoming identified.",
         "C. Generalizing the date of birth to age makes this data point unattributable to an individual.",
         "D. Disclosing the data set with no outlier data points will ensure individuals cannot be identified."],
        "A"
    ),
    Question(
        "Which of the following is a subset of artificial intelligence that learns through repetition of computational tasks and processes unstructured data such as text and images?",
        ["A. Deep learning.",
         "B. Neural networks.",
         "C. Context-aware computing.",
         "D. Queries of structured data."],
        "A"
    ),
    Question(
        "Which of the following statements is NOT correct with respect to the unmasking of user identities?",
        ["A. Unmasking existing users’ identities could violate the GDPR and other laws and regulations regarding notice.",
         "B. Unmasking existing users’ identities could invite potential class action claims and affect your company’s reputation.",
         "C. Unmasking existing users’ identities would constitute an unfair and deceptive trade practice under the FTC Act, Section 5.",
         "D. Unmasking existing users’ identities would cause your company to gain customers and be better able to compete with competitors."],
        "D"
    ),
    Question(
        "Allowing users the ability to mask their identities on the platform aligns with which of the FTC’s Five Fair Information Practice Principles?",
        ["A. Notice principle.",
         "B. Choice principle.",
         "C. Security principle.",
         "D. Transparency principle."],
        "B"
    ),
    Question(
        "A vulnerability in the customer relationship management (CRM) software is being exploited by malicious hackers. The CRM vendor indicated that a quick-fix to the software will not be available for a week. The patch management process will take another 3 days to complete after receiving the quick-fix. What compensating control should be put in place to protect the CRM system and customers’ personal data in the meantime?",
        ["A. Inform customers about the situation and the potential risk to their personal data.",
         "B. Monitor the CRM system and review the system logs for anomalies on a daily basis.",
         "C. Shut down the CRM system until the patch is installed and email customers about delays.",
         "D. Shorten the testing period for the patch management process to release the patch sooner."],
        "B"
    ),
    Question(
        "A company is developing a web-based chatbot that will ask customers to input information about preferences and hobbies to direct them to relevant products and services. Which of the following is the first step software developers should take to ensure only the data needed is collected?",
        ["A. Work with stakeholders to clearly define the project’s goals and identify which data components are necessary for success.",
         "B. Create logs for interactions with the chatbot to confirm customers understand and appropriately respond to the chatbot’s questions.",
         "C. Develop processes to transform collected data so that developers cannot see customer’s personal data unless necessary to perform their jobs.",
         "D. Leverage Open Web Application Security Project (OWASP) resources to avoid common vulnerabilities and protect confidentiality of collected information."],
        "A"
    ),
    Question(
        "Jack is a privacy engineer working in a bank. DevOps is enhancing the user interface of the bank’s mobile application and contemplating the use of an open-source library module for facial recognition. DevOps approached Jack for his guidance. What is the first step that Jack must take?",
        ["A. Conduct a risk/benefits analysis of the open-source software.",
         "B. Test the open-source software in the bank sandbox environment.",
         "C. Review and interpret the bank’s policy on the use of open-source software.",
         "D. Contact the developer about the level of support for the open-source software."],
        "C"
    ),
    Question(
        "When implementing privacy by design, the processing and use of personal data should not be obscured or obfuscated. Notice and disclosure regarding the use or personal data should consider the needs of the audience. Which of the following is a foundational privacy principle that best reflects this statement?",
        ["A. Transparency.",
         "B. Accountability.",
         "C. Privacy by default.",
         "D. Privacy engineering."],
        "A"
    ),
    Question(
        "Chatbots can interact with users through natural language and can provide guidance in a conversational manner, using human-like cues such as warm greetings with a real name. How are such tools categorized from a privacy perspective?",
        ["A. Epimorphism.",
         "B. Paedomorphism.",
         "C. Homeomorphism.",
         "D. Anthropomorphism."],
        "D"
    ),
    Question(
        "Peter works for SipCorp and is renewing a service level agreement (SLA) with a third-party vendor that he has procured for a critical IT project. Which of the following should NOT be included in the SLA?",
        ["A. The vendor’s servicing routine.",
         "B. SipCorp’s disaster recovery plan.",
         "C. Alternative provisions already in place.",
         "D. Expectations to respond if the system fails."],
        "B"
    ),
    Question(
        "Which activity will most help a controller ensure the operations of a processor are within the scope of the personal data processing agreement?",
        ["A. Privacy audit.",
         "B. Video surveillance.",
         "C. Runtime behavior monitoring.",
         "D. Privacy risk assessment and analysis."],
        "A"
    ),
    Question(
        "Which of the following are required to implement effective privacy engineering?",
        ["A. Data governance, technological controls, engineering lifecycle.",
         "B. Technological controls, entity level controls, business process controls.",
         "C. Building scalable solutions, enforcement of privacy safeguards, systems design.",
         "D. Minimization of data, data protection impact assessments, purpose use limitation."],
        "A"
    ),
    Question(
        "Value-sensitive design is an iterative process that involves many types of investigations. Which investigation type focuses on how stakeholders configure, use or are otherwise affected by the technology involved?",
        ["A. Empirical.",
         "B. Technical.",
         "C. Conceptual.",
         "D. Comparative."],
        "A"
    ),
    Question(
        "A company provides training to its employees about customer privacy rights and company privacy policies. The company wants to assess the impact of its training as well as find areas for improvement. Which is the best way to evaluate the effectiveness of training in achieving the company’s privacy objectives?",
        ["A. Submit questionnaires to training participants after each training, requesting feedback on how the trainings can be made more engaging.",
         "B. Require team leaders who develop and deliver trainings and refresher courses report to management on which methods are most effective.",
         "C. Collect information about employees’ interactions with customer databases and email correspondences to be reviewed after a complaint has been filed.",
         "D. Define goals or key performance indicators (KPIs) for the training program and create an audit process for logging and regularly reviewing these KPIs and goals."],
        "D"
    ),
    Question(
        "Kyle and Maggie installed an electronic thermostat in their home so they could control indoor temperature and track their energy use. It required an internet connection to a webserver, which stored the data necessary for the usage reports. Kyle consented to the website’s privacy policy and understood the data is well protected. The electronic thermostat is an example of which of the following?",
        ["A. Internet router.",
         "B. Wi-Fi extender device.",
         "C. Bluetooth repeater device.",
         "D. Ubiquitous computing device."],
        "D"
    ),
    Question(
        "ABC Company provides technical white papers to interested consumers who register on their website. The website requires a user to enter their mobile phone number as a condition of registration, although the website’s primary function does not require phone numbers and there is no statutory or regulatory requirement to do so. Using Daniel Solove’s Taxonomy of Privacy model, this is an example of which problem?",
        ["A. Intrusion.",
         "B. Insecurity.",
         "C. Interference.",
         "D. Interrogation."],
        "D"
    ),
    Question(
        "Which of the following is a main goal of using the Factor Analysis of Information Risk (FAIR) methodology?",
        ["A. Build an estimate of overall threat.",
         "B. Create a policy on privacy controls.",
         "C. Focus on organizational costs and fines.",
         "D. Develop a strategy for qualitative analysis."],
        "A"
    ),
    Question(
        "Which technique would allow the identification of regular customers to be performed in a way that does not require either company to directly share customers’ personal data with the other?",
        ["A. Both companies encrypt their customer lists using asymmetric encryption prior to sharing.",
         "B. Both companies run each of their customers email addresses through the same hash algorithm and compare the results.",
         "C. Both companies load the datasets into a single database and only access it through private information retrieval techniques.",
         "D. The companies set up secure multiparty computation so that neither of them can perform the analysis without the other companies’ knowledge."],
        "B"
    ),
    Question(
        "Which of the following actions could the company take with respect to the old customer data set identified by the CMO that will provide the most privacy protection?",
        ["A. Delete the dataset after confirming that there is no legal or business reason to retain it.",
         "B. Email every customer in the dataset to ask whether they would like their data to be deleted.",
         "C. Strip out any directly identifiable information and then make it available to the analytics team.",
         "D. Apply access controls to restrict access to just the CMO in the event that a use case is identified."],
        "A"
    ),
    Question(
        "Which of the following is an example of the predictability objective in privacy engineering?",
        ["A. Enabling users to view their privacy preferences when accessing a website.",
         "B. Allowing users to make corrections or updates to inaccurate personal data.",
         "C. Requiring users to check a box stating they have read and agreed to the privacy notice.",
         "D. Providing users with a contact individual to administer changes to their personal data."],
        "C"
    ),
    Question(
        "Which of the following privacy technologists’ activities is recognized as part of the software evolution process?",
        ["A. Analyzing technical log performance data on a regular basis.",
         "B. Participating in developers’ team meetings to discuss new projects.",
         "C. Assessing the existing privacy controls in the technological ecosystem.",
         "D. Running a privacy impact assessment when software is being updated."],
        "D"
    ),
    Question(
        "Artificial intelligence can potentially introduce privacy harms to individuals in which of the following ways?",
        ["A. Excluding personal data from collection.",
         "B. Using personal data in unintended ways.",
         "C. Hashing data from one set to another set.",
         "D. Mixing data types to hide relationships among data."],
        "B"
    ),
    Question(
        "To sign up for a retailer’s loyalty program, Peter must complete a form asking for his name, contact information, income and other demographic information. Peter completing and submitting the form to the retailer is an example of what type of data collection?",
        ["A. Passive collection.",
         "B. First-party collection.",
         "C. Qualitative collection.",
         "D. Third-party collection."],
        "B"
    ),
     Question(
        "The use of data aggregation can aid in protecting the privacy of individuals while executing statistical analysis. Which of the following is the most aggregated result?",
        ["A. A summary of data for customers who purchased fishing gear on a Saturday in the spring.",
         "B. A summary of data for women who used a smartphone on a Saturday in California to purchase fishing gear.",
         "C. A summary of data for men who used a smartphone on a Saturday in California to purchase fishing gear and bait.",
         "D. A summary of data for customers who used a smartphone on a Saturday to purchase fishing gear in the United States."],
        "A"
    ),
    Question(
        "A company has hired a marketing company to identify past website visitors who revisit its site for future marketing. This is an example of what type of activity?",
        ["A. A digital distraction.",
         "B. A retargeting campaign.",
         "C. A keyword ad campaign.",
         "D. A website personalization."],
        "B"
    ),
    Question(
        "Encryption protects the confidentiality of digital data transmitted through a network, such as the internet, or at rest on computer systems by scrambling text into an unreadable format or code. What is the new text format called?",
        ["A. Clean text.",
         "B. Ciphertext.",
         "C. Covert text.",
         "D. Symmetric text."],
        "B"
    ),
    Question(
        "A game app available on a popular app store wants to add functionality to have players sign into their social media accounts. The game app will receive marketing leads from this functionality, and players will get to display their scores and interact with other players. Which of the following would cause a privacy concern?",
        ["A. A setting that requires players access the app through the social media account sign-in buttons before playing.",
         "B. A setting that requires users to provide their payment details in the app store if they want to receive daily rewards.",
         "C. A setting that allows signed in players to form and join teams with other signed in players in their area and demographic.",
         "D. A setting that asks players whether the app can use their location services to display their country in the player’s profile."],
        "A"
    ),
    Question(
        "Julia decided to reformat her company’s website privacy notice by bringing critical elements to the foreground and then supplementing those elements with additional related detail. Her goal is to make the privacy notice easier for users to navigate and comprehend. This is an example of utilizing which of the following?",
        ["A. Privacy pattern.",
         "B. Clickstream pattern.",
         "C. Data pattern theory.",
         "D. Website design model."],
        "A"
    ),
    Question(
        "An organization is looking to outsource part of its business operations to a third party. As part of the outsourcing, some employees from the third party will require access to the organization’s physical locations and some IT systems that contain personal data. Which of the following should an organization do first to provide the highest level of security and work to ensure the outsourcing company is granted only appropriate access to personal data?",
        ["A. Configure the system’s role-based access controls (RBAC).",
         "B. Determine which employees will need access to specific data.",
         "C. Have each individual sign a non-disclosure agreement (NDA).",
         "D. Perform a background check on each employee of the third-party company."],
        "A"
    ),
    Question(
        "When a company is setting up an anonymous ethical complaints system, which of the following privacy controls is most important to implement?",
        ["A. User setting that allows individuals to erase their history.",
         "B. Log files that record randomly assigned IDs for each access.",
         "C. Single sign on authentication for secure entry into the system.",
         "D. Database back up to and recovery from a separate company server."],
        "B"
    ),
    Question(
        "When an application uses data features such as user location, display preferences or audio volume levels, this is known as which of the following?",
        ["A. Deep learning.",
         "B. Machine learning.",
         "C. Autonomic computing.",
         "D. Context-aware computing."],
        "D"
    ),
    Question(
        "What can HomeConnect do to reduce a customer’s exposure to threats?",
        ["A. Block the implementation of additional layers of security by the customer.",
         "B. Require users to change their passwords as part of the initial configuration.",
         "C. Set up systems to bypass authentication when a customer’s home network is not secure.",
         "D. Advise customers to add household members to their accounts by sharing login credentials."],
        "B"
    ),
    Question(
        "What best practice can the HomeConnect cyber-engineering team adopt for running software updates and patches?",
        ["A. Ensure security patches are delivered over multiple channels.",
         "B. Inform the customer when an update is not ready for implementation.",
         "C. Notify users when they access the device if there is a software update.",
         "D. Conduct device vulnerability assessments only after an incident occurs."],
        "C"
    ),
    Question(
        "Information technology has great value across all facets of an organization. Which of the following is a strong business case for holistic data protection, inclusive of privacy, protection and security?",
        ["A. Data protection responsibility should remain with the information technology and information security teams.",
         "B. Information technology is fundamental to the data life cycle for managing engagement with suppliers and customers.",
         "C. Collaborative efforts between information technology and other areas of an organization are not a regulatory requirement.",
         "D. The relationship between information technology and other departments has no true correlation to operational efficiency."],
        "B"
    ),
    Question(
        "Which statement below is FALSE with respect to the beta testing of a product?",
        ["A. Performed on feature-complete systems.",
         "B. Privacy risks are minimal or non-existent.",
         "C. Open to the broader public but may be capped.",
         "D. Users populate their profiles with personal data."],
        "B"
    ),
    Question(
        "Value-source analysis involves which of the following?",
        ["A. Using visual aides to influence and elicit values from stakeholders that will better align with a requisite response.",
         "B. Leveraging narratives or scenarios to identify, communicate, or illustrate the impact of design choices on stakeholder values.",
         "C. Assessing project, designer and stakeholder values and considering the ways in which each group’s values may be in conflict.",
         "D. Striving to balance technology and social structure in the design space with a goal of identifying new solutions that might not be readily apparent."],
        "C"
    ),
    Question(
        "Which of the following would be considered part of software vulnerability management?",
        ["A. Software testing regime.",
         "B. Software intrusion reports.",
         "C. Software design blueprints.",
         "D. Software developer training."],
        "B"
    ),
    Question(
        "Which of the following is NOT an example of the usefulness of conducting a record of processing activity (RoPA) to all types and sizes of organizations?",
        ["A. Creating a collated list of personal data from entire book of clients.",
         "B. Identifying who has access to what data and where for supervisory auditing purposes.",
         "C. Classifying sensitive or criminal data to implement data protection policy & procedures.",
         "D. Distinguishing high-risk processing to identify the best solutions to mitigate or manage."],
        "A"
    ),
    Question(
        "Transport Layer Security (TLS) is established using asymmetric cryptography and symmetric encryption and is used primarily to?",
        ["A. Protect data in use.",
         "B. Protect data at rest.",
         "C. Protect data in transit.",
         "D. Protect data once received."],
        "C"
    ),
    Question(
        "What must a hiring organization assess while using a third-party service for testing its software?",
        ["A. Whether the service provider has service infrastructure in the cloud.",
         "B. Whether the service provider has additional services offered at a competitive price.",
         "C. Whether the service provider has privacy and security equal to or stricter than its own.",
         "D. Whether the service provider has levels of financial risk tolerance equivalent to its own."],
        "C"
    ),
    Question(
        "What are some of the key principles under the Digital Advertising Alliance’s (DAA) Self-Regulatory Principles for Online Behavioral Advertising?",
        ["A. Suppression, education and deletion.",
         "B. Transparency, education and deletion.",
         "C. Suppression, transparency and education.",
         "D. Education, transparency and consumer control."],
        "D"
    ),
    Question(
        "Which of the following privacy threats and violations is the man’s action an example of?",
        ["A. Blackmail.",
         "B. Accessibility.",
         "C. Surveillance.",
         "D. Appropriation."],
        "A"
    ),
    Question(
        "Which type of privacy threat and violation did the retailer enable through unsecured lists outside its store?",
        ["A. Dark patterns.",
         "B. Digital profiling.",
         "C. Specific surveillance.",
         "D. Increased accessibility."],
        "D"
    ),
     Question(
        "If the store that adopted this questionable practice also used the list to engage in email or SMS marketing to customers, what type of privacy threat and violation would this be?",
        ["A. Intrusion.",
         "B. Insecurity.",
         "C. Data misuse.",
         "D. Interrogation."],
        "C"
    ),
    Question(
        "Which of the following is an example of the use of a privacy pattern?",
        ["A. A common recurrence of privacy law violations within a company.",
         "B. An organization’s color scheme within their privacy policy documentation.",
         "C. A preformatted response to similar privacy-related inquiries received on a website.",
         "D. A phone app feature which reminds the user that their location data is being shared."],
        "D"
    ),
    Question(
        "Which of the following protects information while it is in use by multiple parties?",
        ["A. Using Secure Multiparty Computation application.",
         "B. Using password to protect a Microsoft Word document.",
         "C. Using URL that begins with https:// when accessing a website.",
         "D. Using WPA2 wireless network protocol for free public internet access."],
        "A"
    ),
    Question(
        "Other than when new privacy laws or regulations are enacted, how often, at a minimum, should an organization update its privacy standards to ensure they are meeting expectations and requirements?",
        ["A. Annually.",
         "B. Quarterly.",
         "C. Bi-annually.",
         "D. Semi-annually."],
        "A"
    ),
    Question(
        "To prevent the identity of employees from being exposed when analyzing data for potential automation opportunities, the compliance team requires that information captured to perform capacity diagnostics on employee screen time usage be?",
        ["A. Perturbed.",
         "B. Correlated.",
         "C. Summarized.",
         "D. Disseminated."],
        "C"
    ),
    Question(
        "Which of the following is an example of applying transient storage to information?",
        ["A. Saving a customer’s session cookies in a browser.",
         "B. Creating a copy of financial documents for backup.",
         "C. Maintaining HR data in several different databases.",
         "D. Keeping a company’s permanent files on a hard drive."],
        "A"
    ),
    Question(
        "BitHealth has recently implemented an electronic medical record (EMR) system. All patient information is now stored in the EMR. Only those who have gone through an approval process by the privacy team have access to the EMR. Lea, a member of the BitHealth IT team, has received a request from Stony Surgery requesting access to the EMR for their case management team to approve/authorize inpatient interactions. How should Lea respond to the request from Stony Surgery?",
        ["A. Delete the email at once as it could be a phishing attempt.",
         "B. Forward the request to the privacy team at BitHealth to respond.",
         "C. Provide access to Stony Surgery because they are a healthcare provider.",
         "D. Request a signed letter from a senior member of the practice to verify authority."],
        "B"
    ),
    Question(
        "To help Jane to take a more proactive role and to comply with standards, Peter and Mark will need to send her standard operating procedures (SOP) covering which of EdMed’s privacy-by-design process activities?",
        ["A. Raw data testing and validation SOP.",
         "B. Identify training information needs SOP.",
         "C. Documenting training requirements SOP.",
         "D. Low-level design and implementation SOP."],
        "B"
    ),
    Question(
        "To check that the raw data media format is always recognized by the parsing application, Mark has decided to improve DONAT testing and validation for new formats on the market. What would be his best approach?",
        ["A. Deploy a machine learning module utilizing a personal data recognition algorithm.",
         "B. Hire a new tester with extensive experience in x-ray processing to review the new formats.",
         "C. Purchase a state-of-the-art application that includes an x-ray format subscription which will replace DONAT.",
         "D. Purchase a subscription to a system that defines the formats for medical image transfers to trigger a secondary review."],
        "D"
    ),
    Question(
        "The type of requirement that Peter proposed related to the upgrade of the technological system that parses the raw input data for TristarGlobe Inc. processing is known as what?",
        ["A. A functional requirement.",
         "B. An exclusion requirement.",
         "C. A predictability requirement.",
         "D. A nonfunctional requirement."],
        "D"
    ),
    Question(
        "Following the report from the legal department, Mark should require which of the following be performed?",
        ["A. Legal impact assessment.",
         "B. Privacy impact assessment.",
         "C. Transfer impact assessment.",
         "D. Legitimate impact assessment."],
        "B"
    ),
    Question(
        "Which control will be used to implement the final statement on which Peter, Mark and Jane agree?",
        ["A. Balance.",
         "B. Security.",
         "C. Supervision.",
         "D. Architecture."],
        "C"
    ),
    Question(
        "Peter and Mark’s first step was to collect all the facts about the reported situation, which included software, procedures and vendors. What is this process known as?",
        ["A. Privacy audit and IT control review.",
         "B. Penetration test reporting and analysis.",
         "C. Incident response procedure and review.",
         "D. Data protection gap and process analysis."],
        "C"
    ),
    Question(
        "Which of the following would be considered a type of privacy interference?",
        ["A. Installing closed circuit television cameras on public streets.",
         "B. Providing credit history that leads to inaccurate credit scores.",
         "C. Completing an employment application truthfully and accurately.",
         "D. Submitting an email address to receive a marketing email newsletter."],
        "B"
    ),
    Question(
        "Which of the following scenarios best describes a situation where there could be surveillance without the reasonable knowledge of the individual?",
        ["A. A review platform discloses users’ identities rather than allowing for anonymity when providing reviews.",
         "B. An airport uses heat sensing cameras to screen individuals for fever while individuals pass through security checks.",
         "C. A regulator reviews the financial transactions of individuals who have been placed on a government sanctions list.",
         "D. A website matches the user’s IP address and browsing pattern to registered users regardless of whether the user is logged in."],
        "D"
    ),
    Question(
        "Which of the following best describes the goal of privacy engineering?",
        ["A. To ensure that all personal data is completely anonymized within a system.",
         "B. To develop privacy-protective solutions that are in line with the business’ needs.",
         "C. To ensure that data collection practices are aligned to an appropriate legal basis of processing.",
         "D. To ensure that solutions appropriately protect confidential data in accordance with company policies."],
        "B"
    ),
    Question(
        "A data broker collects information on medications that are prescribed to individuals and sells this information to pharmaceutical companies to allow them to target their advertising budgets. The information they collect does not contain direct identifiers regarding the individuals to whom the medications are prescribed, but does contain several indirect identifiers that in combination could allow reidentification. What must the data broker do prior to selling this data to pharmaceutical companies?",
        ["A. No action is necessary prior to selling this data.",
         "B. The data broker is not allowed to sell this data set.",
         "C. The data broker must anonymize the data set before it can be sold.",
         "D. The dataset must have a k-anonymity value greater than eighteen before it can be sold."],
        "C"
    ),
    Question(
        "The leadership team for a retailer wants to improve customer satisfaction and increase customer retention. They propose introducing software that would enable them to learn more about their customers’ attitudes and behaviors to act upon. Their IT team is leading efforts to select a closed-source loyalty management system for this purpose by creating a list of software requirements and undertaking a tender process. These requirements include ensuring robustness of software against attack and vendor support for patching and customizations. Which is the following is TRUE?",
        ["A. A closed-source loyalty management system has easily viewable code.",
         "B. A closed-source loyalty management system can only be fixed by the vendor.",
         "C. A closed-source loyalty management system has code that is regularly shared and modified.",
         "D. A closed-source loyalty management system by its very nature is more resistant to attack than open-source."],
        "B"
    ),
    Question(
        "ABC Company sells t-shirts from multiple manufacturers on its website. Several t-shirts sold are made by ABC. The company’s website allows consumers to review products and provide comments on their experiences. However, when a new user attempts to view negative product reviews on ABC’s brand of t-shirts, the company limits access to them. Using Daniel Solove’s Taxonomy of Privacy model, which privacy problem is this an example of?",
        ["A. Decisional exposure.",
         "B. Decisional distortion.",
         "C. Decisional intervention.",
         "D. Decisional interference."],
        "D"
    ),
    Question(
        "A company wants to build a brand image that differentiates itself from the competition by focusing on enhancing customer trust to grow its business. In the company’s online environment, they want to empower data subjects to play an active role in the management of their own data, via a consent mechanism. Which of the following privacy by design foundational principles best supports this initiative?",
        ["A. Full functionality – allow users full access.",
         "B. End to end security – full life-cycle protection.",
         "C. Respect for user privacy – keep it user centric.",
         "D. Proactive not reactive - preventive not remedial."],
        "C"
    ),
    Question(
        "Software that collects and reports runtime failures to a bug tracker may sometimes include the user’s personal data as part of the bug report. What should be a design consideration for such automated bug trackers?",
        ["A. Transmit user’s personal data without explicit disclosures.",
         "B. Publish the bug report online with the user’s personal data.",
         "C. Encrypt personal data during transmission and after receipt.",
         "D. Duplicate the entries in the bug report, including the personal data."],
        "C"
    ),
    Question(
        "Do the company’s data collection processes regarding building access align with the OECD Fair Information Practices and Ann Cavoukian’s Privacy by Design framework?",
        ["A. Yes, the company has a right to use non-personal data in its possession to further legitimate business objectives.",
         "B. Yes, provided the company obtains explicit, written consent from the data subjects to utilize the de-identified data.",
         "C. Yes, as long as the data is used to determine which specific employees need access on certain days to provide appropriate workspaces.",
         "D. Yes, provided only the IT team can reidentify individuals from the data collected and it is used for facilities management, a reasonably anticipated secondary use."],
        "A"
    ),
    Question(
        "Which of the following did you neglect to do in your haste to comply with your CEO’s request?",
        ["A. Obtain employee explicit consent prior to engaging in any monitoring of their activities.",
         "B. Ensure you do not monitor employees’ productivity to avoid breaking their trust and invading privacy.",
         "C. Consult with the legal department to ensure compliance with all applicable laws and regulations.",
         "D. Evaluate whether the processes ensure employees’ productivity and the company’s profitability."],
        "C"
    ),
    Question(
        "Which of the following is an example of first-party collection?",
        ["A. A salesperson uses client lists for marketing purposes.",
         "B. A customer fills out and submits an online survey form.",
         "C. A Data Analyst infers information from viewing a database.",
         "D. An HR Manager pulls employee data from a payroll system."],
        "B"
    ),
    Question(
        "Industrial Industries, Inc. collects customer personal data to assist with product returns. Three years after the sale, customers can no longer return the product, but Industrial Industries wants to continue using some of this information to analyze the percentage of returns during that period of time. Of the following options, which is the best practice to mitigate risks associated with maintaining this data for return analyses?",
        ["A. Review the information collected in the database and delete any personal data that could be used to identify customers.",
         "B. Review employee access levels for the database and remove those individuals who no longer have a business need to access the information.",
         "C. Develop an automated process that removes the customer’s email address from the database and avoids human error when deleting that information.",
         "D. Save unneeded customer personal data in a distinct database that has additional security measures, such as enhanced authentication requirements."],
        "A"
    ),
    Question(
        "During a recent software inventory review, Jim noted that the Web Server software currently deployed is Apache Version 2.4.39 whereas the latest version is 2.4.50. Which of the following is a control that will reduce Apache Web Server vulnerabilities by impeding malicious state-sponsored hackers from exploiting the gap in the software versions?",
        ["A. Encrypt back-end databases.",
         "B. Install web application firewalls.",
         "C. Apply patches to the Apache Web Server software.",
         "D. Upgrade web server software from Apache to Microsoft IIS."],
        "C"
    ),
    Question(
        "Which of the following IT roles serve as a repository of privacy knowledge and tailors this knowledge as needed to help the different stakeholders to fulfill their roles?",
        ["A. Area specialists.",
         "B. Project managers.",
         "C. Process administrators.",
         "D. Software programmers."],
        "A"
    ),
    Question(
        "Which of the following is a tool that shows the relationship between the requirements of a privacy law and the implemented software design elements?",
        ["A. Digital signature.",
         "B. Traceability matrix.",
         "C. Block level disk encryption.",
         "D. Cryptographic hash function."],
        "B"
    ),
    Question(
        "Which IT framework is held up as the de facto for IT service management worldwide?",
        ["A. ITIL.",
         "B. COBIT.",
         "C. ISO27001.",
         "D. NIST Risk Management Framework."],
        "A"
    ),
    Question(
        "Which of the following is an example of a privacy threat during data collection?",
        ["A. A credit card payment processor monitoring each transaction as it occurs.",
         "B. An employer asking an interviewee about marital status during a job interview.",
         "C. A doctor adding auxiliary information to a patient’s record during a consultation.",
         "D. A credit bureau aggregating an individual’s payment history from multiple creditors."],
        "B"
    ),
     Question(
        "As part of a major rebranding effort, a social media company is adding new features to its mobile app, including embedded application programming interfaces (APIs) that easily give users access to other social media services. Before rolling out these changes, what should the company’s privacy team do?",
        ["A. The company should develop an email and social media marketing campaign targeting existing customers to make them aware of these features.",
         "B. The company should assess if the inclusion of the APIs alters the way current customer’s data is used and notify those customers of those changes.",
         "C. The company should select a group of current customers for a beta test and confirm there are no conflicts with the core product before sending out notice.",
         "D. The company should create a new privacy policy and notify current customers of new features and provide links to descriptions of the technologies being used."],
        "B"
    ),
    Question(
        "Which security mechanism would be the most reliable technology to keep data confidential at rest, in-transit, or when processing real-time analytics?",
        ["A. Data backup.",
         "B. Data encryption.",
         "C. Hardware-based security.",
         "D. Two-factor authentication."],
        "B"
    ),
    Question(
        "Which of the following events is a trigger to update a data protection impact assessment or privacy impact assessment (DPIA/PIA) for a system?",
        ["A. The organization merges with a competitor.",
         "B. The organization patches its operating system.",
         "C. The organization hires a new chief privacy officer.",
         "D. The organization acquires a new office space in the same city."],
        "A"
    ),
    Question(
        "There has been an increase in calls to the customer service department of Shop4Electronics with complaints that orders were rejected incorrectly due to fraud. Which recommendation should be provided to reduce the number of false positives identified by FraudNoMore?",
        ["A. Disable FraudNoMore entirely as fraud detection is not a valid business reason to track users.",
         "B. Ask users to reset cookies in their browser and try again if their transaction is rejected as fraudulent.",
         "C. Stop marking transactions as fraudulent when third-party code is unable to set cookies and collect associated data.",
         "D. Require all users to have a unique IP address when making a purchase to avoid matching a known fraudulent IP address."],
        "C"
    ),
    Question(
        "Shop4Electronics runs internal analytics to identify unique users using their mobile application. Can a user who declined to be tracked via Apple’s App Tracking Transparency (ATT) dialog be included in the internal analytics report?",
        ["A. Yes, because the analytics report identifies unique users and not aggregate users.",
         "B. No, because Shop4Electronics shares mobile advertising IDs with its social media partners.",
         "C. Yes, because app tracking transparency (ATT) framework does not apply to internal analytics.",
         "D. No, because the user declined permission to be tracked in the mobile app via the App Tracking Transparency (ATT) framework."],
        "D"
    ),
    Question(
        "If a guest visitor on the Shop4Electronics website cleared their cookies, which technique could be used to continue to uniquely identify that user, based on the data collected by Shop4Electronics and its partners?",
        ["A. Federated Identity.",
         "B. Anthropomorphism.",
         "C. Cross-site Scripting.",
         "D. Device Fingerprinting."],
        "D"
    ),
    Question(
        "Shop4Electronics wants to identify users who have made purchases on both their website and mobile application. Which of the following methods best serves this purpose?",
        ["A. Match web IP address to mobile app IP address.",
         "B. Match web cookieID to mobile app advertising identifier.",
         "C. Match email address from web orders to email from app orders.",
         "D. Match device fingerprints from the website with those on the mobile app."],
        "C"
    ),
    Question(
        "A Shop4Electronics customer signs-up to receive email marketing. This customer is concerned about privacy and wants to take steps to ensure Shop4Electronics is not notified when they open a Shop4Electronics email. Which method would limit email open tracking?",
        ["A. Use of an email client that blocks images and execution of specific scripts.",
         "B. Installing an ad blocker on each browser the customer uses on all devices.",
         "C. Disable location tracking in the Shop4Electronics mobile app and on all browsers.",
         "D. Use of a virtual private network (VPN) service to access email and Shop4Electronics’ website."],
        "A"
    ),
    Question(
        "The Shop4Electronics website requests a user’s location via their browser upon first visit to the site. This location data is used to determine a zip code to calculate shipping cost and tax. Upon navigating to checkout, the user notices their zip code has been pre-populated. Which mechanism was likely used to determine location if the user rejected to share location via their browser?",
        ["A. Location from GPS data.",
         "B. Location from IP address.",
         "C. Location from MAC address.",
         "D. Location from advertising ID."],
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
