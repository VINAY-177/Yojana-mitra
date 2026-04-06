import json
import os

SCHEMES_PATH = os.path.join(os.path.dirname(__file__), "schemes.json")

STATES = [
    ("Andhra Pradesh", "andhra pradesh", "आंध्र प्रदेश"),
    ("Arunachal Pradesh", "arunachal pradesh", "अरुणाचल प्रदेश"),
    ("Assam", "assam", "असम"),
    ("Bihar", "bihar", "बिहार"),
    ("Chhattisgarh", "chhattisgarh", "छत्तीसगढ़"),
    ("Goa", "goa", "गोवा"),
    ("Gujarat", "gujarat", "गुजरात"),
    ("Haryana", "haryana", "हरियाणा"),
    ("Himachal Pradesh", "himachal pradesh", "हिमाचल प्रदेश"),
    ("Jharkhand", "jharkhand", "झारखंड"),
    ("Karnataka", "karnataka", "कर्नाटक"),
    ("Kerala", "kerala", "केरल"),
    ("Madhya Pradesh", "madhya pradesh", "मध्य प्रदेश"),
    ("Maharashtra", "maharashtra", "महाराष्ट्र"),
    ("Manipur", "manipur", "मणिपुर"),
    ("Meghalaya", "meghalaya", "मेघालय"),
    ("Mizoram", "mizoram", "मिजोरम"),
    ("Nagaland", "nagaland", "नागालैंड"),
    ("Odisha", "odisha", "ओडिशा"),
    ("Punjab", "punjab", "पंजाब"),
    ("Rajasthan", "rajasthan", "राजस्थान"),
    ("Sikkim", "sikkim", "सिक्किम"),
    ("Tamil Nadu", "tamil nadu", "तमिलनाडु"),
    ("Telangana", "telangana", "तेलंगाना"),
    ("Tripura", "tripura", "त्रिपुरा"),
    ("Uttar Pradesh", "uttar pradesh", "उत्तर प्रदेश"),
    ("Uttarakhand", "uttarakhand", "उत्तराखंड"),
    ("West Bengal", "west bengal", "पश्चिम बंगाल"),
    ("Delhi", "delhi", "दिल्ली"),
    ("Jammu and Kashmir", "jammu and kashmir", "जम्मू और कश्मीर")
]

new_schemes = []

for s_name, s_id, s_hi in STATES:
    new_schemes.extend([
        # HEALTH
        {
            "id": f"{s_id.replace(' ','-')}-ayushman-supplement",
            "name": f"{s_name} Ayushman Arogya Supplement",
            "shortName": f"{s_name} Health Supplement",
            "category": "health",
            "icon": "🏥",
            "benefit": f"Extra ₹2 Lakhs health cover for critical illness over Ayushman Bharat in {s_name}",
            "benefitValue": 200000,
            "simpleExplanation": f"The {s_name} government provides an additional safety net for serious medical procedures.",
            "eligibility": {"minAge": 0, "maxAge": 100, "maxIncome": 500000, "categories": ["general", "obc", "sc", "st"], "gender": ["male", "female", "other"], "occupations": ["all"], "states": [s_id], "conditions": []},
            "howToApply": ["Apply via state health portal with existing Ayushman card"],
            "documentsRequired": ["Aadhaar", "Ayushman Card", "Income Certificate"],
            "officialUrl": "https://mohfw.gov.in",
            "whyQualifyTemplate": "Eligible for state-level health top-up based on income.",
            "nameHi": f"{s_hi} आयुष्मान आरोग्य पूरक",
            "shortNameHi": f"{s_hi} स्वास्थ्य पूरक",
            "benefitHi": f"आयुष्मान भारत के अलावा {s_hi} में गंभीर बीमारी के लिए अतिरिक्त ₹2 लाख का स्वास्थ्य कवर",
            "simpleExplanationHi": "गंभीर चिकित्सा प्रक्रियाओं के लिए अतिरिक्त सुरक्षा जाल।",
            "documentsRequiredHi": ["आधार", "आयुष्मान कार्ड", "आय प्रमाण पत्र"],
            "howToApplyHi": ["मौजूदा आयुष्मान कार्ड के साथ राज्य स्वास्थ्य पोर्टल के माध्यम से आवेदन करें"]
        },
        {
             "id": f"{s_id.replace(' ','-')}-maternity-care",
            "name": f"{s_name} Safe Maternity Care Assistance",
            "shortName": f"{s_name} Maternity Care",
            "category": "health",
            "icon": "🤰",
            "benefit": f"₹12,000 cash assistance for pregnant women delivery & nutrition in {s_name}",
            "benefitValue": 12000,
            "simpleExplanation": "Financial help directly to the bank account for pregnant women to ensure proper nutrition.",
            "eligibility": {"minAge": 18, "maxAge": 45, "maxIncome": 250000, "categories": ["general", "obc", "sc", "st"], "gender": ["female"], "occupations": ["all"], "states": [s_id], "conditions": []},
            "howToApply": ["Register pregnancy at nearest Anganwadi center"],
            "documentsRequired": ["Aadhaar", "Bank Account Details", "Mother and Child Protection (MCP) Card"],
            "officialUrl": "https://wcd.nic.in",
            "whyQualifyTemplate": "Eligible for maternity nutritional support.",
            "nameHi": f"{s_hi} सुरक्षित मातृत्व देखभाल सहायता",
            "shortNameHi": f"{s_hi} मातृत्व देखभाल",
            "benefitHi": f"{s_hi} में गर्भवती महिलाओं की डिलीवरी और पोषण के लिए ₹12,000 नकद सहायता",
            "simpleExplanationHi": "गर्भवती महिलाओं को उचित पोषण सुनिश्चित करने के लिए बैंक खाते में प्रत्यक्ष वित्तीय सहायता।",
            "documentsRequiredHi": ["आधार", "बैंक खाता विवरण", "एमसीपी कार्ड"],
            "howToApplyHi": ["निकटतम आंगनवाड़ी केंद्र पर गर्भावस्था दर्ज करें"]
        },

        # EMPLOYMENT
        {
            "id": f"{s_id.replace(' ','-')}-youth-employment",
            "name": f"{s_name} Youth Skill Employment Guarantee",
            "shortName": f"{s_name} Youth Skill Job",
            "category": "employment",
            "icon": "💼",
            "benefit": f"Guaranteed 100 days of urban employment or ₹3000/month unemployment allowance in {s_name}",
            "benefitValue": 36000,
            "simpleExplanation": "Ensures livelihood security for urban youth through guaranteed unskilled work or an allowance.",
            "eligibility": {"minAge": 18, "maxAge": 35, "maxIncome": 200000, "categories": ["general", "obc", "sc", "st"], "gender": ["male", "female", "other"], "occupations": ["unemployed"], "states": [s_id], "conditions": []},
            "howToApply": ["Register on the State Employment Exchange portal"],
            "documentsRequired": ["Aadhaar", "Educational Certificates", "Domicile Certificate"],
            "officialUrl": "https://labour.gov.in",
            "whyQualifyTemplate": "Eligible based on age and employment status.",
            "nameHi": f"{s_hi} युवा कौशल रोजगार गारंटी",
            "shortNameHi": f"{s_hi} युवा रोजगार",
            "benefitHi": f"{s_hi} में शहरी रोजगार के 100 दिनों की गारंटी या ₹3000/माह बेरोजगारी भत्ता",
            "simpleExplanationHi": "शहरी युवाओं के लिए गारंटीकृत काम या भत्ते के माध्यम से आजीविका सुरक्षा।",
            "documentsRequiredHi": ["आधार", "शैक्षिक प्रमाण पत्र", "मूल निवास प्रमाण पत्र"],
            "howToApplyHi": ["राज्य रोजगार विनिमय पोर्टल पर पंजीकरण करें"]
        },
        {
            "id": f"{s_id.replace(' ','-')}-self-employment-loan",
            "name": f"{s_name} Mukhyamantri Self-Employment Loan",
            "shortName": f"{s_name} CM Self-Employment",
            "category": "employment",
            "icon": "🛠️",
            "benefit": f"Collateral-free loans up to ₹5 Lakhs with 25% subsidy for new ventures in {s_name}",
            "benefitValue": 500000,
            "simpleExplanation": "Financial support to encourage young entrepreneurs to start their own businesses.",
            "eligibility": {"minAge": 18, "maxAge": 45, "maxIncome": 500000, "categories": ["general", "obc", "sc", "st"], "gender": ["male", "female", "other"], "occupations": ["unemployed", "self_employed"], "states": [s_id], "conditions": []},
            "howToApply": ["Submit a project report via the District Industries Centre (DIC) portal"],
            "documentsRequired": ["Aadhaar", "Project Report", "Caste Certificate (if applicable)"],
            "officialUrl": "https://msme.gov.in",
            "whyQualifyTemplate": "Eligible for preferential entrepreneurial loans.",
            "nameHi": f"{s_hi} मुख्यमंत्री स्वरोजगार ऋण",
            "shortNameHi": f"{s_hi} मुख्यमंत्री स्वरोजगार",
            "benefitHi": f"{s_hi} में नए उद्यमों के लिए 25% सब्सिडी के साथ ₹5 लाख तक का कोलैटरल-मुक्त ऋण",
            "simpleExplanationHi": "युवा उद्यमियों को अपना व्यवसाय शुरू करने के लिए वित्तीय सहायता।",
            "documentsRequiredHi": ["आधार", "परियोजना रिपोर्ट", "जाति प्रमाण पत्र (यदि लागू हो)"],
            "howToApplyHi": ["जिला उद्योग केंद्र (डीआईसी) पोर्टल के माध्यम से परियोजना रिपोर्ट जमा करें"]
        },
        
        # FINANCE
        {
             "id": f"{s_id.replace(' ','-')}-shg-finance",
            "name": f"{s_name} Mahila SHG Micro-Finance Scheme",
            "shortName": f"{s_name} SHG Micro-Finance",
            "category": "finance",
            "icon": "💸",
            "benefit": f"Interest-free loans up to ₹10 Lakhs for Women Self-Help Groups in {s_name}",
            "benefitValue": 1000000,
            "simpleExplanation": "Boosts rural and urban women-led micro-enterprises through accessible credit.",
            "eligibility": {"minAge": 18, "maxAge": 60, "maxIncome": 999999999, "categories": ["general", "obc", "sc", "st"], "gender": ["female"], "occupations": ["all"], "states": [s_id], "conditions": ["woman_head"]},
            "howToApply": ["Apply through local Block Development Office via the SHG network"],
            "documentsRequired": ["Aadhaar", "SHG Registration Certificate", "Bank Passbook"],
            "officialUrl": "https://rural.nic.in",
            "whyQualifyTemplate": "Eligible for SHG subsidized financing.",
            "nameHi": f"{s_hi} महिला एसएचजी माइक्रो-फाइनेंस योजना",
            "shortNameHi": f"{s_hi} एसएचजी माइक्रो-फाइनेंस",
            "benefitHi": f"{s_hi} में महिला स्वयं सहायता समूहों के लिए ₹10 लाख तक का ब्याज-मुक्त ऋण",
            "simpleExplanationHi": "सुलभ ऋण के माध्यम से सूक्ष्म उद्यमों को बढ़ावा देता है।",
            "documentsRequiredHi": ["आधार", "एसएचजी पंजीकरण प्रमाणपत्र", "बैंक पासबुक"],
            "howToApplyHi": ["एसएचजी नेटवर्क के माध्यम से स्थानीय खंड विकास कार्यालय के माध्यम से आवेदन करें"]
        },
        {
            "id": f"{s_id.replace(' ','-')}-street-vendor-credit",
            "name": f"{s_name} SVANidhi Top-Up Loan",
            "shortName": f"{s_name} Vendor Credit",
            "category": "finance",
            "icon": "🛒",
            "benefit": f"Additional ₹20,000 working capital loan for street vendors in {s_name}",
            "benefitValue": 20000,
            "simpleExplanation": "Extra financing for vendors who have successfully repaid their initial PM SVANidhi loans.",
            "eligibility": {"minAge": 18, "maxAge": 65, "maxIncome": 300000, "categories": ["general", "obc", "sc", "st"], "gender": ["male", "female", "other"], "occupations": ["street_vendor"], "states": [s_id], "conditions": ["street_vendor"]},
            "howToApply": ["Apply via PM SVANidhi portal or local municipal office"],
            "documentsRequired": ["Aadhaar", "Vending Certificate (CoV)", "Previous Loan Repayment Proof"],
            "officialUrl": "https://pmsvanidhi.mohua.gov.in",
            "whyQualifyTemplate": "Eligible as a street vendor.",
            "nameHi": f"{s_hi} स्वनिधि टॉप-अप ऋण",
            "shortNameHi": f"{s_hi} वेंडर क्रेडिट",
            "benefitHi": f"{s_hi} में स्ट्रीट वेंडरों के लिए अतिरिक्त ₹20,000 कार्यशील पूंजी ऋण",
            "simpleExplanationHi": "प्रारंभिक ऋण चुकाने वाले विक्रेताओं के लिए अतिरिक्त वित्तपोषण।",
            "documentsRequiredHi": ["आधार", "वेंडिंग प्रमाणपत्र", "पिछले ऋण चुकाने का प्रमाण"],
            "howToApplyHi": ["पीएम स्वनिधि पोर्टल या स्थानीय नगर निगम कार्यालय के माध्यम से आवेदन करें"]
        },
        
        # PENSION
        {
            "id": f"{s_id.replace(' ','-')}-senior-dignity-pension",
            "name": f"{s_name} Senior Citizen Dignity Pension",
            "shortName": f"{s_name} Senior Pension",
            "category": "pension",
            "icon": "🧓",
            "benefit": f"Monthly pension of ₹1,500 for senior citizens (60+) not covered by national pension in {s_name}",
            "benefitValue": 18000,
            "simpleExplanation": "Provides a minimum income for destitute elderly citizens.",
            "eligibility": {"minAge": 60, "maxAge": 120, "maxIncome": 100000, "categories": ["general", "obc", "sc", "st"], "gender": ["male", "female", "other"], "occupations": ["all"], "states": [s_id], "conditions": ["senior_citizen"]},
            "howToApply": ["Apply at the District Social Welfare Office or online portal"],
            "documentsRequired": ["Aadhaar", "Age Proof", "Income Certificate"],
            "officialUrl": "https://socialjustice.gov.in",
            "whyQualifyTemplate": "Eligible based on senior citizen status and income limit.",
            "nameHi": f"{s_hi} वरिष्ठ नागरिक गरिमा पेंशन",
            "shortNameHi": f"{s_hi} वरिष्ठ पेंशन",
            "benefitHi": f"{s_hi} में 60+ वरिष्ठ नागरिकों के लिए ₹1,500 की मासिक पेंशन",
            "simpleExplanationHi": "निराश्रित बुजुर्ग नागरिकों के लिए न्यूनतम आय प्रदान करता है।",
            "documentsRequiredHi": ["आधार", "आयु प्रमाण", "आय प्रमाण पत्र"],
            "howToApplyHi": ["जिला समाज कल्याण कार्यालय या ऑनलाइन पोर्टल पर आवेदन करें"]
        },
        {
             "id": f"{s_id.replace(' ','-')}-divyang-pension",
            "name": f"{s_name} Divyangjan Sahayata Pension",
            "shortName": f"{s_name} Divyang Pension",
            "category": "pension",
            "icon": "♿",
            "benefit": f"Monthly pension of ₹2,000 for persons with 40%+ disability in {s_name}",
            "benefitValue": 24000,
            "simpleExplanation": "Financial assistance to support the living expenses of persons with disabilities.",
            "eligibility": {"minAge": 0, "maxAge": 100, "maxIncome": 250000, "categories": ["general", "obc", "sc", "st"], "gender": ["male", "female", "other"], "occupations": ["all"], "states": [s_id], "conditions": ["disability"]},
            "howToApply": ["Submit application with UDID to Social Welfare Dept"],
            "documentsRequired": ["Aadhaar", "UDID Card / Disability Certificate", "Bank Details"],
            "officialUrl": "https://disabilityaffairs.gov.in",
            "whyQualifyTemplate": "Eligible based on disability condition.",
            "nameHi": f"{s_hi} दिव्यांगजन सहायता पेंशन",
            "shortNameHi": f"{s_hi} दिव्यांग पेंशन",
            "benefitHi": f"{s_hi} में 40%+ विकलांगता वाले व्यक्तियों के लिए ₹2,000 की मासिक पेंशन",
            "simpleExplanationHi": "विकलांग व्यक्तियों के रहने के खर्च में सहायता के लिए वित्तीय सहायता।",
            "documentsRequiredHi": ["आधार", "UDID कार्ड", "बैंक विवरण"],
            "howToApplyHi": ["समाज कल्याण विभाग में UDID के साथ आवेदन जमा करें"]
        },
        
        # HOUSING
        {
            "id": f"{s_id.replace(' ','-')}-urban-poor-housing",
            "name": f"{s_name} CM Urban Poor Housing Mission",
            "shortName": f"{s_name} Urban Housing",
            "category": "housing",
            "icon": "🏙️",
            "benefit": f"Financial grant of ₹2.5 Lakhs to construct a pucca house for EWS in {s_name}",
            "benefitValue": 250000,
            "simpleExplanation": "Subsidy provided in increments linked to the construction stages of the house.",
            "eligibility": {"minAge": 18, "maxAge": 100, "maxIncome": 300000, "categories": ["general", "obc", "sc", "st"], "gender": ["male", "female", "other"], "occupations": ["all"], "states": [s_id], "conditions": []},
            "howToApply": ["Apply via the urban local body/municipal corporation"],
            "documentsRequired": ["Aadhaar", "Land Ownership Proof", "Income Certificate"],
            "officialUrl": "https://mohua.gov.in",
            "whyQualifyTemplate": "Matches EWS income requirements for housing grants.",
            "nameHi": f"{s_hi} सीएम शहरी गरीब आवास मिशन",
            "shortNameHi": f"{s_hi} शहरी आवास",
            "benefitHi": f"{s_hi} में EWS के लिए पक्का घर बनाने के लिए ₹2.5 लाख का वित्तीय अनुदान",
            "simpleExplanationHi": "घर के निर्माण चरणों से जुड़ी वेतन वृद्धि में प्रदान की जाने वाली सब्सिडी।",
            "documentsRequiredHi": ["आधार", "भूमि स्वामित्व प्रमाण", "आय प्रमाण पत्र"],
            "howToApplyHi": ["शहरी स्थानीय निकाय/नगर निगम के माध्यम से आवेदन करें"]
        },
        {
            "id": f"{s_id.replace(' ','-')}-house-repair-grant",
            "name": f"{s_name} BPL Ghar Murammat Yojna",
            "shortName": f"{s_name} House Repair",
            "category": "housing",
            "icon": "🏠",
            "benefit": f"₹50,000 one-time grant for repairing dilapidated houses for BPL families in {s_name}",
            "benefitValue": 50000,
            "simpleExplanation": "Provides urgent financial help to poor families to repair failing roofs or structures.",
            "eligibility": {"minAge": 18, "maxAge": 100, "maxIncome": 100000, "categories": ["general", "obc", "sc", "st"], "gender": ["male", "female", "other"], "occupations": ["all"], "states": [s_id], "conditions": []},
            "howToApply": ["Apply at Gram Panchayat / Block Office"],
            "documentsRequired": ["Aadhaar", "BPL Certificate", "Photos of the damaged house"],
            "officialUrl": "https://rural.nic.in",
            "whyQualifyTemplate": "Eligible for BPL home repair grants.",
            "nameHi": f"{s_hi} बीपीएल घर मरम्मत योजना",
            "shortNameHi": f"{s_hi} घर की मरम्मत",
            "benefitHi": f"{s_hi} में बीपीएल परिवारों के लिए जर्जर घरों की मरम्मत के लिए ₹50,000 का एकमुश्त अनुदान",
            "simpleExplanationHi": "गरीब परिवारों को छत या संरचनाओं की मरम्मत के लिए तत्काल वित्तीय सहायता।",
            "documentsRequiredHi": ["आधार", "बीपीएल प्रमाणपत्र", "क्षतिग्रस्त घर की तस्वीरें"],
            "howToApplyHi": ["ग्राम पंचायत / ब्लॉक कार्यालय में आवेदन करें"]
        }
    ])

try:
    with open(SCHEMES_PATH, "r", encoding="utf-8") as f:
        existing_schemes = json.load(f)
except Exception:
    existing_schemes = []

existing_ids = {s.get("id") for s in existing_schemes}
added_count = 0

for s in new_schemes:
    if s["id"] not in existing_ids:
        existing_schemes.append(s)
        added_count += 1
        existing_ids.add(s["id"])

with open(SCHEMES_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_schemes, f, indent=4, ensure_ascii=False)

print(f"✅ Generated and added {added_count} new miscellaneous schemes. Total is now {len(existing_schemes)}.")
