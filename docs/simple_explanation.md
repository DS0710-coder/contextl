# How ContextL Works (The Simple Version)

Imagine you are looking for a specific recipe in a giant, thousand-page cookbook, but the book has no index. 

Normally, an AI coding assistant (like Cursor or Claude) acts like a person flipping through the book page by page. If your codebase is huge, this takes a very long time, and the AI often gets distracted by recipes that use similar ingredients but aren't what you asked for.

**ContextL fixes this by instantly building an index for your AI.**

Here is exactly what happens behind the scenes in plain English:

### 1. Drawing the Map
When ContextL first looks at your code, it doesn't try to read every single line of logic. Instead, it only looks at **how the files are connected**. 

If `login.js` imports `auth-helper.js`, ContextL draws a line connecting them. It does this for every file in your project, creating a massive, invisible "spiderweb" (a graph) of your entire app.

### 2. Finding the Most Important Files
ContextL looks at the spiderweb and uses the same math that Google uses to rank websites (PageRank) to figure out which files are the most important. 
- A utility file that gets imported by 50 different files is given a high score.
- A random, isolated file that nothing talks to is given a low score.

### 3. Searching with Context
When you ask your AI a question like *"How does our password reset work?"*, the AI secretly passes that question to ContextL.

ContextL scans the text of your files looking for matches, but with a twist:
- If a file matches your question, ContextL doesn't just return that file. It actually looks at the spiderweb and **shares some of those points with the file's neighbors**.
- If `password.js` has a high score, ContextL says: *"Hey, `email-sender.js` is imported by `password.js`, so it's probably highly relevant to the password reset feature, even if the word 'password' isn't explicitly written inside it!"*

### The Result
ContextL instantly hands your AI a perfectly curated list of the exact files it needs to read to solve your problem. 

Because ContextL relies on actual code connections instead of guessing with expensive, slow AI models, it is lightning fast and works entirely on your local machine without sending your private code to the cloud.
