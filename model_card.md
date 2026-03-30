## 🎧 Model Card: Music Recommender Simulation
## 1. Model Name

TuneRanker 1.0
---
## 2. Intended Use

This recommender generates song suggestions based on user preferences like genre, mood, and energy. It is designed to simulate how music recommendation systems work rather than being used for real-world deployment.

The model assumes that users have clear preferences (e.g., one main genre, mood, and target energy level). It does not handle complex or mixed tastes very well.

This project is mainly for classroom exploration to understand how recommendation systems rank items using simple scoring logic.
---
## 3. How the Model Works

The model uses three main features: genre, mood, and energy. Each song is compared against the user’s preferences, and a score is calculated based on how well it matches.

Genre and mood are treated as exact matches (either they match or they don’t)
Energy is treated as a continuous value, where closer values to the user’s target get higher scores

The final score is a combination of these features, with adjustable weights. Increasing the weight of energy makes the system prioritize songs with similar intensity, while reducing genre weight allows more cross-genre recommendations.

Compared to the starter logic, I adjusted feature weights (e.g., doubling energy and reducing genre importance) and tested how these changes affected ranking behavior across different user profiles.
---
## 4. Data

The dataset contains 18 songs loaded from data/songs.csv. Each song includes metadata such as genre, mood, and energy level.

The dataset includes a mix of genres like pop, lofi, and rock, along with moods like chill, happy, and intense.

No major additions were made, but the small size of the dataset limits diversity. Many types of music (e.g., jazz, classical, niche genres) are missing, which affects how realistic the recommendations feel.
---
## 5. Strengths

The system works well when user preferences are clear and aligned with the dataset.

It gives strong recommendations when songs match all three features (genre, mood, energy)
It correctly prioritizes songs that closely match the user’s target energy
For profiles like Chill Lofi or High-Energy Pop, the top results matched expectations

The scoring approach captures the intuition that multiple matching features should lead to higher-ranked songs.
---
## 6. Limitations and Bias

The system has several limitations due to its simplicity and dataset size.

It only considers three features (genre, mood, energy), ignoring others like tempo or valence
Some genres and moods are underrepresented, leading to repeated recommendations
When energy weight is increased, the system tends to favor high-energy songs across different profiles
Cross-genre recommendations appear even when genre preference is strong

This can introduce bias where certain types of songs (especially high-energy ones) dominate results regardless of user intent.
---
## 7. Evaluation

I tested the model using three profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock.

For each profile, I checked whether:

Top recommendations matched the intended genre and mood
Energy values were close to the target
Rankings changed when feature weights were adjusted

One interesting observation was that even small weight changes significantly affected rankings. Also, despite the simple scoring system, the recommendations still felt reasonable, especially for top results.
---
## 8. Future Work

There are several ways to improve the model:

Add more features like tempo, valence, and artist similarity
Increase dataset size to improve diversity and reduce repetition
Experiment with equal weighting across features for more balanced results
Test niche or mixed user profiles to evaluate flexibility
Improve explanation logic to make recommendations more interpretable

Overall, future work would focus on making the system more diverse, flexible, and closer to real-world recommendation behavior.
---
## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps
 learned how recommender systems balance multiple features like genre, mood, and energy to rank songs. Small changes in weights can significantly impact the final recommendations.
One interesting thing I noticed was how simple scoring can still produce results that feel personalized. Even with a small dataset, the system gave reasonable recommendations, but the same songs kept repeating due to limited diversity.
Testing different profiles showed how bias can appear. For example, high-energy songs started dominating when energy was weighted more, even if genre didn’t match well. This made me realize how sensitive recommendation systems are to feature tuning.
Using AI tools like Copilot helped speed up implementation and understand function structure, but I still had to double-check outputs to make sure the logic was correct.
This project changed how I think about music apps. I now see that recommendations are not just based on taste, but on how features are weighted and how much data is available. It also made me think about the scale of infrastructure needed to store metadata and personalize recommendations for millions of users.
If I extend this project, I would add more features like tempo and valence, test niche genre profiles, and increase dataset size for better diversity. I would also try equal weighting across features to compare how balanced recommendations perform.
Overall, I also got a clearer understanding of the difference between collaborative filtering and individual-based approaches, and how metadata plays a key role in building recommendation systems.
