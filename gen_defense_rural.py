"""
Add Defense and Rural schemes to schemes.json
"""
import json
import os

SCHEMES_PATH = os.path.join(os.path.dirname(__file__), "schemes.json")

NEW_SCHEMES = [
    # ===================== DEFENSE SCHEMES =====================
    {
        "id": "agnipath-agniveer",
        "name": "Agnipath Scheme (Agniveer)",
        "shortName": "Agnipath / Agniveer",
        "category": "defense",
        "icon": "🎖️",
        "benefit": "4-year military service with ₹11.71 lakh Seva Nidhi package on exit + monthly salary up to ₹40,000",
        "benefitValue": 1171000,
        "simpleExplanation": "Agnipath is the new recruitment pathway for the Indian Armed Forces (Army, Navy, Air Force). Youth aged 17.5–21 serve for 4 years as 'Agniveers'. You receive a monthly salary starting at ₹30,000 (rising to ₹40,000), plus a lump-sum Seva Nidhi package of ₹11.71 lakh upon exit. 25% of Agniveers are retained for permanent service. You also get extensive skill training, life insurance, and a certificate recognized for future jobs.",
        "eligibility": {
            "minAge": 17,
            "maxAge": 23,
            "maxIncome": 999999999,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female"],
            "occupations": "all",
            "states": "all",
            "conditions": []
        },
        "howToApply": [
            "Visit the official Indian Army (joinindianarmy.nic.in), Navy (joinindiannavy.gov.in), or Air Force (agnipathvayu.cdac.in) recruitment portals",
            "Register online and fill the application form",
            "Upload your Class 10/12 marksheet, Aadhaar, and medical fitness certificate",
            "Appear for the online written examination",
            "Clear the physical fitness test and medical examination",
            "Selected candidates join their respective training centres"
        ],
        "documentsRequired": [
            "Aadhaar Card",
            "Class 10th & 12th Marksheets",
            "Domicile Certificate",
            "Character Certificate",
            "Medical Fitness Certificate",
            "Passport-size Photos",
            "Sports/NCC Certificates (if any)"
        ],
        "officialUrl": "https://agnipathvayu.cdac.in",
        "whyQualifyTemplate": "Your age makes you eligible for the Agnipath scheme to serve in the Indian Armed Forces as an Agniveer.",
        "nameHi": "अग्निपथ योजना (अग्निवीर)",
        "shortNameHi": "अग्निपथ / अग्निवीर",
        "benefitHi": "4 साल की सैन्य सेवा, बाहर निकलने पर ₹11.71 लाख सेवा निधि पैकेज + ₹40,000 तक मासिक वेतन",
        "simpleExplanationHi": "अग्निपथ भारतीय सशस्त्र बलों (सेना, नौसेना, वायुसेना) में भर्ती का नया रास्ता है। 17.5-21 वर्ष की आयु के युवा 4 वर्ष तक 'अग्निवीर' के रूप में सेवा करते हैं। आपको ₹30,000 (₹40,000 तक बढ़ने वाला) मासिक वेतन और बाहर निकलने पर ₹11.71 लाख का सेवा निधि पैकेज मिलता है। 25% अग्निवीरों को स्थायी सेवा में रखा जाता है।",
        "documentsRequiredHi": ["आधार कार्ड", "कक्षा 10वीं और 12वीं की मार्कशीट", "अधिवास प्रमाण पत्र", "चरित्र प्रमाण पत्र", "चिकित्सा फिटनेस प्रमाण पत्र", "पासपोर्ट साइज फोटो", "खेल/एनसीसी प्रमाण पत्र (यदि हो)"],
        "howToApplyHi": ["आधिकारिक भारतीय सेना, नौसेना या वायुसेना भर्ती पोर्टल पर जाएं", "ऑनलाइन पंजीकरण करें और आवेदन पत्र भरें", "अपनी कक्षा 10/12 की मार्कशीट, आधार और मेडिकल फिटनेस प्रमाणपत्र अपलोड करें", "ऑनलाइन लिखित परीक्षा दें", "शारीरिक फिटनेस टेस्ट और मेडिकल परीक्षा पास करें", "चयनित उम्मीदवार अपने प्रशिक्षण केंद्रों में शामिल होते हैं"]
    },
    {
        "id": "ex-servicemen-echs",
        "name": "Ex-Servicemen Contributory Health Scheme (ECHS)",
        "shortName": "ECHS Health Cover",
        "category": "defense",
        "icon": "🏥",
        "benefit": "Free lifetime medical treatment for ex-servicemen and their dependents at ECHS polyclinics and empanelled hospitals",
        "benefitValue": 500000,
        "simpleExplanation": "If you are a retired/released armed forces personnel, you and your family get free medical care for life. This covers OPD consultations, medicines, hospital admissions, surgeries, and even advanced treatments like heart surgery or cancer treatment at ECHS polyclinics and empanelled private hospitals across India.",
        "eligibility": {
            "minAge": 18,
            "maxAge": 100,
            "maxIncome": 999999999,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female", "other"],
            "occupations": "all",
            "states": "all",
            "conditions": ["ex_servicemen"]
        },
        "howToApply": [
            "Visit the nearest ECHS polyclinic or record office",
            "Fill the ECHS membership application form",
            "Submit your discharge book/PPO (Pension Payment Order)",
            "Pay the one-time contribution amount based on your rank",
            "A Smart Card will be issued for you and your dependents",
            "Use this card at any ECHS polyclinic or empanelled hospital"
        ],
        "documentsRequired": ["Discharge Book", "Pension Payment Order (PPO)", "Aadhaar Card", "Family Details/Dependents Certificate", "Passport-size Photos", "Bank Account Details"],
        "officialUrl": "https://echs.gov.in",
        "whyQualifyTemplate": "As an ex-serviceman, you and your dependents are eligible for free lifetime medical care under ECHS.",
        "nameHi": "पूर्व सैनिक अंशदायी स्वास्थ्य योजना (ईसीएचएस)",
        "shortNameHi": "ईसीएचएस स्वास्थ्य कवर",
        "benefitHi": "पूर्व सैनिकों और उनके आश्रितों के लिए ईसीएचएस पॉलीक्लिनिक और पैनलबद्ध अस्पतालों में मुफ्त आजीवन चिकित्सा उपचार",
        "simpleExplanationHi": "यदि आप एक सेवानिवृत्त/मुक्त सशस्त्र बल कर्मी हैं, तो आपको और आपके परिवार को जीवन भर मुफ्त चिकित्सा देखभाल मिलती है।",
        "documentsRequiredHi": ["डिस्चार्ज बुक", "पेंशन भुगतान आदेश (पीपीओ)", "आधार कार्ड", "परिवार विवरण/आश्रित प्रमाण पत्र", "पासपोर्ट साइज फोटो", "बैंक खाता विवरण"],
        "howToApplyHi": ["निकटतम ईसीएचएस पॉलीक्लिनिक या रिकॉर्ड ऑफिस जाएं", "ईसीएचएस सदस्यता आवेदन पत्र भरें", "अपनी डिस्चार्ज बुक/पीपीओ जमा करें", "अपने रैंक के आधार पर एकमुश्त अंशदान राशि का भुगतान करें", "आपके और आपके आश्रितों के लिए स्मार्ट कार्ड जारी किया जाएगा", "किसी भी ईसीएचएस पॉलीक्लिनिक या पैनलबद्ध अस्पताल में इस कार्ड का उपयोग करें"]
    },
    {
        "id": "armed-forces-flag-day",
        "name": "Armed Forces Flag Day Fund (AFFDF)",
        "shortName": "Flag Day Fund",
        "category": "defense",
        "icon": "🇮🇳",
        "benefit": "Financial assistance for war widows, disabled soldiers, and ex-servicemen — grants from ₹4,000 to ₹16,000/month + lump sum aid",
        "benefitValue": 192000,
        "simpleExplanation": "This fund provides financial help to families of martyred soldiers (war widows), battle-disabled soldiers, and needy ex-servicemen. It covers monthly grants for survival, education grants for children, medical assistance, and one-time financial aid during emergencies. War widows receive enhanced monthly pensions and their children get priority admission in Sainik Schools.",
        "eligibility": {
            "minAge": 18,
            "maxAge": 100,
            "maxIncome": 999999999,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female", "other"],
            "occupations": "all",
            "states": "all",
            "conditions": ["ex_servicemen", "widow"]
        },
        "howToApply": [
            "Contact your nearest Kendriya Sainik Board or Rajya Sainik Board",
            "Submit your application through the Zila Sainik Board",
            "Provide discharge documents and proof of disability/war widow status",
            "The board will verify your records and process the grant",
            "Financial assistance is disbursed through your bank account"
        ],
        "documentsRequired": ["Discharge Certificate", "Pension Payment Order", "Aadhaar Card", "Disability Certificate (if applicable)", "Death Certificate of soldier (for war widows)", "Bank Account Details"],
        "officialUrl": "https://ksb.gov.in",
        "whyQualifyTemplate": "As an ex-serviceman or dependent of a defense personnel, you may be eligible for financial assistance.",
        "nameHi": "सशस्त्र बल ध्वज दिवस निधि",
        "shortNameHi": "ध्वज दिवस निधि",
        "benefitHi": "युद्ध विधवाओं, विकलांग सैनिकों और पूर्व सैनिकों के लिए वित्तीय सहायता — ₹4,000 से ₹16,000/माह अनुदान + एकमुश्त सहायता",
        "simpleExplanationHi": "यह कोष शहीद सैनिकों के परिवारों (युद्ध विधवाओं), युद्ध-विकलांग सैनिकों और जरूरतमंद पूर्व सैनिकों को वित्तीय सहायता प्रदान करता है।",
        "documentsRequiredHi": ["मुक्ति प्रमाण पत्र", "पेंशन भुगतान आदेश", "आधार कार्ड", "विकलांगता प्रमाण पत्र (यदि लागू हो)", "सैनिक का मृत्यु प्रमाण पत्र (युद्ध विधवाओं के लिए)", "बैंक खाता विवरण"],
        "howToApplyHi": ["अपने निकटतम केंद्रीय सैनिक बोर्ड या राज्य सैनिक बोर्ड से संपर्क करें", "जिला सैनिक बोर्ड के माध्यम से अपना आवेदन जमा करें", "मुक्ति दस्तावेज और विकलांगता/युद्ध विधवा स्थिति का प्रमाण प्रदान करें", "बोर्ड आपके रिकॉर्ड सत्यापित करेगा और अनुदान की प्रक्रिया करेगा", "वित्तीय सहायता आपके बैंक खाते के माध्यम से वितरित की जाती है"]
    },
    {
        "id": "desw-scholarship",
        "name": "PM Scholarship Scheme for Children of Armed Forces/Ex-Servicemen (DESW)",
        "shortName": "PM Defense Scholarship",
        "category": "defense",
        "icon": "🎓",
        "benefit": "₹30,000/year for boys and ₹36,000/year for girls pursuing professional courses",
        "benefitValue": 36000,
        "simpleExplanation": "If your father/mother served in the Armed Forces (Army, Navy, Air Force) or paramilitary forces, you can get a scholarship for professional degree courses like engineering, medicine, MBA, etc. Boys get ₹2,500/month and girls get ₹3,000/month for the entire duration of the course. Children of martyred/disabled soldiers get priority.",
        "eligibility": {
            "minAge": 16,
            "maxAge": 30,
            "maxIncome": 999999999,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female"],
            "occupations": ["student"],
            "states": "all",
            "conditions": ["student", "ex_servicemen"]
        },
        "howToApply": [
            "Visit the Kendriya Sainik Board Scholarship Portal (ksb.gov.in)",
            "Register and create an account with your parent's service details",
            "Fill the scholarship application form online",
            "Upload your admission letter, marksheets, and parent's service documents",
            "Application is verified by Zila Sainik Board",
            "Scholarship is directly credited to your bank account"
        ],
        "documentsRequired": ["Parent's Discharge/Service Certificate", "Student's Aadhaar Card", "Admission Letter from College", "Marksheets", "Bank Account Details", "Passport-size Photo"],
        "officialUrl": "https://ksb.gov.in",
        "whyQualifyTemplate": "As a child of an armed forces/ex-servicemen, you qualify for this scholarship for professional education.",
        "nameHi": "सशस्त्र बल/पूर्व सैनिकों के बच्चों के लिए पीएम छात्रवृत्ति योजना (डीईएसडब्ल्यू)",
        "shortNameHi": "पीएम रक्षा छात्रवृत्ति",
        "benefitHi": "पेशेवर पाठ्यक्रमों के लिए लड़कों को ₹30,000/वर्ष और लड़कियों को ₹36,000/वर्ष",
        "simpleExplanationHi": "यदि आपके पिता/माता ने सशस्त्र बलों या अर्धसैनिक बलों में सेवा की है, तो आप पेशेवर डिग्री पाठ्यक्रमों के लिए छात्रवृत्ति प्राप्त कर सकते हैं।",
        "documentsRequiredHi": ["माता-पिता का डिस्चार्ज/सेवा प्रमाण पत्र", "छात्र का आधार कार्ड", "कॉलेज से प्रवेश पत्र", "मार्कशीट", "बैंक खाता विवरण", "पासपोर्ट साइज फोटो"],
        "howToApplyHi": ["केंद्रीय सैनिक बोर्ड छात्रवृत्ति पोर्टल (ksb.gov.in) पर जाएं", "अपने माता-पिता के सेवा विवरण के साथ पंजीकरण करें", "ऑनलाइन छात्रवृत्ति आवेदन पत्र भरें", "अपना प्रवेश पत्र, मार्कशीट और माता-पिता के सेवा दस्तावेज अपलोड करें", "आवेदन जिला सैनिक बोर्ड द्वारा सत्यापित किया जाता है", "छात्रवृत्ति सीधे आपके बैंक खाते में जमा की जाती है"]
    },
    {
        "id": "csd-canteen",
        "name": "Canteen Stores Department (CSD) Benefits",
        "shortName": "CSD Canteen",
        "category": "defense",
        "icon": "🛒",
        "benefit": "Subsidized goods (cars, appliances, groceries) at 15-30% below market rates for defense personnel",
        "benefitValue": 100000,
        "simpleExplanation": "Serving and retired defense personnel can buy daily use items, electronics, vehicles, and appliances at heavily subsidized rates through CSD canteens. The prices are 15-30% lower than market rates. This includes cars, two-wheelers, TVs, refrigerators, groceries, and much more. Family members with valid dependent cards can also avail benefits.",
        "eligibility": {
            "minAge": 18,
            "maxAge": 100,
            "maxIncome": 999999999,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female", "other"],
            "occupations": "all",
            "states": "all",
            "conditions": ["ex_servicemen"]
        },
        "howToApply": [
            "Visit your nearest CSD (Canteen Stores Department) outlet",
            "Carry your valid CSD Smart Card or dependent card",
            "For vehicles and high-value items, an indent must be placed through Unit/Record Office",
            "Items are delivered through the CSD network",
            "Online ordering is also available via the CSD portal for select items"
        ],
        "documentsRequired": ["CSD Smart Card", "Service/Discharge Book", "Aadhaar Card", "Dependent Card (for family members)"],
        "officialUrl": "https://csdindia.gov.in",
        "whyQualifyTemplate": "As defense personnel or an ex-serviceman, you qualify for subsidized purchases through CSD canteens.",
        "nameHi": "कैंटीन स्टोर्स डिपार्टमेंट (सीएसडी) लाभ",
        "shortNameHi": "सीएसडी कैंटीन",
        "benefitHi": "रक्षा कर्मियों के लिए बाजार दरों से 15-30% कम पर रियायती सामान (कारें, उपकरण, किराने का सामान)",
        "simpleExplanationHi": "सेवारत और सेवानिवृत्त रक्षा कर्मी सीएसडी कैंटीन के माध्यम से दैनिक उपयोग की वस्तुएं, इलेक्ट्रॉनिक्स, वाहन और उपकरण भारी रियायती दरों पर खरीद सकते हैं।",
        "documentsRequiredHi": ["सीएसडी स्मार्ट कार्ड", "सेवा/डिस्चार्ज बुक", "आधार कार्ड", "आश्रित कार्ड (परिवार के सदस्यों के लिए)"],
        "howToApplyHi": ["अपने निकटतम सीएसडी आउटलेट पर जाएं", "अपना वैध सीएसडी स्मार्ट कार्ड या आश्रित कार्ड ले जाएं", "वाहनों और उच्च-मूल्य की वस्तुओं के लिए यूनिट/रिकॉर्ड ऑफिस के माध्यम से इंडेंट लगाना होगा", "सामान सीएसडी नेटवर्क के माध्यम से वितरित किया जाता है", "चुनिंदा वस्तुओं के लिए सीएसडी पोर्टल के माध्यम से ऑनलाइन ऑर्डर भी उपलब्ध है"]
    },

    # ===================== RURAL SCHEMES =====================
    {
        "id": "pmgsy",
        "name": "Pradhan Mantri Gram Sadak Yojana (PMGSY)",
        "shortName": "PM Gram Sadak Yojana",
        "category": "rural",
        "icon": "🛤️",
        "benefit": "All-weather road connectivity to unconnected rural habitations — community benefit",
        "benefitValue": 0,
        "simpleExplanation": "This scheme builds proper pucca (all-weather) roads connecting villages to nearby towns and markets. If your village doesn't have a proper road, you can request the Gram Panchayat to include it in the PMGSY plan. Priority is given to villages with 500+ population (250+ in hilly/tribal areas). The roads are built to national standards and maintained for 5 years.",
        "eligibility": {
            "minAge": 18,
            "maxAge": 100,
            "maxIncome": 999999999,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female", "other"],
            "occupations": "all",
            "states": "all",
            "conditions": ["rural"]
        },
        "howToApply": [
            "Submit a request through your Gram Panchayat",
            "The village must be listed in the Core Network as unconnected",
            "State-level PMGSY team surveys and approves the road project",
            "Road construction is monitored through satellite imagery",
            "You can track progress at pmgsy.nic.in"
        ],
        "documentsRequired": ["Gram Panchayat Resolution Letter", "Village Census Data"],
        "officialUrl": "https://pmgsy.nic.in",
        "whyQualifyTemplate": "As a rural resident, your village may benefit from the PMGSY all-weather road construction program.",
        "nameHi": "प्रधानमंत्री ग्राम सड़क योजना (पीएमजीएसवाई)",
        "shortNameHi": "पीएम ग्राम सड़क योजना",
        "benefitHi": "असंबद्ध ग्रामीण बस्तियों को सर्व-ऋतु सड़क कनेक्टिविटी — सामुदायिक लाभ",
        "simpleExplanationHi": "यह योजना गांवों को पास के शहरों और बाजारों से जोड़ने वाली उचित पक्की (सर्व-ऋतु) सड़कें बनाती है।",
        "documentsRequiredHi": ["ग्राम पंचायत प्रस्ताव पत्र", "गांव की जनगणना डेटा"],
        "howToApplyHi": ["अपने ग्राम पंचायत के माध्यम से अनुरोध जमा करें", "गांव को कोर नेटवर्क में असंबद्ध के रूप में सूचीबद्ध होना चाहिए", "राज्य स्तरीय पीएमजीएसवाई टीम सर्वेक्षण करती है और सड़क परियोजना को मंजूरी देती है", "सड़क निर्माण की निगरानी उपग्रह इमेजरी के माध्यम से की जाती है", "आप pmgsy.nic.in पर प्रगति देख सकते हैं"]
    },
    {
        "id": "ddu-gky",
        "name": "Deen Dayal Upadhyaya Grameen Kaushalya Yojana (DDU-GKY)",
        "shortName": "DDU-GKY",
        "category": "rural",
        "icon": "🛠️",
        "benefit": "Free skill training + guaranteed job placement with minimum ₹6,000/month salary for rural youth",
        "benefitValue": 72000,
        "simpleExplanation": "Are you a young person from a rural area looking for a good job? DDU-GKY provides completely free skill training (3-12 months) in sectors like IT, retail, healthcare, automobile, hospitality, and more. After training, you are guaranteed a job with a minimum salary of ₹6,000/month. Training includes free food, accommodation, and uniform. The government also helps with job placement in cities.",
        "eligibility": {
            "minAge": 15,
            "maxAge": 35,
            "maxIncome": 300000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female", "other"],
            "occupations": ["unemployed", "laborer", "daily_wage", "student"],
            "states": "all",
            "conditions": ["rural"],
            "priority": ["sc", "st"]
        },
        "howToApply": [
            "Visit ddugky.gov.in or contact your Gram Panchayat",
            "Register at the nearest DDU-GKY training centre",
            "Choose your preferred skill/trade from available courses",
            "Complete the training program (3-12 months)",
            "Get placed in a job with a minimum guaranteed salary"
        ],
        "documentsRequired": ["Aadhaar Card", "Class 10th Marksheet", "Bank Account Details", "BPL/Income Certificate", "Passport-size Photos", "Address Proof"],
        "officialUrl": "https://ddugky.gov.in",
        "whyQualifyTemplate": "As a rural youth, you qualify for free skill training and guaranteed job placement under DDU-GKY.",
        "nameHi": "दीन दयाल उपाध्याय ग्रामीण कौशल्य योजना (डीडीयू-जीकेवाई)",
        "shortNameHi": "डीडीयू-जीकेवाई",
        "benefitHi": "मुफ्त कौशल प्रशिक्षण + ग्रामीण युवाओं के लिए न्यूनतम ₹6,000/माह वेतन के साथ गारंटीड नौकरी",
        "simpleExplanationHi": "क्या आप ग्रामीण क्षेत्र के एक युवा हैं जो अच्छी नौकरी की तलाश में हैं? डीडीयू-जीकेवाई विभिन्न क्षेत्रों में पूरी तरह से मुफ्त कौशल प्रशिक्षण (3-12 महीने) प्रदान करता है।",
        "documentsRequiredHi": ["आधार कार्ड", "कक्षा 10वीं मार्कशीट", "बैंक खाता विवरण", "बीपीएल/आय प्रमाण पत्र", "पासपोर्ट साइज फोटो", "पता प्रमाण"],
        "howToApplyHi": ["ddugky.gov.in पर जाएं या अपने ग्राम पंचायत से संपर्क करें", "निकटतम डीडीयू-जीकेवाई प्रशिक्षण केंद्र में पंजीकरण करें", "उपलब्ध पाठ्यक्रमों में से अपना पसंदीदा कौशल/व्यापार चुनें", "प्रशिक्षण कार्यक्रम पूरा करें (3-12 महीने)", "न्यूनतम गारंटीड वेतन के साथ नौकरी में रखा जाए"]
    },
    {
        "id": "rurban-mission",
        "name": "Shyama Prasad Mukherji Rurban Mission (SPMRM)",
        "shortName": "Rurban Mission",
        "category": "rural",
        "icon": "🏘️",
        "benefit": "Urban-level amenities (water, roads, internet, markets) delivered to rural clusters",
        "benefitValue": 0,
        "simpleExplanation": "This mission transforms clusters of villages into 'Rurban' areas by providing urban facilities while retaining the village character. Your village cluster can get piped water, proper drainage, paved internal roads, digital connectivity, skill development centres, health centres, upgraded schools, and rural markets — all funded by the government.",
        "eligibility": {
            "minAge": 18,
            "maxAge": 100,
            "maxIncome": 999999999,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female", "other"],
            "occupations": "all",
            "states": "all",
            "conditions": ["rural"]
        },
        "howToApply": [
            "Your Gram Panchayat applies through the state government for cluster selection",
            "Selected clusters receive an Integrated Cluster Action Plan (ICAP)",
            "Projects are executed by line departments and monitored centrally",
            "Residents benefit from improved infrastructure as projects are completed",
            "Track progress at rurban.gov.in"
        ],
        "documentsRequired": ["Gram Panchayat application"],
        "officialUrl": "https://rurban.gov.in",
        "whyQualifyTemplate": "As a rural resident, your village cluster may benefit from urban-level infrastructure under the Rurban Mission.",
        "nameHi": "श्यामा प्रसाद मुखर्जी रूर्बन मिशन",
        "shortNameHi": "रूर्बन मिशन",
        "benefitHi": "ग्रामीण समूहों को शहरी स्तर की सुविधाएं (पानी, सड़कें, इंटरनेट, बाजार)",
        "simpleExplanationHi": "यह मिशन गांवों के समूहों को 'रूर्बन' क्षेत्रों में बदलता है, गांव के चरित्र को बनाए रखते हुए शहरी सुविधाएं प्रदान करता है।",
        "documentsRequiredHi": ["ग्राम पंचायत आवेदन"],
        "howToApplyHi": ["आपका ग्राम पंचायत क्लस्टर चयन के लिए राज्य सरकार के माध्यम से आवेदन करता है", "चयनित क्लस्टर को एकीकृत क्लस्टर कार्य योजना (आईसीएपी) प्राप्त होती है", "परियोजनाओं को लाइन विभागों द्वारा निष्पादित किया जाता है", "बुनियादी ढांचे में सुधार से निवासियों को लाभ होता है", "rurban.gov.in पर प्रगति देखें"]
    },
    {
        "id": "pmksy-irrigation",
        "name": "Pradhan Mantri Krishi Sinchayee Yojana (PMKSY)",
        "shortName": "PM Krishi Sinchayee",
        "category": "rural",
        "icon": "💧",
        "benefit": "Subsidized micro-irrigation (drip/sprinkler) systems — 55-80% government subsidy on equipment cost",
        "benefitValue": 50000,
        "simpleExplanation": "Water is the lifeline of farming. This scheme helps you irrigate your farmland efficiently using drip and sprinkler systems at very low cost. The government pays 55% of the equipment cost for general farmers and up to 80% for small/marginal farmers and SC/ST farmers. This saves water by 40-50% and increases crop yield significantly.",
        "eligibility": {
            "minAge": 18,
            "maxAge": 100,
            "maxIncome": 500000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female", "other"],
            "occupations": ["farmer"],
            "states": "all",
            "conditions": ["farmer", "rural"],
            "priority": ["sc", "st"]
        },
        "howToApply": [
            "Contact your District Agriculture Office or Block Development Office",
            "Apply online through your state's agriculture department portal",
            "Select the micro-irrigation system (drip or sprinkler) suitable for your crop",
            "Submit land documents and farmer ID",
            "After approval, purchase the system from empanelled vendors",
            "Submit bills for subsidy reimbursement"
        ],
        "documentsRequired": ["Aadhaar Card", "Land Ownership Documents", "Kisan Credit Card or Farmer ID", "Bank Account Details", "Passport-size Photo"],
        "officialUrl": "https://pmksy.gov.in",
        "whyQualifyTemplate": "As a farmer, you qualify for heavily subsidized micro-irrigation systems to improve your crop yield and save water.",
        "nameHi": "प्रधानमंत्री कृषि सिंचाई योजना (पीएमकेएसवाई)",
        "shortNameHi": "पीएम कृषि सिंचाई",
        "benefitHi": "रियायती सूक्ष्म सिंचाई (ड्रिप/स्प्रिंकलर) प्रणाली — उपकरण लागत पर 55-80% सरकारी सब्सिडी",
        "simpleExplanationHi": "पानी खेती की जीवन रेखा है। यह योजना आपको बहुत कम लागत पर ड्रिप और स्प्रिंकलर प्रणालियों का उपयोग करके अपनी खेती की जमीन को कुशलतापूर्वक सिंचित करने में मदद करती है।",
        "documentsRequiredHi": ["आधार कार्ड", "भूमि स्वामित्व दस्तावेज", "किसान क्रेडिट कार्ड या किसान आईडी", "बैंक खाता विवरण", "पासपोर्ट साइज फोटो"],
        "howToApplyHi": ["अपने जिला कृषि कार्यालय या ब्लॉक विकास कार्यालय से संपर्क करें", "अपने राज्य के कृषि विभाग पोर्टल के माध्यम से ऑनलाइन आवेदन करें", "अपनी फसल के लिए उपयुक्त सूक्ष्म सिंचाई प्रणाली (ड्रिप या स्प्रिंकलर) चुनें", "भूमि दस्तावेज और किसान आईडी जमा करें", "अनुमोदन के बाद पैनलबद्ध विक्रेताओं से प्रणाली खरीदें", "सब्सिडी प्रतिपूर्ति के लिए बिल जमा करें"]
    },
    {
        "id": "saansad-adarsh-gram",
        "name": "Saansad Adarsh Gram Yojana (SAGY)",
        "shortName": "Adarsh Gram Yojana",
        "category": "rural",
        "icon": "🏡",
        "benefit": "Holistic village development — your entire village gets upgraded infrastructure, education, and healthcare facilities",
        "benefitValue": 0,
        "simpleExplanation": "Under this scheme, your local Member of Parliament (MP) adopts a village and works to transform it into a 'Model Village' (Adarsh Gram). The village gets improved sanitation, clean drinking water, better roads, schools, health centres, solar lights, digital connectivity, and livelihood opportunities. It's a complete package to make your village self-sufficient and modern.",
        "eligibility": {
            "minAge": 18,
            "maxAge": 100,
            "maxIncome": 999999999,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female", "other"],
            "occupations": "all",
            "states": "all",
            "conditions": ["rural"]
        },
        "howToApply": [
            "Contact your local Member of Parliament (MP) to nominate your village",
            "The MP selects a Gram Panchayat to adopt as Adarsh Gram",
            "A Village Development Plan (VDP) is created with community participation",
            "Various central and state schemes are converged for implementation",
            "Track adopted villages and progress at saanjhi.gov.in"
        ],
        "documentsRequired": ["Gram Panchayat details", "Community request letter to MP"],
        "officialUrl": "https://saanjhi.gov.in",
        "whyQualifyTemplate": "As a rural resident, your village can benefit from holistic development under the Adarsh Gram Yojana.",
        "nameHi": "सांसद आदर्श ग्राम योजना (एसएजीवाई)",
        "shortNameHi": "आदर्श ग्राम योजना",
        "benefitHi": "समग्र ग्राम विकास — आपके पूरे गांव को उन्नत बुनियादी ढांचा, शिक्षा और स्वास्थ्य सुविधाएं मिलती हैं",
        "simpleExplanationHi": "इस योजना के तहत आपके स्थानीय सांसद एक गांव को गोद लेते हैं और इसे 'आदर्श ग्राम' में बदलने के लिए काम करते हैं।",
        "documentsRequiredHi": ["ग्राम पंचायत विवरण", "सांसद को सामुदायिक अनुरोध पत्र"],
        "howToApplyHi": ["अपने गांव को मनोनीत करने के लिए अपने स्थानीय सांसद से संपर्क करें", "सांसद आदर्श ग्राम के रूप में अपनाने के लिए एक ग्राम पंचायत का चयन करते हैं", "सामुदायिक भागीदारी के साथ ग्राम विकास योजना (वीडीपी) बनाई जाती है", "विभिन्न केंद्रीय और राज्य योजनाओं को कार्यान्वयन के लिए अभिसरित किया जाता है", "saanjhi.gov.in पर गोद लिए गए गांवों और प्रगति को देखें"]
    },
    {
        "id": "national-rural-livelihood",
        "name": "Deendayal Antyodaya Yojana - National Rural Livelihoods Mission (DAY-NRLM)",
        "shortName": "DAY-NRLM",
        "category": "rural",
        "icon": "👩‍🌾",
        "benefit": "Self-Help Group formation + revolving fund of ₹15,000 + community investment fund up to ₹2.5 lakh + bank linkage",
        "benefitValue": 250000,
        "simpleExplanation": "This mission helps poor rural women form Self-Help Groups (SHGs) for savings and creating their own income. Each SHG receives a revolving fund (₹15,000) and can access community investment fund (up to ₹2.5 lakh). The SHG also gets linked to banks for larger loans. Members learn livelihood skills, start micro-enterprises, and become financially independent.",
        "eligibility": {
            "minAge": 18,
            "maxAge": 65,
            "maxIncome": 300000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["female"],
            "occupations": ["homemaker", "farmer", "laborer", "daily_wage", "self_employed", "unemployed"],
            "states": "all",
            "conditions": ["rural"],
            "priority": ["sc", "st"]
        },
        "howToApply": [
            "Contact your Gram Panchayat or Block Development Office",
            "Form a Self-Help Group (SHG) with 10-15 women from your village",
            "Register the SHG at the Block Mission Management Unit",
            "Start regular savings and internal lending within the group",
            "Apply for the revolving fund through your cluster/block coordinator",
            "Get bank linkage for larger credit access"
        ],
        "documentsRequired": ["Aadhaar Card of all SHG members", "SHG Registration Document", "Bank Account (in SHG name)", "Minutes of SHG meetings", "BPL/Income Certificate"],
        "officialUrl": "https://aajeevika.gov.in",
        "whyQualifyTemplate": "As a rural woman, you can form a Self-Help Group and access revolving funds, bank linkages, and livelihood training.",
        "nameHi": "दीनदयाल अंत्योदय योजना - राष्ट्रीय ग्रामीण आजीविका मिशन (डीएवाई-एनआरएलएम)",
        "shortNameHi": "डीएवाई-एनआरएलएम",
        "benefitHi": "स्वयं सहायता समूह गठन + ₹15,000 का रिवॉल्विंग फंड + ₹2.5 लाख तक का सामुदायिक निवेश कोष + बैंक लिंकेज",
        "simpleExplanationHi": "यह मिशन गरीब ग्रामीण महिलाओं को बचत और अपनी आय बनाने के लिए स्वयं सहायता समूह (एसएचजी) बनाने में मदद करता है।",
        "documentsRequiredHi": ["सभी एसएचजी सदस्यों का आधार कार्ड", "एसएचजी पंजीकरण दस्तावेज", "बैंक खाता (एसएचजी के नाम पर)", "एसएचजी बैठकों के कार्यवृत्त", "बीपीएल/आय प्रमाण पत्र"],
        "howToApplyHi": ["अपने ग्राम पंचायत या ब्लॉक विकास कार्यालय से संपर्क करें", "अपने गांव की 10-15 महिलाओं के साथ स्वयं सहायता समूह (एसएचजी) बनाएं", "ब्लॉक मिशन प्रबंधन इकाई में एसएचजी का पंजीकरण करें", "समूह के भीतर नियमित बचत और आंतरिक ऋण शुरू करें", "अपने क्लस्टर/ब्लॉक समन्वयक के माध्यम से रिवॉल्विंग फंड के लिए आवेदन करें", "बड़ी क्रेडिट पहुंच के लिए बैंक लिंकेज प्राप्त करें"]
    },
    {
        "id": "swachh-bharat-gramin",
        "name": "Swachh Bharat Mission (Gramin) - Phase 2",
        "shortName": "Swachh Bharat Gramin",
        "category": "rural",
        "icon": "🚽",
        "benefit": "₹12,000 incentive for building a household toilet + community sanitary complexes in villages",
        "benefitValue": 12000,
        "simpleExplanation": "Don't have a toilet at home? The government gives ₹12,000 to help you build one. This is for rural families who don't have a proper toilet. The money is deposited into your bank account in two parts — after starting construction and after completion. The scheme also builds community toilets, solid waste management systems, and plastic waste management units in villages.",
        "eligibility": {
            "minAge": 18,
            "maxAge": 100,
            "maxIncome": 300000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female", "other"],
            "occupations": "all",
            "states": "all",
            "conditions": ["rural"],
            "priority": ["sc", "st"]
        },
        "howToApply": [
            "Contact your Gram Panchayat and apply for toilet construction support",
            "A village survey will confirm your eligibility (no existing toilet)",
            "Receive the first installment to begin construction",
            "Build the toilet as per the approved design",
            "After verification by Gram Panchayat, receive the second installment"
        ],
        "documentsRequired": ["Aadhaar Card", "BPL Card/Income Certificate", "Bank Account Details", "Address Proof", "No-toilet Declaration"],
        "officialUrl": "https://swachhbharatmission.gov.in",
        "whyQualifyTemplate": "As a rural resident without a household toilet, you qualify for ₹12,000 construction incentive under Swachh Bharat.",
        "nameHi": "स्वच्छ भारत मिशन (ग्रामीण) - चरण 2",
        "shortNameHi": "स्वच्छ भारत ग्रामीण",
        "benefitHi": "घरेलू शौचालय बनाने के लिए ₹12,000 प्रोत्साहन + गांवों में सामुदायिक स्वच्छता परिसर",
        "simpleExplanationHi": "क्या आपके घर में शौचालय नहीं है? सरकार इसे बनाने में मदद के लिए ₹12,000 देती है।",
        "documentsRequiredHi": ["आधार कार्ड", "बीपीएल कार्ड/आय प्रमाण पत्र", "बैंक खाता विवरण", "पता प्रमाण", "शौचालय नहीं होने की घोषणा"],
        "howToApplyHi": ["अपने ग्राम पंचायत से संपर्क करें और शौचालय निर्माण सहायता के लिए आवेदन करें", "एक ग्राम सर्वेक्षण आपकी पात्रता की पुष्टि करेगा (कोई मौजूदा शौचालय नहीं)", "निर्माण शुरू करने के लिए पहली किस्त प्राप्त करें", "स्वीकृत डिजाइन के अनुसार शौचालय बनाएं", "ग्राम पंचायत द्वारा सत्यापन के बाद दूसरी किस्त प्राप्त करें"]
    },
    {
        "id": "pm-ujala-rural",
        "name": "UJALA Yojana (Unnat Jyoti by Affordable LEDs for All)",
        "shortName": "UJALA LED Scheme",
        "category": "rural",
        "icon": "💡",
        "benefit": "LED bulbs at just ₹10 each (market price ₹100+) — save up to ₹500/year on electricity bills",
        "benefitValue": 500,
        "simpleExplanation": "Replace your old incandescent bulbs with energy-efficient LED bulbs at just ₹10 each! Normal LED bulbs cost ₹100+ in the market. Each household can buy up to 5 LED bulbs. This reduces your electricity bill by 40-50% on lighting costs. The bulbs come with a 3-year replacement warranty — if they stop working, you get a free replacement.",
        "eligibility": {
            "minAge": 18,
            "maxAge": 100,
            "maxIncome": 999999999,
            "categories": ["general", "obc", "sc", "st"],
            "gender": ["male", "female", "other"],
            "occupations": "all",
            "states": "all",
            "conditions": []
        },
        "howToApply": [
            "Visit a UJALA distribution centre (usually at DISCOM office or designated kiosks)",
            "Bring your latest electricity bill as proof of connection",
            "Buy up to 5 LED bulbs at ₹10 each",
            "The old bulbs are collected and recycled",
            "For replacement of faulty bulbs, carry the original bill"
        ],
        "documentsRequired": ["Latest Electricity Bill", "Aadhaar Card or any Photo ID"],
        "officialUrl": "https://www.ujala.gov.in",
        "whyQualifyTemplate": "Any household with an electricity connection can buy subsidized LED bulbs under the UJALA scheme.",
        "nameHi": "उजाला योजना (सभी के लिए किफायती एलईडी द्वारा उन्नत ज्योति)",
        "shortNameHi": "उजाला एलईडी योजना",
        "benefitHi": "सिर्फ ₹10 में एलईडी बल्ब (बाजार मूल्य ₹100+) — बिजली बिलों पर सालाना ₹500 तक बचाएं",
        "simpleExplanationHi": "अपने पुराने बल्बों को मात्र ₹10 में ऊर्जा-कुशल एलईडी बल्बों से बदलें! प्रत्येक परिवार 5 एलईडी बल्ब तक खरीद सकता है।",
        "documentsRequiredHi": ["नवीनतम बिजली बिल", "आधार कार्ड या कोई फोटो आईडी"],
        "howToApplyHi": ["उजाला वितरण केंद्र पर जाएं", "कनेक्शन के प्रमाण के रूप में अपना नवीनतम बिजली बिल लाएं", "₹10 प्रत्येक पर 5 एलईडी बल्ब तक खरीदें", "पुराने बल्ब एकत्र किए जाते हैं और रीसायकल किए जाते हैं", "खराब बल्बों के प्रतिस्थापन के लिए मूल बिल ले जाएं"]
    }
]

# Load existing schemes
with open(SCHEMES_PATH, "r", encoding="utf-8") as f:
    schemes = json.load(f)

# Check for duplicates
existing_ids = {s["id"] for s in schemes}
added = 0
for scheme in NEW_SCHEMES:
    if scheme["id"] not in existing_ids:
        schemes.append(scheme)
        added += 1
        print(f"  ✅ Added: {scheme['shortName']}")
    else:
        print(f"  ⏩ Skipped (exists): {scheme['shortName']}")

# Save
with open(SCHEMES_PATH, "w", encoding="utf-8") as f:
    json.dump(schemes, f, ensure_ascii=False, indent=4)

print(f"\n🎯 Done! Added {added} new schemes. Total schemes now: {len(schemes)}")
