# Internship Task: Web Scraping and JSON Structuring

## Task Overview
The objective of this task is to extract structured information from the Summer Camp. (any one link)
- https://world-camps.org/camp/global-enrichment-programme/
- https://world-camps.org/camp/chiang-mai-climbing-and-adventure-camps/
- https://world-camps.org/camp/bromsgrove-international-school-thailand/

webpage and store it in a properly formatted JSON file. This task will evaluate students on their ability to:
- Extract relevant information from a webpage.
- Structure the extracted data in a JSON format.
- Ensure data accuracy and consistency.
- Use Git and GitHub for version control.


## Repository Setup

1. **Clone the repository** to your local machine using:
   ```sh
   git clone <your-forked-repo-url>
   ```
2. **Define a unique branch name** for your task:
   - Format: `extract-camp-data-<your-github-username>`
   - Example: `extract-camp-data-johndoe`
   ```sh
   git checkout -b extract-camp-data-<your-github-username>
   ```

## Task Instructions
### 1. Extract Information
Extract the following details from the webpage:
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

### 2. Format in JSON
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

### 3. Submit Your Work
1. **Save your JSON file** as `camp_data.json` in the repository.
2. **Commit your changes**:
   ```sh
   git add camp_data.json
   git commit -m "Added extracted camp data in JSON format"
   ```
3. **Push your branch to GitHub**:
   ```sh
   git push origin extract-camp-data-<your-github-username>
   ```
4. **Create a Pull Request (PR)**:
   - Go to your GitHub repository.
   - Navigate to the "Pull Requests" tab.
   - Click on "New Pull Request."
   - Select the `extract-camp-data-<your-github-username>` branch.
   - Click on "Create Pull Request."
   - Add a title and description explaining your changes.
   - Click "Submit" to send your PR for review.



## Evaluation Criteria
- **Accuracy**: The extracted information should match the website content.
- **JSON Structure**: Proper key-value structuring, formatted neatly.
- **Code Cleanliness**: Avoid unnecessary data or redundant fields.
- **Git Usage**: Correctly using branches, commits, and PRs.

## Additional Resources
- [JSON Formatting Guide](https://www.json.org/json-en.html)
- [GitHub Basics](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [Web Scraping with Python](https://realpython.com/beautiful-soup-web-scraper-python/)

Good luck! 🚀
