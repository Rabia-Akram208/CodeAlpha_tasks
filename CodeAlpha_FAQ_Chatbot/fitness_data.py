# fitness_data.py

faq_data = {
    # --- NUTRITION & DIET ---
    "What is a balanced diet?": (
        "### Understanding a Balanced Diet\n"
        "A balanced diet provides all essential nutrients your body needs in proper proportions. "
        "It typically includes:\n"
        "* **Proteins:** Lean meat, eggs, legumes, tofu for muscle repair and growth.\n"
        "* **Carbohydrates:** Whole grains, vegetables, and fruits for energy.\n"
        "* **Fats:** Healthy fats from nuts, seeds, avocados, and olive oil for brain function.\n"
        "* **Vitamins & Minerals:** From fruits, vegetables, dairy, and fortified foods.\n"
        "* **Hydration:** Adequate water intake (~2–3 liters/day) is essential for metabolism and digestion.\n"
        "> **Pro Tip:** Aim for variety and portion control; avoid excessive processed foods."
    ),

    "How many calories should I eat daily?": (
        "### Daily Calorie Requirements\n"
        "Calories depend on age, sex, weight, height, and activity level:\n"
        "* **Sedentary adult female:** ~1,800–2,000 kcal/day\n"
        "* **Sedentary adult male:** ~2,200–2,400 kcal/day\n"
        "* **Active adult:** Add 300–500 kcal/day depending on exercise intensity\n"
        "> **Tip:** Use online calculators for precision and adjust according to weight goals."
    ),

    "What are macronutrients?": (
        "### The Building Blocks of Food\n"
        "Macronutrients are nutrients your body requires in large amounts:\n"
        "* **Proteins:** Repair tissues, build muscles.\n"
        "* **Carbohydrates:** Primary energy source.\n"
        "* **Fats:** Support hormones, brain function, and fat-soluble vitamin absorption.\n"
        "> **Balanced Intake:** Roughly 50% carbs, 25% protein, 25% fat is a common guideline for general health."
    ),

    "Is intermittent fasting healthy?": (
        "### Intermittent Fasting (IF)\n"
        "IF involves alternating periods of eating and fasting:\n"
        "* **Popular Methods:** 16:8 (16 hours fasting, 8 hours eating), 5:2 (normal eating 5 days, restricted 2 days).\n"
        "* **Benefits:** Weight loss, improved insulin sensitivity, cellular repair.\n"
        "* **Risks:** Not suitable for pregnant women, children, or those with certain medical conditions.\n"
        "> **Professional Tip:** Focus on nutrient-dense foods during eating windows."
    ),

    "How can I lose weight effectively?": (
        "### Evidence-Based Weight Loss Strategies\n"
        "* **Calorie Deficit:** Burn more calories than consumed.\n"
        "* **Exercise:** Combine strength training and cardiovascular exercise.\n"
        "* **Nutrition:** Eat whole foods, control portions, reduce sugar and refined carbs.\n"
        "* **Behavioral Changes:** Track meals, maintain sleep hygiene, manage stress.\n"
        "> **Warning:** Avoid extreme fad diets; sustainable lifestyle changes work best."
    ),

    "How to gain muscle?": (
        "### Muscle Gain Principles\n"
        "* **Progressive Strength Training:** Lift heavier or increase reps gradually.\n"
        "* **Protein Intake:** 1.6–2.2g protein per kg body weight daily.\n"
        "* **Calorie Surplus:** Consume slightly more calories than your maintenance.\n"
        "* **Recovery:** 7–9 hours sleep, rest days for muscles to repair.\n"
        "> **Tip:** Track workouts and protein consumption for optimal growth."
    ),

    "What are healthy fats?": (
        "### Sources of Healthy Fats\n"
        "Healthy fats support brain health, hormone production, and cell membranes:\n"
        "* **Monounsaturated Fats:** Olive oil, avocado, nuts.\n"
        "* **Polyunsaturated Fats:** Omega-3s (salmon, flaxseeds, walnuts).\n"
        "* **Moderation:** 20–35% of daily calories can come from fats.\n"
        "> **Avoid:** Trans fats and excessive saturated fats found in fried and processed foods."
    ),

    "Are supplements necessary?": (
        "### Dietary Supplements Explained\n"
        "* **Not Always Required:** Whole foods provide most nutrients.\n"
        "* **Common Supplements:** Vitamin D (sunlight deficient areas), Omega-3, B12 (vegans), protein powders (high activity levels).\n"
        "* **Risks:** Over-supplementation can be harmful; consult a dietitian before starting.\n"
        "> **Pro Tip:** Focus on nutrient-dense meals first, supplement only if needed."
    ),

    "How much water should I drink daily?": (
        "### Hydration Guidelines\n"
        "* **General Recommendation:** 2–3 liters/day for adults.\n"
        "* **Factors Affecting Needs:** Climate, activity level, body size, diet.\n"
        "* **Tips:** Drink water before meals, carry a reusable bottle, monitor urine color (light yellow indicates proper hydration)."
    ),

    "What are micronutrients?": (
        "### Vitamins & Minerals\n"
        "Micronutrients are essential in small amounts for metabolic functions:\n"
        "* **Vitamins:** A, C, D, E, K, B-complex\n"
        "* **Minerals:** Calcium, Magnesium, Iron, Zinc, Selenium\n"
        "* **Sources:** Vegetables, fruits, dairy, nuts, whole grains.\n"
        "> **Tip:** Diverse diet usually covers micronutrient needs without supplements."
    ),


    # --- EXERCISE & FITNESS ---
    "How often should I exercise?": (
        "### Exercise Frequency\n"
        "* **General Health:** 150 mins/week moderate-intensity OR 75 mins/week vigorous cardio.\n"
        "* **Strength Training:** 2–3 days/week for major muscle groups.\n"
        "* **Flexibility & Mobility:** Daily stretching or yoga improves performance and prevents injury."
    ),

    "What is cardio exercise?": (
        "### Cardiovascular Exercise Explained\n"
        "* **Definition:** Activities that raise your heart rate and improve cardiovascular health.\n"
        "* **Examples:** Running, cycling, swimming, brisk walking.\n"
        "* **Benefits:** Improves heart & lung efficiency, burns calories, reduces risk of chronic diseases."
    ),

    "What is strength training?": (
        "### Strength Training Basics\n"
        "* **Purpose:** Build muscle mass, increase metabolism, and improve bone density.\n"
        "* **Examples:** Weightlifting, resistance bands, bodyweight exercises.\n"
        "* **Frequency:** 2–4 times/week with progressive overload."
    ),

    "Can I do cardio and strength on the same day?": (
        "### Combining Cardio & Strength\n"
        "* **Yes, but order matters:**\n"
        "  - Strength first if goal is muscle gain\n"
        "  - Cardio first if goal is endurance\n"
        "* **Avoid excessive cardio after strength:** May limit muscle recovery."
    ),

    "How to prevent workout injuries?": (
        "### Injury Prevention Tips\n"
        "* **Warm-Up:** 5–10 mins of light cardio and dynamic stretching.\n"
        "* **Proper Form:** Focus on technique, not weight.\n"
        "* **Progressive Load:** Increase intensity gradually.\n"
        "* **Rest & Recovery:** Allow 24–48 hours between intense sessions.\n"
        "* **Hydration & Nutrition:** Supports tissue repair and joint health."
    ),

    "What is HIIT?": (
        "### High-Intensity Interval Training (HIIT)\n"
        "* **Definition:** Alternating short bursts of high-intensity exercise with recovery periods.\n"
        "* **Benefits:** Burns fat, improves cardiovascular health, saves time.\n"
        "* **Example:** 30s sprint + 90s walking, repeat 8–10 cycles.\n"
        "> **Tip:** Start with 2–3 sessions/week to avoid overtraining."
    ),

    "How many steps should I walk daily?": (
        "### Step Goals for Health\n"
        "* **General Target:** 10,000 steps/day (~5 miles).\n"
        "* **Beginners:** Start with 5,000 steps/day and increase gradually.\n"
        "* **Benefits:** Improves cardiovascular health, reduces sedentary lifestyle risks."
    ),

    "Is stretching necessary?": (
        "### Importance of Stretching\n"
        "* **Pre-Workout:** Dynamic stretches to increase mobility and prepare muscles.\n"
        "* **Post-Workout:** Static stretches to improve flexibility and reduce muscle soreness.\n"
        "* **Daily Routine:** Yoga or full-body stretching 10–15 mins can enhance posture and reduce injuries."
    ),

    "What are the benefits of yoga?": (
        "### Yoga Advantages\n"
        "* **Physical:** Flexibility, balance, core strength, improved circulation.\n"
        "* **Mental:** Reduces stress, improves focus, promotes relaxation.\n"
        "* **Lifestyle:** Encourages mindfulness, better breathing, and holistic wellness."
    ),

    "How long should a workout session be?": (
        "### Workout Duration Guidelines\n"
        "* **Cardio:** 20–60 minutes per session\n"
        "* **Strength Training:** 45–60 minutes per session\n"
        "* **Flexibility / Mobility:** 10–20 minutes daily\n"
        "> **Note:** Consistency and quality > duration; overtraining can cause injuries."
    ),

    # --- WEIGHT MANAGEMENT & METABOLISM ---
    "Why is metabolism important?": (
        "### Understanding Metabolism\n"
        "Metabolism is the process by which your body converts food into energy.\n"
        "* **Higher Metabolism:** Burns more calories at rest.\n"
        "* **Lower Metabolism:** Stores more fat if calories are excessive.\n"
        "* **Influencing Factors:** Age, genetics, muscle mass, hormones, activity level.\n"
        "> **Tip:** Strength training increases muscle mass and boosts metabolic rate."
    ),

    "How can I boost my metabolism naturally?": (
        "### Natural Ways to Increase Metabolism\n"
        "* **Build Muscle:** More muscle = higher calorie burn.\n"
        "* **Eat Enough Protein:** Increases thermic effect of food.\n"
        "* **Stay Active:** Daily movement matters.\n"
        "* **Drink Water:** Supports metabolic processes.\n"
        "* **Sleep Well:** Poor sleep slows metabolism."
    ),

    "What causes weight gain?": (
        "### Causes of Weight Gain\n"
        "* **Excess Calories:** Consuming more than you burn.\n"
        "* **Sedentary Lifestyle:** Low physical activity.\n"
        "* **Hormonal Imbalances:** Thyroid, insulin resistance.\n"
        "* **Stress & Sleep Loss:** Increases fat storage hormones.\n"
        "* **Poor Diet Choices:** Processed and sugary foods."
    ),

    "Why do I gain weight despite dieting?": (
        "### Hidden Reasons for Weight Gain\n"
        "* **Underestimating Calories:** Hidden sugars and fats.\n"
        "* **Slow Metabolism:** Due to crash dieting.\n"
        "* **Water Retention:** Salt and hormonal changes.\n"
        "* **Muscle Gain:** May increase weight but improve shape.\n"
        "> **Tip:** Focus on body composition, not just scale weight."
    ),

    "What is BMI?": (
        "### Body Mass Index (BMI)\n"
        "BMI measures weight relative to height:\n"
        "* **Underweight:** < 18.5\n"
        "* **Normal:** 18.5–24.9\n"
        "* **Overweight:** 25–29.9\n"
        "* **Obese:** ≥ 30\n"
        "> **Note:** BMI does not measure body fat directly."
    ),

    "Is belly fat dangerous?": (
        "### Health Risks of Belly Fat\n"
        "* Increases risk of heart disease\n"
        "* Raises diabetes risk\n"
        "* Linked to hormonal imbalance\n"
        "* Affects metabolic health\n"
        "> **Solution:** Combine diet, exercise, and stress management."
    ),

    "How to reduce belly fat?": (
        "### Reducing Abdominal Fat\n"
        "* **Balanced Diet:** Reduce refined carbs and sugar.\n"
        "* **Regular Exercise:** Cardio + strength training.\n"
        "* **Stress Control:** High cortisol increases belly fat.\n"
        "* **Adequate Sleep:** Regulates fat hormones."
    ),

    "Does skipping meals help weight loss?": (
        "### Meal Skipping & Weight Loss\n"
        "* May slow metabolism\n"
        "* Leads to overeating later\n"
        "* Causes energy crashes\n"
        "* Reduces nutrient intake\n"
        "> **Better Approach:** Eat small, balanced meals regularly."
    ),

    "What is emotional eating?": (
        "### Emotional Eating Explained\n"
        "Eating in response to emotions instead of hunger:\n"
        "* Triggered by stress, sadness, boredom\n"
        "* Often involves junk food\n"
        "* Leads to weight gain\n"
        "> **Tip:** Practice mindful eating and stress management."
    ),

    "How to control food cravings?": (
        "### Managing Cravings\n"
        "* Eat balanced meals\n"
        "* Drink enough water\n"
        "* Sleep well\n"
        "* Manage stress\n"
        "* Allow occasional healthy treats"
    ),


    # --- MENTAL HEALTH & WELLNESS ---
    "How does exercise affect mental health?": (
        "### Exercise & Mental Wellbeing\n"
        "* Releases endorphins (feel-good hormones)\n"
        "* Reduces anxiety and depression\n"
        "* Improves sleep quality\n"
        "* Boosts self-confidence\n"
        "* Enhances brain function"
    ),

    "What is stress and how does it affect health?": (
        "### Stress & Its Effects\n"
        "* Raises blood pressure\n"
        "* Weakens immunity\n"
        "* Increases fat storage\n"
        "* Disturbs sleep\n"
        "* Affects digestion\n"
        "> **Management:** Meditation, exercise, proper rest."
    ),

    "How to manage daily stress?": (
        "### Stress Management Techniques\n"
        "* Deep breathing exercises\n"
        "* Regular physical activity\n"
        "* Time management\n"
        "* Social support\n"
        "* Mindfulness practices"
    ),

    "What is mindfulness?": (
        "### Mindfulness Explained\n"
        "Mindfulness means being fully present in the moment:\n"
        "* Improves emotional control\n"
        "* Reduces anxiety\n"
        "* Enhances focus\n"
        "* Promotes mental clarity\n"
        "* Supports healthy lifestyle choices"
    ),

    "How much sleep do adults need?": (
        "### Sleep Requirements\n"
        "* Adults: 7–9 hours/night\n"
        "* Teenagers: 8–10 hours\n"
        "* Older adults: 7–8 hours\n"
        "> **Quality sleep supports immunity, memory, and weight control."
    ),

    "Why is sleep important for fitness?": (
        "### Sleep & Physical Performance\n"
        "* Supports muscle recovery\n"
        "* Regulates hormones\n"
        "* Improves energy levels\n"
        "* Enhances focus\n"
        "* Reduces injury risk"
    ),

    "What causes insomnia?": (
        "### Causes of Insomnia\n"
        "* Stress and anxiety\n"
        "* Excess screen time\n"
        "* Caffeine intake\n"
        "* Irregular sleep schedule\n"
        "* Poor sleep environment"
    ),

    "How can I improve my sleep quality?": (
        "### Better Sleep Habits\n"
        "* Fixed sleep schedule\n"
        "* Reduce screen time before bed\n"
        "* Avoid caffeine at night\n"
        "* Create dark, quiet bedroom\n"
        "* Practice relaxation techniques"
    ),

    "What is burnout?": (
        "### Burnout Syndrome\n"
        "* Physical and emotional exhaustion\n"
        "* Loss of motivation\n"
        "* Reduced productivity\n"
        "* Increased irritability\n"
        "> **Prevention:** Balance work, rest, and personal life."
    ),

    "How does social support affect health?": (
        "### Social Connections & Health\n"
        "* Reduces stress levels\n"
        "* Improves mental wellbeing\n"
        "* Encourages healthy habits\n"
        "* Enhances life satisfaction\n"
        "* Supports emotional resilience"
    ),

    # --- IMMUNITY & DISEASE PREVENTION ---

    "What is immunity?": (
        "### Immune System Overview\n"
        "Immunity is the body's defense system against infections and diseases.\n"
        "* Identifies harmful bacteria and viruses\n"
        "* Produces antibodies\n"
        "* Protects against repeated infections\n"
        "* Maintains overall health\n"
        "> Strong immunity reduces illness frequency."
    ),

    "How can I strengthen my immune system?": (
        "### Boosting Immunity Naturally\n"
        "* Balanced diet with fruits and vegetables\n"
        "* Regular physical activity\n"
        "* Quality sleep (7–9 hours)\n"
        "* Proper hydration\n"
        "* Stress management\n"
        "* Avoid smoking and alcohol"
    ),

    "What foods improve immunity?": (
        "### Immune-Boosting Foods\n"
        "* Citrus fruits (Vitamin C)\n"
        "* Yogurt (Probiotics)\n"
        "* Garlic and ginger\n"
        "* Green leafy vegetables\n"
        "* Nuts and seeds\n"
        "* Turmeric and honey"
    ),

    "What weakens the immune system?": (
        "### Factors That Reduce Immunity\n"
        "* Chronic stress\n"
        "* Lack of sleep\n"
        "* Poor nutrition\n"
        "* Excess sugar intake\n"
        "* Smoking and alcohol\n"
        "* Sedentary lifestyle"
    ),

    "What are lifestyle diseases?": (
        "### Lifestyle-Related Diseases\n"
        "Diseases caused by unhealthy habits:\n"
        "* Diabetes\n"
        "* Heart disease\n"
        "* Obesity\n"
        "* Hypertension\n"
        "* Stroke\n"
        "> Prevention is possible through healthy living."
    ),

    "How can lifestyle diseases be prevented?": (
        "### Prevention Strategies\n"
        "* Regular exercise\n"
        "* Healthy diet\n"
        "* Weight management\n"
        "* Routine medical checkups\n"
        "* Avoid tobacco\n"
        "* Stress control"
    ),

    "What is diabetes?": (
        "### Diabetes Explained\n"
        "A condition where blood sugar levels remain high due to insulin problems.\n"
        "* Type 1: Insulin deficiency\n"
        "* Type 2: Insulin resistance\n"
        "* Gestational: During pregnancy\n"
        "> Controlled through diet, exercise, and medication."
    ),

    "How does exercise help control diabetes?": (
        "### Exercise & Blood Sugar Control\n"
        "* Improves insulin sensitivity\n"
        "* Reduces blood glucose levels\n"
        "* Supports weight control\n"
        "* Improves heart health\n"
        "* Enhances energy levels"
    ),

    "What is hypertension?": (
        "### High Blood Pressure\n"
        "Hypertension is when blood pressure remains above normal levels.\n"
        "* Normal: 120/80 mmHg\n"
        "* High: Above 140/90 mmHg\n"
        "* Increases heart and stroke risk\n"
        "> Requires lifestyle changes and medication."
    ),

    "How can high blood pressure be controlled naturally?": (
        "### Natural BP Control\n"
        "* Reduce salt intake\n"
        "* Exercise regularly\n"
        "* Maintain healthy weight\n"
        "* Manage stress\n"
        "* Eat potassium-rich foods"
    ),


    # --- HEART, BONES & MUSCLES ---

    "What is cardiovascular health?": (
        "### Heart & Blood Vessel Health\n"
        "Cardiovascular health refers to the proper functioning of heart and blood vessels.\n"
        "* Ensures oxygen supply\n"
        "* Maintains energy levels\n"
        "* Prevents heart disease\n"
        "* Supports longevity"
    ),

    "How can I improve heart health?": (
        "### Heart-Healthy Habits\n"
        "* Aerobic exercise (30 min daily)\n"
        "* Balanced diet\n"
        "* Avoid smoking\n"
        "* Control cholesterol\n"
        "* Manage stress"
    ),

    "What causes heart disease?": (
        "### Causes of Heart Disease\n"
        "* High cholesterol\n"
        "* Smoking\n"
        "* Obesity\n"
        "* Diabetes\n"
        "* High blood pressure\n"
        "* Lack of exercise"
    ),

    "What is osteoporosis?": (
        "### Bone Density Disorder\n"
        "Osteoporosis causes weak and fragile bones.\n"
        "* Common in older adults\n"
        "* Increases fracture risk\n"
        "* Often due to calcium deficiency\n"
        "> Preventable with nutrition and exercise."
    ),

    "How can I keep my bones strong?": (
        "### Bone Strength Tips\n"
        "* Adequate calcium intake\n"
        "* Vitamin D exposure\n"
        "* Weight-bearing exercises\n"
        "* Avoid excessive caffeine\n"
        "* Stop smoking"
    ),

    "Why is muscle strength important?": (
        "### Benefits of Strong Muscles\n"
        "* Improves posture\n"
        "* Enhances mobility\n"
        "* Prevents injuries\n"
        "* Supports metabolism\n"
        "* Promotes independence"
    ),

    "What is muscle recovery?": (
        "### Muscle Repair Process\n"
        "Muscle recovery is the repair of micro-tears after exercise.\n"
        "* Prevents soreness\n"
        "* Improves strength\n"
        "* Reduces injury risk\n"
        "* Requires rest and nutrition"
    ),

    "How long should muscles rest?": (
        "### Rest Duration\n"
        "* 24–48 hours between intense sessions\n"
        "* Light activity allowed\n"
        "* Sleep supports recovery\n"
        "> Overtraining delays progress."
    ),

    "What is overtraining syndrome?": (
        "### Excessive Training Effects\n"
        "* Chronic fatigue\n"
        "* Poor performance\n"
        "* Weak immunity\n"
        "* Sleep problems\n"
        "* Mood changes\n"
        "> Balance training with rest."
    ),

    "How does posture affect health?": (
        "### Posture & Wellbeing\n"
        "* Reduces back pain\n"
        "* Improves breathing\n"
        "* Enhances confidence\n"
        "* Prevents muscle imbalance\n"
        "* Supports spinal health"
    ),

    # --- HORMONES, AGING & GENDER HEALTH ---

    "What are hormones?": (
        "### Hormones Explained\n"
        "Hormones are chemical messengers produced by endocrine glands.\n"
        "* Regulate growth and development\n"
        "* Control metabolism\n"
        "* Influence mood and emotions\n"
        "* Manage reproductive health\n"
        "* Affect sleep and appetite"
    ),

    "How do hormones affect weight?": (
        "### Hormones & Body Weight\n"
        "* Insulin controls blood sugar\n"
        "* Thyroid regulates metabolism\n"
        "* Cortisol increases fat storage\n"
        "* Estrogen and testosterone affect fat distribution\n"
        "> Hormonal imbalance may cause unexplained weight gain."
    ),

    "What is hormonal imbalance?": (
        "### Hormonal Disorders\n"
        "A condition where hormone levels are too high or too low.\n"
        "* Causes fatigue\n"
        "* Weight changes\n"
        "* Mood swings\n"
        "* Irregular periods\n"
        "* Sleep problems"
    ),

    "How can hormonal balance be maintained?": (
        "### Balancing Hormones Naturally\n"
        "* Balanced nutrition\n"
        "* Regular exercise\n"
        "* Adequate sleep\n"
        "* Stress reduction\n"
        "* Medical consultation if needed"
    ),

    "How does aging affect fitness?": (
        "### Aging & Physical Performance\n"
        "* Reduced muscle mass\n"
        "* Slower metabolism\n"
        "* Decreased bone density\n"
        "* Reduced flexibility\n"
        "* Lower recovery speed\n"
        "> Exercise slows aging effects."
    ),

    "Can older adults exercise safely?": (
        "### Fitness for Seniors\n"
        "* Yes, with medical approval\n"
        "* Focus on balance and strength\n"
        "* Low-impact cardio\n"
        "* Stretching exercises\n"
        "* Avoid heavy strain"
    ),

    "What are common health issues in women?": (
        "### Women’s Health Concerns\n"
        "* Iron deficiency\n"
        "* Hormonal disorders\n"
        "* Osteoporosis\n"
        "* Thyroid problems\n"
        "* PCOS"
    ),

    "What is PCOS?": (
        "### Polycystic Ovary Syndrome\n"
        "PCOS is a hormonal disorder affecting women of reproductive age.\n"
        "* Irregular periods\n"
        "* Weight gain\n"
        "* Acne and hair growth\n"
        "* Fertility issues\n"
        "> Managed through lifestyle and medication."
    ),

    "How can women improve reproductive health?": (
        "### Reproductive Health Tips\n"
        "* Balanced diet\n"
        "* Regular checkups\n"
        "* Exercise\n"
        "* Avoid smoking\n"
        "* Manage stress"
    ),

    "What are common health issues in men?": (
        "### Men’s Health Concerns\n"
        "* Low testosterone\n"
        "* Heart disease\n"
        "* Obesity\n"
        "* Prostate problems\n"
        "* Stress-related disorders"
    ),

    "What is testosterone?": (
        "### Male Hormone Overview\n"
        "Testosterone is the primary male sex hormone.\n"
        "* Builds muscle mass\n"
        "* Maintains bone density\n"
        "* Supports libido\n"
        "* Affects mood and energy\n"
        "* Declines with age"
    ),

    "How can men boost testosterone naturally?": (
        "### Natural Testosterone Boost\n"
        "* Strength training\n"
        "* Adequate sleep\n"
        "* Healthy fats\n"
        "* Stress control\n"
        "* Avoid alcohol excess"
    ),

    "What is menopause?": (
        "### Menopause Explained\n"
        "Menopause marks the end of menstrual cycles.\n"
        "* Occurs around age 45–55\n"
        "* Hot flashes\n"
        "* Mood changes\n"
        "* Sleep issues\n"
        "* Bone loss risk"
    ),

    "How can women manage menopause symptoms?": (
        "### Managing Menopause\n"
        "* Regular exercise\n"
        "* Balanced diet\n"
        "* Hydration\n"
        "* Medical advice\n"
        "* Stress reduction"
    ),

    "What is andropause?": (
        "### Male Menopause\n"
        "Andropause refers to age-related testosterone decline in men.\n"
        "* Fatigue\n"
        "* Reduced libido\n"
        "* Mood changes\n"
        "* Muscle loss\n"
        "* Weight gain"
    ),

    "How does fitness affect fertility?": (
        "### Exercise & Fertility\n"
        "* Improves hormonal balance\n"
        "* Enhances circulation\n"
        "* Reduces stress\n"
        "* Supports healthy weight\n"
        "* Boosts reproductive health"
    ),

    "Why is flexibility important with age?": (
        "### Flexibility Benefits\n"
        "* Prevents injuries\n"
        "* Improves mobility\n"
        "* Reduces stiffness\n"
        "* Enhances balance\n"
        "* Supports independence"
    ),

    "What exercises improve balance?": (
        "### Balance Training\n"
        "* Yoga\n"
        "* Tai Chi\n"
        "* Single-leg stands\n"
        "* Heel-to-toe walk\n"
        "* Stability ball exercises"
    ),

    "How can seniors prevent falls?": (
        "### Fall Prevention Tips\n"
        "* Improve home lighting\n"
        "* Remove loose rugs\n"
        "* Wear proper footwear\n"
        "* Do balance training\n"
        "* Regular vision checks"
    ),

    "What is healthy aging?": (
        "### Healthy Aging Concept\n"
        "Healthy aging focuses on maintaining physical, mental, and social wellbeing.\n"
        "* Active lifestyle\n"
        "* Good nutrition\n"
        "* Social engagement\n"
        "* Regular checkups\n"
        "* Positive mindset"
    ),

    # --- NUTRITION, SUPPLEMENTS & LIFESTYLE ---

    "Are dietary supplements necessary?": (
        "### Supplement Use\n"
        "Supplements are products that provide extra nutrients.\n"
        "* Useful when diet is insufficient\n"
        "* Not a substitute for real food\n"
        "* Should be used under guidance\n"
        "* Excess intake may cause harm\n"
        "> Food remains the best nutrient source."
    ),

    "What are common nutrition myths?": (
        "### Nutrition Misconceptions\n"
        "* Carbs always cause weight gain (False)\n"
        "* Fat is unhealthy (False)\n"
        "* Skipping meals is healthy (False)\n"
        "* Detox diets cleanse body (False)\n"
        "* Supplements replace food (False)"
    ),

    "Is protein powder safe?": (
        "### Protein Supplement Safety\n"
        "* Safe when used in moderation\n"
        "* Helps muscle recovery\n"
        "* Should match daily protein needs\n"
        "* Not required for everyone\n"
        "* Excess strains kidneys"
    ),

    "What is a balanced diet?": (
        "### Balanced Nutrition\n"
        "A balanced diet includes:\n"
        "* Carbohydrates for energy\n"
        "* Proteins for repair\n"
        "* Healthy fats\n"
        "* Vitamins and minerals\n"
        "* Adequate fiber\n"
        "* Sufficient water"
    ),

    "How does junk food affect health?": (
        "### Effects of Junk Food\n"
        "* High in sugar and fat\n"
        "* Causes weight gain\n"
        "* Raises cholesterol\n"
        "* Reduces immunity\n"
        "* Increases disease risk"
    ),

    "What is mindful eating?": (
        "### Conscious Eating\n"
        "Mindful eating means eating with full awareness.\n"
        "* Improves digestion\n"
        "* Prevents overeating\n"
        "* Enhances food enjoyment\n"
        "* Supports weight control\n"
        "* Reduces emotional eating"
    ),

    "How does screen time affect health?": (
        "### Digital Health Impact\n"
        "* Eye strain\n"
        "* Poor posture\n"
        "* Sleep disturbance\n"
        "* Reduced activity\n"
        "* Mental fatigue"
    ),

    "How can I reduce screen addiction?": (
        "### Limiting Screen Use\n"
        "* Set time limits\n"
        "* Digital detox days\n"
        "* Outdoor activities\n"
        "* Reading books\n"
        "* Social interactions"
    ),

    "Why is hydration important?": (
        "### Water & Body Function\n"
        "* Regulates temperature\n"
        "* Supports digestion\n"
        "* Improves circulation\n"
        "* Enhances energy\n"
        "* Removes toxins"
    ),

    "Can green tea help weight loss?": (
        "### Green Tea Benefits\n"
        "* Boosts metabolism\n"
        "* Rich in antioxidants\n"
        "* Improves fat oxidation\n"
        "* Supports heart health\n"
        "* Aids digestion"
    ),

    "How does smoking affect fitness?": (
        "### Smoking & Health\n"
        "* Reduces lung capacity\n"
        "* Weakens immunity\n"
        "* Increases heart disease risk\n"
        "* Delays recovery\n"
        "* Causes premature aging"
    ),

    "What are benefits of quitting smoking?": (
        "### Smoking Cessation Benefits\n"
        "* Improved breathing\n"
        "* Better heart health\n"
        "* Increased energy\n"
        "* Reduced cancer risk\n"
        "* Longer lifespan"
    ),

    "How does alcohol affect health?": (
        "### Alcohol Impact\n"
        "* Liver damage\n"
        "* Weight gain\n"
        "* Sleep disturbance\n"
        "* Poor judgment\n"
        "* Increased disease risk"
    ),

    "What is preventive healthcare?": (
        "### Disease Prevention\n"
        "Preventive healthcare focuses on avoiding illness.\n"
        "* Regular checkups\n"
        "* Vaccinations\n"
        "* Screenings\n"
        "* Healthy habits\n"
        "* Early detection"
    ),

    "Why are regular medical checkups important?": (
        "### Health Monitoring\n"
        "* Early disease detection\n"
        "* Risk assessment\n"
        "* Personalized advice\n"
        "* Cost-effective care\n"
        "* Peace of mind"
    ),

    "How does laughter improve health?": (
        "### Laughter Therapy\n"
        "* Reduces stress\n"
        "* Boosts immunity\n"
        "* Improves mood\n"
        "* Lowers blood pressure\n"
        "* Enhances social bonds"
    ),

    "What is work-life balance?": (
        "### Balanced Living\n"
        "Work-life balance means managing work and personal life effectively.\n"
        "* Reduces burnout\n"
        "* Improves productivity\n"
        "* Enhances relationships\n"
        "* Supports mental health\n"
        "* Promotes happiness"
    ),

    "How can I stay motivated for fitness?": (
        "### Motivation Strategies\n"
        "* Set realistic goals\n"
        "* Track progress\n"
        "* Find workout partner\n"
        "* Reward consistency\n"
        "* Stay positive"
    ),

    "Why is consistency important in fitness?": (
        "### Importance of Consistency\n"
        "* Builds lasting habits\n"
        "* Improves results\n"
        "* Prevents regression\n"
        "* Enhances discipline\n"
        "* Ensures long-term success"
    ),

    "What is holistic health?": (
        "### Whole-Person Health\n"
        "Holistic health focuses on physical, mental, emotional, and social wellbeing.\n"
        "* Balanced lifestyle\n"
        "* Mind-body connection\n"
        "* Preventive approach\n"
        "* Sustainable wellness\n"
        "* Overall life satisfaction"
    ),

}
