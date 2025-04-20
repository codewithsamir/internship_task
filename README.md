
# **Internship Task: Web Scraping and JSON Structuring**

## **Task Overview**
The objective of this task is to extract structured information from one of the Summer Camp webpages listed below and store it in a properly formatted JSON file. This task will evaluate students on their ability to:
- Extract relevant information from a webpage.
- Structure the extracted data in a JSON format.
- Ensure data accuracy and consistency.
- Use Git and GitHub for version control.

### **Webpage Links**
Choose **one** of the following links:
1. [Global Enrichment Programme](https://world-camps.org/camp/global-enrichment-programme/)
2. [Chiang Mai Climbing and Adventure Camps](https://world-camps.org/camp/chiang-mai-climbing-and-adventure-camps/)
3. [Bromsgrove International School Thailand](https://world-camps.org/camp/bromsgrove-international-school-thailand/)

---

## **Repository Setup**

### **Step 1: Clone the Starter Repository**
1. Clone the starter repository provided by us to your local machine using:
   ```
   git clone <starter-repo-url>
   ```
2. Navigate into the cloned directory:
   ```
   cd <repository-name>
   ```

### **Step 2: Create a New Public Repository**
1. Go to your **GitHub account** and create a new public repository (e.g., `internship-task-web-scraping`).

### **Step 3: Push Code to Your Public Repository**
1. Link your local cloned repository to your new public repository:
   ```
   git remote set-url origin https://github.com/<your-username>/<your-private-repo-name>.git
   ```
2. Push the code to your repository:
   ```
   git push origin main
   ```

---

## **Task Instructions**

### **1. Extract Information**
Extract the following details from the chosen webpage:
- **Highlights**
- **Overview**
- **Age range**
- **Availability**
- **Minimum stay**
- **Price**
- **Main language**
- **Number of campers**
- **Gender**
- **Bedrooms**
- **Activities**
- **Language lessons**
- **Languages taught**
- **Accommodation & Facilities**

### **2. Format in JSON**
Structure the extracted data in a JSON format like below:

```json
{
  "highlights": [
    "International immersion",
    "Professional and experienced staff",
    "Self-contained (all activities on site)",
    "Excellent health and safety protocols",
    "Specialty: Languages"
  ],
  "overview": "International Summer Camp Montana, nestled in the Alpine resort of Crans-Montana, provides a mix of fun, sports, and language learning for children and teens aged 8-17 from around the globe...",
  "age_range": "8-17 yo",
  "availability": "From end of June to end of August",
  "minimum_stay": "2 weeks",
  "price": "From $9,292",
  "main_language": "English",
  "nr_of_campers": "Max 320 campers",
  "gender": "Co-Education",
  "bedrooms": "Shared",
  "activities": [
    "Archery",
    "Arts & Crafts",
    "Climbing",
    "Drama",
    "Excursions",
    "Fencing",
    "Football",
    "Mountain Biking",
    "Overnight Mountain Trip",
    "Riding"
  ],
  "language_lessons": {
    "offered": ["English", "French", "Spanish"],
    "cost": "CHF 300 per session",
    "schedule": "5-6 days a week, 1 hour per day",
    "taught_by": "Native speakers",
    "certificate": "Yes"
  },
  "accommodation_facilities": {
    "buildings": "Moubra House and six additional buildings",
    "capacity": "Up to 330 campers",
    "amenities": [
      "Dining hall",
      "Clubroom",
      "Camp lounge",
      "Library",
      "Classrooms",
      "Sports facilities"
    ]
  }
}
```

### **3. Save Your JSON File**
Save the JSON file as `camp_data.json` in the root directory of your private repository.

---

## **Submission Steps**

### **Step 1: Commit Your Changes**
1. Add the JSON file to the staging area:
   ```sh
   git add camp_data.json
   ```
2. Commit your changes with a meaningful message:
   ```sh
   git commit -m "Added extracted camp data in JSON format"
   ```

### **Step 2: Push Changes to Your Private Repository**
Push your changes to the `main` branch of your private repository:
```sh
git push origin main
```



### **Step 3: Share Your Repository URL**

1. Copy the URL of your public GitHub repository.  
2. Share the URL by filling out the following form:  
   **[Submit your GitHub URL here](https://docs.google.com/forms/d/e/1FAIpQLScGYGStfdn_FfUzpgRWjH-_4W7232jglpFyrOtCAHXCG5KRQQ/viewform?usp=header)**

## **Evaluation Criteria**
Your submission will be evaluated based on the following criteria:
- **Accuracy**: The extracted information should match the website content.
- **JSON Structure**: Proper key-value structuring, formatted neatly.
- **Code Cleanliness**: Avoid unnecessary data or redundant fields.
- **Git Usage**: Correctly using branches, commits, and maintaining a clean commit history.

---

## **Additional Resources**
- [JSON Formatting Guide](https://www.json.org/json-en.html)
- [GitHub Basics](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [Web Scraping with Python](https://realpython.com/beautiful-soup-web-scraper-python/)

Good luck! 🚀

