# Complete Blood Count (CBC) Parameters

## White Blood Cell Count (WBC)

WBC measures the number of white blood cells in the blood. White blood cells are part of the immune system and help the body fight infections. Changes in WBC can occur in infections, inflammatory conditions, bone marrow disorders, and other medical conditions.

## Red Blood Cell Count (RBC)

RBC measures the number of red blood cells. These cells transport oxygen throughout the body using hemoglobin. RBC levels can vary with hydration, oxygen availability, and several medical conditions.

## Hemoglobin (HGB)

Hemoglobin is the oxygen-carrying protein present in red blood cells. Hemoglobin measurement is commonly used when evaluating conditions such as anemia and other blood-related abnormalities.

## Platelet Count (PLT)

Platelets are blood components that help form clots and control bleeding. Platelet count abnormalities may be associated with bleeding or clotting-related conditions.

## Neutrophils (NEUT)

Neutrophils are white blood cells that play an important role in the body's response to infections, particularly bacterial infections. Their levels may change in infections, inflammation, medication effects, and bone marrow conditions.

## Lymphocytes (LYMPH)

Lymphocytes are white blood cells involved in immune responses. They include B cells, T cells, and natural killer cells. Changes in lymphocyte levels may occur during infections and immune-related conditions.

## Monocytes (MONO)

Monocytes are white blood cells involved in immune defense and the removal of damaged cells and microorganisms. Their levels may change during infections, inflammation, and other conditions.

## Eosinophils (EOS)

Eosinophils are white blood cells involved in allergic responses, defense against parasites, and certain inflammatory conditions. Increased levels can be associated with allergies, parasitic infections, and other conditions.

## Basophils (BASO)

Basophils are a type of white blood cell involved in inflammatory and allergic responses. They release substances such as histamine and may be elevated in certain inflammatory or blood-related conditions.

## Important Interpretation Note

CBC parameters must be interpreted using the units and reference intervals provided by the reporting laboratory. Individual values should not be interpreted in isolation. Clinical history, age, sex, medications, and other laboratory findings may affect interpretation.

Source:
MedlinePlus - Complete Blood Count (CBC)
https://medlineplus.gov/lab-tests/complete-blood-count-cbc/

# HemoPredict CBC Parameters Knowledge Base (`cbc_parameters.md`)

**Purpose:** Educational reference knowledge base on nine Complete Blood Count (CBC) parameters, written for chunking and embedding (RAG / ChromaDB).
**Compiled:** 2026-11-03 from sources retrieved during this research session (see Section 8 for URLs, dates, and a list of what could NOT be verified).
**Not for diagnosis.** This document explains what CBC parameters measure and what changes in them _may be associated with_. It does not diagnose disease, recommend medication, or give treatment or dosing advice. Any CBC result must be interpreted by a qualified clinician using the patient's age, sex, pregnancy status, symptoms, medical history, and the reference intervals printed on the reporting laboratory's own report.

## 0. Conventions used in this document

- **Source tags** such as `(S4)` point to the bibliography in Section 8. A tag marked `secondary` means the claim comes from a lower-authority source (clinical wiki, patient-education site, or encyclopedia) and should be treated with lower confidence.
- **Unmarked explanatory sentences** (for example, "red cells carry oxygen") are standard physiology background. They were not individually re-verified in this session.
- **`[UNVERIFIED]`** marks a statement or number that could not be confirmed in an authoritative source during research.
- **Each subsection repeats the parameter name** (for example "WBC — ...") so that a chunk retrieved alone remains understandable.
- **Unit shorthand:** `×10⁹/L` = `×10³/µL` = `K/µL` = `thousand cells per microliter`. `cells/µL` = `cells/mcL` = `cells/mm³`. RBC `×10¹²/L` = `million cells/µL`. Hemoglobin `g/dL × 10 = g/L`.

---

## 1. Introduction to the Complete Blood Count (CBC)

**Complete Blood Count (CBC)**, also called **full blood count (FBC)** or **blood cell count**, is a group of blood tests that measure the number and size of the different cells in the blood (S1). MedlinePlus lists the following as measured by a CBC: red blood cells (RBC), white blood cells (WBC), platelets, hemoglobin, hematocrit, and mean corpuscular volume (MCV) (S1).

A CBC measures the **total** number of white cells. A **CBC with differential** (also called **blood differential**, **WBC differential**, or **leukocyte differential count**) additionally reports the amount and/or percentage of each of the five white cell types: neutrophils, lymphocytes, monocytes, eosinophils, and basophils (S2).

**Why a CBC is ordered.** It is often part of a routine checkup and is also used to monitor conditions or treatments that may affect blood cell counts, such as infections, anemia, immune system disorders, and blood cancers (S1). It may also be used to help find the cause of symptoms such as fatigue, weakness, or unexplained bruising (S2).

**How it is collected and measured.** Blood is drawn from a vein, usually into an EDTA anticoagulant (lavender-top) tube (S21). Usually no special preparation is needed (S1). Automated analyzers directly measure hemoglobin, RBC count, WBC count, platelet count, and MCV; hematocrit, MCH, and MCHC are calculated values (S4). One hospital laboratory describes its method as hydrodynamic focusing and flow cytometry on a Sysmex analyzer (S21). A manual microscope review of a blood smear may be added when the automated results are flagged or abnormal (S21, S4).

**What the CBC is and is not.** MedlinePlus describes the CBC as only one tool; providers also consider medical history, symptoms, and other tests (S1). MedlinePlus states that a white blood count "can't confirm a diagnosis" on its own (S3). An abnormal CBC value does not always mean a condition needing treatment, because diet, activity level, medicines, menstrual periods, hydration, and other factors can change results (S1). In one large clinical laboratory experience, roughly 10% to 20% of CBC results were reported as abnormal (S13).

**The nine HemoPredict parameters.** WBC, RBC, HGB, PLT, NEUT, LYMPH, MONO, EOS, BASO. Related CBC values that are _not_ among the nine but appear in context are hematocrit (HCT), MCV, MCH, MCHC, RDW, and reticulocyte count. They are defined in the glossary (Section 7).

---

## 2. Understanding CBC Measurements and Reference Intervals

### 2.1 Absolute counts versus percentages

- **Absolute count:** the number of cells in a fixed volume of blood (for example, neutrophils ×10⁹/L, or cells/µL).
- **Percentage (relative count):** the fraction of all white cells that a cell type represents. Percentages apply only to the white cell differential.
- **Conversion:** absolute count = total WBC × (percentage ÷ 100). Example: WBC 30,000/µL with 30% lymphocytes gives an absolute lymphocyte count of 9,000/µL.
- **Why absolute counts matter:** percentages change whenever another white cell type rises or falls. A rising neutrophil count can make the lymphocyte _percentage_ look low even when the absolute lymphocyte count is unchanged. Clinicians therefore generally rely on absolute counts when judging a cell type.
- **Absolute neutrophil count (ANC)** is calculated as WBC × (% segmented neutrophils + % band neutrophils) ÷ 100 (S26 secondary).

### 2.2 Common units and equivalent notations

| Parameter                    | Common US notation                       | SI / alternative notation                         | Equivalence                            |
| ---------------------------- | ---------------------------------------- | ------------------------------------------------- | -------------------------------------- |
| WBC                          | cells/µL, K/µL, ×10³/µL, cells/mm³       | ×10⁹/L                                            | 7,500 cells/µL = 7.5 K/µL = 7.5 ×10⁹/L |
| RBC                          | million cells/µL, ×10⁶/µL                | ×10¹²/L ("trillion cells/L" on Mayo Clinic pages) | 5.0 million/µL = 5.0 ×10¹²/L           |
| HGB                          | g/dL                                     | g/L                                               | 14.0 g/dL = 140 g/L                    |
| PLT                          | cells/µL, K/µL, ×10³/µL                  | ×10⁹/L ("billion/L" on Mayo Clinic pages)         | 250,000/µL = 250 K/µL = 250 ×10⁹/L     |
| NEUT, LYMPH, MONO, EOS, BASO | cells/µL (absolute); % of WBC (relative) | ×10⁹/L                                            | 1,500 cells/µL = 1.5 ×10⁹/L            |

### 2.3 What a reference interval is, and what it is not

- A **reference interval** (often called "normal range") is generally the range of values seen in 95% of healthy people in a particular group (S11). By construction, about 5% of healthy people fall outside a 95% interval.
- A **diagnostic threshold** is a cut-off used by a guideline or textbook to _define a clinical condition_. It is not the same thing as the laboratory's reference interval. Example: Merck Manual defines anemia in adults as hemoglobin below 13 g/dL in males and below 12 g/dL in females (S4), whereas one Mayo Clinic reference interval for hemoglobin has lower limits of 13.2 g/dL (male) and 11.6 g/dL (female) (S12).
- A **critical value** is a laboratory-defined result so far from the interval that the laboratory contacts the clinician urgently. Critical values are laboratory-specific and are not listed in this document.
- **Do not apply one universal range to every patient.** Normal ranges differ with age, sex, pregnancy, altitude, and other factors (S11).

### 2.4 Why reference ranges differ between laboratories

1. **Population:** each laboratory's interval reflects its local reference population (S11).
2. **Method and analyzer:** different measurement methods and instruments give slightly different results (S21 describes one method; the Mayo-authored ASH abstract documents inter-hospital variation) (S14).
3. **Documented variation:** in a 2023 ASH abstract, Mayo Clinic investigators collected CBC reference limits from 143 US hospitals in 43 states. About 93.5% of hospitals set the male hemoglobin upper limit above 16.5 g/dL, while only about 3.6% set the female upper limit above 16.0 g/dL; the authors noted that common upper limits for hemoglobin and platelets exceed WHO criteria used to define polycythemia vera and essential thrombocythemia, so clinical context matters even when a result is flagged "normal" (S14).
4. **Subject factors:** age, sex, pregnancy, altitude, and ancestry (S11, S19, S18).

### 2.5 Example comparison: published adult reference values from different sources

These are **examples of variation, not recommendations**. Use the interval printed on the actual lab report.

| Parameter   | Mayo Clinic Health Information Library, via Mayo Clinic Care Network pages (S12) | NHLBI "What Do Blood Tests Show?" (archived 2009 page) (S11) | Example hospital laboratory (Boone Health test catalog) (S21) |
| ----------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------- |
| WBC         | 3.4 to 9.6 ×10⁹/L (both sexes)                                                   | 4,500 to 10,000 cells/µL                                     | 3.8 to 9.9 K/µL (both sexes)                                  |
| RBC, male   | 4.35 to 5.65 ×10¹²/L                                                             | 5 to 6 million/µL (varies with altitude)                     | 4.6 to 5.8 M/µL                                               |
| RBC, female | 3.92 to 5.13 ×10¹²/L                                                             | 4 to 5 million/µL (varies with altitude)                     | 3.9 to 5.2 M/µL                                               |
| HGB, male   | 13.2 to 16.6 g/dL                                                                | 14 to 17 g/dL (varies with altitude)                         | 13.0 to 17.5 g/dL                                             |
| HGB, female | 11.6 to 15.0 g/dL                                                                | 12 to 15 g/dL (varies with altitude)                         | 11.9 to 15.5 g/dL                                             |
| PLT         | male 135 to 317 ×10⁹/L; female 157 to 371 ×10⁹/L                                 | 140,000 to 450,000/µL                                        | not captured                                                  |

Another NHLBI page of similar vintage gives the platelet range as 150,000 to 450,000/µL (S10). The differences across rows above illustrate why a single universal range cannot be used.

### 2.6 Differential percentages and absolute differential ranges

Reliable adult reference intervals for the five differential cell types were **not retrieved from an authoritative source** in this session, apart from the items quoted in each parameter section (for example, Merck's lymphocyte count of 1,000 to 4,800/µL and the 1,500/µL lower limit for neutrophils). Do not hard-code differential percentages from this document; use the laboratory report's own intervals. `[UNVERIFIED for general differential percentage ranges]`

### 2.7 Other factors that move reference ranges

- **Sex:** RBC, hemoglobin, hematocrit, and platelet intervals differ between males and females in the sources above; WBC intervals were not sex-specific in them.
- **Age:** infant and child values differ from adult values; the Merck Manual notes that hemoglobin and hematocrit in infants and children vary with age and require age-specific tables (S4).
- **Pregnancy:** hemoglobin, hematocrit, platelets, and WBC have pregnancy-specific intervals (S19, S20).
- **Altitude:** NHLBI notes that RBC count, hemoglobin, and hematocrit vary with altitude (S11).

---

## 3. Individual Parameter Sections

### 3.1 WBC — White Blood Cell Count (Total Leukocyte Count, TLC, Leukocyte Count)

**Synonyms and alternative names:** WBC, WBC count, white cell count, white blood cell count, total leukocyte count (TLC), leukocyte count, leukocytes (S3).
**Low-value terms:** leukopenia (also leucopenia). **High-value terms:** leukocytosis.

#### WBC — A. Definition and physiological role

The WBC count is the total number of white blood cells (leukocytes) in a volume of blood. White blood cells are part of the immune system. They are made in the bone marrow and are found in the blood and in lymph tissue. When a person is injured or sick, white blood cells travel through the bloodstream and tissues to where they are needed and help the body fight infections and other diseases (S3).

There are five major types: neutrophils, lymphocytes, monocytes, eosinophils, and basophils (S3). The total WBC count is the sum of all five; a separate differential reports each type (S2, S3). In an adult, roughly 60% to 70% of circulating WBCs are mature neutrophils (S18).

#### WBC — B. Units and measurement

- **Common units:** cells/µL (cells/mm³), K/µL, ×10³/µL, or ×10⁹/L. Example: 7,500 cells/µL = 7.5 ×10⁹/L.
- **Measurement:** automated hematology analyzers count WBCs directly on an EDTA blood sample (S4, S21).
- **Absolute versus percentage:** the total WBC is an absolute count. Its subtypes are reported both as absolute counts and as percentages of the WBC (see Section 2.1).
- **Synonym caution:** some labs and clinicians say "TLC" (total leukocyte count) for the same quantity.

#### WBC — C. Reference ranges

- **Adult interval examples:** 3.4 to 9.6 ×10⁹/L (Mayo Clinic Health Information Library values via care-network pages) (S12); 4,500 to 10,000 cells/µL (archived NHLBI page) (S11); 3.8 to 9.9 K/µL (example hospital laboratory) (S21); approximately 4,000 to 11,000 cells/µL (StatPearls) (S18). These sources did not give separate male and female WBC intervals.
- **Pregnancy:** WBC rises in normal pregnancy, mainly because neutrophils increase (S19). GLOWM lists baseline 4 to 10 ×10⁹/L versus 6 to 16 ×10⁹/L across trimesters, and notes that mean WBC rises to about 10 to 16 ×10⁹/L during labor, with an upper level of about 29 ×10⁹/L (S19). The Abbassi-Ghanavati tables list 5.7 to 13.6 (first trimester), 5.6 to 14.8 (second), and 5.6 to 16.9 (third) ×10⁹/L (S20). Pregnancy-related WBC changes can persist for 6 to 8 weeks after delivery (S19).
- **Children and infants:** WBC and its differential vary with age and need age-specific intervals. A secondary clinical wiki states that newborn WBC can be as high as about 30,000/µL, with the differential shifting toward lymphocytes in early childhood (S22 secondary). `[Numeric pediatric WBC intervals not retrieved from an authoritative source]`
- **Ancestry:** relative to white people, Black people have on average lower total WBC and lower neutrophil counts (S18).
- **Diagnostic thresholds (not reference intervals):** leukocytosis is conventionally defined as WBC above 11,000/mm³ (11 ×10⁹/L) (S17). A **leukemoid reaction** is a WBC above 50,000/µL from a cause outside the bone marrow (S17). Secondary sources describe WBC above 100,000/µL as "hyperleukocytosis" and a hematologic emergency (S22 secondary).
- **Why intervals differ:** see Section 2.4.

#### WBC — D. Low levels (leukopenia)

- **Terminology:** a low WBC count is called **leukopenia** (S2, S3). Low counts of specific cell types have their own terms, such as neutropenia and lymphopenia (S3).
- **Possible causes (S1, S2, S3):** bone marrow damage from infection, disease, or treatments such as chemotherapy; cancers affecting the bone marrow; autoimmune disorders such as lupus; HIV; certain medicines (including some antibiotics); diseases of the liver or spleen (S3). Viral infections can also lower counts (S6).
- **Physiological contributors:** some people have a chronically low neutrophil count without increased infections (see NEUT section), which lowers total WBC.
- **Symptoms:** a low WBC count has no specific symptoms of its own. Problems come from reduced infection defense, especially when neutrophils are very low (S8).
- **Other CBC changes that may accompany it:** low neutrophils and/or lymphocytes. If anemia or thrombocytopenia occurs at the same time (more than one cell line affected), the Merck Manual lists this as a situation where bone marrow examination may be considered (S4).
- **Tests that may help investigate:** differential count, blood smear, bone marrow test (S3); lymphocyte subsets and immunoglobulins if lymphopenia is present (S6); HIV testing is among tests MedlinePlus links to low WBC (S3).

#### WBC — E. High levels (leukocytosis)

- **Terminology:** **leukocytosis** (S3).
- **Possible causes (S1, S3, S17):**
  - Infection (bacterial or viral)
  - Inflammatory or autoimmune disease such as rheumatoid arthritis
  - Allergy or allergic reaction
  - Tissue damage from burns or surgery, tissue necrosis, infarction
  - Leukemia or Hodgkin disease
  - Smoking, stress, pregnancy, or a reaction to a medicine
  - Medicines commonly associated with leukocytosis: corticosteroids, lithium, and beta agonists (S17)
  - Splenectomy (transient, weeks to months) and hemolytic anemia (S17)
- **Stress leukocytosis:** physical stress (seizures, anesthesia, overexertion) and emotional stress can raise the count; this type reverses within hours after the trigger is removed (S17).
- **Symptoms:** leukocytosis itself usually causes no symptoms. Symptoms reflect the underlying cause, such as fever, chills, body aches, or a wound that is red or will not heal in infection (S3).
- **Other CBC changes that may accompany it:** neutrophilia (often with immature "band" forms, called a left shift) in bacterial infection or inflammation (S17); lymphocytosis in some viral infections; eosinophilia or basophilia in allergy or some marrow disorders (S17).
- **Tests that may help:** WBC differential, blood smear, bone marrow test (S3). Smear review looks for immature cells, atypical lymphocytes, and left shift.

#### WBC — F. Clinical interpretation

Clinicians first ask _which cell type_ is responsible for a high or low WBC by reviewing the differential, because the total count alone cannot say (S3, S17). They then consider symptoms, medications, hydration, pregnancy, recent stress or exercise, and trend over time. A mild, isolated, transient elevation with a clear cause (for example recent steroid use) is treated very differently from a persistent or marked elevation with other abnormalities. Persistent unexplained abnormalities, immature cells on the smear, or additional low red cell or platelet counts prompt hematology evaluation (S4, S17).

**Common patterns:** high WBC with high neutrophils (infection/inflammation/stress/steroids); high WBC with high lymphocytes (viral infection, some lymphoproliferative conditions); low WBC with low neutrophils (marrow suppression, drugs, infection, autoimmune); see Section 4.

**Limitation:** the WBC alone "can't confirm a diagnosis" (S3).

#### WBC — G. Relationship with other CBC parameters

- **NEUT:** neutrophils are usually the largest share of the WBC, so a high or low WBC is often driven by neutrophils (S18).
- **LYMPH:** in some infections and in some lymphoproliferative states, lymphocytes drive the WBC change. MedlinePlus notes neutrophils mostly target bacterial infections and lymphocytes mostly target viral infections (S3); this is a tendency, not a rule.
- **EOS / BASO / MONO:** these are smaller contributors but can raise total WBC in allergy, parasitic infection, chronic inflammation, or marrow disorders (S17).
- **HGB / RBC / PLT:** when WBC abnormality occurs together with abnormal hemoglobin or platelets, a bone marrow cause becomes more likely to be considered (S4). Acute blood loss may show leukocytosis (S4). These relationships are associations, not proof of cause.

#### WBC — H. Important clinical considerations

- **Temporary influences:** acute stress, exercise, smoking, steroid use, pregnancy and labor, and recent surgery (S3, S17, S19).
- **Medications:** corticosteroids, lithium, and beta agonists raise WBC (S17); chemotherapy and some antibiotics can lower it (S2, S3).
- **Infection and inflammation:** the most common reactive causes of high WBC (S3, S17).
- **Hydration:** dehydration can concentrate blood and make cell counts appear higher (S1).
- **Measurement limitations:** automated counts can be flagged; smear review may be added when analyzer results are invalid or abnormal (S21).
- **Interpret cautiously** when the patient is pregnant, a newborn or young child, recently given steroids, or recently stressed or exercising.

**Sources for WBC:** S1 https://medlineplus.gov/lab-tests/complete-blood-count-cbc/ · S2 https://medlineplus.gov/lab-tests/blood-differential/ · S3 https://medlineplus.gov/lab-tests/white-blood-count-wbc/ · S17 https://www.aafp.org/pubs/afp/issues/2000/1101/p2053.html · S18 https://dev3.statpearls.com/point-of-care/126216 · S19 https://www.glowm.com/article/heading/vol-8--maternal-medical-health-and-disorders-in-pregnancy--hematological-normal-ranges-in-pregnancy/id/413403 · S20 https://perinatology.com/Reference/Reference%20Ranges/White%20Blood%20Cell.htm

---

### 3.2 RBC — Red Blood Cell Count (Erythrocyte Count)

**Synonyms and alternative names:** RBC, RBC count, red cell count, erythrocyte count, red blood cells, erythrocytes (S1).
**Low-value terms:** anemia (a low RBC count, hemoglobin, or hematocrit). **High-value terms:** erythrocytosis; polycythemia (clinicians focus on hemoglobin and hematocrit when using these terms) (S23 secondary).

#### RBC — A. Definition and physiological role

The RBC count is the number of red blood cells in a volume of blood. Red blood cells carry oxygen from the lungs to the rest of the body (S1). They contain hemoglobin, the iron-rich protein that binds oxygen. Red cells are produced in the bone marrow; the hormone erythropoietin (EPO), made mainly by the kidney, stimulates production (S4 discusses EPO-related anemias). RBC count, hemoglobin, and hematocrit are related because each measures a feature of red blood cells (S12 mirror of Mayo Clinic text).

#### RBC — B. Units and measurement

- **Common units:** million cells/µL (×10⁶/µL) or ×10¹²/L (the same number). Mayo Clinic pages write this as "trillion cells/L" (S12).
- **Measurement:** the automated analyzer **directly counts** RBCs; MCV is also directly measured, while hematocrit, MCH, and MCHC are calculated (S4).
- **Absolute versus percentage:** RBC is always an absolute count. Hematocrit (HCT) is a related _percentage_ of blood volume occupied by red cells (S1).
- **Red cell indices** (MCV, MCH, MCHC, RDW) describe red cell size and hemoglobin content and help classify the cause of a low RBC (S4).

#### RBC — C. Reference ranges

- **Adult male examples:** 4.35 to 5.65 ×10¹²/L (S12); 5 to 6 million/µL (S11); 4.6 to 5.8 M/µL (S21).
- **Adult female examples:** 3.92 to 5.13 ×10¹²/L (S12); 4 to 5 million/µL (S11); 3.9 to 5.2 M/µL (S21).
- **Altitude:** RBC count varies with altitude (S11).
- **Pregnancy:** plasma volume expands more than red cell mass in healthy pregnancy, which lowers hemoglobin and hematocrit and can lower the apparent RBC concentration (S19). `[Pregnancy-specific RBC numeric intervals were not captured; see Abbassi-Ghanavati table at perinatology.com (S20)]`
- **Children:** values vary with age; use age-specific tables (S4).
- **Reference interval versus threshold:** anemia is _defined_ clinically by hemoglobin (S4), not by an RBC count cut-off.

#### RBC — D. Low levels (low RBC count / anemia)

- **Terminology:** **anemia** is a decrease in hemoglobin concentration or red cell mass below an established threshold. Anemia is not a diagnosis; it is a manifestation of an underlying disorder (S4).
- **Possible causes (S4):**
  - Blood loss (acute or chronic, including gastrointestinal or menstrual)
  - Deficient production: iron deficiency, vitamin B12 deficiency, folate deficiency, marrow failure or marrow replacement, kidney disease, chronic inflammation, infection, or cancer
  - Increased destruction (hemolysis): inherited conditions such as hereditary spherocytosis, sickle cell disease, thalassemia; autoimmune hemolytic anemia; some medicines and infections
  - Hemoglobin-synthesis disorders such as thalassemia
- **Symptoms that may be associated:** fatigue, weakness, shortness of breath on exertion, chest pain, and pallor; severe anemia (hemoglobin below about 7 g/dL) often shows pallor. Symptoms are neither sensitive nor specific, depend on how fast the anemia develops, and are more pronounced when cardiopulmonary reserve is limited (S4).
- **Other CBC parameters that may change:** low HGB and HCT; MCV may be low (microcytic), normal, or high (macrocytic); RDW; reticulocyte count; WBC and platelets may be low if the marrow is involved, or high in some situations such as acute blood loss (leukocytosis) or iron deficiency (thrombocytosis) (S4, S7).
- **Tests that may help (S4, S31):** reticulocyte count, peripheral blood smear, iron studies and ferritin, vitamin B12 and folate, haptoglobin, LDH, indirect bilirubin, direct antiglobulin test, kidney function, and sometimes bone marrow aspiration and biopsy.

#### RBC — E. High levels (high RBC count / erythrocytosis)

- **Terminology:** **erythrocytosis** (high red cell count). **Polycythemia** is the related term applied when hemoglobin or hematocrit is above the reference range (S23 secondary).
- **Two broad mechanisms:** _relative_ (apparent) erythrocytosis, where plasma volume is reduced and red cell mass is normal; and _absolute_ erythrocytosis, where red cell mass is truly increased (S24 secondary, S23 secondary).
  - **Relative causes:** dehydration, diuretics, vomiting, sweating, acute stress (S23 secondary).
  - **Absolute secondary causes (appropriate or inappropriate EPO rise):** smoking (carbon monoxide), chronic lung disease, sleep apnea, high altitude, kidney conditions with local hypoxia, EPO-producing tumors (rare), and exogenous erythropoietin or androgen/testosterone (S24 secondary, S23 secondary).
  - **Absolute primary cause:** polycythemia vera (PV), a myeloproliferative neoplasm often associated with a JAK2 mutation (S24 secondary).
- **Special pattern:** an _RBC count_ can be high while hemoglobin is not high, for example in thalassemia trait or iron deficiency with very small red cells. This pattern is erythrocytosis in count but does not mean polycythemia; hemoglobin and hematocrit are what matter for diagnosing polycythemia (S23 secondary). The Merck Manual also notes that red cells preserve hemoglobin concentration at the expense of size, which is why microcytosis occurs in iron deficiency, impaired hemoglobin synthesis, and in the erythrocytosis of polycythemia vera (S4).
- **Symptoms:** high RBC from common reversible causes usually causes few or no symptoms; symptoms usually reflect the underlying condition (for example snoring/daytime fatigue in sleep apnea). Itching after warm showers is described as more typical of PV (S23 secondary).
- **Other CBC changes:** high hemoglobin and hematocrit; in PV, platelets and WBC may also be elevated (S24 secondary). Normal WBC and platelets are typical of benign causes (S23 secondary).
- **Tests that may help (secondary sources):** repeat CBC after rehydration, oxygen saturation or assessment for low-oxygen states, kidney function, serum EPO level, JAK2 mutation testing, iron studies, and review of smoking/nicotine and medications (S23, S24 secondary).

#### RBC — F. Clinical interpretation

Clinicians read RBC count together with hemoglobin, hematocrit, MCV, MCH, MCHC, and RDW, then add the reticulocyte count and a blood smear to separate _under-production_ from _excess destruction or loss_ (S4). The MCV groups anemias into microcytic (below 80 fL), normocytic, and macrocytic (above 100 fL) types, with different common causes (S4):

| MCV category              | Common associated causes (Merck Manual)                                                                                                        | Notes                                                                   |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Microcytic (below 80 fL)  | iron deficiency; thalassemia and related hemoglobin-synthesis defects; some anemia of chronic disease                                          | RBC count may be normal or high in thalassemia trait (S23 secondary)    |
| Normocytic                | hypoproliferative anemias (low EPO or poor response); hemorrhage before iron deficiency develops                                               | reticulocyte count helps separate loss/destruction from poor production |
| Macrocytic (above 100 fL) | vitamin B12 or folate deficiency; alcohol use disorder; chemotherapy agents such as hydroxyurea or antifolates; large numbers of reticulocytes | cold agglutinin disease can give a false macrocytosis artifact          |

**Limitation:** RBC count alone does not identify the cause. Anemia is not a diagnosis, and even mild asymptomatic anemia warrants looking for the underlying problem (S4).

#### RBC — G. Relationship with other CBC parameters

- **HGB:** RBC count and hemoglobin usually move together because hemoglobin is carried inside red cells. They can diverge when cells are small or pale (microcytic/hypochromic): the count can be normal or high while hemoglobin is low or normal (S4, S23 secondary).
- **HCT / MCV:** hematocrit reflects the proportion of blood made up of red cells; MCV reflects the average cell size (S1).
- **PLT:** iron deficiency and acute or chronic blood loss are associated with _high_ platelets (reactive thrombocytosis) (S7); thrombocytopenia plus anemia raises the question of marrow involvement or a destructive process (S4).
- **WBC / NEUT:** acute severe blood loss may produce leukocytosis and a left shift (S4); low white cells with anemia and low platelets suggests considering a marrow disorder (S4).
- These are associations that guide testing; they do not establish cause.

#### RBC — H. Important clinical considerations

- **Hydration:** dehydration raises RBC, hemoglobin, and hematocrit by concentrating blood without increasing red cell mass; overhydration or pregnancy-related plasma expansion lowers them (S1, S19, S23 secondary).
- **Altitude and smoking:** both can raise RBC (S11, S24 secondary).
- **Medications and hormones:** testosterone/androgens and erythropoiesis-stimulating agents can raise hemoglobin and RBC (S24 secondary); hydroxyurea and antifolates can enlarge red cells (S4).
- **Menstruation:** MedlinePlus lists having a menstrual period among factors that can affect results (S1).
- **Specimen issues:** cold agglutinins can produce a falsely high MCV and RBC agglutination (S4).
- **Interpret cautiously** in pregnancy, at altitude, in children, and when dehydration or recent blood loss is possible.

**Sources for RBC:** S1 https://medlineplus.gov/lab-tests/complete-blood-count-cbc/ · S4 https://www.merckmanuals.com/professional/hematology/approach-to-the-patient-with-anemia/evaluation-of-anemia · S11 https://webarchive.library.unt.edu/eot2008/20090201074819/http:/www.nhlbi.nih.gov/health/dci/Diseases/bdt/bdt_whatdo.html · S12 https://www.kuh.ku.edu.tr/mayo-clinic-care-network/mayo-clinic-health-information-library/test-procedure/complete-blood-count-cbc · S23 https://www.thebloodproject.com/understanding-polycythemia/ · S24 https://www.gponline.com/elevated-haemoglobin-adults/haematology/article/1133349 · S31 https://labtestsonline.org/anemia-testing

---

### 3.3 HGB — Hemoglobin (Hb, Hgb, Haemoglobin)

**Synonyms and alternative names:** HGB, Hgb, Hb, hemoglobin, haemoglobin, hemoglobin concentration (S1).
**Low-value terms:** anemia. **High-value terms:** high hemoglobin, erythrocytosis, polycythemia (S23 secondary).

#### HGB — A. Definition and physiological role

Hemoglobin (HGB) is an iron-rich protein inside red blood cells that carries oxygen from the lungs to the rest of the body (S1). HGB concentration is the main laboratory measure used to define anemia (S4). Hemoglobin synthesis requires iron, so iron deficiency reduces hemoglobin production (S1).

#### HGB — B. Units and measurement

- **Common units:** g/dL (US) or g/L (SI). 14.0 g/dL = 140 g/L (multiply g/dL by 10).
- **Measurement:** hemoglobin is **directly measured** by the automated analyzer (S4).
- **Related calculated values:** MCH (hemoglobin per red cell) and MCHC (hemoglobin concentration per red cell) are calculated; the Merck Manual notes MCHC below 30% defines hypochromia (S4).
- **Absolute versus percentage:** hemoglobin is a concentration, not a percentage. Do not confuse it with hematocrit (%) or with hemoglobin A1c (%), which is a different test.

#### HGB — C. Reference ranges

- **Adult male examples:** 13.2 to 16.6 g/dL (S12); 14 to 17 g/dL (S11); 13.0 to 17.5 g/dL (S21).
- **Adult female examples:** 11.6 to 15.0 g/dL (S12); 12 to 15 g/dL (S11); 11.9 to 15.5 g/dL (S21).
- **Diagnostic threshold for anemia (not a reference interval):** below 13 g/dL (130 g/L) in adult males and below 12 g/dL (120 g/L) in adult females, according to the Merck Manual, which cites the WHO 2011 document (S4, S30). Note how this threshold differs slightly from the example laboratory lower limits above.
- **Polycythemia-related thresholds:** WHO criteria for polycythemia vera referenced in a 2023 ASH abstract use hemoglobin above 16.5 g/dL (male) and above 16.0 g/dL (female); the abstract found most US hospital male upper limits exceed 16.5 g/dL (S14). `[WHO classification document itself not opened; verify before using as a threshold]`
- **Pregnancy:** hemoglobin falls in healthy pregnancy because plasma volume rises more than red cell mass (S19). Sample intervals: GLOWM lists baseline 12 to 16 g/dL, first trimester 11.5 to 14, second 10 to 15, third 9.5 to 15 g/dL (S19). The Abbassi-Ghanavati table at perinatology.com lists nonpregnant female 12 to 15.8, first trimester 11.6 to 13.9, second 9.7 to 14.8, third 9.5 to 15 g/dL (S20). These two summaries differ slightly; use the reporting laboratory's pregnancy-specific range. WHO 2011 also gives pregnancy- and child-specific anemia thresholds `[UNVERIFIED in this session; document cited by Merck but not opened]` (S30).
- **Children:** hemoglobin and hematocrit vary with age from the perinatal period onward and require age-specific tables (S4). `[Numeric pediatric intervals not captured]`
- **Altitude:** hemoglobin varies with altitude (S11).

#### HGB — D. Low levels (low hemoglobin / anemia)

- **Terminology:** **anemia**; qualitative descriptors are mild, moderate, severe (thresholds vary by guideline and population) `[WHO severity cut-offs not verified here]`.
- **Possible causes (S4):** blood loss; iron, B12, or folate deficiency; chronic kidney disease or chronic inflammation; hemolysis; thalassemia and other hemoglobinopathies; marrow failure; marrow infiltration. Pregnancy can lower hemoglobin through plasma expansion (S19).
- **Common associated conditions:** iron-deficiency anemia, anemia of chronic disease, megaloblastic anemias, hemolytic anemias, aplastic anemia, myelodysplastic syndromes, and others (S4).
- **Symptoms:** fatigue, weakness, drowsiness, shortness of breath on exertion, chest pain, angina, fainting, dizziness, headache, pulsatile tinnitus, and pallor, especially when hemoglobin is below about 7 g/dL. Severe or rapid anemia can lead to heart failure or shock in vulnerable patients (S4).
- **Urgent considerations supported by Merck:** hemorrhagic shock (low blood pressure, rapid pulse, pallor, confusion) can result from acute bleeding (S4).
- **Other CBC changes:** low RBC and HCT; abnormal MCV, MCH, MCHC, RDW; reticulocytes high (loss/destruction/recovery) or inappropriately low (poor production) (S4).
- **Tests that may help (S4, S31):** reticulocyte count, smear, ferritin and iron studies, B12, folate, haptoglobin, LDH, bilirubin, direct antiglobulin test, stool occult blood, urinalysis, bone marrow evaluation in selected cases.

#### HGB — E. High levels (high hemoglobin)

- **Terminology:** high hemoglobin; **erythrocytosis**; **polycythemia** (S23 secondary).
- **Possible causes:** see RBC — E. Relative causes (dehydration, diuretics, vomiting) and absolute causes (smoking, sleep apnea, chronic lung disease, altitude, kidney and EPO-related causes, testosterone or EPO use, polycythemia vera) (S23, S24 secondary).
- **Symptoms:** often none from the hemoglobin itself; symptoms usually come from the underlying condition. PV-associated symptoms described in a patient-education source include itching after warm showers (S23 secondary).
- **Other CBC changes:** high hematocrit and RBC; in PV, WBC and platelets may also be high (S24 secondary).
- **Tests that may help (secondary sources):** repeat after hydration, oxygen saturation, EPO level, kidney tests, iron studies, JAK2 testing when absolute erythrocytosis is unexplained (S23, S24 secondary).

#### HGB — F. Clinical interpretation

Hemoglobin is the starting point for anemia assessment: clinicians compare it with sex-, age-, and pregnancy-appropriate thresholds, then use MCV, RDW, reticulocytes, smear, and iron/B12/folate studies to find the cause (S4). Trend relative to the person's own baseline matters; symptoms usually appear when hemoglobin falls well below the individual's baseline (S4). A high hemoglobin is first checked for hydration effects and repeated (S23 secondary).

**Limitations:** hemoglobin alone does not identify cause; reference limits vary by laboratory (S14); anemia is a finding, not a diagnosis (S4).

#### HGB — G. Relationship with other CBC parameters

- **RBC and HCT:** hemoglobin, RBC count, and hematocrit are interrelated measures of red cell mass (S12 mirror).
- **MCV / MCH / MCHC:** classify anemia by cell size and hemoglobin content (S4).
- **PLT:** high platelets with low hemoglobin and low MCV suggests iron deficiency as one possibility (S7); low platelets plus low hemoglobin may point to marrow involvement or a destructive/consumptive process and often prompts marrow evaluation when unexplained (S4).
- **WBC:** abnormal WBC alongside abnormal hemoglobin raises consideration of a marrow disorder (S4).
- These are patterns to investigate, not diagnoses.

#### HGB — H. Important clinical considerations

- **Temporary or non-pathological influences:** hydration status, pregnancy-related plasma expansion, altitude, menstrual period, smoking (S1, S11, S19, S24 secondary).
- **Medication effects:** testosterone and erythropoiesis-stimulating agents raise hemoglobin (S24 secondary); chemotherapy and some drugs reduce production or cause hemolysis (S4).
- **Infection and inflammation:** chronic infection, cancer, and inflammatory disorders can suppress RBC production (S4).
- **Measurement limitations:** reference limits differ among laboratories; a "normal" flagged value may still be abnormal for a given patient, and a value near the limit may be normal for that person (S14).
- **Interpret cautiously** in pregnancy, children, at altitude, and with recent fluid changes.

**Sources for HGB:** S4 https://www.merckmanuals.com/professional/hematology/approach-to-the-patient-with-anemia/evaluation-of-anemia · S14 https://ash.confex.com/ash/2023/webprogram/Paper182994.html · S19 https://www.glowm.com/article/heading/vol-8--maternal-medical-health-and-disorders-in-pregnancy--hematological-normal-ranges-in-pregnancy/id/413403 · S20 https://perinatology.com/Reference/Reference%20Ranges/Hemoglobin.htm · S30 https://iris.who.int/server/api/core/bitstreams/b82789de-df63-41ba-8058-25f9f5da0c40/content (cited by Merck; not opened)

---

### 3.4 PLT — Platelet Count (Thrombocyte Count)

**Synonyms:** PLT, platelets, thrombocytes, platelet count, thrombocyte count. **Low:** thrombocytopenia. **High:** thrombocytosis (thrombocythemia when due to a marrow disorder).

#### PLT — A. Definition and physiological role

Platelets are cell fragments that stop bleeding by helping blood clot (S1, S10). They are made in the bone marrow and live roughly 7 to 10 days.

#### PLT — B. Units and measurement

Units: cells/µL, K/µL, ×10³/µL, or ×10⁹/L (250,000/µL = 250 ×10⁹/L). Counted directly by the analyzer. PLT is an absolute count only; there is no percentage. A related value, mean platelet volume (MPV), reports platelet size (S21).

#### PLT — C. Reference ranges

- **Adult examples:** 150,000 to 450,000/µL (S10, S11 gives 140,000 to 450,000); Mayo Clinic values via care-network pages are 135 to 317 ×10⁹/L (male) and 157 to 371 ×10⁹/L (female) (S12). A 2023 ASH abstract found over a quarter of US hospitals set the platelet upper limit above the WHO essential thrombocythemia criterion of 450 ×10⁹/L (S14).
- **Pregnancy:** GLOWM lists 150 to 400 baseline, 170 to 390 (first trimester), 150 to 400 (second), 145 to 400 (third) ×10⁹/L (S19). NHLBI notes pregnant women are at higher risk of thrombocytopenia (S10).
- **Children:** `[numeric pediatric intervals not retrieved]`.
- **Thresholds:** thrombocytopenia is below 150,000/µL; thrombocytosis is above 450,000/µL (S7, S10). Some labs use 400,000 (S23 secondary).

#### PLT — D. Low levels (thrombocytopenia)

- **Mechanisms (S10):** bone marrow makes too few platelets (viral infections such as chickenpox, mumps, rubella, EBV, parvovirus, HIV; alcohol; marrow disease; genetic conditions); platelets are destroyed or used up (autoimmune destruction, some medicines, TTP, DIC, infection/sepsis, surgery, late pregnancy); or the spleen holds too many.
- **Symptoms:** mild thrombocytopenia often has none. Bleeding is the main sign: small red or purple skin spots, easy bruising, nose or gum bleeding, heavy menstrual bleeding. NHLBI states serious bleeding risk generally arises only when the count is very low (below about 10,000 to 20,000/µL), with milder bleeding sometimes below 50,000/µL; individual variation is large (S10).
- **Urgent consideration:** severe thrombocytopenia with significant bleeding is a medical emergency (S10).
- **Artifact to exclude:** EDTA-induced platelet clumping gives a falsely low count; confirm with a smear and/or a citrate tube (S4, S29, S34).
- **Other CBC changes:** low HGB or WBC alongside suggests marrow involvement and may prompt marrow evaluation (S4).
- **Tests that may help:** repeat count, smear, liver and kidney tests, LDH, reticulocytes, viral testing, medication review, bone marrow in selected cases (S4, S29).

#### PLT — E. High levels (thrombocytosis)

- **Reactive (secondary):** infection, inflammation, iron deficiency, acute blood loss, surgery or trauma, hemolysis, splenectomy, malignancy, rebound after chemotherapy (S7, S32). Reactive thrombocytosis accounts for most cases (over 85% in routine practice per S33). Platelet function is usually normal and thrombotic risk is not increased unless arterial disease exists (S7).
- **Clonal (primary):** essential thrombocythemia and other myeloproliferative neoplasms; if no cause is obvious, patients should be evaluated for these (S7).
- **Symptoms:** usually none; bruising, bleeding, or clotting can occur mainly with primary causes (S23 secondary).
- **Tests that may help:** ferritin/iron studies, inflammatory markers, smear, repeat count over weeks to months; molecular testing and marrow if persistent and unexplained (S7, S32).

#### PLT — F. Clinical interpretation

Clinicians confirm true values on a smear, check bleeding symptoms and medications, then look at HGB and WBC to decide whether the problem is isolated or part of multi-line disease (S4). Persistent unexplained counts over 450 ×10⁹/L (2 to 3 months) are investigated (S32). Limitation: the count does not reflect platelet _function_.

#### PLT — G. Relationship with other CBC parameters

Iron deficiency (low HGB, low MCV) is associated with high PLT (S7). Low PLT with anemia or leukopenia raises the question of marrow failure or infiltration (S4). High PLT with high HGB, WBC, or basophils may prompt evaluation for a myeloproliferative neoplasm (S15). Associations only.

#### PLT — H. Important clinical considerations

Pseudothrombocytopenia (clumping, small clots in the tube, giant platelets miscounted by the analyzer) (S29, S34); pregnancy; alcohol; medicines that lower platelets; exercise and postpartum states can raise counts (S34). Interpret cautiously when only one count is available.

**Sources:** S4, S7 https://www.merckmanuals.com/professional/hematology/myeloproliferative-disorders/reactive-thrombocytosis-secondary-thrombocythemia · S10 https://webarchive.library.unt.edu/eot2008/20080922160927/http:/www.nhlbi.nih.gov/health/dci/Diseases/thcp/thcp_all.html · S29 · S32 · S33 · S34

---

### 3.5 NEUT — Neutrophils (Neutrophil Count, ANC, Segs/Polys)

**Synonyms:** NEUT, NEUT#, NEUT%, neutrophil count, absolute neutrophil count (ANC), polymorphonuclear cells (PMNs), segmented neutrophils plus bands. **Low:** neutropenia. **High:** neutrophilia.

#### NEUT — A. Definition and physiological role

Neutrophils are the most common white cell and the body's main defense against infection when bacteria, viruses, or other germs enter (S2). They are made in the marrow, and immature "band" forms are released in increased numbers during stress or infection (S17).

#### NEUT — B. Units and measurement

Absolute (cells/µL or ×10⁹/L) and percentage of WBC. **ANC = WBC × (% neutrophils + % bands) ÷ 100** (S26 secondary). Example: WBC 8,000/µL with 60% neutrophils gives ANC 4,800/µL.

#### NEUT — C. Reference ranges

- The typical lower limit is about 1,500/µL (1.5 ×10⁹/L) (S8); it is slightly lower in Black patients per a Merck/MSD page, and relative to white people Black people have lower average neutrophil counts (S9, S18). Upper threshold for neutrophilia is about 7,700/µL (S18). Percentage: roughly 60% to 70% of WBC (S18).
- **Neutropenia severity:** mild 1,000 to 1,500; moderate 500 to 1,000; severe below 500/µL (S8, S16). Agranulocytosis cut-offs vary by source (below 100 or below 200/µL) (S26 secondary).
- **Pregnancy:** neutrophils rise (S19). **Children:** after age 10 neutrophils normally exceed 1,500/µL (S26 secondary); younger children need age-specific ranges.

#### NEUT — D. Low levels (neutropenia)

- **Causes:** medicines (one of the most frequent causes), infections, immune reactions, marrow infiltration or failure, chemotherapy, autoimmune disease, enlarged spleen trapping cells, congenital syndromes (genes such as ELANE, HAX1), cyclic neutropenia, and chronic benign neutropenia in which counts stay low but infections are rare (S8, S16).
- **Symptoms:** none specific; frequent or unusual infections lead to testing. Below 500/µL, infection risk rises greatly, including from organisms normally harmless in the mouth and gut (S8).
- **Other CBC changes:** low total WBC; anemia/thrombocytopenia suggest marrow involvement (S4).
- **Tests:** repeat CBC, smear, medication and infection review, marrow exam in selected cases (S8).

#### NEUT — E. High levels (neutrophilia)

- **Causes:** bacterial infection (often with left shift, toxic granulation, Döhle bodies), tissue injury, inflammation, stress, smoking, pregnancy, corticosteroids, lithium, beta agonists, G-CSF, splenectomy, hemolysis, solid-tumor and myeloproliferative disease (S17, S18).
- **Symptoms:** reflect the cause (fever, localized infection signs).
- **Tests:** smear, repeat CBC, cause-directed tests; WBC above 50,000 from a non-marrow cause is a leukemoid reaction (S17).

#### NEUT — F. Clinical interpretation

Neutrophil count is read as an _absolute_ number with symptoms, medications (especially steroids), and trend. Mild, transient changes are common. Limitation: a normal ANC does not exclude infection, and neutrophilia does not prove bacterial infection.

#### NEUT — G. Relationship with other CBC parameters

Neutrophils dominate total WBC, so WBC and NEUT usually move together (S18). A high neutrophil count can lower the _percentage_ of lymphocytes, eosinophils, and basophils without changing their absolute counts. Neutropenia with low HGB or PLT suggests marrow disease or splenic or immune processes (S4).

#### NEUT — H. Important clinical considerations

Steroids, stress, exercise, smoking, pregnancy and ancestry affect baseline (S9, S17, S19). Chemotherapy and many medicines lower counts (S8). Pseudoneutropenia can reflect shifts between circulating and marginated pools (S16). Interpret cautiously with a single value.

**Sources:** S2 https://medlineplus.gov/lab-tests/blood-differential/ · S8 https://merckmanuals.com/home/blood-disorders/white-blood-cell-disorders/neutropenia · S16 https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12106181/ · S17 · S18

---

### 3.6 LYMPH — Lymphocytes (Lymphocyte Count, ALC)

**Synonyms:** LYMPH, LYM#, LYM%, lymphocyte count, absolute lymphocyte count (ALC). **Low:** lymphocytopenia / lymphopenia. **High:** lymphocytosis.

#### LYMPH — A. Definition and physiological role

Lymphocytes include B cells (fight invading viruses, bacteria, toxins) and T cells (some destroy cancer cells and virus-infected cells) (S2). Blood lymphocytes are a small share of the total lymphocyte pool in nodes and tissues (S6).

#### LYMPH — B. Units and measurement

Absolute (cells/µL, ×10⁹/L) and percentage. ALC = WBC × % lymphocytes ÷ 100. Subsets (CD4, CD8, B, NK) need flow cytometry (S6).

#### LYMPH — C. Reference ranges

- **Adult:** 1,000 to 4,800/µL; lymphocytes are about 20% to 40% of WBC (S6). Labs may differ slightly (S6).
- **Children:** under 2 years 3,000 to 9,500/µL; lower limit about 1,500/µL at age 6 (S6).
- **Pregnancy:** lymphocytes fall in the first and second trimesters and rise in the third (S19); sample range 0.9 to 3.9 ×10⁹/L (S20).
- **Thresholds:** lymphocytopenia is below 1,000/µL in adults or below 3,000/µL in children under 2 (S6).

#### LYMPH — D. Low levels (lymphocytopenia)

- **Causes:** viral infections (HIV, COVID-19, EBV), protein-energy undernutrition, corticosteroids and Cushing syndrome, chemotherapy, radiation, antilymphocyte therapies, autoimmune disease, inherited immunodeficiency; often transient in infection, sepsis, or stress (S6).
- **Symptoms:** usually none; recurrent or unusual infections may occur (S6).
- **Tests:** smear, lymphocyte subsets by flow cytometry, immunoglobulins, HIV testing, usually after acute illness resolves (S6).

#### LYMPH — E. High levels (lymphocytosis)

- **Reactive:** viral infections (EBV, CMV, hepatitis), pertussis, toxoplasmosis, stress, smoking, splenectomy; reactive forms typically normalize within weeks (S25 secondary).
- **Clonal:** chronic lymphocytic leukemia, lymphoma, acute lymphoblastic leukemia (S25 secondary). Persistent or marked elevation, atypical cells, or other cytopenias prompt smear review and flow cytometry.
- **Symptoms:** reflect the cause (fever, enlarged nodes, night sweats).

#### LYMPH — F. Clinical interpretation

Use the absolute count and age-specific range, check the smear for atypical lymphocytes, and consider symptoms and duration. Limitation: blood counts may not reflect lymphocytes in tissues (S6).

#### LYMPH — G. Relationship with other CBC parameters

MedlinePlus notes neutrophils mostly target bacterial infections and lymphocytes mostly target viral ones, a tendency not a rule (S3). Lymphopenia with anemia or thrombocytopenia suggests considering marrow or systemic disease; neutrophil-to-lymphocyte balance shifts under steroids and stress.

#### LYMPH — H. Important clinical considerations

Steroids, stress, smoking, pregnancy, age, and recent infection alter counts (S6, S19). Interpret cautiously in children and in the weeks after an infection.

**Sources:** S6 https://www.merckmanuals.com/professional/hematology/leukopenias/lymphocytopenia · S19 · S20 https://www.perinatology.com/Reference/Reference%20Ranges/Lymphocytes.htm · S25 https://pediatriceducation.org/?p=2163

---

### 3.7 MONO — Monocytes (Monocyte Count)

**Synonyms:** MONO, MONO#, MONO%, monocyte count. **High:** monocytosis. **Low:** monocytopenia.
**Evidence note:** MedlinePlus covers monocyte _function_; numeric thresholds below come from secondary sources and have **lower confidence** `[UNVERIFIED against an authoritative primary reference]`.

#### MONO — A. Definition and physiological role

Monocytes kill bacteria, viruses, and other germs, boost the immune response, and clear away dead cells (S2). They mature into macrophages and dendritic cells in tissue (S27 secondary).

#### MONO — B. Units and measurement

Absolute (cells/µL, ×10⁹/L) and % of WBC; absolute = WBC × % ÷ 100.

#### MONO — C. Reference ranges

Secondary sources give about 0.2 to 0.8 ×10⁹/L (200 to 800/µL) and 2% to 10% of WBC in adults (S28 secondary). Monocytosis thresholds vary between sources (above 500, 800, or 1,000/µL) (S27, S28 secondary). Pregnancy: monocytes rise in the first trimester then fall (S19). Children: age-specific ranges needed. Reference ranges vary by laboratory.

#### MONO — D. Low levels (monocytopenia)

Reported associations (secondary): myelotoxic drugs, acute infection stress, aplastic anemia, hairy cell leukemia, myeloid leukemia. Usually no symptoms. A low count is rarely interpreted alone; check the other cell lines and smear.

#### MONO — E. High levels (monocytosis)

- **Associations:** chronic infections (tuberculosis, endocarditis, brucellosis, syphilis), recovery from acute infection or neutropenia, autoimmune and inflammatory disease (lupus, rheumatoid arthritis, IBD), sarcoidosis, Hodgkin lymphoma, chronic myelomonocytic leukemia (S27 secondary).
- **Symptoms:** none directly; reflect the cause.
- **Tests that may help:** repeat CBC, smear, inflammatory markers, cultures or serology, chest imaging, marrow if persistent and unexplained (S28 secondary).

#### MONO — F. Clinical interpretation

Mild, transient rises are common during recovery from illness. Persistent or marked monocytosis, or abnormal other lines, calls for clinical assessment. It never confirms a specific disease alone.

#### MONO — G. Relationship with other CBC parameters

Monocytosis often accompanies neutrophilia during infection recovery; with anemia, cytopenias, or abnormal smear it raises consideration of marrow disorders. Association only.

#### MONO — H. Important clinical considerations

Smoking, recent infection, steroids, and pregnancy may shift counts. Percentage can mislead when other WBCs change; check the absolute count.

**Sources:** S2 · S19 · S27 https://en.wikipedia.org/wiki/Monocytosis · S28 https://ubiehealth.com/doctors-note/high-monocytes-counts-threshold-causes-symptoms-54101q1

---

### 3.8 EOS — Eosinophils (Eosinophil Count, AEC)

**Synonyms:** EOS, EOS#, EOS%, eosinophil count, absolute eosinophil count (AEC). **High:** eosinophilia; hypereosinophilia. **Low:** eosinopenia.

#### EOS — A. Definition and physiological role

Eosinophils defend against parasites and infections, take part in allergies, and help control inflammation (S2). Eosinophil-released products can injure tissue when high levels persist (S5).

#### EOS — B. Units and measurement

Absolute (cells/µL, ×10⁹/L) and %. The absolute count is the standard for grading because percentages shift when other WBCs change.

#### EOS — C. Reference ranges

- **Threshold:** eosinophilia is a count above 500/µL (0.5 ×10⁹/L) (S5). Severity: mild 500 to 1,500; moderate 1,500 to 5,000; severe above 5,000/µL. Counts of 1,500/µL or more can cause organ damage if they persist (S5).
- **Pregnancy:** eosinophils are unchanged (S19). **Children, lower limit:** `[not retrieved]`; labs report their own interval.

#### EOS — D. Low levels (eosinopenia)

The lower limit is near zero, so low values are usually not interpretable on their own. Corticosteroids and acute stress are commonly cited reasons `[general knowledge; not verified in this session]`.

#### EOS — E. High levels (eosinophilia)

- **Causes (S5):** allergic or atopic disorders (most common cause in the US, usually mild to moderate); medication reactions (including DRESS; drugs such as allopurinol, vancomycin, lamotrigine, carbamazepine, trimethoprim-sulfamethoxazole); parasitic infections, especially tissue-invasive helminths (protozoa and non-invasive worms usually do not); eosinophilic esophagitis; eosinophilic granulomatosis with polyangiitis; some cancers, notably Hodgkin lymphoma; primary clonal disorders; idiopathic hypereosinophilic syndrome (eosinophilia with organ dysfunction without a parasitic or allergic cause).
- **Symptoms:** mild eosinophilia causes none; high persistent levels can involve heart, lungs, skin, spleen, and nervous system (S5).
- **Tests (S5):** travel and medication history, stool ova and parasites (three specimens; negative does not exclude a parasite), organ function tests, serology for parasites or rheumatic disease, chest imaging, marrow if clonal disease is suspected.

#### EOS — F. Clinical interpretation

Clinicians consider allergy, drugs, and parasites first, then check organ involvement when the count is 1,500/µL or more (S5). Repeat testing separates transient from persistent elevation.

#### EOS — G. Relationship with other CBC parameters

Eosinophilia with basophilia, anemia, or thrombocytosis raises consideration of a myeloproliferative process (S15). Eosinophils and basophils may both rise in allergic states. Eosinophil percentage looks lower when neutrophils surge. Association only.

#### EOS — H. Important clinical considerations

Medications, allergy season, travel exposure, and corticosteroid use influence counts. A normal count does not exclude allergy or parasites.

**Sources:** S5 https://www.merckmanuals.com/professional/hematology/eosinophilic-disorders/eosinophilia · S2 · S15 · S19

---

### 3.9 BASO — Basophils (Basophil Count)

**Synonyms:** BASO, BASO#, BASO%, basophil count, absolute basophil count. **High:** basophilia. **Low:** basopenia (rarely interpretable).

#### BASO — A. Definition and physiological role

Basophils release chemical mediators during allergic reactions and asthma attacks (S2). They are the least numerous white cells in the blood (S15).

#### BASO — B. Units and measurement

Absolute (cells/µL) and % of WBC (usually well under 1% to a few percent of WBC; lab-specific).

#### BASO — C. Reference ranges

Basophilia is generally an absolute count above 200 cells/µL; ranges differ by laboratory and local population (S15). Pregnancy: unchanged (S19). Pediatric intervals: `[not retrieved]`.

#### BASO — D. Low levels

Because normal values are near zero, a low basophil count is not usually clinically interpretable `[general knowledge; unverified]`.

#### BASO — E. High levels (basophilia)

- **Causes (S15):** allergic reactions, chronic inflammation or infection (influenza, tuberculosis), inflammatory bowel disease, autoimmune disease; and neoplasms such as chronic myeloid leukemia, polycythemia vera, primary myelofibrosis, essential thrombocythemia, acute myeloid leukemia, and rarely solid tumors. Secondary sources add hypothyroidism.
- **Symptoms:** none directly; itching can occur from histamine release; otherwise reflect the cause.
- **Tests:** repeat CBC, smear, other lines; thyroid testing if suggested; molecular testing such as BCR-ABL1 or JAK2 when myeloproliferative disease is suspected (S15; see MedlinePlus "BCR-ABL1 Genetic Test").

#### BASO — F. Clinical interpretation

Isolated mild basophilia is often reactive. Persistent basophilia with other abnormal lines (left-shifted neutrophilia, thrombocytosis, anemia) warrants evaluation for a myeloproliferative neoplasm. Concurrent eosinophilia above 1,500/µL may lead to consideration of hypereosinophilic syndrome (S15).

#### BASO — G. Relationship with other CBC parameters

Usually evaluated with EOS, NEUT, PLT, HGB, and WBC; a combination of abnormal lines points toward marrow disorders. Association only.

#### BASO — H. Important clinical considerations

Allergic exposure, inflammation, thyroid status, and estrogen use may shift counts (secondary). Analyzer counts of very low numbers are imprecise.

**Sources:** S15 https://ncbi.nlm.nih.gov/books/NBK535365 · S2 · S19

---

## 4. Clinical Patterns Involving Multiple Parameters

Each pattern is a prompt for further evaluation, not a diagnosis.

**4.1 Low WBC with low neutrophils.** _May indicate_ reduced production, increased destruction, or sequestration of neutrophils. _Causes:_ medicines, chemotherapy, viral infection, autoimmune disease, marrow disease, enlarged spleen, congenital or benign ethnic/chronic neutropenia (S3, S8). _Investigations:_ repeat CBC, smear, medication review, infection and immune tests, marrow if persistent or other lines are abnormal. _Why not confirmatory:_ many benign or transient causes; ANC below 500/µL raises infection risk but does not name the cause (S8).

**4.2 High WBC with high neutrophils.** _May indicate_ infection, inflammation, tissue injury, stress, or drug effect (S17). _Investigations:_ smear for left shift and toxic changes, cause-directed testing, repeat count. _Why not confirmatory:_ steroids, smoking, pregnancy, and exercise also cause it.

**4.3 Low hemoglobin with low RBC.** _May indicate_ anemia from blood loss, deficiency, hemolysis, chronic disease, or marrow failure (S4). _Investigations:_ MCV/RDW, reticulocytes, smear, ferritin/iron, B12, folate, hemolysis tests. _Why not confirmatory:_ anemia is a finding, not a diagnosis (S4). RBC may stay near normal in thalassemia trait.

**4.4 High RBC with high hemoglobin.** _May indicate_ relative (dehydration) or absolute erythrocytosis (hypoxia, smoking, EPO or testosterone, PV) (S23, S24 secondary). _Investigations:_ repeat after hydration, oxygen assessment, EPO, JAK2 when unexplained. _Why not confirmatory:_ most mild elevations are reversible.

**4.5 Low platelet count.** _May indicate_ reduced production, immune destruction, consumption, or splenic sequestration; first exclude clumping artifact (S10, S29). _Investigations:_ smear/citrate repeat, liver and kidney tests, viral and medication review. _Why not confirmatory:_ many causes; bleeding risk depends on the level and individual (S10).

**4.6 High platelet count.** _May indicate_ reactive thrombocytosis (most often) or a myeloproliferative neoplasm (S7, S33). _Investigations:_ iron studies, inflammatory markers, repeat count, molecular tests if persistent and unexplained. _Why not confirmatory:_ reactive causes are common and usually resolve.

**4.7 Low lymphocyte count.** _May indicate_ viral illness, steroids, chemotherapy, undernutrition, autoimmune disease, or immunodeficiency (S6). _Investigations:_ subsets, immunoglobulins, HIV test when indicated. _Why not confirmatory:_ often transient.

**4.8 High lymphocyte count.** _May indicate_ viral infection or pertussis (reactive), or clonal lymphoproliferative disease (S25 secondary). _Investigations:_ smear, viral serology, flow cytometry if persistent. _Why not confirmatory:_ reactive lymphocytosis is common, especially in children.

**4.9 High eosinophil count.** _May indicate_ allergy, drug reaction, parasites, or less often neoplasm (S5). _Investigations:_ history, stool studies, organ function, serology. _Why not confirmatory:_ the most common cause is allergic disease (S5).

**4.10 High monocyte count.** _May indicate_ chronic infection or inflammation, recovery phase, or rarely a myeloid disorder (S27 secondary). _Investigations:_ repeat CBC, smear, inflammatory markers. _Why not confirmatory:_ low-confidence thresholds and many benign causes.

**4.11 High basophil count.** _May indicate_ allergy/inflammation, or myeloproliferative neoplasm when persistent with other abnormalities (S15). _Investigations:_ smear, BCR-ABL1/JAK2 when suspected. _Why not confirmatory:_ isolated mild basophilia is nonspecific.

**4.12 Multiple abnormalities together.** Two or more abnormal lines (for example anemia with thrombocytopenia or leukopenia, or all three: **pancytopenia**) raise the possibility of marrow disease, and the Merck Manual lists more than one lineage abnormality as a reason to consider marrow examination (S4). Other causes include drugs, infection, autoimmune disease, nutritional deficiency, and splenic sequestration. _Investigations:_ smear review, reticulocytes, B12/folate, liver/spleen assessment, hematology referral. _Why not confirmatory:_ the pattern is nonspecific.

---

## 5. Factors Affecting CBC Results

| Factor                       | Typical effect                                                                                                                            | Source               |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Dehydration                  | raises RBC, HGB, HCT (relative)                                                                                                           | S1, S23              |
| Pregnancy                    | lower HGB/HCT; higher WBC and neutrophils; lymphocytes fall then rise; PLT slightly lower late                                            | S19, S20             |
| Altitude                     | raises RBC, HGB, HCT                                                                                                                      | S11                  |
| Smoking                      | higher WBC, RBC, HGB                                                                                                                      | S3, S24              |
| Stress, exercise             | higher WBC and neutrophils, reverses within hours                                                                                         | S17                  |
| Corticosteroids              | higher neutrophils; lymphocyte destruction with long-term use                                                                             | S17, S6              |
| Other drugs                  | lithium, beta agonists raise WBC; chemotherapy and some antibiotics lower WBC; testosterone and EPO raise HGB; hydroxyurea enlarges cells | S2, S3, S4, S17, S24 |
| Menstruation, diet, activity | can alter results                                                                                                                         | S1                   |
| Infection, inflammation      | WBC, neutrophil, platelet changes                                                                                                         | S3, S7, S17          |
| Age, sex, ancestry           | different intervals                                                                                                                       | S4, S9, S18          |
| Specimen/lab                 | EDTA clumping, small clots, giant platelets, cold agglutinins, reticulocytes inflating MCV, analyzer flags and smear review               | S4, S21, S29, S34    |

---

## 6. Limitations of CBC Interpretation

1. A CBC is a screening tool and one piece of the picture; history, symptoms, and other tests are needed (S1).
2. A single parameter cannot confirm a disease (S3).
3. Reference intervals vary between laboratories and populations; a flagged value is not always disease and a "normal" value is not always healthy for that person (S14).
4. Reference intervals differ from diagnostic thresholds (Section 2.3).
5. Percentages can mislead; use absolute counts (Section 2.1).
6. Pre-analytic and analytic artifacts occur (Section 5).
7. Peripheral counts do not show tissue or marrow cell numbers, and the smear can reveal abnormalities despite normal automated counts (S4, S6).
8. Interpretation needs age, sex, pregnancy, medications, symptoms, and trend over time.
9. **For HemoPredict:** use the report's own reference range when available, show absolute and percentage values separately, label outputs as educational, and avoid language implying a diagnosis.

---

## 7. Medical Terminology Glossary

- **Absolute count:** cells per volume of blood.
- **Agranulocytosis:** extremely low neutrophil count (cut-off varies by source).
- **ANC:** absolute neutrophil count.
- **Anemia:** hemoglobin or red cell mass below a threshold; a finding, not a diagnosis.
- **Band neutrophil:** immature neutrophil.
- **Basophilia / basopenia:** high / low basophils.
- **Bicytopenia / pancytopenia:** two / three cell lines low.
- **Eosinophilia / hypereosinophilia:** eosinophils above 500/µL / persistently 1,500/µL or more.
- **Erythrocytosis / polycythemia:** high red cell count / hemoglobin or hematocrit above the reference range.
- **Hematocrit (HCT):** percentage of blood volume made of red cells.
- **Hemoconcentration:** blood concentrated by reduced plasma volume.
- **Leukemoid reaction:** WBC above 50,000/µL from a non-marrow cause.
- **Leukocytosis / leukopenia:** high / low WBC.
- **Left shift:** increased immature neutrophils.
- **Lymphocytosis / lymphocytopenia:** high / low lymphocytes.
- **MCV, MCH, MCHC, RDW:** red cell size, hemoglobin per cell, hemoglobin concentration per cell, size variation.
- **Microcytic / macrocytic / normocytic:** small / large / normal red cells.
- **Monocytosis / monocytopenia:** high / low monocytes.
- **Neutrophilia / neutropenia:** high / low neutrophils.
- **Peripheral blood smear:** microscope slide review of blood cells.
- **Pseudothrombocytopenia:** falsely low platelet count from clumping.
- **Reference interval:** range covering about 95% of a healthy group.
- **Relative count:** percentage of WBC.
- **Reticulocyte:** young red cell; reflects marrow response.
- **Thrombocytopenia / thrombocytosis:** low / high platelets.

---

## 8. References and Source URLs

Retrieved 2026-11-03. "Date" is the page's stated update or review date when visible.

| ID  | Source, organization/author                                                                         | Date                  | URL                                                                                                                                                                                                                                                | Supports                                   |
| --- | --------------------------------------------------------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| S1  | Complete Blood Count (CBC), MedlinePlus, NLM/NIH                                                    | updated Oct 15, 2024  | https://medlineplus.gov/lab-tests/complete-blood-count-cbc/                                                                                                                                                                                        | CBC basics, factors, limits                |
| S2  | Blood Differential, MedlinePlus                                                                     | updated Oct 9, 2024   | https://medlineplus.gov/lab-tests/blood-differential/                                                                                                                                                                                              | WBC types and roles                        |
| S3  | White Blood Count (WBC), MedlinePlus                                                                | updated Aug 6, 2024   | https://medlineplus.gov/lab-tests/white-blood-count-wbc/                                                                                                                                                                                           | WBC, leukocytosis, leukopenia              |
| S4  | Evaluation of Anemia, Gerber G, Merck Manual Professional                                           | updated Oct 2026      | https://www.merckmanuals.com/professional/hematology/approach-to-the-patient-with-anemia/evaluation-of-anemia                                                                                                                                      | RBC, HGB, anemia thresholds, indices       |
| S5  | Eosinophilia, Liesveld J, Merck Manual Professional                                                 | updated May 2026      | https://www.merckmanuals.com/professional/hematology/eosinophilic-disorders/eosinophilia                                                                                                                                                           | EOS                                        |
| S6  | Lymphocytopenia, Merck Manual Professional                                                          | not captured          | https://www.merckmanuals.com/professional/hematology/leukopenias/lymphocytopenia                                                                                                                                                                   | LYMPH                                      |
| S7  | Reactive Thrombocytosis, Merck Manual Professional                                                  | updated Sept 2025     | https://www.merckmanuals.com/professional/hematology/myeloproliferative-disorders/reactive-thrombocytosis-secondary-thrombocythemia                                                                                                                | PLT high                                   |
| S8  | Neutropenia, Merck Manual Consumer                                                                  | not captured          | https://merckmanuals.com/home/blood-disorders/white-blood-cell-disorders/neutropenia                                                                                                                                                               | NEUT low                                   |
| S9  | Neutropénie, MSD/Merck Manual (French)                                                              | not captured          | https://www.msdmanuals.com/fr/professional/hématologie-et-oncologie/leucopénie/neutropénie                                                                                                                                                         | NEUT ancestry note (snippet only)          |
| S10 | Thrombocytopenia, NHLBI (archived 2008 copy)                                                        | 2008 archive          | https://webarchive.library.unt.edu/eot2008/20080922160927/http:/www.nhlbi.nih.gov/health/dci/Diseases/thcp/thcp_all.html                                                                                                                           | PLT low                                    |
| S11 | What Do Blood Tests Show?, NHLBI (archived 2009 copy)                                               | 2009 archive          | https://webarchive.library.unt.edu/eot2008/20090201074819/http:/www.nhlbi.nih.gov/health/dci/Diseases/bdt/bdt_whatdo.html                                                                                                                          | Reference interval concept, example ranges |
| S12 | Complete blood count, Mayo Clinic Health Information Library (values read from care-network mirror) | Nov 15, 2023 (mirror) | https://www.kuh.ku.edu.tr/mayo-clinic-care-network/mayo-clinic-health-information-library/test-procedure/complete-blood-count-cbc ; official page https://www.mayoclinic.org/tests-procedures/complete-blood-count/about/pac-20384919 (not opened) | Example ranges                             |
| S13 | Tefferi A, Hanson CA, Inwards DJ. Mayo Clin Proc 2005;80(7):923-936 (abstract only)                 | 2005                  | https://pubmed.ncbi.nlm.nih.gov/16007898/                                                                                                                                                                                                          | Abnormal CBC frequency                     |
| S14 | Variations in CBC Reference Limits Among US Hospitals, ASH 2023 abstract 3701                       | 2023                  | https://ash.confex.com/ash/2023/webprogram/Paper182994.html                                                                                                                                                                                        | Lab variation                              |
| S15 | Basophilia, StatPearls (NCBI Bookshelf NBK535365)                                                   | not captured          | https://ncbi.nlm.nih.gov/books/NBK535365                                                                                                                                                                                                           | BASO                                       |
| S16 | Diagnosis and management of neutropenia (review)                                                    | not captured          | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12106181/                                                                                                                                                                                             | NEUT low                                   |
| S17 | Leukocytosis: Basics of Clinical Assessment, Am Fam Physician                                       | Nov 1, 2000           | https://www.aafp.org/pubs/afp/issues/2000/1101/p2053.html                                                                                                                                                                                          | WBC high, NEUT                             |
| S18 | Neutrophilia, StatPearls (via statpearls.com mirror)                                                | not captured          | https://dev3.statpearls.com/point-of-care/126216                                                                                                                                                                                                   | NEUT thresholds, ancestry                  |
| S19 | Hematological normal ranges in pregnancy, GLOWM                                                     | not captured          | https://www.glowm.com/article/heading/vol-8--maternal-medical-health-and-disorders-in-pregnancy--hematological-normal-ranges-in-pregnancy/id/413403                                                                                                | Pregnancy                                  |
| S20 | Abbassi-Ghanavati M et al. Obstet Gynecol 2009;114(6):1326-31, tables at perinatology.com           | 2009                  | https://perinatology.com/Reference/Reference%20Ranges/Hemoglobin.htm                                                                                                                                                                               | Pregnancy ranges                           |
| S21 | CBC with auto differential, Boone Health test catalog                                               | not captured          | https://boonehealth.testcatalog.org/show/CBC                                                                                                                                                                                                       | Method, example lab ranges                 |
| S22 | Leukocytosis, WikEM (secondary)                                                                     | not captured          | https://www.wikem.org/wiki/Leukocytosis                                                                                                                                                                                                            | Pediatric/hyperleukocytosis notes          |
| S23 | Understanding Polycythemia, The Blood Project (secondary)                                           | not captured          | https://www.thebloodproject.com/understanding-polycythemia/                                                                                                                                                                                        | Erythrocytosis                             |
| S24 | Elevated haemoglobin in adults, GPonline (secondary)                                                | not captured          | https://www.gponline.com/elevated-haemoglobin-adults/haematology/article/1133349                                                                                                                                                                   | Erythrocytosis causes                      |
| S25 | What Causes Lymphocytosis?, pediatriceducation.org (secondary)                                      | not captured          | https://pediatriceducation.org/?p=2163                                                                                                                                                                                                             | Lymphocytosis                              |
| S26 | Evaluation of neutropenia, Epocrates (secondary)                                                    | not captured          | https://www.epocrates.com/online/diseases/893/evaluation-of-neutropenia                                                                                                                                                                            | ANC formula                                |
| S27 | Monocytosis, Wikipedia (secondary, low confidence)                                                  | not captured          | https://en.wikipedia.org/wiki/Monocytosis                                                                                                                                                                                                          | MONO                                       |
| S28 | High monocyte count, Ubie Doctors Note (secondary, low confidence)                                  | Oct 1, 2026           | https://ubiehealth.com/doctors-note/high-monocytes-counts-threshold-causes-symptoms-54101q1                                                                                                                                                        | MONO ranges                                |
| S29 | EDTA-dependent pseudothrombocytopenia, J Ayub Med Coll                                              | not captured          | https://www.jamc.ayubmed.edu.pk/index.php/jamc/article/download/12300/3614                                                                                                                                                                         | PLT artifact                               |
| S30 | Haemoglobin concentrations for the diagnosis of anaemia, WHO (cited by Merck, not opened)           | 2011                  | https://iris.who.int/server/api/core/bitstreams/b82789de-df63-41ba-8058-25f9f5da0c40/content                                                                                                                                                       | Anemia thresholds                          |
| S31 | Anemia testing, Lab Tests Online                                                                    | not captured          | https://labtestsonline.org/anemia-testing                                                                                                                                                                                                          | Anemia tests                               |
| S32 | Thrombocytosis advice leaflet, NHS (NNUH)                                                           | not captured          | https://www.nnuh.nhs.uk/publication/download/thrombocytosis-advice-leaflet-h-a005-v9                                                                                                                                                               | PLT high                                   |
| S33 | Raised or high platelets, GPnotebook (secondary)                                                    | not captured          | https://gpnotebook.com/en-IE/pages/surgery/raised-or-high-platelets                                                                                                                                                                                | Reactive share                             |
| S34 | Platelet count, Labcorp                                                                             | not captured          | https://womenshealth.labcorp.com/tests/005249/platelet-count                                                                                                                                                                                       | Platelet artifacts                         |

### Verification gaps (flagged honestly)

- **Not retrieved:** Cleveland Clinic pages, ASH patient pages, the official Mayo Clinic page, the WHO anemia document, StatPearls leukocytosis full text, and any pediatric reference-interval table. No claims were attributed to them.
- **Mayo Clinic ranges** came from care-network mirror pages, not the mayoclinic.org page.
- **NHLBI pages** are archived copies from 2008 to 2009 and may be outdated.
- **Monocyte, basophil (percentage), and eosinophil (lower limit) reference values** lack authoritative numeric sources here.
- **Pediatric numeric ranges**, **WHO anemia severity grades**, and **pregnancy anemia thresholds** were not verified.
- **Secondary sources** (S22 to S28, S33) are marked "secondary" in text and should be replaced with primary or guideline sources before production use.
